# V1

## Connections

Types:

```python
from kater.types.v1 import Connection, DatabaseConfig, SyncEventResponse, ConnectionListResponse
```

Methods:

- <code title="get /api/v1/connections">client.v1.connections.<a href="./src/kater/resources/v1/connections/connections.py">list</a>(\*\*<a href="src/kater/types/v1/connection_list_params.py">params</a>) -> <a href="./src/kater/types/v1/connection_list_response.py">ConnectionListResponse</a></code>

## GitHub

### Repos

Types:

```python
from kater.types.v1.github import Repository
```

### Scaffold

Types:

```python
from kater.types.v1.github import ScaffoldTrigger
```

## Groups

Types:

```python
from kater.types.v1 import GroupDetail
```

## Me

Types:

```python
from kater.types.v1 import ClientUser, ClientUserRole
```

## Org

### Client

Types:

```python
from kater.types.v1.org import Client, TenancyType
```

## Tenants

Types:

```python
from kater.types.v1 import CreateTenant, Tenant
```

### Batch

Types:

```python
from kater.types.v1.tenants import BatchTenantError, BatchTenantSuccess
```

### Import

Types:

```python
from kater.types.v1.tenants import ImportTenants
```

Methods:

- <code title="post /api/v1/tenants/import/csv">client.v1.tenants.import*.<a href="./src/kater/resources/v1/tenants/import*.py">from_csv</a>(\*\*<a href="src/kater/types/v1/tenants/import_from_csv_params.py">params</a>) -> <a href="./src/kater/types/v1/tenants/import_tenants.py">ImportTenants</a></code>
- <code title="post /api/v1/tenants/import/warehouse">client.v1.tenants.import*.<a href="./src/kater/resources/v1/tenants/import*.py">from_warehouse</a>(\*\*<a href="src/kater/types/v1/tenants/import_from_warehouse_params.py">params</a>) -> <a href="./src/kater/types/v1/tenants/import_tenants.py">ImportTenants</a></code>
