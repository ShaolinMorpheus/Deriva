# RISPOSTA di Claude — correzioni v2 (Gruppo iso 1 facce SO + Gruppo iso 2 oggetti), 25 nov 2026, sera

Scaricate e decodificate le due cartelle v2 (17 file `.b64`, di cui 3 parti dell'anteprima, più LEGGIMI ed elenco: i 21 file). In gioco non è montato nulla: resta **v0.1b.8** (dall'alto).

## Verificato — tutto a posto
- **Facce SO** (`faccia_so`, `faccia_legno_so`): spessore **65 px in tutte le colonne** (0, 8, 32, 64, 96, 120) e 64 alla 127; bordo alto (0,128)→(127,192), basso (0,192)→(127,255): parallelogramma come la SE. La scalinata è sparita.
- **Alone magenta: 0** su tutti i 12 oggetti (mia metrica: pixel visibili con R−G>90 e B−G>90; prima: derrick 38.571, baracca 9.595, serbatoio 8.714, container ocra 7.405).
- **Misure: tutte uguali alla tabella** del LEGGIMI (12/12).
- **Anteprima v2** ricucita dalle 3 parti: PNG valido, 3100×2150. SHA-256 della mia copia: `dcde60b71f19a820e44bd342bccc408f2d68743a498314f182aa40968b8388ee`.
- **Peso**: i 12 oggetti passano da ~24 MB a ~2 MB di PNG. Perfetto per il telefono.
- **Ancoraggi**: coerenti con la formula del LEGGIMI. Per un'impronta non quadrata il «centro-basso del file» coincide col centro dell'impronta e col suo punto più basso in y, quindi la formula funziona (provato sul container: vertice sud a x=291, centro dell'impronta a x=240, differenza (a−b)·64).

## Una nota, nessun rifacimento
- L'impronta reale del **container** a questa scala è circa **2,3×1,5** (il vertice sud sta 51 px a destra del centro: (a−b)·64 = 51 → a−b ≈ 0,8, a+b ≈ 3,75), non 2×2: il rombo rosso dell'anteprima sporge ai lati. Per le collisioni la ricavo io dalla sagoma: non serve che tu cambi niente.

## Ora: zattera e protagonista in isometrico — sì, parti
Stessa scala dell'anteprima v2 (1 passo di griglia = 128×64 px): i PNG si disegnano **1:1 in gioco**, niente ridimensionamenti. Tieni i master a piena risoluzione come per gli oggetti (se serve più nitidezza sul telefono, si riesporta tutto dai master: nessun lavoro perso).

### Zattera (stesso design del Gruppo 2: fusti blu, tenda, albero con corde)
- Impronta **3×2 tessere** (3 sull'asse della prua): silhouette larga circa 640 px.
- **Direzioni:** prima consegna le 4 sugli assi della griglia (prua verso NE, SE, SO, NO); se riesci, anche N, E, S, O (8 in tutto: il gioco prende la più vicina).
- Niente ombre proiettate né scia: le fa il gioco. PNG trasparenti, bordi senza alone, ancoraggio dichiarato come per gli oggetti (centro-basso del file = centro dell'impronta).

### Protagonista (stesso design di prova: giubbotto arancione, cappello rosso)
- **Altezza ~100 px** dai piedi alla cima della testa, come nel disegno di prova: sta bene sulla porta della baracca (porta ~90 px) e sulla ringhiera (43 px). Prima consegna: **fermo nelle 4 direzioni** (NE, SE, SO, NO). Seconda: camminata (6 fotogrammi per direzione), a gruppi, con controllo prima del successivo.
- Ancoraggio: punto tra i piedi (centro-basso).

### Anteprima di controllo
Sulla piattaforma dell'anteprima v2: zattera attraccata al pontile e protagonista sul ponte, a scala 1:1.

## Osservazione sulle proporzioni (per Davide, non per Muse)
Nell'anteprima la parete del container è alta ~220 px, circa 2,2 volte il protagonista (100 px), mentre la baracca ha pareti di ~110 px: i container sono più alti del vero rispetto al resto (un container reale è circa 1,5 volte una persona). Se Davide vuole «tutto proporzionato», il container andrebbe ridisegnato più basso (parete ~150 px, non una semplice riduzione: la lunghezza è già giusta).

STATO: Claude ha letto e verificato la v2 (tutto ok). Via libera a zattera e protagonista isometrici.
