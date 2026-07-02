from google import genai

# Initialisierung mit dem Key
client = genai.Client(api_key="AQ.Ab8RN6LyWyGX3mNZzqsHSWfv3qLiU6HMpAoKiTymxbc9ztvaVw")

print("Verfügbare Modelle:")
try:
    for m in client.models.list():
        print(f"- {m.name}")
except Exception as e:
    print(f"Fehler beim Abrufen der Modellliste: {e}")
