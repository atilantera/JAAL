Notes from https://json-schema.org/understanding-json-schema/

- `uri`: URI (URL)  (draft 6)
- `pattern`: regular expressions
- `title` and `description` are optional, but recommended
- `examples` provide example data for documentation
- `enum`: enumerated values
- `contentMediaType`: XML inside JSON
- `$ref` mahdollistaa osaskeemaan viittaamisen samassa tiedostossa,
    esim: `"$ref": "#/definitions/address"`

Näitä ei toistaiseksi:
- `dependencies`: yksi ominaisuus voi vaatia toisia. (Ei laiteta rajoituksia ennen kuin speksi on kunnolla muovautunut.) Tämä voisi olla tulevaisuudessa: jos on ilmoitettu, että jonkin tietorakenteen tulkinnaksi on ilmoitettu binääripuu, pitää vaatia jokaiselle solmulle enintään kaksi lasta.
- `allOf`, `anyOf`, `not`, `if`-`then`-`else`: samanlaista
edistynyttä kamaa.

JAALin JSON-skeema yhdessä tiedostossa vs. useammassa

Yksi tiedosto
-------------
+ nopeampi ladata yhdellä HTTP-pyynnöllä

Useampi tiedosto
----------------
+ git näyttää, mitä moduuleita muutettu
+ pienempi koko per tiedosto
  -> helpompi navigoida
+ moduulikohtainen testaus
  + testidatatiedostoissa vain olennainen
  + yhden moduulin muuttaminen ei vaikuta muiden moduulien yksikkötesteihin
+ voidaan muuttaa yhdeksi tiedostoksi jollain JSON schema bundlerilla, esim.
   https://www.npmjs.com/package/gulp-jsonschema-bundle
