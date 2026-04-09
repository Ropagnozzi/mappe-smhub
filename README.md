# SM Hub — Mappa Maxi Impianti Napoli

## Link pubblico (clienti)
**https://ropagnozzi.github.io/mappe-smhub/mappa_clienti.html**

---

## Struttura cartella

```
mappe-smhub/
├── mappa_clienti.html      ← mappa pubblica (sola lettura)
├── aggiorna_mappa.py       ← script di aggiornamento
├── lista_impianti.xlsx     ← fonte dati (tienilo aggiornato)
├── data/
│   └── impianti.json       ← generato automaticamente dallo script
└── img/
    └── foto/
        ├── NA04.jpg        ← nome file = codice cimasa
        ├── NA05.jpg
        └── ...
```

---

## Setup iniziale GitHub Pages (una volta sola)

### 1. Crea il repository su GitHub
1. Vai su https://github.com/new
2. Nome repository: **mappe-smhub**
3. Visibilità: **Public**
4. Clicca "Create repository"

### 2. Carica i file (prima volta)
Apri il Terminale/PowerShell nella cartella `mappe-smhub/` e digita:

```bash
git init
git add .
git commit -m "Prima versione mappa"
git branch -M main
git remote add origin https://github.com/Ropagnozzi/mappe-smhub.git
git push -u origin main
```

### 3. Attiva GitHub Pages
1. Vai su https://github.com/Ropagnozzi/mappe-smhub
2. Clicca **Settings** (in alto)
3. Nel menu a sinistra clicca **Pages**
4. In "Branch" seleziona **main** e cartella **/ (root)**
5. Clicca **Save**
6. Aspetta 1-2 minuti → il link è attivo

---

## Aggiornare la mappa (uso quotidiano)

### Aggiungere / modificare impianti
1. Modifica `lista_impianti.xlsx`
2. Apri il Terminale nella cartella `mappe-smhub/`
3. Esegui:
   ```bash
   python aggiorna_mappa.py
   ```
4. Poi:
   ```bash
   git add .
   git commit -m "Aggiornamento impianti"
   git push
   ```
5. La mappa si aggiorna in ~30 secondi. Il link non cambia.

### Aggiungere foto a un impianto
1. Rinomina la foto con il codice cimasa: `NA04.jpg`
2. Copia il file in `img/foto/`
3. Esegui il push (vedi sopra)
4. La foto appare automaticamente nel popup della mappa

**Formati supportati:** .jpg (consigliato), .jpeg, .png  
**Dimensione consigliata:** 800×600px, max 500KB per foto

---

## Usare il link nelle presentazioni

### Embed in PDF (Acrobat / Canva)
Inserisci come link ipertestuale sul pulsante o sull'immagine:
```
https://ropagnozzi.github.io/mappe-smhub/mappa_clienti.html
```

### Embed in sito web (iframe)
```html
<iframe
  src="https://ropagnozzi.github.io/mappe-smhub/mappa_clienti.html"
  width="100%"
  height="600px"
  frameborder="0"
  allowfullscreen>
</iframe>
```

### WhatsApp / Email
Incolla direttamente il link:
```
https://ropagnozzi.github.io/mappe-smhub/mappa_clienti.html
```
