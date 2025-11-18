
```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Aloitus "1" -- "1" Ruutu
    Vankila "1" -- "1" Ruutu
    Monopolipeli "1" -- "1" Aloitus
    Monopolipeli "1" -- "1" Vankila
    Ruutu "6" -- "6" Sattumaa ja yhteismaa
    Sattumaa ja yhteismaa "6" -- "32" kortteja
    Toiminto "32" -- "32" kortteja
    Monopolipeli "1" -- "6" Sattumaa ja yhteismaa
    Monopolipeli "1" -- "4" Asemat ja laitokset
    Ruutu "6" -- "6" Asemat ja laitokset
    Ruutu "26" -- "26" Normaalit kadut
    Normaalit kadut "26" -- "26" kadun nimet
    Monopolipeli "1" -- "26" Normaalit kadut
    Monopolipeli "1" -- "32" Talot
    Monopolipeli "1" -- "12" Hotellit
    Normaalit kadut "1" -- "4" Talot
    Normaalit kadut "1" -- "1" Hotellit
    Normaalit kadut "1" -- "1" Pelaaja
    Pelaaja "1" -- Raha
    Monopolipeli "1" -- "20 580" Raha

```