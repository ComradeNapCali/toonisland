#!/bin/sh
clear
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo What do you want to do!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo 1 - Run Toon Island Aftermath
echo


while true; do
    read -p "Selection: " sel
    case $sel in
        [1]* )
        clear
        if [ ! -d "resources" ]; then
            echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
            echo Fetching Submodules!
            echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
            git submodule update --init
        fi
        if [ ! -d "build" ]; then
            echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
            echo Fetching Submodules!
            echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
            git submodule update --init
        fi
        clear
        echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
        echo What do you want to launch!
        echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
        echo 1 - Locally Host a Server
        echo 2 - Connect to an Existing Server
        echo
        while true; do
            read -p "Selection: " sel2
            case $sel2 in
                [1]* )
                clear
                echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
                echo Starting Localhost!
                echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
                cd scripts
                echo Launching the AI Server...
                xterm -e sh ai-server-linux.sh &
                echo Launching Astron...
                xterm -e sh astron-cluster-linux.sh &
                echo Launching the Uberdog Server...
                xterm -e sh uberdog-server-linux.sh &
                cd ..
                export TIA_GAMESERVER=127.0.0.1
                clear
                echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
                echo Username [!] This does get stored in your source code so beware!
                echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
                read -p "Username: " tiaUsername
                read -p "Password: " tiaPassowrd
                export TIA_PLAYCOOKIE=$tiaUsername$tiaPassowrd
                clear
                echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
                echo Welcome to Toon Island Aftermath, $tiaUsername!
                echo The Tooniverse Awaits You!
                echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
                while [ true ]
                do
                    /usr/bin/python -m toontown.launcher.TIAQuickStartLauncherLOCAL
                    read -r -p "Press any key to continue..." key
                done
                ;;
                [2]* )
                clear
                echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
                echo What Server are you connecting to!
                echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
                read -p "Server IP: " TIA_GAMESERVER
                TIA_GAMESERVER=${TIA_GAMESERVER:-"127.0.0.1"}
                export TIA_GAMESERVER=$TIA_GAMESERVER
                clear
                echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
                echo Username [!] This does get stored in your source code so beware!
                echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
                read -p "Username: " tiaUsername
                read -p "Password: " tiaPassowrd
                export TIA_PLAYCOOKIE=$tiaUsername$tiaPassowrd
                clear
                echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
                echo Welcome to Toon Island Aftermath, $tiaUsername!
                echo The Tooniverse Awaits You!
                echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
                while [ true ]
                do
                    /usr/bin/python -m toontown.launcher.TIAQuickStartLauncher
                    read -r -p "Press any key to continue..." key
                done
                ;;
                * ) echo "";;
            esac
        done
        ;;
        * );;
    esac
done
