# Zattera: più frame (richiesta di Davide)

Problema: la rotazione a 16 viste (ogni 22,5°) scatta, e da ferma la zattera è statica.

## Parte 1 — 32 viste (priorità)
- Le 16 attuali restano. Servono le 16 INTERMEDIE: angoli 11,25° + k·22,5° (k=0..15).
- Nomi: zattera_iso_00b.png … 15b.png (la "b" è a metà tra N e N+1).
- Stessa tela 704×512, centro impronta (352,336), stessa luce, stessi oggetti, stesse proporzioni.
- Le taniche sulle posizioni della guida (anche nelle 04 e 12 da correggere).
- Niente contorni scuri, sfondo magenta pulito.

## Parte 2 — dondolo (dopo la parte 1)
- Ciclo di 4 frame per ognuna delle 16 viste principali: zattera_iso_NN_f1..f4.png.
- Movimento piccolo: sali/scendi di 2-3 px, leggero beccheggio, teli e cavi che oscillano. Il frame 1 = la vista attuale.
- Il ciclo deve chiudersi senza scatti (f4 → f1).

Consegna a lotti: prima le 32 viste in 2 lotti da 8, poi il dondolo.
