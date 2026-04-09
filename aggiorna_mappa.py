"""
aggiorna_mappa.py
-----------------
Legge lista_impianti.xlsx e genera data/impianti.json
Esegui ogni volta che modifichi il file Excel, poi fai git push.

Uso:
    python aggiorna_mappa.py
"""

import pandas as pd
import json
import os
from datetime import datetime

EXCEL_FILE = "lista_impianti.xlsx"
JSON_OUT   = "data/impianti.json"

def main():
    if not os.path.exists(EXCEL_FILE):
        print(f"ERRORE: file '{EXCEL_FILE}' non trovato.")
        print("Assicurati di eseguire lo script dalla cartella mappe-smhub/")
        return

    print(f"Leggo {EXCEL_FILE}...")
    df = pd.read_excel(EXCEL_FILE)

    impianti = []
    saltati  = []

    for _, r in df.iterrows():
        # Salta righe senza coordinate
        if pd.isna(r.get("latitudine")) or pd.isna(r.get("longitudine")):
            saltati.append(str(r.get("indirizzo", "?")))
            continue

        impianti.append({
            "cimasa":    str(r["Cimasa"]).strip() if pd.notna(r.get("Cimasa")) else "N/D",
            "indirizzo": str(r["indirizzo"]).strip(),
            "lat":       round(float(r["latitudine"]),  7),
            "lng":       round(float(r["longitudine"]), 7),
            "dimensione": str(r["dimensione"]).strip() if pd.notna(r.get("dimensione")) else "-",
        })

    os.makedirs("data", exist_ok=True)
    with open(JSON_OUT, "w", encoding="utf-8") as f:
        json.dump(impianti, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Completato il {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"   Impianti esportati : {len(impianti)}")
    if saltati:
        print(f"   Saltati (no coord) : {len(saltati)}")
        for s in saltati:
            print(f"     - {s}")
    print(f"\n   File salvato in : {JSON_OUT}")
    print("\nOra esegui:")
    print("   git add .")
    print('   git commit -m "Aggiornamento impianti"')
    print("   git push")
    print("\nLa mappa si aggiorna in ~30 secondi.")

if __name__ == "__main__":
    main()
