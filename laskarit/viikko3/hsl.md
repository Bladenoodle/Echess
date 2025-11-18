
``` mermaid
sequenceDiagram
    participant main
    participant laitehallinto as HKLLaitehallinto
    participant rautatietori as Lataajalaite
    participant ratikka6 as Lukijalaite
    participant bussi244 as Lukijalaite2
    participant lippu_luukku as Kioski
    participant kallen_kortti as Matkakortti
    
    main->>laitehallinto: HKLLaitehallinto()
    main->>rautatietori: Lataajalaite()
    main->>ratikka6: Lukijalaite()
    main->>bussi244: Lukijalaite()

    main->>laitehallinto: lisaa_lataaja(rautatietori)
    laitehallinto-->>main: -
    main->>laitehallinto: lisaa_lukija(ratikka6)
    laitehallinto-->>main: -
    main->>laitehallinto: lisaa_lukija(bussi244)
    laitehallinto-->>main: -

    main->>lippu_luukku: Kioski()
    main->>lippu_luukku: osta_matkakortti("Kalle")
    lippu_luukku->>kallen_kortti: Matkakortti("Kalle")
    kallen_kortti-->>lippu_luukku: uusi_kortti
    lippu_luukku-->>main: kallen_kortti

    main->>rautatientori: lataa_arvoa(kallen_kortti, 3)
    rautatientori->>kallen_kortti: kasvata_arvoa(3)
    kallen_kortti->>rautatientori: -
    rautatientori->> main: -

    main->>ratikka6: osta_lippu(kallen_kortti, 0)
    ratikka6->>kallen_kortti: tarkista arvo, vahenna_arvoa(RATIKKA)
    kallen_kortti-->>ratikka6: True/False
    ratikka6-->>main: True/False

    main->>bussi244: osta_lippu(kallen_kortti, 2)
    bussi244->>kallen_kortti: tarkista arvo, vahenna_arvoa(SEUTU)
    kallen_kortti-->>bussi244: True/False
    bussi244-->>main: True/False
```
