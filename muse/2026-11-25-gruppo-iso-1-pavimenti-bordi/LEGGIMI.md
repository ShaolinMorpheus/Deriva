# Gruppo iso 1 — pavimenti e bordi isometrici (Deriva)

Primo set di pezzi isometrici, costruito dalle varianti approvate da Davide il 25 nov 2026 (cartella `2026-11-25-piattaforme-isometriche`). Sostituisce la 4a a tessere quadrate, supersata dalla svolta isometrica.

## Geometria (da rispettare nel gioco)
- Ogni pezzo: PNG 256×256 trasparente, allineato alla sua tessera.
- Rombo 2:1: alto (128,64), destro (256,128), basso (128,192), sinistro (0,128); centro rombo (128,128).
- Centro della tessera (i,j) sullo schermo: `x = OX + (i−j)·128`, `y = OY + (i+j)·64`; il canvas si piazza con l'angolo alto-sinistro a (centro − 128, centro − 128). Disegnare in ordine pittore per (i+j) crescente.
- Le facce stanno nello stesso canvas sotto il rombo (spessore 64 px, fino a y 256): si disegnano con la tessera, prima del rombo della tessera a sud, così l'ordine pittore le copre dove serve.

## I file (tutti 256×256, PNG trasparenti, tranne palo_iso 96×256)
| File | Note |
|---|---|
| `ponte_iso_a.png`, `ponte_iso_b.png`, `ponte_iso_c.png` | Rombo di lamiera striata con ruggine e macchie di petrolio; varianti con interni diversi e cornice comune: si affiancano senza giunture |
| `ponte_iso_buco.png` | Buco trasparente al centro, lamiera piegata sul bordo (non si cammina) |
| `pontile_iso_a.png`, `pontile_iso_b.png` | Rombo di assi di legno bagnato con alghe |
| `faccia_se.png`, `faccia_so.png` | Faccia sud-est / sud-ovest in acciaio scuro rivettato, alta 64 px, linea di galleggiamento in basso; la SO è un pelo più scura |
| `faccia_legno_se.png`, `faccia_legno_so.png` | Facce in legno per il pontile, con un pneumatico appeso come parabordo (centro del pneumatico trasparente) |
| `bordo_ne.png`, `bordo_no.png` | Ringhiera arrugginita lungo il lato nord-est / nord-ovest: 2 correnti, 4 montanti, si alza ~43 px sopra il bordo |
| `bordo_angolo_nord.png` | Angolo nord con entrambe le ringhiere e montante d'angolo più alto |
| `palo_iso.png` | Palo singolo 96×256 da piazzare sotto facce e pontile; la base sfuma in acqua |
| `anteprima_iso1.png` | Piattaforma 6×4 rombi assemblata con questi pezzi: facce, ringhiere nord, pontile a sud-ovest con pali, oggetti 3/4 di prova (container, serbatoio, baracca, protagonista), zattera attraccata, sul mare vero |

## Come sono fatti (dichiarato)
- I rombi sono le trame tileabili del Gruppo 4a (lamiera striata e legno bagnato) deformate a programma nella geometria 2:1; la cornice comune delle varianti garantisce l'affiancamento senza giunture.
- Facce, ringhiere e palo disegnati a programma nelle misure esatte. Niente ombre proiettate, niente contorno scuro, niente scritte.

## Controlli fatti
- Prima versione scartata e rifatta: il ponte veniva bucherellato da una maschera sbagliata (decine di fori circolari). Controllo numerico sulla versione definitiva: 0 buchi nei rombi pieni (solo antialias del bordo, 192 px semitrasparenti sul perimetro); buco vero solo in `ponte_iso_buco` (3.025 px).
- Anteprima assemblata dai pezzi veri (non un disegno unico): rombi affiancati senza buchi né giunture visibili, facce continue lungo il perimetro sud, ringhiere continue sui lati nord, pontile con pneumatici sulle facce e pali in acqua.
- Limiti dichiarati: gli oggetti nell'anteprima sono i disegni 3/4 già approvati (non ancora isometrici puri); la zattera è quella dall'alto del Gruppo 2.

## Cosa manca / prossime consegne
- Oggetti isometrici separati (derrick, testa pozzo, tubi, gru, serbatoi grandi, fusti) — Gruppo iso 2.
- Zattera e protagonista in isometrico quando si monta il nuovo sistema (Claude: griglia a rombi).

STATO: pronto
