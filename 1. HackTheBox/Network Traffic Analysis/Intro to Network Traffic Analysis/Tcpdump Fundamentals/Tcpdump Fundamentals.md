- **Utilizing the output shown in question-1.png, who is the server in this communication? (IP Address)**

![[question-1.png]]

⇒ `**174.143.213.184**`

⇒ **Web Server kết nối qua TCP.**

- **Were absolute or relative sequence numbers used during the capture? (see question-1.zip to answer)**

⇒ `Relative SEQ number` vì mặc định là theo tương đối, còn tuyệt đối thì dùng `tcpdump -S`

- If I wish to start a capture without hostname resolution, verbose output, showing contents in ASCII and hex, and grab the first 100 packets; what are the switches used? please answer in the order the switches are asked for in the question.

⇒ `-nvXc 100`

- Given the capture file at /tmp/capture.pcap, what tcpdump command will enable you to read from the capture and show the output contents in Hex and ASCII? (Please use best practices when using switches)

⇒ `sudo tcpdump -Xr /tmp/capture.pcap`