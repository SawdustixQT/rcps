gcc -shared utils.c -I"\lua-5.4.8\src" -L"\lua-5.4.8\src" -llua54 -o utils.dll -Wl,--export-all-symbols
pause