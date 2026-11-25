# RISPOSTA di Claude — Gruppo 1 v3 (chiazze quasi ferme)

Montato in **v0.1b.4 · «grafica Muse»**. 4 PNG 512×512 RGBA validi (2 acqua + 2 petrolio), sostituiscono quelli della v2.

- Cambio fotogramma ogni **1,8 s**, con dissolvenza incrociata di **1 s**; per il resto del tempo la chiazza sta ferma.
- Deriva ridotta da ±14 px a **±1,5 px**, lentissima (regolabile: 0 = nessuna).
- Misurato nel simulatore: variazione minima tra un istante e l'altro, senza scatti al cambio. L'effetto vero lo giudica Davide in gioco.

STATO: risposta pronta

## Richiesta nuova (Davide, 25 nov): il mare deve muoversi
Oggi il mare è fermo: sono solo le tessere statiche. Davide vuole che si veda che è in movimento, senza perdere il registro desaturato approvato e senza effetti «troppo animati» come le chiazze (movimento lento e continuo, tipo onda lunga, mai sfarfallio).
Proposta (la più leggera per il telefono): **un overlay di onde/luce**, PNG trasparente, **tileabile senza giunture**, 1024×1024 (= 256 px in gioco = 4×4 tessere). Creste e riflessi chiari desaturati + qualche zona appena più scura, copertura ~25–35%, niente ombre proiettate, niente bianco bruciato, niente ovali. Il gioco lo fa scorrere piano in due strati (direzioni e velocità diverse) sopra il mare: il movimento viene dal codice, il disegno resta fermo. Aiuta anche a rompere la ripetizione della tessera.
Alternativa più costosa: 3–4 fotogrammi per ogni livello di profondità, simili tra loro, con dissolvenza lenta.
