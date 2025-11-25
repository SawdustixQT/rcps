REM Для определения текущей директории 
cd /d "%~dp0"
set folder=%CD%
echo %folder%

REM Компиляция
gcc main.c -I%folder%\lua-5.4.8\src -L%folder%\lua-5.4.8\src -llua -ISDL2-2.32.10\x86_64-w64-mingw32\include\SDL2 -LSDL2-2.32.10\x86_64-w64-mingw32\lib -w -lmingw32 -lSDL2main -lSDL2 -o test.exe
test.exe