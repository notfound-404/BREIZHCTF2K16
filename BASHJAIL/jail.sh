#!/bin/bash
. /home/game/omg

_start(){
    echo "Hi. U got $TIME second(s) to do this. Don't fap"
    sleep "$TIME"
    _quit
}

_quit(){
    echo -e '\n\033[0;31mA breton is faster than u. Bye\033[0m'
    kill -9 "$PID" &>/dev/null
    exit
}

_trapped(){
    kill "$sPID"
    local TIME="$((RANDOM%1337))"
    echo -e "Poor guyz. U wanna leave this GAME ?\nStay with me for ${TIME}s <3.\nTake a drink? For milk, ask @saxx. For beer, ask @kaluche"
    sleep "$TIME"
}


_is_hacker_or_breton(){
        [[ $1 == *[02abcdefghijklmnopqrstuvwyzABDEFGHIJKLMNOPQRSTUVWXYZ';''&'' ''"''*''`''?''.''<''>']* ]] && return 0
        return 1
}

PID="$$"
echo "PIIIID : $PID"
trap _trapped SIGINT SIGTERM
TIME=5 ; _start & sPID="$!" ; sleep 0.01

while true; do
    echo -ne "\033[32mEnter a cmd > \033[0m"
    read -r cmd
    _is_hacker_or_breton "$cmd" && {
            echo -e '\033[0;31mDont hack me !\033[0m'
            exit 1
        } || {
            out="echo Your command is: $cmd"
            eval "$out"
    }
done
