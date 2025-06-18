---

---
- **Tags:** #WebExploitation
---
## **Enumeration**

```
rustscan -a nahamstore.thm -- -sC -sV
```

```
PORT     STATE SERVICE REASON         VERSION
22/tcp   open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 84:6e:52:ca:db:9e:df:0a:ae:b5:70:3d:07:d6:91:78 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDk0dfNL0GNTinnjUpwRlY3LsS7cLO2jAp3QRvFXOB+s+bPPk+m4duQ95Z6qagERl/ovdPsSJTdiPXy2Qpf+aZI4ba2DvFWfvFzfh9Jrx7rvzrOj0i0kUUwot9WmxhuoDfvTT3S6LmuFw7SAXVTADLnQIJ4k8URm5wQjpj86u7IdCEsIc126krLk2Nb7A3qoWaI+KJw0UHOR6/dhjD72Xl0ttvsEHq8LPfdEhPQQyefozVtOJ50I1Tc3cNVsz/wLnlLTaVui2oOXd/P9/4hIDiIeOI0bSgvrTToyjjTKH8CDet8cmzQDqpII6JCvmYhpqcT5nR+pf0QmytlUJqXaC6T
|   256 1a:1d:db:ca:99:8a:64:b1:8b:10:df:a9:39:d5:5c:d3 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBC/YPu9Zsy/Gmgz+aLeoHKA1L5FO8MqiyEaalrkDetgQr/XoRMvsIeNkArvIPMDUL2otZ3F57VBMKfgydtBcOIA=
|   256 f6:36:16:b7:66:8e:7b:35:09:07:cb:90:c9:84:63:38 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPAicOmkn8r1FCga8kLxn9QC7NdeGg0bttFiaaj11qec
80/tcp   open  http    syn-ack ttl 63 nginx 1.14.0 (Ubuntu)
|_http-title: NahamStore - Home
|_http-server-header: nginx/1.14.0 (Ubuntu)
| http-cookie-flags: 
|   /: 
|     session: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD POST
8000/tcp open  http    syn-ack ttl 62 nginx 1.18.0 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_http-open-proxy: Proxy might be redirecting requests
| http-methods: 
|_  Supported Methods: GET HEAD POST
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


---
#### **Recon**
> Using a combination of subdomain enumeration, brute force, content discovery and fuzzing find all the subdomains you can and answer the below questions.
- Answer the questions below:

**Jimmy Jones SSN**
-> 

#### **XSS**
> We've put quite a few XSS vulnerabilities into the web application. See if you can find them all and answer the questions below.
- **Answer the questions below:**

Enter an URL ( including parameters ) of an endpoint that is vulnerable to XSS  
-> 

What HTTP header can be used to create a Stored XXS  
-> 

What HTML tag needs to be escaped on the product page to get the XSS to work?  
-> 

What JavaScript variable needs to be escaped to get the XSS to work?  
-> 

What hidden parameter can be found on the shop home page that introduces an XSS vulnerability.  
-> 

What HTML tag needs to be escaped on the returns page to get the XSS to work?  
-> 

What is the value of the H1 tag of the page that uses the requested URL to create an XSS  
-> 

What other hidden parameter can be found on the shop which can introduce an XSS vulnerability ?
-> 

