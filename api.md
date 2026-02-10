# V1

## Connections

Types:

```python
from kater.types.v1 import Connection, ConnectionListConnectionsResponse
```

Methods:

- <code title="get /api/v1/connections">client.v1.connections.<a href="./src/kater/resources/v1/connections/connections.py">list_connections</a>(\*\*<a href="src/kater/types/v1/connection_list_connections_params.py">params</a>) -> <a href="./src/kater/types/v1/connection_list_connections_response.py">ConnectionListConnectionsResponse</a></code>

### Compiler

Types:

```python
from kater.types.v1.connections import (
    CompilerCompileResponse,
    CompilerResolveResponse,
    CompilerValidateResponse,
)
```

Methods:

- <code title="post /api/v1/compiler/compile">client.v1.connections.compiler.<a href="./src/kater/resources/v1/connections/compiler.py">compile</a>(\*\*<a href="src/kater/types/v1/connections/compiler_compile_params.py">params</a>) -> <a href="./src/kater/types/v1/connections/compiler_compile_response.py">CompilerCompileResponse</a></code>
- <code title="post /api/v1/compiler/resolve">client.v1.connections.compiler.<a href="./src/kater/resources/v1/connections/compiler.py">resolve</a>(\*\*<a href="src/kater/types/v1/connections/compiler_resolve_params.py">params</a>) -> <a href="./src/kater/types/v1/connections/compiler_resolve_response.py">CompilerResolveResponse</a></code>
- <code title="post /api/v1/compiler/validate">client.v1.connections.compiler.<a href="./src/kater/resources/v1/connections/compiler.py">validate</a>(\*\*<a href="src/kater/types/v1/connections/compiler_validate_params.py">params</a>) -> <a href="./src/kater/types/v1/connections/compiler_validate_response.py">CompilerValidateResponse</a></code>

## Tenants

Types:

```python
from kater.types.v1 import ImportTenantsResponse
```

Methods:

- <code title="post /api/v1/tenants/import/csv">client.v1.tenants.<a href="./src/kater/resources/v1/tenants.py">import_from_csv</a>(\*\*<a href="src/kater/types/v1/tenant_import_from_csv_params.py">params</a>) -> <a href="./src/kater/types/v1/import_tenants_response.py">ImportTenantsResponse</a></code>
- <code title="post /api/v1/tenants/import/warehouse">client.v1.tenants.<a href="./src/kater/resources/v1/tenants.py">import_from_warehouse</a>(\*\*<a href="src/kater/types/v1/tenant_import_from_warehouse_params.py">params</a>) -> <a href="./src/kater/types/v1/import_tenants_response.py">ImportTenantsResponse</a></code>
