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


def _idunno(credentials, tsv_download):
    credentials = \
        service_account.Credentials.from_service_account_info(credentials)

    scoped_credentials = credentials.with_scopes(
        ['https://www.googleapis.com/auth/drive'])

    session = AuthorizedSession(scoped_credentials)
    response = session.get(tsv_download)

    return response
