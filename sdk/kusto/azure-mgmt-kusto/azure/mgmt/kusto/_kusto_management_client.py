# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import KustoManagementClientConfiguration
from .operations import ClustersOperations
from .operations import DatabasesOperations
from .operations import AttachedDatabaseConfigurationsOperations
from .operations import DataConnectionsOperations
from .operations import Operations
from . import models


class KustoManagementClient(SDKClient):
    """The Azure Kusto management API provides a RESTful set of web services that interact with Azure Kusto services to manage your clusters and databases. The API enables you to create, update, and delete clusters and databases.

    :ivar config: Configuration for client.
    :vartype config: KustoManagementClientConfiguration

    :ivar clusters: Clusters operations
    :vartype clusters: azure.mgmt.kusto.operations.ClustersOperations
    :ivar databases: Databases operations
    :vartype databases: azure.mgmt.kusto.operations.DatabasesOperations
    :ivar attached_database_configurations: AttachedDatabaseConfigurations operations
    :vartype attached_database_configurations: azure.mgmt.kusto.operations.AttachedDatabaseConfigurationsOperations
    :ivar data_connections: DataConnections operations
    :vartype data_connections: azure.mgmt.kusto.operations.DataConnectionsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.kusto.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = KustoManagementClientConfiguration(credentials, subscription_id, base_url)
        super(KustoManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-09-07'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.clusters = ClustersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.databases = DatabasesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.attached_database_configurations = AttachedDatabaseConfigurationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.data_connections = DataConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
