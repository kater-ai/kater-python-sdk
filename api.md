# V1

## Connections

Types:

```python
from kater.types.v1 import (
    Connection,
    DatabaseConfig,
    ConnectionListResponse,
    ConnectionRetrieveCredentialResponse,
    ConnectionSyncResponse,
)
```

Methods:

- <code title="post /api/v1/connections">client.v1.connections.<a href="./src/kater/resources/v1/connections/connections.py">create</a>(\*\*<a href="src/kater/types/v1/connection_create_params.py">params</a>) -> <a href="./src/kater/types/v1/connection.py">Connection</a></code>
- <code title="get /api/v1/connections/{connection_id}">client.v1.connections.<a href="./src/kater/resources/v1/connections/connections.py">retrieve</a>(connection_id) -> <a href="./src/kater/types/v1/connection.py">Connection</a></code>
- <code title="patch /api/v1/connections/{connection_id}">client.v1.connections.<a href="./src/kater/resources/v1/connections/connections.py">update</a>(connection_id, \*\*<a href="src/kater/types/v1/connection_update_params.py">params</a>) -> <a href="./src/kater/types/v1/connection.py">Connection</a></code>
- <code title="get /api/v1/connections">client.v1.connections.<a href="./src/kater/resources/v1/connections/connections.py">list</a>() -> <a href="./src/kater/types/v1/connection_list_response.py">ConnectionListResponse</a></code>
- <code title="delete /api/v1/connections/{connection_id}">client.v1.connections.<a href="./src/kater/resources/v1/connections/connections.py">delete</a>(connection_id) -> None</code>
- <code title="get /api/v1/connections/{connection_id}/credential">client.v1.connections.<a href="./src/kater/resources/v1/connections/connections.py">retrieve_credential</a>(connection_id) -> <a href="./src/kater/types/v1/connection_retrieve_credential_response.py">ConnectionRetrieveCredentialResponse</a></code>
- <code title="post /api/v1/connections/{connection_id}/sync">client.v1.connections.<a href="./src/kater/resources/v1/connections/connections.py">sync</a>(connection_id) -> <a href="./src/kater/types/v1/connection_sync_response.py">ConnectionSyncResponse</a></code>

### Databases

Methods:

- <code title="delete /api/v1/connections/{connection_id}/databases/{database_id}/schemas/{schema_id}">client.v1.connections.databases.<a href="./src/kater/resources/v1/connections/databases.py">delete_schema</a>(schema_id, \*, connection_id, database_id) -> None</code>

## GitHub

Types:

```python
from kater.types.v1 import (
    GitHubConnectResponse,
    GitHubGetInstallationLinkResponse,
    GitHubGetStatusResponse,
)
```

Methods:

- <code title="get /api/v1/github/callback">client.v1.github.<a href="./src/kater/resources/v1/github/github.py">callback</a>(\*\*<a href="src/kater/types/v1/github_callback_params.py">params</a>) -> object</code>
- <code title="get /api/v1/github/connect">client.v1.github.<a href="./src/kater/resources/v1/github/github.py">connect</a>(\*\*<a href="src/kater/types/v1/github_connect_params.py">params</a>) -> <a href="./src/kater/types/v1/github_connect_response.py">GitHubConnectResponse</a></code>
- <code title="get /api/v1/github/installation-link">client.v1.github.<a href="./src/kater/resources/v1/github/github.py">get_installation_link</a>() -> <a href="./src/kater/types/v1/github_get_installation_link_response.py">GitHubGetInstallationLinkResponse</a></code>
- <code title="get /api/v1/github/status">client.v1.github.<a href="./src/kater/resources/v1/github/github.py">get_status</a>() -> <a href="./src/kater/types/v1/github_get_status_response.py">GitHubGetStatusResponse</a></code>

### Repos

Types:

```python
from kater.types.v1.github import Repository, RepoListResponse, RepoSelectResponse
```

Methods:

- <code title="get /api/v1/github/repos">client.v1.github.repos.<a href="./src/kater/resources/v1/github/repos.py">list</a>() -> <a href="./src/kater/types/v1/github/repo_list_response.py">RepoListResponse</a></code>
- <code title="post /api/v1/github/repos/{repo_id}/select">client.v1.github.repos.<a href="./src/kater/resources/v1/github/repos.py">select</a>(repo_id, \*\*<a href="src/kater/types/v1/github/repo_select_params.py">params</a>) -> <a href="./src/kater/types/v1/github/repo_select_response.py">RepoSelectResponse</a></code>

### Scaffold

Types:

```python
from kater.types.v1.github import ScaffoldTrigger
```

Methods:

- <code title="post /api/v1/github/scaffold/retry">client.v1.github.scaffold.<a href="./src/kater/resources/v1/github/scaffold.py">retry</a>() -> <a href="./src/kater/types/v1/github/scaffold_trigger.py">ScaffoldTrigger</a></code>
- <code title="post /api/v1/github/scaffold">client.v1.github.scaffold.<a href="./src/kater/resources/v1/github/scaffold.py">trigger</a>() -> <a href="./src/kater/types/v1/github/scaffold_trigger.py">ScaffoldTrigger</a></code>

### Webhooks

Types:

```python
from kater.types.v1.github import WebhookReceiveResponse
```

Methods:

- <code title="post /api/v1/github/webhooks/receiver">client.v1.github.webhooks.<a href="./src/kater/resources/v1/github/webhooks.py">receive</a>() -> <a href="./src/kater/types/v1/github/webhook_receive_response.py">WebhookReceiveResponse</a></code>

## Groups

Types:

```python
from kater.types.v1 import GroupDetail, GroupListResponse
```

Methods:

- <code title="post /api/v1/groups">client.v1.groups.<a href="./src/kater/resources/v1/groups/groups.py">create</a>(\*\*<a href="src/kater/types/v1/group_create_params.py">params</a>) -> <a href="./src/kater/types/v1/group_detail.py">GroupDetail</a></code>
- <code title="get /api/v1/groups/{group_id}">client.v1.groups.<a href="./src/kater/resources/v1/groups/groups.py">retrieve</a>(group_id) -> <a href="./src/kater/types/v1/group_detail.py">GroupDetail</a></code>
- <code title="patch /api/v1/groups/{group_id}">client.v1.groups.<a href="./src/kater/resources/v1/groups/groups.py">update</a>(group_id, \*\*<a href="src/kater/types/v1/group_update_params.py">params</a>) -> <a href="./src/kater/types/v1/group_detail.py">GroupDetail</a></code>
- <code title="get /api/v1/groups">client.v1.groups.<a href="./src/kater/resources/v1/groups/groups.py">list</a>() -> <a href="./src/kater/types/v1/group_list_response.py">GroupListResponse</a></code>
- <code title="delete /api/v1/groups/{group_id}">client.v1.groups.<a href="./src/kater/resources/v1/groups/groups.py">delete</a>(group_id) -> None</code>

### Tenants

Types:

```python
from kater.types.v1.groups import TenantAddResponse
```

Methods:

- <code title="post /api/v1/groups/{group_id}/tenants">client.v1.groups.tenants.<a href="./src/kater/resources/v1/groups/tenants.py">add</a>(group_id, \*\*<a href="src/kater/types/v1/groups/tenant_add_params.py">params</a>) -> <a href="./src/kater/types/v1/groups/tenant_add_response.py">TenantAddResponse</a></code>
- <code title="delete /api/v1/groups/{group_id}/tenants/{tenant_id}">client.v1.groups.tenants.<a href="./src/kater/resources/v1/groups/tenants.py">remove</a>(tenant_id, \*, group_id) -> None</code>

## Me

Types:

```python
from kater.types.v1 import ClientUser, ClientUserRole
```

Methods:

- <code title="get /api/v1/me">client.v1.me.<a href="./src/kater/resources/v1/me.py">retrieve</a>() -> <a href="./src/kater/types/v1/client_user.py">ClientUser</a></code>

## Org

### Client

Types:

```python
from kater.types.v1.org import Client, TenancyType
```

Methods:

- <code title="get /api/v1/org/client">client.v1.org.client.<a href="./src/kater/resources/v1/org/client.py">retrieve</a>() -> <a href="./src/kater/types/v1/org/client.py">Client</a></code>
- <code title="patch /api/v1/org/client">client.v1.org.client.<a href="./src/kater/resources/v1/org/client.py">update</a>(\*\*<a href="src/kater/types/v1/org/client_update_params.py">params</a>) -> <a href="./src/kater/types/v1/org/client.py">Client</a></code>

### Users

Types:

```python
from kater.types.v1.org import UserListResponse, UserDeleteResponse
```

Methods:

- <code title="post /api/v1/org/users">client.v1.org.users.<a href="./src/kater/resources/v1/org/users.py">create</a>(\*\*<a href="src/kater/types/v1/org/user_create_params.py">params</a>) -> <a href="./src/kater/types/v1/client_user.py">ClientUser</a></code>
- <code title="get /api/v1/org/users/{user_id}">client.v1.org.users.<a href="./src/kater/resources/v1/org/users.py">retrieve</a>(user_id) -> <a href="./src/kater/types/v1/client_user.py">ClientUser</a></code>
- <code title="patch /api/v1/org/users/{user_id}">client.v1.org.users.<a href="./src/kater/resources/v1/org/users.py">update</a>(user_id, \*\*<a href="src/kater/types/v1/org/user_update_params.py">params</a>) -> <a href="./src/kater/types/v1/client_user.py">ClientUser</a></code>
- <code title="get /api/v1/org/users">client.v1.org.users.<a href="./src/kater/resources/v1/org/users.py">list</a>() -> <a href="./src/kater/types/v1/org/user_list_response.py">UserListResponse</a></code>
- <code title="delete /api/v1/org/users/{user_id}">client.v1.org.users.<a href="./src/kater/resources/v1/org/users.py">delete</a>(user_id) -> <a href="./src/kater/types/v1/org/user_delete_response.py">UserDeleteResponse</a></code>

## Tenants

Types:

```python
from kater.types.v1 import CreateTenant, Tenant, TenantListResponse
```

Methods:

- <code title="post /api/v1/tenants">client.v1.tenants.<a href="./src/kater/resources/v1/tenants/tenants.py">create</a>(\*\*<a href="src/kater/types/v1/tenant_create_params.py">params</a>) -> <a href="./src/kater/types/v1/tenant.py">Tenant</a></code>
- <code title="get /api/v1/tenants/{tenant_id}">client.v1.tenants.<a href="./src/kater/resources/v1/tenants/tenants.py">retrieve</a>(tenant_id) -> <a href="./src/kater/types/v1/tenant.py">Tenant</a></code>
- <code title="patch /api/v1/tenants/{tenant_id}">client.v1.tenants.<a href="./src/kater/resources/v1/tenants/tenants.py">update</a>(tenant_id, \*\*<a href="src/kater/types/v1/tenant_update_params.py">params</a>) -> <a href="./src/kater/types/v1/tenant.py">Tenant</a></code>
- <code title="get /api/v1/tenants">client.v1.tenants.<a href="./src/kater/resources/v1/tenants/tenants.py">list</a>() -> <a href="./src/kater/types/v1/tenant_list_response.py">TenantListResponse</a></code>
- <code title="delete /api/v1/tenants/{tenant_id}">client.v1.tenants.<a href="./src/kater/resources/v1/tenants/tenants.py">delete</a>(tenant_id) -> None</code>

### Batch

Types:

```python
from kater.types.v1.tenants import (
    BatchTenantError,
    BatchTenantSuccess,
    BatchCreateResponse,
    BatchUpdateResponse,
    BatchDeleteResponse,
)
```

Methods:

- <code title="post /api/v1/tenants/batch">client.v1.tenants.batch.<a href="./src/kater/resources/v1/tenants/batch.py">create</a>(\*\*<a href="src/kater/types/v1/tenants/batch_create_params.py">params</a>) -> <a href="./src/kater/types/v1/tenants/batch_create_response.py">BatchCreateResponse</a></code>
- <code title="patch /api/v1/tenants/batch">client.v1.tenants.batch.<a href="./src/kater/resources/v1/tenants/batch.py">update</a>(\*\*<a href="src/kater/types/v1/tenants/batch_update_params.py">params</a>) -> <a href="./src/kater/types/v1/tenants/batch_update_response.py">BatchUpdateResponse</a></code>
- <code title="delete /api/v1/tenants/batch">client.v1.tenants.batch.<a href="./src/kater/resources/v1/tenants/batch.py">delete</a>(\*\*<a href="src/kater/types/v1/tenants/batch_delete_params.py">params</a>) -> <a href="./src/kater/types/v1/tenants/batch_delete_response.py">BatchDeleteResponse</a></code>

### Import

Types:

```python
from kater.types.v1.tenants import ImportTenants
```

Methods:

- <code title="post /api/v1/tenants/import/csv">client.v1.tenants.import*.<a href="./src/kater/resources/v1/tenants/import*.py">from_csv</a>(\*\*<a href="src/kater/types/v1/tenants/import_from_csv_params.py">params</a>) -> <a href="./src/kater/types/v1/tenants/import_tenants.py">ImportTenants</a></code>
- <code title="post /api/v1/tenants/import/warehouse">client.v1.tenants.import*.<a href="./src/kater/resources/v1/tenants/import*.py">from_warehouse</a>(\*\*<a href="src/kater/types/v1/tenants/import_from_warehouse_params.py">params</a>) -> <a href="./src/kater/types/v1/tenants/import_tenants.py">ImportTenants</a></code>

# Healthz

Types:

```python
from kater.types import HealthzCheckResponse
```

Methods:

- <code title="get /healthz">client.healthz.<a href="./src/kater/resources/healthz.py">check</a>() -> <a href="./src/kater/types/healthz_check_response.py">HealthzCheckResponse</a></code>

# Readyz

Types:

```python
from kater.types import ReadyzCheckResponse
```

Methods:

- <code title="get /readyz">client.readyz.<a href="./src/kater/resources/readyz.py">check</a>() -> <a href="./src/kater/types/readyz_check_response.py">ReadyzCheckResponse</a></code>
