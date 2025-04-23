## Overview
- Độ khó normal.
- Đề cho ta 1 file ELF.
- Hàm **main()**
```
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  int i; // [rsp+0h] [rbp-280h]
  int j; // [rsp+4h] [rbp-27Ch]
  int k; // [rsp+8h] [rbp-278h]
  int m; // [rsp+Ch] [rbp-274h]
  int v8[48]; // [rsp+10h] [rbp-270h] BYREF
  __int64 th[46]; // [rsp+D0h] [rbp-1B0h] BYREF
  char s[56]; // [rsp+240h] [rbp-40h] BYREF
  unsigned __int64 v11; // [rsp+278h] [rbp-8h]

  v11 = __readfsqword(0x28u);
  printf("FLAG: ");
  if ( (unsigned int)__isoc99_scanf("%45s") == 1 )
  {
    if ( strlen(s) == 45 )
    {
      for ( i = 0; i <= 44; ++i )
        dword_561755396140[i] = s[i];
      pthread_mutex_init(&mutex, 0LL);
      for ( j = 0; j <= 44; ++j )
      {
        v8[j] = j;
        pthread_create((pthread_t *)&th[j], 0LL, start_routine, &v8[j]);
      }
      for ( k = 0; k <= 44; ++k )
        pthread_join(th[k], 0LL);
      pthread_mutex_destroy(&mutex);
      for ( m = 0; m <= 44; ++m )
      {
        if ( dword_561755396140[m] != dword_561755396020[m] )
        {
          puts("Incorrect.");
          return 1LL;
        }
      }
      puts("Correct!");
      return 0LL;
    }
    else
    {
      puts("Incorrect.");
      return 1LL;
    }
  }
  else
  {
    puts("Failed to scan.");
    return 1LL;
  }
}
```
- Đầu tiên, chương trình bắt ta nhập 1 string với hàm *__isoc99_scanf()*.
- Nếu độ dài string khác 45 và scanf() != 1, chương trình in *Incorrect* hoặc *Failed to scan*.
- Ta rút gọn để nhìn cho rõ:
```
if ( (unsigned int)__isoc99_scanf("%45s") == 1 )
  {
    if ( strlen(s) == 45 )
    {
      ...
    }
    else
    {
      puts("Incorrect.");
      return 1LL;
    }
  }
  else
  {
    puts("Failed to scan.");
    return 1LL;
  }
```
- Tiếp theo, chuỗi *dword_561755396140* copy chuỗi nhập và bị biến đổi bởi hàm `pthread_create()` với parameter `start_routine()`.
```
  for ( i = 0; i <= 44; ++i ) {
    dword_561755396140[i] = s[i];
    thread_mutex_init(&mutex, 0LL);
  }
  for ( j = 0; j <= 44; ++j ) {
      v8[j] = j;
      pthread_create((pthread_t *)&th[j], 0LL, start_routine, &v8[j]);
  }
  for ( k = 0; k <= 44; ++k ) {
    pthread_join(th[k], 0LL);
    pthread_mutex_destroy(&mutex);
  }
```
- Hàm *start_routine()*
```
void *__fastcall start_routine(int *a1)
{
  int v2; // [rsp+14h] [rbp-Ch]
  int v3; // [rsp+18h] [rbp-8h]
  int v4; // [rsp+1Ch] [rbp-4h]

  v3 = *a1;
  v2 = 0;
  while ( v2 <= 2 )
  {
    pthread_mutex_lock(&mutex);
    v4 = (unk_56508FD50200[v3] + v3) % 3;
    if ( !v4 )
      dword_56508FD50140[v3] *= 3;
    if ( v4 == 1 )
      dword_56508FD50140[v3] += 5;
    if ( v4 == 2 )
      dword_56508FD50140[v3] ^= 0x7Fu;
    v2 = ++unk_56508FD50200[v3];
    pthread_mutex_unlock(&mutex);
  }
  return 0LL;
}
```
- Sau khi bị encrypted, chương trình check bằng cách so sánh với chuỗi *dword_561755396020*.
```
for ( m = 0; m <= 44; ++m ) {
  if ( dword_561755396140[m] != dword_561755396020[m] ) {
    puts("Incorrect.");
    return 1LL;
  }
}
puts("Correct!");
return 0LL;
```
## Solution
- Để tìm ra flag, ta chỉ cần lấy string *dword_561755396020* rồi decrypt bằng cách dịch ngược hàm *start_routine()*.
- Trước hết, tóm tắt lại quá trình biến đổi input:
Hàm *main()*
```
for ( j = 0; j <= 44; ++j ) {
  v8[j] = j;
  pthread_create(&th[j], 0LL, start_routine, &v8[j]);
}
```
Hàm *start_routine()*
```
void routine(int *a1){
  int v2;
  int v3;
  int v4;
  v3 = *a1;
  v2 = 0;
  while(v2 <= 2){
    v4 = (dword_5621E95B4200[v3] + v3) % 3;
    if(!v4) 
      dword_5621E95B4140[v3] *= 3;
    if(v4 == 1) 
      dword_5621E95B4140[v3] += 5;
    if(v4 == 2)
      dword_5621E95B4140[v3] ^= 0x7f
    v2 = ++dword_5621E95B4200[v3];
  }
}
```
- Lưu ý: Mảng *dword_5621E95B4200* gồm các phần tử giá trị 0. Sau khi xong 1 vòng lặp, từng phần tử mảng tăng lên 3 => khi dịch ngược, giảm dần từ 2 -> 0.
- **Reversing Script:**
```
enc_flag = [168,138,191,165,765,89,222,36,101,271,222,35,349,66,44,222,9,101,222,81,239,319,36,83,349,72,83,222,9,83,331,36,101,222,54,83,349,18,74,292,63,95,334,213,11]

for j in range(len(enc_flag)):
    for i in range(2, -1, -1): # 2 -> 0
        v4 = (j + i) % 3
        if v4 == 0:
            enc_flag[j] //= 3
        elif v4 == 1:
            enc_flag[j] -= 5
        elif v4 == 2:
            enc_flag[j] ^= 0x7f
for i in enc_flag:
    print(chr(i), end = "")
```
- Flag: `FLAG{c4n_y0u_dr4w_4_1ine_be4ween_4he_thread3}`
