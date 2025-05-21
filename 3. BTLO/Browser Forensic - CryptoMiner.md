### **Tools**
---
- BrowserHistoryViewer
- FTK Imager
### **Scenario**
---
Our SOC alerted that there is some traffic related to crypto mining from a PC that was just joined to the network. The incident response team acted immediately, observed that the traffic is originating from browser applications. After collecting all key browser data using FTK Imager, it is your job to use the **ad1** file to investigate the crypto mining activity.
## **Overview**
---
- **BrowserHistoryViewer** là công cụ xem và phân tích lịch sử duyệt web trên máy tính từ các trình duyệt như Chrome, Firefox, Edge.
- **FTK Imager** là phần mềm tạo bản sao forensic của ổ đĩa, xem dữ liệu, và kiểm tra tính toàn vẹn bằng hash, hỗ trợ định dạng như E01, DD.
- File **AD1** là một định dạng tệp hình ảnh forensic được tạo bởi FTK Imager, phần mềm của AccessData, sử dụng để lưu trữ bản sao dữ liệu bit-by-bit của ổ đĩa hoặc phân vùng.

## Methodology
---
- Chrome browser-profiles: 



### Challenge Submission
---
1. How many browser-profiles are present in Google Chrome?
	- Answer: 2
2. What is the name of the browser theme installed on Google Chrome?
	-  Answer: earth in space
3. Identify the Extension ID and Extension Name of the cryptominer _(2 points)_
	- **Answer:** egnfmleidkolminhjlkaomjefheafbbb, DFP Cryptocurrency Miner
4. What is the description text of this extension? _(1 points)_
	- **Answer:** Allows staff members to mine cryptocurrency in the background of their web browser
5. What is the name of the specific javascript web miner used in the browser extension? _(1 points)_
	- **Answer:** CryptoLoot
6. How many hashes is the crypto miner calculating per second? _(2 points)_
	- **Answer:** 20
7. What is the public key associated with this mining activity? _(1 points)_
	- **Answer:** b23efb4650150d5bc5b2de6f05267272cada06d985a0
8. What is the URL of the official Twitter page of the javascript web miner? _(1 points)_
	- **Answer**: twitter.com/CryptoLootMiner