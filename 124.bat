@echo off
title hackeado aaaaaaaaa
taskkil /f /im explorer.exe /PID 8972
:bucle
cls
msg * holaaaaaaaa
echo.
echo.
color 04
echo ================================================================
echo =                                                              =
echo =                       Que desafortunado                      = 
echo =                                                              =
echo ================================================================
set /p pass=coloca la pass: 
if %pass%==WIF (goto passcorrecto) ELSE (goto :bucle)
:passcorrecto
timeout /t 20 /nobreak >nul
start explorer.exe
echo bueno ":v"
pause 
exit
