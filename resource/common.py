from google.auth.transport.requests import AuthorizedSession
from googleapiclient.discovery import build
from google.oauth2 import service_account


def get_service(credentials):
    credentials = \
        service_account.Credentials.from_service_account_info(credentials)

    scoped_credentials = credentials.with_scopes(
        ['https://www.googleapis.com/auth/drive'])

    service = build('drive', 'v2', credentials=scoped_credentials)

    return service


def get_file(credentials, tsv_download):
    credentials = \
        service_account.Credentials.from_service_account_info(credentials)

    scoped_credentials = credentials.with_scopes(
        ['https://www.googleapis.com/auth/drive'])

    session = AuthorizedSession(scoped_credentials)
    response = session.get(tsv_download)

    return response

def get_opts(source):
    cred = {'type', 'project_id', 'private_key_id', 'private_key',
            'client_email', 'client_id', 'auth_uri', 'token_uri',
            'auth_provider_x509_cert_url', 'client_x509_cert_url'}
    credentials = {k: v for k, v in source.items() if k in cred}
    file_id, rev_key = source['file_id'], source['rev_key']
    return dict(file_id=file_id, rev_key=rev_key, credentials=credentials)