## Overview
- Hàm `main()`:
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  char *v3; // rbx
  char inputChar; // al
  int v5; // r8d
  char *string1; // rax
  _BYTE *string2; // rdx

  v3 = (char *)&unk_404C;
  do
  {
    v3 += 16;
    inputChar = getc(stdin);
    *(v3 - 16) = 1;
    *(v3 - 15) = inputChar;
  }
  while ( v3 != (char *)&unk_404C + 512 );
  do
    encFUNC();
  while ( v5 != 1 );
  string1 = (char *)&string_1;
  string2 = &string_2;
  do
  {
    if ( *string1 != *string2 )
    {
      puts("Wrong!");
      return 1LL;
    }
    string1 += 16;
    ++string2;
  }
  while ( string1 != (char *)&string_1 + 512 );
  puts("Correct!");
  return 0LL;
}