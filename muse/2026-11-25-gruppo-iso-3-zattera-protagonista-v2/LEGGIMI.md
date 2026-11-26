# Gruppo iso 3 v2 — correzione zattera NE (Deriva)

Correzione della consegna `2026-11-25-gruppo-iso-3-zattera-protagonista/`: la zattera NE era uscita senza la cassa sul ponte (difetto dichiarato nel LEGGIMI della v1). Questa v2 contiene SOLO il file corretto; gli altri 7 sprite restano quelli della v1, che sostituisce solo per questo file.

## Il file
| File | Dimensioni | Impronta | Ancoraggio | Note |
|---|---|---|---|---|
| `zattera_iso_ne.png` | 640×468 | 3×2 | (320, 468) centro-basso | Stessa zattera NE della v1, stessi albero/vela ammainata, tenda, bidoni e taniche, con la cassa di legno aggiunta sul ponte davanti alla tenda, come nelle altre tre direzioni. Master a piena risoluzione in `lavoro-gruppo4a/gen_iso3/zattera_iso_ne_cassa_master.png` |

## Controlli fatti
- Ritaglio dal fondo (il generatore ha restituito lo sfondo rosso-vinoso invece del magenta: rimozione per flood-fill dal bordo, despill solo sulla zona di bordo per non spengere i rossi del disegno, es. la tanica rossa).
- Residuo colore di fondo: 0 pixel; verificata sul mare vero, bordi puliti, niente ombre.
- Tela e ancoraggio identici alla NE della v1 (640×468, (320, 468)): sostituzione diretta, senza toccare il codice di piazzamento.

STATO: pronto
