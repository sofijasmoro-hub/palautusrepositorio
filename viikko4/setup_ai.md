# Tehtävä 4: testien siistiminen agentilla

Käytin OpenCodea (Build-agentti) ja pyysin sitä siirtämään testien yhteiset alustukset setUp-metodiin muuttamatta testien toiminnallisuutta.

**Poistiko agentti toisteisuuden järkevästi? Onko koodi luettavampaa?**
Kyllä. Agentti siirsi mockien luomisen ja niiden toteutukset setUp-metodiin, ja testitiedosto lyheni noin 144 rivistä 72 riviin. Jokaisessa testissä näkyy nyt vain se, mikä testissä on olennaista, eli mitä koriin lisätään ja mitä tilisiirrolta odotetaan. Siksi testit ovat helpompia lukea. Agentti poisti myös käyttämättömät importit (ANY, Viitegeneraattori, Varasto).

**Muuttiko agentti testien toiminnallisuutta?**
Ei. Kaikki testit menevät edelleen läpi, ja assert_called_with-tarkistukset säilyivät. Agentti ei siis vaihtanut niitä heikompaan assert_called-muotoon. Tarkistin tämän git diffillä.

**Jouduinko korjaamaan agentin muutoksia?**
En. Muutos oli sellainen kuin pyysin, joten hyväksyin sen sellaisenaan.
