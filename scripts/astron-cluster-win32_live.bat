@echo off
cd "../dependencies/astron/"
title Toon Island Aftermath Astron
mode con: cols=60 lines=20

:start
astrond_win32 --loglevel info config/astrond_live.yml
PAUSE
goto start
