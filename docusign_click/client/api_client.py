# coding: utf-8
"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import base64
import json
import math
import mimetypes
import os
import re
import tempfile
import threading
from datetime import date, datetime
from time import time

import jwt
# python 2 and python 3 compatibility library
from six import PY3, integer_types, iteritems, text_type
from six.moves.urllib.parse import quote

from docusign_click import client
from docusign_click import models
from .configuration import Configuration
from .api_exception import ApiException, ArgumentException
from .api_response import RESTClientObject, RESTResponse
from .auth.oauth import OAuthUserInfo, OAuthToken, OAuth, Account, Organization, Link


class ApiClient(object):
    """
    Generic API client for Swagger client library builds.

    Swagger generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the Swagger
    templates.

    NOTE: This class is auto generated by the swagger code generator program.
    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.

    :param host: The base path for the server to call.
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to the API.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, text_type) + integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': date,
        'datetime': datetime,
        'object': object,
    }
    OAUTH_TYPES = (OAuthToken.__name__, OAuthUserInfo.__name__, Account.__name__, Organization.__name__, Link.__name__)

    def __init__(self, host=None, header_name=None, header_value=None, cookie=None, oauth_host_name=None,
                 base_path=None):
        """
        Constructor of the class.
        """
        self.rest_client = RESTClientObject()
        self.default_headers = {'X-DocuSign-SDK': 'Python'}

        if header_name is not None:
            self.default_headers[header_name] = header_value

        if host is None:
            self.host = Configuration().host
        elif host == "":
            raise ArgumentException("basePath cannot be empty")
        else:
            self.host = host

        self.cookie = cookie
        self.oauth_host_name = oauth_host_name
        self.base_path = base_path
        # Set default User-Agent.
        self.user_agent = Configuration().user_agent

    @property
    def user_agent(self):
        """
        Gets user agent.
        """
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        """
        Sets user agent.
        """
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def __call_api(self, resource_path, method,
                   path_params=None, query_params=None, header_params=None,
                   body=None, post_params=None, files=None,
                   response_type=None, auth_settings=None, callback=None,
                   _return_http_data_only=None, collection_formats=None, _preload_content=True,
                   _request_timeout=None):
        """
        :param _preload_content: if False, the urllib3.HTTPResponse object will be returned without
                                 reading/decoding response data. Default is True. 
        :return: 
        """

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params,
                                                           collection_formats))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params,
                                                    collection_formats)
            for k, v in path_params:
                resource_path = resource_path.replace(
                    '{%s}' % k, quote(str(v), safe=""))

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params,
                                                     collection_formats)

        # post parameters
        if post_params or files:
            post_params = self.prepare_post_parameters(post_params, files)
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params,
                                                    collection_formats)

        # auth setting
        self.update_params_for_auth(header_params, query_params, auth_settings)

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # request url
        url = self.host + resource_path

        # perform request and return response
        response_data = self.request(method, url,
                                     query_params=query_params,
                                     headers=header_params,
                                     post_params=post_params, body=body,
                                     _preload_content=_preload_content,
                                     _request_timeout=_request_timeout)

        self.last_response = response_data

        return_data = response_data

        if _preload_content:
            r = RESTResponse(response_data)
            # deserialize response data
            if response_type and response_type != "file":
                # In the python 3, the response.data is bytes.
                # we need to decode it to string.
                if PY3:
                    r.data = r.data.decode('utf8', 'replace')
                return_data = self.deserialize(r, response_type)
            elif response_type:
                return_data = self.deserialize(r, response_type)
            else:
                return_data = None

        if callback:
            if _return_http_data_only:
                callback(return_data)
            else:
                callback((return_data, response_data.status, response_data.getheaders()))
        elif _return_http_data_only:
            return (return_data)
        else:
            return (return_data, response_data.status, response_data.getheaders())

    def sanitize_for_serialization(self, obj):
        """
        Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj)
                         for sub_obj in obj)
        elif isinstance(obj, (datetime, date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `swagger_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                        for attr, _ in iteritems(obj.swagger_types)
                        if getattr(obj, attr) is not None}

        return {key: self.sanitize_for_serialization(val)
                for key, val in iteritems(obj_dict)}

    def deserialize(self, response, response_type):
        """
        Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        if response_type == "file":
            return self.__deserialize_file(response)

        # fetch data from response object
        try:
            data = json.loads(response.data)
        except ValueError:
            data = response.data

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        """
        Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match('list\[(.*)\]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('dict('):
                sub_kls = re.match('dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in iteritems(data)}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                if klass in self.OAUTH_TYPES:
                    klass = getattr(client, klass)
                else:
                    klass = getattr(models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == date:
            return self.__deserialize_date(data)
        elif klass == datetime:
            return self.__deserialize_datatime(data)
        else:
            return self.__deserialize_model(data, klass)

    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, files=None,
                 response_type=None, auth_settings=None, callback=None,
                 _return_http_data_only=None, collection_formats=None, _preload_content=True,
                 _request_timeout=None):
        """
        Makes the HTTP request (synchronous) and return the deserialized data.
        To make an async request, define a function for callback.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response: Response data type.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param callback function: Callback function for asynchronous request.
            If provide this parameter,
            the request will be called asynchronously.
        :param _return_http_data_only: response data without head status code and headers
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _preload_content: if False, the urllib3.HTTPResponse object will be returned without
                                 reading/decoding response data. Default is True.
        :param _request_timeout: timeout setting for this request. If one number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of (connection, read) timeouts.
        :return:
            If provide parameter callback,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter callback is None,
            then the method will return the response directly.
        """
        if callback is None:
            return self.__call_api(resource_path, method,
                                   path_params, query_params, header_params,
                                   body, post_params, files,
                                   response_type, auth_settings, callback,
                                   _return_http_data_only, collection_formats, _preload_content, _request_timeout)
        else:
            thread = threading.Thread(target=self.__call_api,
                                      args=(resource_path, method,
                                            path_params, query_params,
                                            header_params, body,
                                            post_params, files,
                                            response_type, auth_settings,
                                            callback, _return_http_data_only,
                                            collection_formats, _preload_content, _request_timeout))
        thread.start()
        return thread

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True, _request_timeout=None):
        """
        Makes the HTTP request using RESTClient.
        """
        if method == "GET":
            return self.rest_client.GET(url,
                                        query_params=query_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        headers=headers)
        elif method == "HEAD":
            return self.rest_client.HEAD(url,
                                         query_params=query_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         headers=headers)
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(url,
                                            query_params=query_params,
                                            headers=headers,
                                            post_params=post_params,
                                            _preload_content=_preload_content,
                                            _request_timeout=_request_timeout,
                                            body=body)
        elif method == "POST":
            return self.rest_client.POST(url,
                                         query_params=query_params,
                                         headers=headers,
                                         post_params=post_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         body=body)
        elif method == "PUT":
            return self.rest_client.PUT(url,
                                        query_params=query_params,
                                        headers=headers,
                                        post_params=post_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        body=body)
        elif method == "PATCH":
            return self.rest_client.PATCH(url,
                                          query_params=query_params,
                                          headers=headers,
                                          post_params=post_params,
                                          _preload_content=_preload_content,
                                          _request_timeout=_request_timeout,
                                          body=body)
        elif method == "DELETE":
            return self.rest_client.DELETE(url,
                                           query_params=query_params,
                                           headers=headers,
                                           _preload_content=_preload_content,
                                           _request_timeout=_request_timeout,
                                           body=body)
        else:
            raise ValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def parameters_to_tuples(self, params, collection_formats):
        """
        Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in iteritems(params) if isinstance(params, dict) else params:
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def prepare_post_parameters(self, post_params=None, files=None):
        """
        Builds form parameters.

        :param post_params: Normal form parameters.
        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []

        if post_params:
            params = post_params

        if files:
            for k, v in iteritems(files):
                if not v:
                    continue
                file_names = v if type(v) is list else [v]
                for n in file_names:
                    with open(n, 'rb') as f:
                        filename = os.path.basename(f.name)
                        filedata = f.read()
                        mimetype = mimetypes. \
                                       guess_type(filename)[0] or 'application/octet-stream'
                        params.append(tuple([k, tuple([filename, filedata, mimetype])]))

        return params

    def select_header_accept(self, accepts):
        """
        Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    def select_header_content_type(self, content_types):
        """
        Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return 'application/json'

        content_types = [x.lower() for x in content_types]

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]

    def update_params_for_auth(self, headers, querys, auth_settings):
        """
        Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        """
        config = Configuration()

        if not auth_settings:
            return

        for auth in auth_settings:
            auth_setting = config.auth_settings().get(auth)
            if auth_setting:
                if not auth_setting['value']:
                    continue
                elif auth_setting['in'] == 'header':
                    headers[auth_setting['key']] = auth_setting['value']
                elif auth_setting['in'] == 'query':
                    querys.append((auth_setting['key'], auth_setting['value']))
                else:
                    raise ValueError(
                        'Authentication token must be in `query` or `header`'
                    )

    def __deserialize_file(self, response):
        """
        Saves response body into a file in a temporary folder,
        using the filename from the `Content-Disposition` header if provided.

        :param response:  RESTResponse.
        :return: file path.
        """
        config = Configuration()

        fd, path = tempfile.mkstemp(dir=config.temp_folder_path)
        os.close(fd)
        os.remove(path)

        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            filename = re. \
                search(r'filename=[\'"]?([^\'"\s]+)[\'"]?', content_disposition). \
                group(1)

            curr_time = datetime.now()
            formatted_time = curr_time.strftime('%m%d%Y_%H%M%S_%f')
            filename = "{}_{}".format(formatted_time, filename)
            path = os.path.join(os.path.dirname(path), filename)

        with open(path, "wb") as f:
            f.write(response.data)
        return path

    def __deserialize_primitive(self, data, klass):
        """
        Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return unicode(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """
        Return a original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """
        Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            from dateutil.parser import parse
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise ApiException(
                status=0,
                reason="Failed to parse `{0}` into a date object".format(string)
            )

    def __deserialize_datatime(self, string):
        """
        Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` into a datetime object"
                        .format(string)
                )
            )

    def __deserialize_model(self, data, klass):
        """
        Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """
        instance = klass()

        if not instance.swagger_types:
            return data

        for attr, attr_type in iteritems(instance.swagger_types):
            if data is not None \
                    and instance.attribute_map[attr] in data \
                    and isinstance(data, (list, dict)):
                value = data[instance.attribute_map[attr]]
                setattr(instance, attr, self.__deserialize(value, attr_type))

        return instance

    def request_jwt_user_token(self, client_id, user_id, oauth_host_name, private_key_bytes, expires_in,
                               scopes=(OAuth.SCOPE_SIGNATURE,)):
        """
        Request JWT User Token
        :param client_id: DocuSign OAuth Client Id(AKA Integrator Key)
        :param user_id: DocuSign user Id to be impersonated
        :param oauth_host_name: DocuSign OAuth host name
        :param private_key_bytes: the byte contents of the RSA private key
        :param expires_in: number of seconds remaining before the JWT assertion is considered as invalid
        :param scopes: Optional. The list of requested scopes may include (but not limited to) You can also pass any
        advanced scope.
        :return: OAuthToken object
        """
        if not private_key_bytes:
            raise ArgumentException("Private key not supplied or is invalid!")
        if not user_id:
            raise ArgumentException("User Id not supplied or is invalid!")
        if not oauth_host_name:
            raise ArgumentException("oAuthBasePath cannot be empty")

        now = math.floor(time())
        later = now + (expires_in * 1)
        claim = {"iss": client_id, "sub": user_id, "aud": oauth_host_name, "iat": now, "exp": later,
                 "scope": " ".join(scopes)}
        token = jwt.encode(payload=claim, key=private_key_bytes, algorithm='RS256')
        response = self.request("POST", "https://" + oauth_host_name + "/oauth/token",
                                headers=self.sanitize_for_serialization(
                                    {"Content-Type": "application/x-www-form-urlencoded"}),
                                post_params=self.sanitize_for_serialization(
                                    {"assertion": token, "grant_type": OAuth.GRANT_TYPE_JWT}))

        response_data = json.loads(response.data)

        if 'token_type' in response_data and 'access_token' in response_data:
            self.set_default_header("Authorization", response_data['token_type'] + " " + response_data['access_token'])
        else:
            raise ApiException(status=response.status,
                               reason="Error while requesting server, received a non successful HTTP code {}"
                                       " with response Body: {}".format(response.status, response.data)
                               )

        return self.deserialize(response=response, response_type=OAuthToken)

    def request_jwt_application_token(self, client_id, oauth_host_name, private_key_bytes, expires_in,
                                      scopes=(OAuth.SCOPE_SIGNATURE,)):
        """
        Request JWT Application Token
        :param client_id: DocuSign OAuth Client Id(AKA Integrator Key)
        :param oauth_host_name: DocuSign OAuth host name
        :param private_key_bytes: the byte contents of the RSA private key
        :param expires_in: number of seconds remaining before the JWT assertion is considered as invalid
        :param scopes: Optional. The list of requested scopes may include (but not limited to) You can also pass any
        advanced scope.
        :return: OAuthToken object
        """

        if not private_key_bytes:
            raise ArgumentException("Private key not supplied or is invalid!")
        if not oauth_host_name:
            raise ArgumentException("oAuthBasePath cannot be empty")

        now = math.floor(time())
        later = now + (expires_in * 1)
        claim = {"iss": client_id, "aud": oauth_host_name, "iat": now, "exp": later,
                 "scope": " ".join(scopes)}
        token = jwt.encode(payload=claim, key=private_key_bytes, algorithm='RS256')

        response = self.request("POST", "https://" + oauth_host_name + "/oauth/token",
                                headers=self.sanitize_for_serialization(
                                    {"Content-Type": "application/x-www-form-urlencoded"}),
                                post_params=self.sanitize_for_serialization(
                                    {"assertion": token, "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer"}))
        response_data = json.loads(response.data)

        if 'token_type' in response_data and 'access_token' in response_data:
            self.set_default_header("Authorization", response_data['token_type'] + " " + response_data['access_token'])
        else:
            ApiException(status=response.status,
                         reason="Error while requesting server, received a non successful HTTP code {}"
                                " with response Body: {}".format(response.status, response.data)
                         )

        return self.deserialize(response=response, response_type=OAuthToken)

    def get_user_info(self, access_token):
        """
        Get User Info method takes the accessToken to retrieve User Account Data.
        :param access_token:
        :return: The User Info model.
        """
        if not access_token:
            raise ArgumentException("Cannot find a valid access token."
                                    " Make sure OAuth is configured before you try again.")
        if not self.oauth_host_name:
            raise ArgumentException("oAuthBasePath cannot be empty")

        resource_path = '/oauth/userinfo'
        headers = {"Authorization": "Bearer " + access_token}

        response = self.request("GET", "https://" + self.oauth_host_name + resource_path, headers=headers)
        return self.deserialize(response=response, response_type=OAuthUserInfo)

    def generate_access_token(self, client_id, client_secret, code):
        """
        GenerateAccessToken will exchange the authorization code for an access token and refresh tokens.
        :param client_id: DocuSign OAuth Client Id(AKA Integrator Key)
        :param client_secret: The secret key you generated when you set up the integration in DocuSign Admin console.
        :param code: The authorization code
        :return: OAuthToken object
        """
        if not client_id or not client_secret or not code:
            raise ArgumentException
        url = "https://{0}/oauth/token".format(self.oauth_host_name)
        integrator_and_secret_key = b"Basic " + base64.b64encode(str.encode("{}:{}".format(client_id, client_secret)))
        headers = {
            "Authorization": integrator_and_secret_key.decode("utf-8"),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        post_params = self.sanitize_for_serialization({
            "grant_type": "authorization_code",
            "code": code
        })
        response = self.rest_client.POST(url, headers=headers, post_params=post_params)

        return self.deserialize(response=response, response_type=OAuthToken)

    def set_base_path(self, base_path):
        """
        :param base_path:
        :return:
        """
        self.base_path = base_path

    def set_oauth_host_name(self, oauth_host_name=None):
        """
        :param oauth_host_name:
        :return:
        """
        if oauth_host_name:
            self.oauth_host_name = oauth_host_name
            return

        if not oauth_host_name:
            raise ArgumentException('oAuthBasePath cannot be empty')

        # Derive OAuth Base Path if not given
        if self.base_path.startswith("https://demo") or self.base_path.startswith("http://demo"):
            self.oauth_host_name = OAuth.DEMO_OAUTH_BASE_PATH
        elif self.base_path.startswith("https://stage") or self.base_path.startswith("http://stage"):
            self.oauth_host_name = OAuth.STAGE_OAUTH_BASE_PATH
        else:
            self.oauth_host_name = OAuth.PRODUCTION_OAUTH_BASE_PATH

    def set_access_token(self, token_obj):
        """

        :param token_obj: 
        :return: 
        """
        self.default_headers['Authorization'] = token_obj.access_token

    def get_authorization_uri(self, client_id, scopes, redirect_uri, response_type, state=None):
        """
        Helper method to configure the OAuth accessCode/implicit flow parameters
        :param client_id: DocuSign OAuth Client Id(AKA Integrator Key)
        :param scopes: The list of requested scopes.  Client applications may be scoped to a limited set of system access.
        :param redirect_uri: This determines where to deliver the response containing the authorization code
        :param response_type: Determines the response type of the authorization request, NOTE: these response types are
        mutually exclusive for a client application. A public/native client application may only request a response type
         of "token". A private/trusted client application may only request a response type of "code".
        :param state: Allows for arbitrary state that may be useful to your application. The value in this parameter
        will be round-tripped along with the response so you can make sure it didn't change.
        :return: string
        """
        if not self.oauth_host_name:
            self.oauth_host_name = self.get_oauth_host_name()
        scopes = " ".join(scopes) if scopes else ""
        uri = "https://{}/oauth/auth?response_type={}&scope={}&client_id={}&redirect_uri={}"
        if state:
            uri += "&state={}"
        return uri.format(self.oauth_host_name, response_type, quote(scopes), client_id, redirect_uri, state)

    def get_oauth_host_name(self):
        """
        :return: string
        """
        if not self.oauth_host_name:
            self.set_oauth_host_name()

        return self.oauth_host_name
