# -*- coding: utf-8 -*-
import mimetypes
import os

from flask import Flask, request, redirect, jsonify
from flask import render_template
from flask import send_from_directory
from werkzeug.utils import secure_filename

from app import GetArg
from app import conf
from app.conf import CDN_JS
from app.conf import VIDEO_SUFFIX
from app.path_util import get_filename
from app.path_util import get_suffix
from app.path_util import is_child
from app.path_util import is_dir
from app.path_util import is_file
from app.path_util import normalize_path
from app.path_util import parent_path
from app.path_util import translate_path
from app.util import debug
from app.util import warning

app = Flask(__name__, template_folder='templates')


@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def do_get(path):
    arg = GetArg(request.args)
    debug('do_get: path %s,' % path, 'arg is', arg.to_dict())
    if path == '' or path == '/':
        return get_root()
    local_path = translate_path(path)
    if is_dir(local_path):  # 目录
        return list_dir(path)
    elif is_file(local_path) and not path_permission_deny(path):  # 文件
        if arg.mode is None or arg.mode == GetArg.MODE_NORMAL:
            if get_suffix(path) in VIDEO_SUFFIX:
                return play_video(path)
            else:
                return respond_file(path)
        elif arg.mode == GetArg.MODE_TXT:
            return respond_file(path, mime='text/plain')
        elif arg.mode == GetArg.MODE_DOWN:
            return respond_file(path, as_attachment=True)
        elif arg.mode == GetArg.MODE_VIDEO:
            return play_video(path)

    if os.path.exists(path) and path_permission_deny(path):
        warning('permission deny: ' + path)
        return resp_permission_deny(path)
    else:
        return render_template('error.html', error='No such dir or file: ' + path)


def get_root():
    if len(conf.WHITE_LIST) == 0 and len(conf.BLACK_LIST) == 0:
        return list_dir('')
    else:
        local_path = translate_path('')
        try:
            lst = os.listdir(local_path)
        except OSError:
            lst = []
        lst = [i for i in lst if not path_permission_deny(i)]  # check permission
        lst = [i + '/' if is_dir(local_path + '/' + i) else i for i in lst]  # add '/' to dir
        return render_template('list.html',
                               upload=conf.UPLOAD,
                               path='',
                               arg=GetArg(request.args).format_for_url(),
                               list=lst)


@app.route('/', defaults={'path': ''}, methods=['POST'])
@app.route('/<path:path>', methods=['POST'])
def do_post(path):
    debug('post_path: %s' % path)
    if path_permission_deny(path):
        resp_permission_deny(path)
    if not conf.UPLOAD:
        return redirect(request.url)
    try:
        if 'file' not in request.files:
            debug('do_post: No file in request')
            return redirect(request.url)
        else:
            request_file = request.files['file']
            filename = secure_filename(request_file.filename)
            local_path = os.path.join(translate_path(path), filename)
            if os.path.exists(local_path):
                if not conf.UPLOAD_OVERRIDE_MODE:
                    local_path = plus_filename(local_path)
            request_file.save(local_path)
            debug('save file to: %s' % local_path)
            res = {'operation': 'upload_file', 'state': 'succeed', 'filename': request_file.filename}
            return jsonify(**res)
    except Exception as e:
        debug('do_post (error): ', e)
        return render_template('error.html', error=e)


def list_dir(path):
    debug('list_dir', path)
    local_path = translate_path(path)
    arg = GetArg(request.args)
    if is_dir(local_path) and not path_permission_deny(path):  # dir
        try:
            lst = os.listdir(local_path)
        except OSError:
            lst = []
        lst = [i for i in lst if not path_permission_deny(path + '/' + i)]  # check permission
        lst = [i + '/' if is_dir(local_path + '/' + i) else i for i in lst]  # add '/' to dir
        return render_template('list.html',
                               upload=conf.UPLOAD,
                               path=path,
                               arg=arg.format_for_url(),
                               list=lst)
    return resp_permission_deny(path)


def respond_file(path, mime=None, as_attachment=False):
    debug('respond_file:', path)
    if is_dir(path):
        return do_get(path)
    local_path = translate_path(path)
    if mime is None or mime not in mimetypes.types_map.values():  # mime 无效
        mime = mimetypes.guess_type(local_path)[0]
        if mime is None:  # 无法获取类型，默认使用 text/plain
            mime = 'text/plain'
    if mime in ['text/html', '']:
        mime = 'text/plain'
    return send_from_directory(parent_path(local_path),
                               get_filename(local_path),
                               mimetype=mime,
                               as_attachment=as_attachment)


def play_video(path):
    debug('play_video:', path)
    if is_dir(translate_path(path)):
        return do_get(path)

    arg = GetArg(request.args)
    suffix = get_suffix(path)
    t = suffix if arg.play is None else arg.play

    try:
        tj = CDN_JS[t]
        tjs = []
    except Exception as e:
        debug('play_video (error):', e, 't:', t)
        tj = ''
        tjs = CDN_JS.values()
    return render_template('video.html',
                           name=get_filename(path),
                           url='/%s?%s=%s' % (path, GetArg.ARG_MODE, GetArg.MODE_DOWN),
                           type=t,
                           typejs=tj,
                           typejss=tjs)


def path_permission_deny(path):
    """
    note that prior of black list is high than one of white list,
    that is, even path is sub of white list, path will be denied if path is in black or black' sub path
    :param path:
    :return:
    """
    DENY = True
    if path == '' or path == '/' or path == 'favicon.ico':
        return not DENY
    if len(conf.BLACK_LIST) == 0 and len(conf.WHITE_LIST) == 0:  # disable white or black list function
        return not DENY

    np = normalize_path(path)
    if len(conf.WHITE_LIST) > 0:  # white mode
        if np in conf.WHITE_LIST_PARENTS or np in conf.WHITE_LIST:  # path is white or parent of white
            return not DENY
        black_child = False
        for w in conf.WHITE_LIST:
            if is_child(np, w):
                for b in conf.BLACK_LIST:
                    if is_child(np, w):
                        black_child = True
                if not black_child:
                    return not DENY  # path is child of white and not child of black
        return DENY  # define white_list while path not satisfy white_list

    if len(conf.BLACK_LIST) > 0:  # black mode
        for b in conf.BLACK_LIST:
            if is_child(np, b):
                return DENY  # path is in black list.
        return not DENY
    return DENY


def resp_permission_deny(path):
    return render_template('error.html', error='Permission deny for such dir or file: ' + path)


def plus_filename(filename):
    ind = -1 if '.' not in filename else filename.rindex('.')
    prefix = filename[:ind] if ind >= 0 else filename
    suffix = get_suffix(filename)
    i = 0
    while True:
        i += 1
        res = prefix + '(' + str(i) + ')'
        res = res + '.' + suffix if suffix != '' else res
        if not os.path.exists(res):
            return res
