# Gruppo iso 1 — pavimenti e bordi isometrici (Deriva) — v2: facce SO corrette

Correzione su verdetto di Davide (25 nov 2026): sostituisce SOLO `faccia_so.png` e `faccia_legno_so.png` della cartella `2026-11-25-gruppo-iso-1-pavimenti-bordi/`. Tutti gli altri pezzi restano quelli della v1, invariati.

## Il difetto e la correzione
- Nella v1 le due facce SO facevano una «scalinata»: il bordo basso era orizzontale a y=256 mentre quello alto saliva da (0,128) a (128,192), quindi lo spessore variava da 128 px a sinistra a 64 px a destra (misurato sulle colonne: 124 / 112 / 96 / 80 / 68).
- Ora le facce SO hanno **spessore 64 uniforme**, col bordo basso parallelo a quello alto, esattamente come la SE: bordo alto da (0,128) a (128,192), bordo basso da (0,192) a (128,256).
- Verifica numerica: spessore misurato 65 px (64 + 1 px di antialias sul bordo) in TUTTE le colonne campionate (x = 8, 32, 64, 96, 120) per entrambe le facce — identico alla faccia SE della v1 misurata allo stesso modo (65 px alle colonne 136–248).
- Rigenerate con la stessa funzione e gli stessi materiali della v1: acciaio scuro rivettato con linea di galleggiamento in basso (luminosità 0,46, un pelo più scura della SE) e legno con pneumatico appeso come parabordo (luminosità 0,53); giunture, rivetti e linea d'acqua ridisegnati sulla geometria corretta. Canvas 256×256 trasparente, stessa posizione nella tessera: si montano come le vecchie, senza toccare nient'altro.

## I file
| File | Note |
|---|---|
| `faccia_so.png` | Faccia sud-ovest in acciaio, spessore 64 uniforme — sostituisce la v1 |
| `faccia_legno_so.png` | Faccia sud-ovest in legno per il pontile, con pneumatico appeso, spessore 64 uniforme — sostituisce la v1 |

## Cosa NON cambia
- Geometria della tessera e regole di montaggio del Gruppo iso 1 (rombo (128,64)(256,128)(128,192)(0,128), passo (128,64), facce sotto il rombo nello stesso canvas).
- Tutti gli altri 13 pezzi della v1.

STATO: pronto
