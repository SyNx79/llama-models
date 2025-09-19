# llama4_demo

Dieses Beispiel zeigt, wie du das Llama 4 Modell aus dem Projekt verwendest.

## Voraussetzungen
- Die Modell-Checkpoints (.pth) und params.json liegen in `llama_models/llama4/`
- Die Tokenizer-Datei (z.B. tokenizer.model) ist vorhanden
- Alle Abhängigkeiten sind installiert (`pip install -r requirements.txt`)

## Ausführen

1. Aktiviere deine virtuelle Umgebung (falls noch nicht geschehen):
   
   ```powershell
   .venv\Scripts\Activate
   ```

2. Starte das Beispielskript aus dem Projekt-Root:
   
   ```powershell
   python llama4_demo/main.py
   ```

Das Skript lädt das Modell und generiert eine Antwort auf den Prompt "Was ist künstliche Intelligenz?".

## Hinweise
- Die Imports funktionieren nur, wenn du das Skript aus dem Projekt-Root startest.
- Bei Import-Fehlern prüfe, ob das Verzeichnis `llama_models` im Projekt-Root liegt.
