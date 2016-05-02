#!/bin/bash

# python create_punch_card.py -w data_nude.png 'KK OO'
# python create_punch_card.py -r grandpa1.png ''


PARAM_ENIGMA=(
    'Einstellungen: 01 01 01'
    'walzenlage: III II I'
    'ringstellung: 01 01 01'
    'reflektor: B'
    'steckerverbindungen: GA ME FN YJ SO PC VD KI XH WZ'
    'I love useless datas'
    'Qrpbqvat ebg13 whfg2ybfr gur tnzr vf ernyyl qvfgnfgrshy'
    'advertising : https://www.notfound.ovh/'
)

CODE_FORTRAN=(
    '      program Hello;Print *,"Hello World!";end program Hello'
    '      program Ctf;Print *,"BREIZH IS SO COOL!";end program Ctf'
    '      program Beer;Print *,"Need a beer!";end program Beer'
    '      program Ntfd;Print *,"<3 Notfound <3";end program Ntfd'
    '      program X;Print*,achar(71),achar(65),achar(77),achar(69);end program X'
    '      Credit card number: 5698'
    '      Paramours phone number: 020 7946 1337'
    '      ## system error ##'
    '      Microsoft Windows is the worst OS EVER'
)

CF='fortran_nude.png'
CD='data_nude.png'

for i in "${CODE_FORTRAN[@]}"; do
    python create_punch_card.py -w "$CF" "${i^^}"
done
for i in "${PARAM_ENIGMA[@]}"; do
    python create_punch_card.py -w "$CD" "${i^^}"
done

[ "$1" == "-v" ] && {
    echo "--- Verification ---"
    for i in ALL_CARD/*.png; do
        python create_punch_card.py -r $i ''
    done
}
