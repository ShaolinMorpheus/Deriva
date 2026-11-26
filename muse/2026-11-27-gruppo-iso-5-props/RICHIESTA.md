# Richiesta a Muse — Gruppo iso 5: oggetti di scena per la piattaforma (Deriva)

**Perché.** La piattaforma ha ora una logica (torre e pozzo, tubi che portano al serbatoio vicino al molo per il rifornimento, magazzini e gru sul lato dietro, baracca accanto al serbatoio). Ma con soli 10 oggetti è mezza vuota. Serve il **disordine abitato**: roba improvvisata, riparata, accatastata, di recupero. Mondo di rottami, ruggine, tele, corde, lamiere; chi ci vive ha costruito tutto con quello che il mare restituisce.

**Regole uguali al resto (Gruppi iso 2/3):** vista isometrica 2:1, luce da in alto a sinistra, nessun contorno scuro, sfondo magenta pieno per il ritaglio, stessi materiali e colori sbiaditi di container, baracca e gru. Scala: il protagonista è alto 100 px; un'impronta di 1 tessera = rombo 256×128 px. Per ogni oggetto: PNG trasparente, dichiarare impronta in tessere (larghezza lungo SE × lungo SO), altezza e ancoraggio (centro-basso della base), come nel Gruppo iso 2. Alone magenta zero.

**Regola di altezza (importante per la vista):** gli oggetti in primo piano e vicino al molo devono essere **bassi** (non più di ~60 px, cioè sotto il ginocchio-vita del protagonista); quelli alti (>120 px) vanno solo dove stanno dietro agli altri. Meglio fare di ogni cosa 2–3 varianti basse che un solo oggetto alto.

## Elenco (in ordine di priorità)
1. **Barili di carburante**: singolo (3 varianti: in piedi, rovesciato, con tappo aperto), gruppo da 3 e catasta da 6 legata con corda. Impronta 0,5×0,5 / 1×1 / 1,3×1. Bassi.
2. **Casse e cassette di legno**: singola (2 varianti), catasta da 2 e da 3, una con telo. Impronta 0,6×0,6 / 1×1. Bassi.
3. **Tela di fortuna tesa su pali** (tettoia): sopra un tavolo di lamiera o dei sacchi; impronta 2×1,5, altezza ~130 px, **con il lato di fronte aperto** (si cammina sotto). Un secondo modello più piccolo.
4. **Pompa di rifornimento con manichetta** a bordo molo (colonnina arrugginita + tubo avvolto), impronta 0,8×0,8, alta ~90 px. E un **tratto di tubo** che esce dal serbatoio (dritto, ad angolo, lungo entrambi gli assi: SE e SO).
5. **Lampione/faro su palo** di recupero (lampada, fili) alto ~160 px; e una **lanterna a terra** bassa.
6. **Antenna/radio**: palo con fili e un pannello di lamiera, alto ~200 px (va dietro).
7. **Stenditoio con panni**: due pali e una corda con 3–4 panni stracciati, impronta 2×0,3 (due orientamenti: lungo SE e lungo SO), alto ~110 px.
8. **Rastrelliera con reti e ami** (pesca), e **un cavalletto con pesci essiccati**, impronta 1,5×0,5, alti ~100 px.
9. **Raccoglitore di acqua piovana**: telo a imbuto su struttura + fusto sotto; impronta 1×1, alto ~110 px. **Pannello solare di fortuna** inclinato su cavalletto, impronta 1×1, alto ~80 px.
10. **Mucchi di rottami**: lamiere, pneumatici, tubi (3 varianti), bassi (≤60 px), impronta 1–1,5 tessere. **Pila di pneumatici** a parte.
11. **Corde e bitte da molo**: bitta di ormeggio, matassa di corda, una **scaletta** che scende all'acqua dal bordo del molo. Per il molo di legno.
12. **Barricata di difesa**: sacchi di sabbia e lamiere appuntite, pezzi componibili lungo SE e lungo SO (bassi).
13. **Fuoco da cucina**: fusto-stufa con pentola e piccola cappa; fornire anche 2 fotogrammi della fiamma/fumo in un file a parte (per l'animazione).
14. Una **bandiera/straccio su asta** con il simbolo dell'avamposto (a scelta di Muse, senza scritte).

## Consegna
A lotti (ogni lotto si monta da solo): **lotto 1 = punti 1, 2, 10, 11** (i bassi, riempiono subito molo e piazzale), **lotto 2 = 3, 4, 7, 8**, **lotto 3 = il resto**. Tutto in un'unica cartella `muse/2026-11-27-gruppo-iso-5-props-<lotto>/` con LEGGIMI, elenco e scheda di verifica sul mare vero a scala 1:1 con il protagonista.
