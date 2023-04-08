@echo off
title Toon Island Obfuscator
cd ../obfuscator
"Themida64.exe" /protect "TIAEngine.tmd" /inputfile "../build/pre_obf/TIAEngine.exe" /outputfile "../bin/TIAEngine.exe"
cd ..
PAUSE