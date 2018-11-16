from configparser import ConfigParser
import json
import os
import io
import sys
import ibm_boto3
import wget
import uuid
import psycopg2
from psycopg2.sql import Identifier, SQL
from ibm_botocore.client import Config
from datetime import datetime, timedelta
from pytz import timezone

yesterday = datetime.now(timezone('UTC')) - timedelta(days=1)


if "ENV" in os.environ:
    environment = os.environ['ENV']
else:
    environment = "YP_QA"

print('Used environment:', environment)

if "TEST_DIR" in os.environ:
    configDir = os.environ['TEST_DIR'] + "config.ini"
else:
    configDir = "./config.ini"

config = ConfigParser()
config.read(configDir)


def get_env():
    return environment


def get_schema_name():
    return config.get(environment, 'schema_name')


def get_schema_name2():
    return config.get(environment, 'schema_name2')


def get_aios_credentials():
    return json.loads(config.get(environment, 'aios_credentials'))


def get_wml_credentials():
    return json.loads(config.get(environment, 'wml_credentials'))


def get_postgres_credentials():
    return json.loads(config.get(environment, 'postgres_credentials'))


def get_cos_credentials():
    return json.loads(config.get(environment, 'cos_credentials'))


def get_feedback_data_reference():
    return json.loads(config.get(environment, 'feedback_data_reference'))


def get_db2_credentials():
    return json.loads(config.get(environment, 'db2_reference'))


def get_spark_reference():
    return json.loads(config.get(environment, 'spark_reference'))


def get_cos_auth_endpoint():
    return config.get(environment, 'cos_auth_endpoint')


def get_cos_service_endpoint():
    return config.get(environment, 'cos_service_endpoint')


def get_client():
    wml_lib = __import__('watson_machine_learning_client', globals(), locals())
    return wml_lib.WatsonMachineLearningAPIClient(get_wml_credentials())


def get_cos_resource():
    cos_credentials = get_cos_credentials()
    api_key = cos_credentials['apikey']
    service_instance_id = cos_credentials['resource_instance_id']
    auth_endpoint = get_cos_auth_endpoint()
    service_endpoint = get_cos_service_endpoint()

    cos = ibm_boto3.resource(
        's3',
        ibm_api_key_id = api_key,
        ibm_service_instance_id = service_instance_id,
        ibm_auth_endpoint = auth_endpoint,
        config = Config(signature_version='oauth'),
        endpoint_url = service_endpoint
    )

    return cos


def prepare_cos(cos_resource, bucket_prefix='wml-test'):
    import datetime

    postfix = datetime.datetime.now().isoformat().replace(":", "-").split(".")[0].replace("T", "-")

    bucket_names = {
        'data': '{}-{}-data-{}'.format(bucket_prefix, environment.lower().replace('_', '-'), postfix),
        'results': '{}-{}-results-{}'.format(bucket_prefix, environment.lower().replace('_', '-'), postfix)
    }

    cos_resource.create_bucket(Bucket=bucket_names['data'])
    cos_resource.create_bucket(Bucket=bucket_names['results'])

    return bucket_names


def get_cos_training_data_reference(bucket_names):
    cos_credentials = get_cos_credentials()
    service_endpoint = get_cos_service_endpoint()

    return {
        "connection": {
            "endpoint_url": service_endpoint,
            "access_key_id": cos_credentials['cos_hmac_keys']['access_key_id'],
            "secret_access_key": cos_credentials['cos_hmac_keys']['secret_access_key']
        },
        "source": {
            "bucket": bucket_names['data'],
        },
        "type": "s3"
    }


def get_cos_training_results_reference(bucket_names):
    cos_credentials = get_cos_credentials()
    service_endpoint = get_cos_service_endpoint()

    return {
        "connection": {
            "endpoint_url": service_endpoint,
            "access_key_id": cos_credentials['cos_hmac_keys']['access_key_id'],
            "secret_access_key": cos_credentials['cos_hmac_keys']['secret_access_key']
        },
        "target": {
            "bucket": bucket_names['results'],
        },
        "type": "s3"
    }


def clean_cos_bucket(cos_resource, bucket_name):
    bucket_obj = cos_resource.Bucket(bucket_name)
    for upload in bucket_obj.multipart_uploads.all():
        upload.abort()
    for o in bucket_obj.objects.all():
        o.delete()
    bucket_obj.delete()


def clean_cos(cos_resource, bucket_names):
    clean_cos_bucket(cos_resource, bucket_names['data'])
    clean_cos_bucket(cos_resource, bucket_names['results'])


def clean_env(cos_resource=None, threshold_date=yesterday, raise_when_not_empty=False):
    rm_els_no = 0

    from ibm_ai_openscale import APIClient
    ai_client = APIClient(get_aios_credentials())
    for uid in ai_client.data_mart.subscriptions.get_uids():
        subscription = ai_client.data_mart.subscriptions.get(uid)
        if subscription.get_details()['metadata']['created_at'] < threshold_date.isoformat():
            print('Deleting \'{}\' subscription.'.format(uid))
            try:
                ai_client.data_mart.subscriptions.delete(uid)
            except Exception as e:
                print('Deleting of subscription failed:', e)

    # TODO unbind
    # etc

    client = get_client()

    rm_els_no += clean_experiments(client, threshold_date)
    rm_els_no += clean_training_runs(client, threshold_date)
    rm_els_no += clean_definitions(client, threshold_date)
    rm_els_no += clean_models(client, threshold_date)
    rm_els_no += clean_deployments(client, threshold_date)
    try:
        rm_els_no += clean_ai_functions(client, threshold_date)
        rm_els_no += clean_runtimes(client, threshold_date)
        rm_els_no += clean_custom_libraries(client, threshold_date)
    except:
        pass

    if cos_resource is not None:
        for bucket in cos_resource.buckets.all():
            if 'wml-test-' in bucket.name and bucket.creation_date < threshold_date:
                rm_els_no +=1
                print('Deleting \'{}\' bucket.'.format(bucket.name))
                try:
                    for upload in bucket.multipart_uploads.all():
                        upload.abort()
                    for o in bucket.objects.all():
                        o.delete()
                    bucket.delete()
                except Exception as e:
                    print("Exception during bucket deletion occured: " + str(e))

    if raise_when_not_empty and rm_els_no > 0:
        raise Exception('Non zero number of elements to clean: {}'.format(rm_els_no))

    try:
        ai_client = APIClient(get_aios_credentials())
        try:
            for uid in ai_client.data_mart.bindings.get_uids():
                ai_client.data_mart.bindings.delete(uid)
        except:
            pass

        try:
            ai_client.data_mart.delete()
        except:
            pass
    except:
        pass

    try:
        delete_schema(get_postgres_credentials(), get_schema_name())
    except:
        pass

    create_schema(get_postgres_credentials(), get_schema_name())

    try:
        delete_schema(get_postgres_credentials(), get_schema_name2())
    except:
        pass

    create_schema(get_postgres_credentials(), get_schema_name2())


def clean_wml_assets(details, delete, asset_name, threshold_date=yesterday):

    number_of_assets = 0

    for asset_details in details['resources']:
        if asset_details['metadata']['created_at'] < threshold_date.isoformat():
            number_of_assets += 0
            print('Deleting \'{}\' {}.'.format(asset_details['metadata']['guid'], asset_name))
            try:
                delete(asset_details['metadata']['guid'])
            except Exception as e:
                print('Deletion of {} failed:'.format(asset_name), e)

    return number_of_assets


def clean_repository_assets(client, details, asset_name, threshold_date=yesterday):
    return clean_wml_assets(details, client.repository.delete, asset_name, threshold_date)


def clean_models(client, threshold_date=yesterday):
    return clean_repository_assets(client, client.repository.get_model_details(), 'model', threshold_date)


def clean_definitions(client, threshold_date=yesterday):
    return clean_repository_assets(client, client.repository.get_definition_details(), 'definition', threshold_date)


def clean_deployments(client, threshold_date=yesterday):
    return clean_wml_assets(client.deployments.get_details(), client.deployments.delete, 'deployment', threshold_date)


def clean_experiments(client, threshold_date=yesterday):
    return clean_repository_assets(client, client.repository.get_experiment_details(), 'experiment', threshold_date)


def clean_training_runs(client, threshold_date=yesterday):
    return clean_wml_assets(client.training.get_details(), client.training.delete, 'training run', threshold_date)


def clean_runtimes(client, threshold_date=yesterday):
    return clean_repository_assets(client, client.runtimes.get_details(), 'runtimes', threshold_date)


def clean_custom_libraries(client, threshold_date=yesterday):
    return clean_wml_assets(client.runtimes.get_library_details(), client.runtimes.delete_library, 'custom library', threshold_date)


def clean_ai_functions(client, threshold_date=yesterday):
    return clean_repository_assets(client, client.repository.get_function_details(), 'python function', threshold_date)


def run_monitor(client, experiment_run_uid, queue):
    stdout_ = sys.stdout
    captured_output = io.StringIO()  # Create StringIO object
    sys.stdout = captured_output  # and redirect stdout.
    client.experiments.monitor_logs(experiment_run_uid)
    sys.stdout = stdout_  # Reset redirect.

    print(captured_output.getvalue())

    queue.put(captured_output.getvalue())


def run_monitor_metrics(client, experiment_run_uid, queue):
    stdout_ = sys.stdout
    captured_output = io.StringIO()  # Create StringIO object
    sys.stdout = captured_output  # and redirect stdout.
    client.experiments.monitor_metrics(experiment_run_uid)
    sys.stdout = stdout_  # Reset redirect.

    print(captured_output.getvalue())

    queue.put(captured_output.getvalue())


def run_monitor_training(client, training_run_uid, queue):
    stdout_ = sys.stdout
    captured_output = io.StringIO()  # Create StringIO object
    sys.stdout = captured_output  # and redirect stdout.
    client.training.monitor_logs(training_run_uid)
    sys.stdout = stdout_  # Reset redirect.

    print(captured_output.getvalue())

    queue.put(captured_output.getvalue())


def prepare_connection_postgres(postgres_credentials):
    uri = postgres_credentials['uri']

    import re
    res = re.search('^[0-9a-zA-Z]+://([0-9a-zA-Z]+):([0-9a-zA-Z]+)@([^:]+):([0-9]+)/([0-9a-zA-Z]+)$', uri)

    if res is None:
        raise Exception('Unexpected format of db uri: {}'.format(uri))

    username = res.group(1)
    password = res.group(2)
    host = res.group(3)
    port = res.group(4)
    database = res.group(5)

    return psycopg2.connect(
        database=database,
        user=username,
        password=password,
        host=host,
        port=port
    )


def create_schema(postgres_credentials, schema_name):
    execute_sql_query(SQL("CREATE SCHEMA {}").format(Identifier(schema_name)), postgres_credentials)


def delete_schema(postgres_credentials, schema_name):
    execute_sql_query(SQL("DROP SCHEMA {} CASCADE").format(Identifier(schema_name)), postgres_credentials)


def print_schema_tables_info(postgres_credentials, schema_name):
    rows = execute_sql_query("SELECT * FROM information_schema.tables WHERE table_schema = '{}'".format(schema_name), postgres_credentials)

    for row in rows:
        print(row)


def wait_until_deleted(ai_client, binding_uid=None, subscription_uid=None, data_mart=None):
    uids_sum = sum([1 if b else 0 for b in [binding_uid, subscription_uid, data_mart]])

    if uids_sum > 1:
        raise Exception('More than one uid passed.')
    elif uids_sum == 0:
        raise Exception('No uids passed.')

    def can_be_found():
        if binding_uid is not None:
            try:
                print(ai_client.data_mart.bindings.get_details(binding_uid))
                return True
            except:
                return False
        elif subscription_uid is not None:
            try:
                print(ai_client.data_mart.subscriptions.get_details(subscription_uid))
                return True
            except:
                return False
        elif data_mart is not None:
            try:
                print(ai_client.data_mart.get_details())
                return True
            except Exception as e:
                print(e)
                return False

    import time

    print('Waiting for {} to delete...'.format(
        'binding with uid=\'{}\''.format(binding_uid) if binding_uid is not None
        else 'subscription with uid=\'{}\''.format(subscription_uid) if subscription_uid is not None
        else 'data_mart'
    ), end='')

    iterator = 0

    while can_be_found() and iterator < 20:
        time.sleep(3)
        print('.', end='')
        iterator += 1

    print(' DELETED')


def execute_sql_query(query, postgres_credentials):
    conn = prepare_connection_postgres(postgres_credentials=postgres_credentials)

    cursor = conn.cursor()
    cursor.execute(query)

    try:
        query_result = cursor.fetchall()
    except psycopg2.ProgrammingError as ex:
        query_result = ""

    conn.commit()
    cursor.close()
    conn.close()

    return query_result
