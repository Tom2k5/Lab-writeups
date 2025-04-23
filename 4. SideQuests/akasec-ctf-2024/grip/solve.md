## Overview
![Alt text](./image/image.png)
- Bài này lúc đầu mình tưởng là mã hóa từng byte của v14, từ đó tạo flag nhưng chưa đến mức ấy.
- Mình bắt đầu công đoạn debug hàm main nhưng program nó không cho `:))`, có lẽ là anti-debug ở đâu đó => debug từ `start`.
![Alt text](./image/image-3.png)
- Debug tiếp rồi nhảy vào lệnh `call  cs:__libc_start_main_ptr` => gọi để bắt đầu main.
![Alt text](./image/image-5.png)
- Chạy tới đây thì bị exit => anti-debug tại đây. => F7 vào, ra 1 hàm.
![Alt text](./image/image-6.png)
- Theo chương trình, nó sẽ chạy về false => set IP để sang true rồi debug tiếp.
![Alt text](./image/image-7.png)
- Ta đã call đc main.
![Alt text](./image/image-8.png)
- Ngắm ngía 1 lúc thì thấy sus mỗi cái `call rdx` vì ngoài này ra program mỗi gắn biến và `call mmap`(hàm ngoài).
![Screenshot 2024-06-10 130535](./image/Screenshot%202024-06-10%20130535.png)
- Để ý kĩ, ta thấy hàm này nó có 1 vòng lặp tạo ra flag vì thấy `0x61` => "a" theo format.
## Solution
- Giờ ta leak từng byte là xong.




