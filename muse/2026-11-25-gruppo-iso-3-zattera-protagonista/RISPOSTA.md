# RISPOSTA di Claude — Gruppo iso 3 (zattera e protagonista), 25 nov 2026, sera

Scaricata, decodificata e provata. In gioco non è montato nulla: resta **v0.1b.8** (dall'alto).

## Verificato — a posto
- 8 sprite + anteprima: tutte le misure uguali al LEGGIMI (zattera 640×468/436/401/461; protagonista 37/40/38/36×100; anteprima 2500×1750).
- **Alone magenta: 0** su tutti (stessa metrica delle consegne iso 2: R−G>90 e B−G>90).
- **Protagonista:** 100 px esatti piedi-testa in tutte e 4 le direzioni, stesso personaggio, di fronte verso SE/SO e di spalle verso NE/NO. Ottimo.
- **Zattera:** stesso design del Gruppo 2 (scafo, bidoni, albero con vela ammainata a prua, tenda a poppa); larghezza 640 px in tutte e 4.
- Cardinali scartate: va bene, il motore usa le 4 diagonali (la zattera ruota a scatti di 90° sulla griglia).

## Da rifare: zattera v2 (Claude non ritocca)
1. **NE senza cassa** (già dichiarato). Va aggiunta.
2. **Disposizione non coerente tra le direzioni.** Nella zattera dall'alto (Gruppo 2, prua a sinistra) la cassa sta a destra e le taniche a sinistra guardando verso la prua. Così sono **SE e NO** (giuste). In **NE** le taniche stanno sul lato destro, in **SO** taniche e cassa sullo stesso lato (destro). Girando, la zattera cambierebbe disposizione. Regola unica: guardando verso la prua (albero), **cassa a destra, taniche a sinistra**, tenda a poppa, tutto nella stessa posizione lungo la lunghezza.
3. **SE: 31 px vuoti in fondo al file** (contenuto fino a y=404 su H=436; nelle altre tre il contenuto arriva in fondo). L'ancoraggio dichiarato (320, 436) sarebbe 32 px sotto lo scafo: ritaglia il margine, o dichiara l'ancoraggio al fondo del contenuto. Intanto lo uso al fondo del contenuto.
4. **Anteprima: la zattera copre il pontile.** Nell'anteprima è disegnata sopra il tavolato e sopra la faccia del pontile, con i pali che le passano sotto: sembra salita sul pontile, non attraccata. La zattera sta in acqua (livello del mare), il pontile ha il ponte 64 px più in alto: il bordo a terra del pontile (la linea d'acqua della faccia) deve toccare l'ingombro della zattera. Rifai l'anteprima in v2 con la zattera in acqua accanto alla faccia del pontile. (Come dichiarato nel LEGGIMI, la sagoma sporge a nord dall'impronta: con la zattera sul lato sud del pontile la sporgenza finisce proprio contro la faccia; va bene se non sale sul ponte.)

## Il resto resta invariato
Protagonista e le tre direzioni giuste non vanno toccati. Dopo la v2: camminata, 6 fotogrammi × 4 direzioni, stessa scala e ancoraggio ai piedi.

STATO: Claude ha letto e verificato; v2 richiesta (zattera NE e SO, ritaglio SE, anteprima).
