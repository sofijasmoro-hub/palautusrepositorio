# Viikko 2 tehtävä 9: OpenCode

Käytin tehtävässä OpenCodea ja CurreChatin GPT-6 Luna -mallia.

## 1. Kuinka hyödyllisiä koodin täydennysehdotukset olivat?

OpenCodessa ei ole inline-täydennystä, joten käytin sen sijaan agenttia. Agentin ehdotukset olivat mielestäni hyödyllisiä.

## 2. Toteuttiko agentti top_goal_scorers-metodin docstringin mukaisesti ja luokan muun koodin tyyliin?

Kyllä. Agentti luki ensin projektin tiedostot ja toteutti metodin yhdellä rivillä: se järjestää pelaajat maalien mukaan laskevaan järjestykseen sorted- ja lambda-rakenteilla ja palauttaa how_many ensimmäistä viipaloinnilla. Tyyli oli sama kuin luokan muissa metodeissa. Lopuksi agentti tarkisti syntaksin. Ensimmäinen komento epäonnistui, koska python-komentoa ei löytynyt, mutta agentti korjasi sen itse muotoon python3.

## 3. Oliko agentin selitys Pylint-varoituksesta oikea?

Kyllä. Pylint antoi varoituksen line-too-long, koska agentin lisäämä docstring oli 110 merkkiä pitkä ja raja on 100. Agentti selitti, että sääntö pitää rivit lyhyinä luettavuuden vuoksi, ja ehdotti docstringin jakamista usealle riville. Selitys vastasi Pylintin dokumentaatiota.

## 4. Tuottiko agentti toimivan ratkaisun ja toimivat testit?

Lopulta kyllä. top_scorers_by_team toimi heti, ja kokeilin sitä itse joukkueella DAL. Testien kanssa agentti tarvitsi useamman yrityksen. Ensimmäisissä testeissä odotettu järjestys oli väärä (Player One 30 pistettä ja Player Three 25 pistettä oli merkitty väärin päin), joten kaksi testiä epäonnistui. Agentti korjasi testin, mikä oli tässä tapauksessa oikein, koska vika oli testissä eikä koodissa. Lisäksi importit eivät aluksi toimineet. Lopussa kaikki neljä testiä menivät läpi.

## 5. Erosivatko testit siitä, miten kirjoitit testejä viime viikolla?

Kyllä, muutamalla tavalla. Agentti laittoi testit kansioon tests/ eikä src/tests/. Stub sai pelaajalistan konstruktorin parametrina, kun viime viikolla lista oli kovakoodattu stubin sisään. Testimetodien nimet olivat englanniksi ja pitkiä, ja agentti ajoi testit komennolla unittest discover eikä pytest. Mukana oli myös reunatapaus (top_goal_scorers(0) palauttaa tyhjän listan), jota en olisi itse välttämättä keksinyt.

## 6. Löysikö Pylint virheitä agentin koodista?

Kyllä. Pylint löysi liian pitkän docstring-rivin sekä testitiedostosta import-error- ja wrong-import-position-virheet. Agentti korjasi importit lisäämällä sys.path-muutoksen, ja viimeisen varoituksen se hiljensi kommentilla "# pylint: disable=wrong-import-position" sen sijaan, että olisi korjannut varsinaisen syyn.

## 7. Mitä muuta opit?

Agentin tekemät muutokset pitää aina lukea ennen hyväksymistä. Kun agentti muuttaa testejä, jotta ne menisivät läpi, pitää tarkistaa, oliko vika oikeasti testissä vai koodissa. Pylint-varoitusten hiljentäminen disable-kommentilla on myös asia, jota agentti tekee helposti, ja se kannattaa huomata. Lupien kysyminen ennen komentojen ajamista (opencode.json) oli hyödyllinen, koska näin, mitä agentti oli tekemässä.
