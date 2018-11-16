import os
from aiohttp import web
import jwt
import motor.motor_asyncio
from bson import ObjectId, json_util
from flatten_dict import flatten
from .hooks import _on_insert, _on_update, _on_push, _on_pull
import time

SECRET = os.getenv("SECRET")
DB_URI = os.getenv("DB_URI")
DB = os.getenv("DB") or 'test'
client = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)
db = client[DB] 

def point_reducer(k1, k2):
    if k1 is None:
        return k2
    else:
        return k1 + "." + k2

def set_cors_headers (request, response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization, Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

async def cors_factory (app, handler):
    async def cors_handler (request):
        # preflight requests
        if request.method == 'OPTIONS':
            return set_cors_headers(request, web.Response())
        else:
            response = await handler(request)
            return set_cors_headers(request, response)
    return cors_handler


def jwt_auth(f):
    async def helper(request):
        try:
            payload = jwt.decode(request.headers['Authorization'], SECRET, algorithms=['HS256'])
            return await f(request, payload)
        except Exception as e:
            return web.json_response({'error': str(e)})
    return helper

def validate(validator, update=False):
    def decorator(f):
        async def helper(col, old_doc, document, request, payload):
            if validator.validate(document, update=update):
                return await f(col, old_doc, document, request, payload)
            else:
                return web.json_response({'error': 'not valid document: ' + str(validator.errors)})                 
        return helper
    return decorator

def has_role(role): 
    def decorator(f):
        async def helper(request, payload):
            if role == '*' or role in payload['roles']:
                return await f(request, payload)
            else:
                return web.json_response({'error': 'not authorized'})
        return helper
    return decorator

def collection(col):
    def decorator(f):
        async def helper(request, payload):
            return await f(col, request, payload)
        return helper    
    return decorator

def read_access(user_permissions):
    def decorator(f):
        async def helper(col, request, payload):            
            return await f(col, user_permissions, request, payload)
        return helper
    return decorator

def write_access(user_permissions):
    def decorator(f):
        async def helper(col, request, payload):
            document = await request.json()
            _id = request.match_info.get('_id')
            old_doc = await db[col].find_one({'_id': ObjectId(_id)})

            for user, args in user_permissions.items():     
                if user == '*' or payload['user'] == old_doc[user]:
                    if args[0] == '*':
                        return await f(col, old_doc, document, request, payload)
                    ret = {}
                    for k in document.keys():
                        if k in args:
                            ret[k] = document[k]
                    if ret == {}:
                        return web.json_response({'error': 'not authorized'})            
                    return await f(col, old_doc, ret, request, payload)
            return web.json_response({'error': 'not authorized'})
        return helper
    return decorator

def pick(document, permissions, user):
    for u, args in permissions.items():  
        if u == '*' or user == document[u]:
            if args == '*':
                return document
            else:
                return {k: document[k] for k in args}
    return {}
    #return web.json_response({'error': 'not authorized'})

def get(f): 
    async def helper(col, permissions, request, payload):            
        _id = request.match_info.get('_id')
        document = await db[col].find_one({'_id': ObjectId(_id)})
        document = await f(document, payload)
        document = pick(document, permissions, payload['user'])
        return web.json_response(document, dumps=json_util.dumps)
    return helper

def get_many(f): 
    async def helper(col, permissions, request, payload):        
        cursor = await f(db[col], request.query, payload)
        documents = await cursor.to_list(length=100)                    # TODO: harcoded limit
        ret = []
        for doc in documents:
            ret.append(pick(doc, permissions, payload['user']))
        return web.json_response(ret, dumps=json_util.dumps)
    return helper

def aggregate(f): 
    async def helper(col, request, payload):        
        cursor = await f(db[col], request.query, payload)
        documents = await cursor.to_list(length=100)                    # TODO: harcoded limit
        return web.json_response(documents, dumps=json_util.dumps)
    return helper

def insert(f):
    async def helper(col, old_doc, document, request, payload):
        document = await f(document, request, payload)
        document['__owner'] = payload['user']   
        document['created_at'] = time.time()
        result = await db[col].insert_one(document)
        #callback = _on_insert.get(col)
        #if callback:
        #    await callback(document)
        return web.json_response(document, dumps=json_util.dumps) 
    return helper

def update(f):
    async def helper(col, old_doc, document, request, payload):        
        document = await f(old_doc, document, request, payload)
        document['updated_at'] = time.time()
        document = flatten(document, reducer=point_reducer)
        _id = request.match_info.get('_id')
        await db[col].update_one({'_id': ObjectId(_id)}, {'$set': document})        
        #callback = _on_update.get(col)
        #if callback:
        #    await callback(document)
        return web.json_response(document)
    return helper

def push(attr):
    def decorator(f):
        async def helper(col, old_doc, document, request, payload):
            document = await f(document, request, payload)
            _id = request.match_info.get('_id')
            document['_id'] = ObjectId()
            await db[col].update_one({'_id': ObjectId(_id)}, {'$set': {'updated_at': time.time()}, '$push': {attr: document}})        
            callback = _on_push.get(col)
            if callback:
                callback(document)
            return web.json_response(document, dumps=json_util.dumps)
        return helper
    return decorator

def pull(f): # TODO
    async def helper(col, document, request, payload):
        await f({}, request, payload)
        _id = request.match_info.get('_id')
        attr = request.match_info.get('pull')
        sub_id = request.match_info.get('sub_id')
        document = {'_id': ObjectId(sub_id)}
        await db[col].update_one({'_id': ObjectId(_id)}, {'$pull': {attr: document}})        
        callback = _on_pull.get(col)
        if callback:
            callback(document)
        return web.json_response({})
    return helper

def json_response(f):
    async def helper(request):
        document = await f(request)
        return web.json_response(document)
    return helper

def delete(f): # TODO permissions
    async def helper(col, document, request, payload):
        _id = request.match_info.get('_id')
        await db[col].delete_one({'_id': ObjectId(_id)})
        return web.json_response({})
    return helper
