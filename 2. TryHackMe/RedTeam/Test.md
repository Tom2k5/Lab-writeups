- `rustscan -a 10.10.91.183 -sC -sV`

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

- Port: 22, 80, 8000
## Web Recon
### subdomain enumeration
- **ffuf**
```
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -u http://nahamstore.thm -H "Host: FUZZ.nahamstore.thm" -fs 0
```

```
webdisk                 [Status: 200, Size: 924, Words: 125, Lines: 25, Duration: 233ms]
whm                     [Status: 200, Size: 920, Words: 125, Lines: 25, Duration: 234ms]
test                    [Status: 200, Size: 921, Words: 125, Lines: 25, Duration: 241ms]
ns4                     [Status: 200, Size: 920, Words: 125, Lines: 25, Duration: 243ms]
smtp                    [Status: 200, Size: 921, Words: 125, Lines: 25, Duration: 244ms]
ftp                     [Status: 200, Size: 920, Words: 125, Lines: 25, Duration: 245ms]
www                     [Status: 301, Size: 194, Words: 7, Lines: 8, Duration: 245ms]
mail                    [Status: 200, Size: 921, Words: 125, Lines: 25, Duration: 245ms]
ns2                     [Status: 200, Size: 920, Words: 125, Lines: 25, Duration: 246ms]
localhost               [Status: 200, Size: 926, Words: 125, Lines: 25, Duration: 244ms]
m                       [Status: 200, Size: 918, Words: 125, Lines: 25, Duration: 245ms]
pop3                    [Status: 200, Size: 921, Words: 125, Lines: 25, Duration: 247ms]
ns1                     [Status: 200, Size: 920, Words: 125, Lines: 25, Duration: 248ms]
cpanel                  [Status: 200, Size: 923, Words: 125, Lines: 25, Duration: 248ms]
autodiscover            [Status: 200, Size: 929, Words: 125, Lines: 25, Duration: 248ms]
admin                   [Status: 200, Size: 922, Words: 125, Lines: 25, Duration: 249ms]
webmail                 [Status: 200, Size: 924, Words: 125, Lines: 25, Duration: 249ms]
ns                      [Status: 200, Size: 919, Words: 125, Lines: 25, Duration: 249ms]
dev                     [Status: 200, Size: 920, Words: 125, Lines: 25, Duration: 249ms]
```

- Lọc bỏ các subdomain có 125 word.
```
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -u http://nahamstore.thm -H "Host: FUZZ.nahamstore.thm" -fw 125
```

```python
www                     [Status: 301, Size: 194, Words: 7, Lines: 8, Duration: 242ms]
shop                    [Status: 301, Size: 194, Words: 7, Lines: 8, Duration: 247ms]
marketing               [Status: 200, Size: 2025, Words: 692, Lines: 42, Duration: 238ms]
stock                   [Status: 200, Size: 67, Words: 1, Lines: 1, Duration: 233ms]
```

```
10.10.181.29    nahamstore.thm something.nahamstore.thm www.nahamstore.thm shop.nahamstore.thm marketing.nahamstore.thm stock.nahamstore.thm
```

- **sublist3r**
```
[-] Total Unique Subdomains Found: 3
www.nahamstore.com
nahamstore-2020.nahamstore.com
shop.nahamstore.com
```

```
10.10.181.29    nahamstore.thm something.nahamstore.thm shop.nahamstore.thm marketing.nahamstore.thm stock.nahamstore.thm www.nahamstore.com nahamstore-2020.nahamstore.com
```
### Check alive domain
- **Tools:** httpx, aquatone, Eyewitness
```
cat hosts.txt | aquatone
```


![](../../Image/Pasted%20image%2020250426094810.png)


![](../../Image/Pasted%20image%2020250426094844.png)

![](../../Image/Pasted%20image%2020250426095211.png)

![](../../Image/Pasted%20image%2020250426095238.png)

![](../../Image/Pasted%20image%2020250426095308.png)

![](../../Image/Pasted%20image%2020250426095331.png)

![](../../Image/Pasted%20image%2020250426095559.png)

![](../../Image/Pasted%20image%2020250426104419.png)

![](../../Image/Pasted%20image%2020250426134046.png)
- Tìm các directory
```
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -u http://nahamstore.thm/FUZZ
```

```
search                  [Status: 200, Size: 3351, Words: 776, Lines: 72, Duration: 385ms]
login                   [Status: 200, Size: 3099, Words: 847, Lines: 61, Duration: 276ms]
staff                   [Status: 200, Size: 2287, Words: 751, Lines: 51, Duration: 264ms]
css                     [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 239ms]
js                      [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 235ms]
register                [Status: 200, Size: 3138, Words: 904, Lines: 60, Duration: 259ms]
uploads                 [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 233ms]
basket                  [Status: 200, Size: 2465, Words: 647, Lines: 54, Duration: 243ms]
```
- 