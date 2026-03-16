# V1

## Compiler

Types:

```python
from kater.types.v1 import (
    ChartConfig,
    CompilerErrorItem,
    InlineField,
    Manifest,
    ManifestEntry,
    RefWithLabel,
    SubqueryCondition,
    CompilerCompileResponse,
    CompilerCompileDashboardResponse,
    CompilerEnumerateResponse,
    CompilerExecuteResponse,
    CompilerResolveResponse,
    CompilerValidateResponse,
)
```

Methods:

- <code title="post /api/v1/compiler/compile">client.v1.compiler.<a href="./src/kater/resources/v1/compiler/compiler.py">compile</a>(\*\*<a href="src/kater/types/v1/compiler_compile_params.py">params</a>) -> <a href="./src/kater/types/v1/compiler_compile_response.py">CompilerCompileResponse</a></code>
- <code title="post /api/v1/compiler/dashboard">client.v1.compiler.<a href="./src/kater/resources/v1/compiler/compiler.py">compile_dashboard</a>(\*\*<a href="src/kater/types/v1/compiler_compile_dashboard_params.py">params</a>) -> <a href="./src/kater/types/v1/compiler_compile_dashboard_response.py">CompilerCompileDashboardResponse</a></code>
- <code title="post /api/v1/compiler/enumerate">client.v1.compiler.<a href="./src/kater/resources/v1/compiler/compiler.py">enumerate</a>(\*\*<a href="src/kater/types/v1/compiler_enumerate_params.py">params</a>) -> <a href="./src/kater/types/v1/compiler_enumerate_response.py">CompilerEnumerateResponse</a></code>
- <code title="post /api/v1/compiler/execute">client.v1.compiler.<a href="./src/kater/resources/v1/compiler/compiler.py">execute</a>(\*\*<a href="src/kater/types/v1/compiler_execute_params.py">params</a>) -> <a href="./src/kater/types/v1/compiler_execute_response.py">CompilerExecuteResponse</a></code>
- <code title="post /api/v1/compiler/resolve">client.v1.compiler.<a href="./src/kater/resources/v1/compiler/compiler.py">resolve</a>(\*\*<a href="src/kater/types/v1/compiler_resolve_params.py">params</a>) -> <a href="./src/kater/types/v1/compiler_resolve_response.py">CompilerResolveResponse</a></code>
- <code title="post /api/v1/compiler/validate">client.v1.compiler.<a href="./src/kater/resources/v1/compiler/compiler.py">validate</a>(\*\*<a href="src/kater/types/v1/compiler_validate_params.py">params</a>) -> <a href="./src/kater/types/v1/compiler_validate_response.py">CompilerValidateResponse</a></code>

### Combination

Types:

```python
from kater.types.v1.compiler import CombinationPreviewResponse
```

Methods:

- <code title="post /api/v1/compiler/combination/preview">client.v1.compiler.combination.<a href="./src/kater/resources/v1/compiler/combination.py">preview</a>(\*\*<a href="src/kater/types/v1/compiler/combination_preview_params.py">params</a>) -> <a href="./src/kater/types/v1/compiler/combination_preview_response.py">CombinationPreviewResponse</a></code>

### Manifest

Types:

```python
from kater.types.v1.compiler import ManifestRegenerateAndCreatePrResponse
```

Methods:

- <code title="post /api/v1/compiler/manifest/recovery-pr">client.v1.compiler.manifest.<a href="./src/kater/resources/v1/compiler/manifest.py">regenerate_and_create_pr</a>(\*\*<a href="src/kater/types/v1/compiler/manifest_regenerate_and_create_pr_params.py">params</a>) -> <a href="./src/kater/types/v1/compiler/manifest_regenerate_and_create_pr_response.py">ManifestRegenerateAndCreatePrResponse</a></code>

## Connections

Types:

```python
from kater.types.v1 import Connection, ConnectionListConnectionsResponse
```

Methods:

- <code title="get /api/v1/connections">client.v1.connections.<a href="./src/kater/resources/v1/connections/connections.py">list_connections</a>(\*\*<a href="src/kater/types/v1/connection_list_connections_params.py">params</a>) -> <a href="./src/kater/types/v1/connection_list_connections_response.py">ConnectionListConnectionsResponse</a></code>

### Client

#### Mcp

##### Servers

Types:

```python
from kater.types.v1.connections.client.mcp import (
    ServerCreateResponse,
    ServerUpdateResponse,
    ServerListResponse,
    ServerDiscoverResponse,
    ServerRediscoverResponse,
    ServerUpdateConfigResponse,
)
```

Methods:

- <code title="post /api/v1/client/mcp/servers">client.v1.connections.client.mcp.servers.<a href="./src/kater/resources/v1/connections/client/mcp/servers.py">create</a>(\*\*<a href="src/kater/types/v1/connections/client/mcp/server_create_params.py">params</a>) -> <a href="./src/kater/types/v1/connections/client/mcp/server_create_response.py">ServerCreateResponse</a></code>
- <code title="put /api/v1/client/mcp/servers/{mcp_id}">client.v1.connections.client.mcp.servers.<a href="./src/kater/resources/v1/connections/client/mcp/servers.py">update</a>(mcp_id, \*\*<a href="src/kater/types/v1/connections/client/mcp/server_update_params.py">params</a>) -> <a href="./src/kater/types/v1/connections/client/mcp/server_update_response.py">ServerUpdateResponse</a></code>
- <code title="get /api/v1/client/mcp/servers">client.v1.connections.client.mcp.servers.<a href="./src/kater/resources/v1/connections/client/mcp/servers.py">list</a>() -> <a href="./src/kater/types/v1/connections/client/mcp/server_list_response.py">ServerListResponse</a></code>
- <code title="delete /api/v1/client/mcp/servers/{mcp_id}">client.v1.connections.client.mcp.servers.<a href="./src/kater/resources/v1/connections/client/mcp/servers.py">delete</a>(mcp_id) -> None</code>
- <code title="post /api/v1/client/mcp/servers/{mcp_id}/discover">client.v1.connections.client.mcp.servers.<a href="./src/kater/resources/v1/connections/client/mcp/servers.py">discover</a>(mcp_id) -> <a href="./src/kater/types/v1/connections/client/mcp/server_discover_response.py">ServerDiscoverResponse</a></code>
- <code title="post /api/v1/client/mcp/servers/{mcp_id}/rediscover">client.v1.connections.client.mcp.servers.<a href="./src/kater/resources/v1/connections/client/mcp/servers.py">rediscover</a>(mcp_id) -> <a href="./src/kater/types/v1/connections/client/mcp/server_rediscover_response.py">ServerRediscoverResponse</a></code>
- <code title="put /api/v1/client/mcp/servers/{mcp_id}/api-key">client.v1.connections.client.mcp.servers.<a href="./src/kater/resources/v1/connections/client/mcp/servers.py">update_api_key</a>(mcp_id, \*\*<a href="src/kater/types/v1/connections/client/mcp/server_update_api_key_params.py">params</a>) -> None</code>
- <code title="patch /api/v1/client/mcp/servers/{mcp_id}/config">client.v1.connections.client.mcp.servers.<a href="./src/kater/resources/v1/connections/client/mcp/servers.py">update_config</a>(mcp_id, \*\*<a href="src/kater/types/v1/connections/client/mcp/server_update_config_params.py">params</a>) -> <a href="./src/kater/types/v1/connections/client/mcp/server_update_config_response.py">ServerUpdateConfigResponse</a></code>

### OAuth

Types:

```python
from kater.types.v1.connections import OAuthHandleCallbackResponse
```

Methods:

- <code title="get /api/v1/oauth/callback">client.v1.connections.oauth.<a href="./src/kater/resources/v1/connections/oauth.py">handle_callback</a>(\*\*<a href="src/kater/types/v1/connections/oauth_handle_callback_params.py">params</a>) -> <a href="./src/kater/types/v1/connections/oauth_handle_callback_response.py">OAuthHandleCallbackResponse</a></code>

### Tenant

#### Mcp

Types:

```python
from kater.types.v1.connections.tenant import McpListResponse, McpGetAuditHistoryResponse
```

Methods:

- <code title="get /api/v1/tenant/mcp">client.v1.connections.tenant.mcp.<a href="./src/kater/resources/v1/connections/tenant/mcp/mcp.py">list</a>(\*\*<a href="src/kater/types/v1/connections/tenant/mcp_list_params.py">params</a>) -> <a href="./src/kater/types/v1/connections/tenant/mcp_list_response.py">McpListResponse</a></code>
- <code title="get /api/v1/tenant/mcp/{mcp_id}/audit">client.v1.connections.tenant.mcp.<a href="./src/kater/resources/v1/connections/tenant/mcp/mcp.py">get_audit_history</a>(mcp_id, \*\*<a href="src/kater/types/v1/connections/tenant/mcp_get_audit_history_params.py">params</a>) -> <a href="./src/kater/types/v1/connections/tenant/mcp_get_audit_history_response.py">McpGetAuditHistoryResponse</a></code>

##### Credentials

Methods:

- <code title="delete /api/v1/tenant/mcp/{mcp_id}/credentials">client.v1.connections.tenant.mcp.credentials.<a href="./src/kater/resources/v1/connections/tenant/mcp/credentials.py">revoke</a>(mcp_id, \*\*<a href="src/kater/types/v1/connections/tenant/mcp/credential_revoke_params.py">params</a>) -> None</code>

##### OAuth

Types:

```python
from kater.types.v1.connections.tenant.mcp import OAuthInitiateResponse
```

Methods:

- <code title="get /api/v1/tenant/mcp/{mcp_id}/oauth/authorize">client.v1.connections.tenant.mcp.oauth.<a href="./src/kater/resources/v1/connections/tenant/mcp/oauth.py">initiate</a>(mcp_id, \*\*<a href="src/kater/types/v1/connections/tenant/mcp/oauth_initiate_params.py">params</a>) -> <a href="./src/kater/types/v1/connections/tenant/mcp/oauth_initiate_response.py">OAuthInitiateResponse</a></code>

## Tenants

Types:

```python
from kater.types.v1 import ImportTenantsResponse, TenantGetTenantsSchemaResponse
```

Methods:

- <code title="get /api/v1/tenants/schema">client.v1.tenants.<a href="./src/kater/resources/v1/tenants/tenants.py">get_tenants_schema</a>() -> <a href="./src/kater/types/v1/tenant_get_tenants_schema_response.py">TenantGetTenantsSchemaResponse</a></code>
- <code title="post /api/v1/tenants/import/csv">client.v1.tenants.<a href="./src/kater/resources/v1/tenants/tenants.py">import_from_csv</a>(\*\*<a href="src/kater/types/v1/tenant_import_from_csv_params.py">params</a>) -> <a href="./src/kater/types/v1/import_tenants_response.py">ImportTenantsResponse</a></code>
- <code title="post /api/v1/tenants/import/warehouse">client.v1.tenants.<a href="./src/kater/resources/v1/tenants/tenants.py">import_from_warehouse</a>(\*\*<a href="src/kater/types/v1/tenant_import_from_warehouse_params.py">params</a>) -> <a href="./src/kater/types/v1/import_tenants_response.py">ImportTenantsResponse</a></code>

### Groups

Types:

```python
from kater.types.v1.tenants import GroupGetTenantGroupsSchemaResponse
```

Methods:

- <code title="get /api/v1/tenants/groups/schema">client.v1.tenants.groups.<a href="./src/kater/resources/v1/tenants/groups.py">get_tenant_groups_schema</a>() -> <a href="./src/kater/types/v1/tenants/group_get_tenant_groups_schema_response.py">GroupGetTenantGroupsSchemaResponse</a></code>
