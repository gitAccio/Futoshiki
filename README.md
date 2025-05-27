# Futoshiki Solver

Questo progetto permette di risolvere il puzzle **Futoshiki**, un gioco logico pubblicato su riviste come **La Settimana Enigmistica**.

---

## Contenuto

- `solver.py`: Script Python per risolvere il puzzle.
- `docs/index.html`: Interfaccia web per inserire manualmente i numeri e i vincoli.
- `README.md`: Questo file.
- `.gitignore`: File di esclusione per Git.

---

## Come funziona

- Inserisci numeri da 1 a 5 in una griglia 5x5.
- Ogni numero può comparire **una sola volta per riga e per colonna**.
- Aggiungi vincoli tra le celle usando simboli:
- `<` e `>` per vincoli orizzontali
- `∧` e `∨` per vincoli verticali

Il risolutore Python (`solver.py`) usa backtracking per cercare una soluzione che rispetti tutti i vincoli.

---

## Requisiti

- Python 3.x
- Nessuna libreria esterna necessaria.

---

## Uso

Esegui lo script:

```bash
python solver.py
```

Segui le istruzioni a video:

1. Inserisci il numero di righe e colonne n.
2. Scrivi le righe come indicato nell'esempio stampato.

---

## Note

Lo script funziona con *n* numero di righe e colonne, non soltanto con una griglia 5x5.

---

## Licenza

Questo progetto è rilasciato sotto licenza MIT. Vedi il file `LICENSE` per i dettagli.

---

## Contatti / Supporto

Per suggerimenti o problemi, apri una issue nel repository o contatta l'autore.

---

Buon divertimento con i tuoi Futoshiki! 🧩

