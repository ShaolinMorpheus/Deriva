# Risposta di Claude al Gruppo iso 4 — camminata del protagonista

Ricevuti **31/31 file**: 24 fotogrammi, scheda, 4 GIF, LEGGIMI. Decodificati e controllati.

## Verificato (tutto ok)
- Tela 70×108 in 24/24; altezza sprite **100 px esatti** in 24/24; piedi a y = 104 in 24/24.
- Residuo magenta 0 e tinta magenta forte 0 in 24/24.
- Stesso personaggio, stessa scala e stessi colori del fermo di Iso 3; il ciclo si chiude (passo6 → passo1 con differenza simile agli altri passaggi).
- **Montata** nel prototipo isometrico (v0.2d): ancoraggio (35,104), passo guidato dalla distanza percorsa, da fermo torna il fermo di Iso 3. Nessun ridimensionamento.

## Difetto: non è ancora un ciclo di camminata
Guardando i 6 fotogrammi uno dopo l'altro, in ogni direzione **le gambe restano sempre aperte alla stessa ampiezza** e **la gamba davanti è sempre la stessa**. Misura: larghezza delle gambe (righe 85–103) per fotogramma
- SE: 53, 53, 55, 52, 49, 54
- SO: 53, 51, 52, 51, 51, 51
- NE: 48, 50, 49, 50, 49, 51
- NO: 49, 47, 48, 41, 45, 49

Un passo vero passa da gambe larghe (contatto, ~50 px) a gambe quasi unite (passaggio, ~15–25 px) e poi si apre con la gamba opposta davanti. Qui cambia soprattutto il dondolio delle braccia: in gioco il personaggio **scivola** con le braccia che si muovono, senza che i piedi si alternino.

## Da rifare — confermato da Davide dopo la prova sul telefono
Davide: «la camminata non mi piace, non muove bene le braccia». Si rifà il ciclo. Stessa tela 70×108, stesso ancoraggio (35,104), stessa altezza 100 px, stesse 4 direzioni, stesso personaggio e design. Cambia la **struttura del ciclo**, in 8 fotogrammi (6 vanno bene solo se contengono tutte le pose):
1. **contatto A**: gamba sinistra davanti (tallone a terra), destra dietro; gambe larghe; **braccio destro in avanti, sinistro indietro**;
2. discesa/appoggio: il peso sulla gamba davanti, il corpo scende di un pelo;
3. **passaggio**: gambe quasi unite, la gamba che si porta avanti piegata; **le due braccia vicine al busto, una sale e l'altra scende**;
4. salita: il corpo sale sulla gamba d'appoggio;
5. **contatto B**: specchio del 1 (gamba destra davanti; **braccio sinistro avanti, destro indietro**);
6–8. come 2–4 con le parti scambiate.
**Braccia:** devono dondolare in controfase con le gambe, con ampiezza ben visibile (circa ±30° alla spalla; il gomito si piega un po' quando il braccio va avanti), **entrambe le braccia leggibili in ogni fotogramma** (nei fotogrammi attuali in NE/NO un pugno resta staccato davanti e in SE/SO un braccio quasi non si muove). Niente braccio rigido lungo il fianco.
Criteri che Claude verificherà: larghezza delle gambe ≤ 25 px nei passaggi e ≥ 45 px nei contatti; gamba davanti diversa fra contatto A e contatto B; posizione orizzontale della mano davanti diversa di almeno 15 px fra contatto A e B; altezza 100 px e piedi a y = 104 in ogni fotogramma; magenta 0; busto sempre centrato sull'ancoraggio.

## Nota sull'angolo
SE e SO sono quasi di profilo (il fermo è tre quarti): lo vedrà Davide a occhio. Se non gli piace, la variante «tre quarti» che proponi nel LEGGIMI va bene.

## In attesa
- Zattera a 16 viste (lotti A/B/C) e palo v2 dalle richieste precedenti.
- Le 8 direzioni del protagonista non sono richieste: aspettano l'ok di Davide.
