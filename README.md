main.py on Python 3 skript, mille eesmärk on testida XSS haavatavuse olemasolu Riigihangete registri esilehel oleva otsinguväljaga seotud lähtekoodis. Esileht asub aadressil https://riigihanked.riik.ee/rhr-web/#/ Käesolev Python 3 skript on loodud RIK testija proovitöö teshnilise osa ülesanne nimega "Variant C" lahendamiseks. Ülesanne nõuab Selenium raamistiku kasutamist. Skript on esialgu loodud edukalt tuvastama kindlasti olemas olevat XSS haavatavust OWASP testrakenuse Juice Shop esilehel oleva otsinguväljaga seotud lähtekoodis https://juice-shop.herokuapp.com/#/ Seejärel skripti on kohandatud orienteerumiseks Riigihangete registri esilehel.

Systeeminõuded/installimine

Skript on loodud töötamiseks Python 3.10.6, Ubuntu 22.04.1 LTS operatsioonisüsteemis aga õigete keskkonnamuudatustega võiks töötada näiteks Windows 10 all ning võib olla ka vanema Python vesrsiooni all.

Kõik käsud on edaspidi Linuxi jaoks.

Sõltuvused olid installitud venv virtuaalkeskkonda. Valik on kasutaja oma, aga venv puhul see peaks olema globaalselt installitud.

Projekti kaustas nimega SeleniumXSS tuleb käivitada python3 -m venv venv
Luuakse uut kaustat nimega venv
Kaustasse SeleniumXSS tuleb kopeerida main.py fail
Virtuaalkeskkonna käivitamiseks tuleb kirjutada käsureale source venv/bin/activate
Käsurea algusesse ilmub (venv)
Virtuaalkeskkond on aktiivne, kõik sõltuvused installitakse sinna.
Pythoni versiooni võib kontrollida käsuga python3 -V
Tuleb installida Selenium käsuga python3 -m pip install selenium

Skript kasutab webdriverina Chrome. Faili nimeks on chromedriver. Linux süsteemis see tuleb paigutada kas kaustasse /usr/bin või /usr/local/bin
chromedriver saab aadressilt https://sites.google.com/a/chromium.org/chromedriver/downloads

Nüüd main.py peaks olema töökorras. Kõik ülejäänud sõltuvused on lahendatud import abil main.py alguses.

Kasutamine

Skripti käivitamiseks tuleb käsureal kirjutada python3 main.py

(venv) [user@workstation SeleniumXSS]$ python3 main.py

Ilmub Chrome internetilehitseja aken Riigihangete registri esilehega ja umbes 15 sekundi pärast kaob.
Käsureale ilmub teade, mis algab "no alert" ja lõpeb "OK". See tähendab, et Riigihangete registri esilehel oleva otsinguväljaga seotud lähtekoodis ei ole XSS haavatavust. Kui käsureale "no alert" asemele ilmub "alert accepted", siis Riigihangete registri esilehel oleva otsinguväljaga seotud lähtekoodis on olemas XSS haavatavus.

