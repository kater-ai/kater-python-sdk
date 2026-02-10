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
    CompilerResolveResponse,
    CompilerValidateResponse,
)
```

Methods:

- <code title="post /api/v1/compiler/compile">client.v1.compiler.<a href="./src/kater/resources/v1/compiler.py">compile</a>(\*\*<a href="src/kater/types/v1/compiler_compile_params.py">params</a>) -> <a href="./src/kater/types/v1/compiler_compile_response.py">CompilerCompileResponse</a></code>
- <code title="post /api/v1/compiler/resolve">client.v1.compiler.<a href="./src/kater/resources/v1/compiler.py">resolve</a>(\*\*<a href="src/kater/types/v1/compiler_resolve_params.py">params</a>) -> <a href="./src/kater/types/v1/compiler_resolve_response.py">CompilerResolveResponse</a></code>
- <code title="post /api/v1/compiler/validate">client.v1.compiler.<a href="./src/kater/resources/v1/compiler.py">validate</a>(\*\*<a href="src/kater/types/v1/compiler_validate_params.py">params</a>) -> <a href="./src/kater/types/v1/compiler_validate_response.py">CompilerValidateResponse</a></code>

## Connections

Types:

```python
from kater.types.v1 import Connection, ConnectionListConnectionsResponse
```

Methods:

- <code title="get /api/v1/connections">client.v1.connections.<a href="./src/kater/resources/v1/connections/connections.py">list_connections</a>(\*\*<a href="src/kater/types/v1/connection_list_connections_params.py">params</a>) -> <a href="./src/kater/types/v1/connection_list_connections_response.py">ConnectionListConnectionsResponse</a></code>

### Tenants

Types:

```python
from kater.types.v1.connections import TenantRetrieveSchemaResponse
```

Methods:

- <code title="get /api/v1/tenants/schema">client.v1.connections.tenants.<a href="./src/kater/resources/v1/connections/tenants/tenants.py">retrieve_schema</a>() -> <a href="./src/kater/types/v1/connections/tenant_retrieve_schema_response.py">TenantRetrieveSchemaResponse</a></code>

#### Groups

Types:

```python
from kater.types.v1.connections.tenants import GroupRetrieveSchemaResponse
```

Methods:

- <code title="get /api/v1/tenants/groups/schema">client.v1.connections.tenants.groups.<a href="./src/kater/resources/v1/connections/tenants/groups.py">retrieve_schema</a>() -> <a href="./src/kater/types/v1/connections/tenants/group_retrieve_schema_response.py">GroupRetrieveSchemaResponse</a></code>

## Tenants

Types:

```python
from kater.types.v1 import ImportTenantsResponse
```

Methods:

- <code title="post /api/v1/tenants/import/csv">client.v1.tenants.<a href="./src/kater/resources/v1/tenants.py">import_from_csv</a>(\*\*<a href="src/kater/types/v1/tenant_import_from_csv_params.py">params</a>) -> <a href="./src/kater/types/v1/import_tenants_response.py">ImportTenantsResponse</a></code>
- <code title="post /api/v1/tenants/import/warehouse">client.v1.tenants.<a href="./src/kater/resources/v1/tenants.py">import_from_warehouse</a>(\*\*<a href="src/kater/types/v1/tenant_import_from_warehouse_params.py">params</a>) -> <a href="./src/kater/types/v1/import_tenants_response.py">ImportTenantsResponse</a></code>
