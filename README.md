## Ohjelmisto tekniikka, harjoitustyö

Alku parhaalle ***shakki*** nettisivulle (ehkä).

Changelog:
https://github.com/Bladenoodle/Echess/blob/main/laskarit/viikko3/changelog.md

### Asennus

Asenna riippuvuudet komennolla:
```
Poetry install
```

Luo database:
```
database.db < schema.sql
```

Nettisivun voi avata komennolla:

```
Poetry run invoke start
```

Testaukset voi tehdä komennoilla:
```
Poetry run invoke test
```
```
Poetry run invoke coverage-report
```
