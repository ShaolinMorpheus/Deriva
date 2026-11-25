# Gruppo iso 2 — oggetti isometrici (Deriva) — v2: scala anteprima, impronte reali, despill prima parte

Correzione su verdetto di Davide (25 nov 2026). Sostituisce i 12 oggetti della cartella `2026-11-25-gruppo-iso-2-oggetti/`: **i disegni sono gli stessi**, cambiano tre cose:

1. **Scala**: i PNG sono GIÀ ridimensionati alla scala a cui gli oggetti compaiono in `anteprima_iso2_completa.png` (stessa formula di quella anteprima: larghezza fissata, altezza in proporzione). Non vanno più scalati in gioco: si disegnano 1:1.
2. **Impronte reali**: le impronte dichiarate sono quelle vere a questa scala (verdetto di Davide per container, derrick, testa pozzo, serbatoio e baracche; gru e tubi ricavati in proporzione dalla larghezza in anteprima: (W+D) ≈ larghezza/128 — gru 700/128 ≈ 5,5 → 4,5×1, base lunga e stretta; tubi 120/128 ≈ 1 → 0,5×0,5).
3. **Despill rifatto sulla prima parte**: `derrick_iso`, `serbatoio_iso`, `baracca_iso` e `container_ocra_iso` sono stati ri-ritagliati dai disegni grezzi con l'algoritmo v3 della seconda parte (despill per tonalità su tutti i pixel + riempimento RGB delle zone trasparenti dal vicino opaco). Prima avevano ancora tinta magenta sui bordi (pixel visibili con tinta magenta forte: derrick 62.645, baracca 14.912, serbatoio 13.089, container ocra 12.758); dopo il ri-ritaglio: **0** su tutti e quattro, e residuo magenta (metrica della seconda parte) 0 su tutti i 12 file finali, verificati anche sul mare vero.

## Ancoraggio (vale per tutti)
Il punto di ancoraggio dichiarato in tabella è, in pixel nel PNG, **l'angolo frontale (sud) dell'impronta**: coincide con il vertice sud del rombo dell'impronta. Per piazzare un oggetto: vertice sud del rombo impronta = centro del rombo + (0, (W+D)·32) px (passo griglia 128×64, vedi Gruppo iso 1); l'angolo alto-sinistro del PNG va a `(vertice_sud_x − ancoraggio_x, vertice_sud_y − ancoraggio_y)`.

## I file (12 oggetti, PNG trasparenti, già in scala)
| File | Dimensioni px | Impronta (tessere) | Ancoraggio (x, y) | Note |
|---|---|---|---|---|
| `serbatoio_iso.png` | 330×188 | 1,3×1,3 | (165, 188) | Cilindro d'acciaio grigio-verde con basamento a rombo disegnato sotto: il basamento È l'impronta |
| `container_ocra_iso.png` | 480×350 | 2×2 | (240, 350) | Container ocra sbiadito, porte doppie sul lato destro |
| `container_ruggine_iso.png` | 480×352 | 2×2 | (240, 352) | Stessa forma dell'ocra, ruggine avanzata |
| `container_verde_iso.png` | 480×352 | 2×2 | (240, 352) | Stessa forma dell'ocra, verde sbiadito dal sole |
| `baracca_iso.png` | 330×273 | 1,3×1,3 | (165, 273) | Baracca di lamiere e assi su pallet, porta aperta sul lato sud-ovest |
| `baracca_interno_iso.png` | 330×278 | 1,3×1,3 | (165, 278) | Stessa baracca, parete frontale bassa aperta: officina visibile dentro |
| `derrick_iso.png` | 170×505 | 1×1 | (85, 505) | Torre di perforazione a traliccio, alta e stretta: il disegno è più stretto del rombo 1×1, la base sta al centro dell'impronta |
| `testa_pozzo_iso.png` | 260×266 | 1×1 | (130, 266) | Gruppo valvole su basamento a pattino, due volantini rossi, due manometri senza numeri |
| `gru_iso.png` | 700×303 | 4,5×1 | (350, 303) | Gru da banchina a traliccio. Il braccio sporge in aria oltre l'impronta: piazzarla in modo che il braccio resti sopra il ponte o verso il mare |
| `tubo_dritto_iso.png` | 120×78 | 0,5×0,5 | (60, 78) | Tratto di tubo dritto basso, flange bullonate alle estremità, piccolo volantino sopra |
| `tubo_curva_iso.png` | 120×68 | 0,5×0,5 | (60, 68) | Tubo a gomito morbido (curva sfalsata, non un angolo secco a 90°), flange alle estremità |
| `tubo_t_iso.png` | 120×94 | 0,5×0,5 | (60, 94) | Giunzione a T con derivazione verso il basso-fronte, flange su tutte e tre le bocche |
| `anteprima_iso2_v2_scala.png` | 3100×2150 | — | — | Anteprima di controllo (nome nuovo): piattaforma 13×9 coi pezzi iso 1 e le facce SO corrette della v2, i 12 oggetti in scala 1:1 piazzati sulle impronte reali — il rombo rosso sotto ogni oggetto È la sua impronta dichiarata; tutte le impronte stanno intere dentro la piattaforma |

## Nota di caricamento
- `anteprima_iso2_v2_scala.png` è sul repo spezzata in tre parti — `anteprima_iso2_v2_scala.png.b64.1`, `.b64.2`, `.b64.3` — per il limite di dimensione del singolo invio: concatenare in ordine e decodificare per riottenere il PNG originale a piena risoluzione (3100×2150), senza riduzioni.

## Controlli fatti
- Despill: residuo magenta 0 su tutti i 12 file (metrica seconda parte); i 4 della prima parte confrontati prima/dopo sulla tinta magenta forte: da 12.758–62.645 pixel a 0. Scheda dei 4 ri-ritagliati sul mare vero: bordi puliti, niente alone.
- Dimensioni: ricavate dalla formula dell'anteprima completa originale applicata alle dimensioni dei file v1 (es. container 1610×1177 → 480×350); la baracca interno, assente da quella anteprima, è scalata alla stessa larghezza della baracca (330) perché stessa impronta e stesso disegno di base.
- Anteprima di controllo assemblata con gli ancoraggi dichiarati: ogni oggetto poggia con l'angolo frontale sulla sua impronta, nessuna impronta a cavallo del bordo.

## Cosa NON cambia / cosa resta fuori
- Disegni, nomi dei file, materiali e stile: invariati rispetto alla v1. Le versioni a piena risoluzione restano nella cartella v1.
- `protagonista_iso.png` non è in questa cartella: resta nella v1 (sarà ridisegnato con la zattera in isometrico, 4 direzioni, in una prossima consegna).

STATO: pronto
