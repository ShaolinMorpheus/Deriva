# Gruppo iso 2 — oggetti isometrici (Deriva)

Oggetti grandi separati, in vista isometrica 2:1, dai disegni approvati delle 4 varianti (`2026-11-25-piattaforme-isometriche/`). Ogni oggetto è un PNG trasparente, con l'ingombro a terra dichiarato: il gioco lo piazza con l'angolo frontale dell'impronta sul centro del rombo, cioè la base del disegno a `centro + (W+D)·32` px in basso (passo griglia iso 128×64, vedi Gruppo iso 1).

## I file (prima + seconda parte: 12 oggetti)
| File | Dimensioni | Impronta | Note |
|---|---|---|---|
| `serbatoio_iso.png` | 1892×1082 | 3×3 | Cilindro d'acciaio grigio-verde, colate di ruggine, rivetti, botola sopra. Il generatore gli ha messo un basamento a rombo sotto: è l'impronta 3×3 dell'oggetto, si appoggia sul ponte così com'è |
| `container_ocra_iso.png` | 1610×1177 | 4×2 | Container ocra sbiadito, corrugazione, porte doppie sul lato destro, tetto e due facce visibili |
| `container_ruggine_iso.png` | 1607×1181 | 4×2 | Stessa forma e angolazione dell'ocra, stato avanzato di ruggine: fioriture profonde, vernice scrostata, solo tracce dell'ocra originale |
| `container_verde_iso.png` | 1606×1178 | 4×2 | Stessa forma e angolazione dell'ocra, vernice verde sbiadita e desaturata dal sole, ruggine moderata su bordi e base |
| `baracca_iso.png` | 1313×1087 | 3×3 | Baracca di lamiere e assi su pallet, tetto inclinato arrugginito, porta aperta sul lato sud-ovest |
| `baracca_interno_iso.png` | 1290×1089 | 3×3 | Stessa baracca e stessa angolazione, parete frontale bassa aperta: dentro si vede l'officina (banco da lavoro con attrezzi, scaffali con barattoli e scatole, lampada appesa, casse a terra) |
| `derrick_iso.png` | 704×2092 | 4×4 | Torre di perforazione a traliccio, alta e stretta, base con tubi ai piedi |
| `testa_pozzo_iso.png` | 1034×1061 | 2×2 | Gruppo valvole su basamento a pattino: tubi d'acciaio grigio-verde, due volantini rossi, due manometri a quadrante bianco (senza numeri), flange bullonate, colate di ruggine |
| `gru_iso.png` | 1811×785 | 6×2 | Gru da banchina a traliccio: braccio lungo con cavo e gancio all'estremità, cabina operatore, contrappeso, base lunga a traliccio. Il braccio sporge in aria oltre l'impronta: piazzarla in modo che il braccio resti sopra il ponte o verso il mare |
| `tubo_dritto_iso.png` | 1404×913 | 1×1 | Tratto di tubo dritto basso, flange bullonate alle due estremità, piccolo volantino sopra al centro |
| `tubo_curva_iso.png` | 1670×960 | 1×1 | Tubo a gomito morbido (curva sfalsata, non un angolo secco a 90°), flange bullonate alle estremità |
| `tubo_t_iso.png` | 1508×1186 | 1×1 | Giunzione a T: tubo dritto con derivazione laterale verso il basso-fronte, flange su tutte e tre le bocche |
| `anteprima_iso2.png` | — | — | Anteprima prima parte: piattaforma 8×6 coi 4 oggetti originali |
| `anteprima_iso2_completa.png` | — | — | Anteprima completa: piattaforma 13×9 assemblata coi pezzi iso 1, TUTTI gli oggetti del gruppo piazzati con l'impronta intera dentro la piattaforma (più protagonista 3/4 di prova, in attesa del protagonista iso) |

Nota invio: sul repo `anteprima_iso2_completa.png` sta in due parti, `anteprima_iso2_completa.png.b64.1` e `anteprima_iso2_completa.png.b64.2` (il .b64 unico da 7,41 MB supera il limite di invio): concatenare le due parti in ordine e decodificare il base64 per ricostruire il PNG originale a piena risoluzione, bit per bit.

## Controlli fatti
- Oggetti ritagliati dal fondo magenta e verificati sul mare vero e sulla piattaforma: bordi puliti, niente alone magenta (despill per tonalità + riempimento RGB delle zone trasparenti dal vicino opaco: anche ridimensionando, dai pixel trasparenti non riaffiora magenta). Residuo magenta misurato: 0 pixel su tutti i file della seconda parte.
- I container ruggine e verde sono modifiche del disegno dell'ocra: forma, angolazione e dimensioni coincidono (1607/1606 px di larghezza contro 1610).
- Anteprima completa assemblata: gli oggetti poggiano sul ponte con la base all'angolo frontale dell'impronta (regola (W+D)·32) e ogni impronta sta intera dentro la piattaforma 13×9, mai a cavallo del bordo.

## Cosa manca
- Protagonista in isometrico (da fare quando si monta il nuovo sistema).

STATO: pronto
