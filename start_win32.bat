@echo off
title Toon Island Aftermath CLI Launcher

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PYTHON_PATH=<PYTHON_PATH

echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo What do you want to do!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo.
echo #1 - Run Toon Island Aftermath
echo #2 - Run TIA Level Editor
echo #3 - Exit
echo.
:selection
choice /C:123 /n /m "Selection: "%1
if errorlevel ==3 EXIT
if errorlevel ==2 goto leveleditor
if errorlevel ==1 goto run


:run
cls
echo ===============================================================
echo What do you want to launch!
echo ===============================================================
echo. 
echo #1 - Locally Host a Server
echo #2 - Connect to an Existing Server
echo.
choice /C:12 /n /m "Selection: "%1
if errorlevel ==2 goto connect
if errorlevel ==1 goto localhost


:localhost
cls 
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Starting Localhost!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
cd scripts
echo Launching the AI Server...
START ai-server-win32.bat
echo Launching Astron...
START astron-cluster-win32.bat
echo Launching the Uberdog Server...
START uberdog-server-win32.bat
cd ..
goto game

:connect
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Gameserver [!]
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
set /P TIA_GAMESERVER="Gameserver: "
SET TIA_GAMESERVER=%TIA_GAMESERVER%
echo.
goto game

:game
cls
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Username [!] This does get stored in your source code so beware!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
set /P TIA_Username="Username: "
set /P TIA_Password="Password: "
echo.
cls
SET TIA_PLAYCOOKIE=%TIA_Username%%TIA_Password%
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Welcome to Toon Island Aftermath, %TIA_Username%!
echo The Tooniverse Awaits You!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
:startgame
title Toon Island Aftermath Client
%PYTHON_PATH% -m toontown.launcher.TIAQuickStartLauncherLOCAL
PAUSE
goto startgame

:leveleditor
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Welcome to the TIA Level Editor!
echo This tool is still in its early stages!
echo Bugs are EXPECTED!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
cd editor
:startleveleditor
title Toon Island Level Editor - Debugger
%PYTHON_PATH% -m ttle
PAUSE
goto startleveleditor
