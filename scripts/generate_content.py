import os
from google import genai

# Initialisierung mit dem Client
client = genai.Client(api_key="AQ.Ab8RN6LyWyGX3mNZzqsHSWfv3qLiU6HMpAoKiTymxbc9ztvaVw")

def generate_seo_article(topic):
    # Optimierter Experten-Prompt
    prompt = f"""
    Schreibe einen tiefgreifenden, SEO-optimierten Vergleichsartikel über: '{topic}'.
    
    Struktur-Vorgaben:
    1. Einleitung: Benenne das Problem oder Bedürfnis des Lesers direkt.
    2. Expertenantalyse: Vergleiche die Optionen (z.B. Öl vs. Wachs) basierend auf Fakten (Verschleiß, Wartungsaufwand, Effizienz).
    3. Experten-Fazit: Gib eine klare Empfehlung für 'Power-User' oder spezifische Zielgruppen.
    4. Lösung: Empfiehl den Wechsel zum empfohlenen Produkt, falls sinnvoll (z.B. Kettenwachs + neue Kette).
    5. Call-to-Action: Füge am Ende einen natürlichen Link-Hinweis ein, z.B.: "Hier findest du das [Produkt-Empfehlung] für dein Upgrade."
    
    WICHTIG: 
    - Sei objektiv, aber entscheidungsfreudig.
    - Maximiere den Mehrwert für den Leser.
    - Maximal 1-2 Affiliate-Produktplatzierungen (sehr subtil, nur als Lösung für das Fazit).
    - Schreibe in flüssigem Deutsch, informativ und hilfreich.
    """
    
    response = client.models.generate_content(
        model='gemini-3.1-flash-lite',
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    if os.path.exists("scripts/keywords.txt"):
        with open("scripts/keywords.txt", "r") as f:
            topics = [line.strip().replace("Thema: ", "") for line in f if line.strip()]
        
        for topic in topics:
            print(f"Generiere Experten-Artikel für: {topic}")
            content = generate_seo_article(topic)
            
            os.makedirs("src/pages/posts", exist_ok=True)
            filename = f"src/pages/posts/{topic.replace(' ', '-').lower()}.md"
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Erstellt: {filename}")
    else:
        print("Datei scripts/keywords.txt nicht gefunden!")
