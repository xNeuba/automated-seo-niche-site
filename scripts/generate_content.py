import os
from google import genai

# Initialisierung mit dem Client
client = genai.Client(api_key="AQ.Ab8RN6LyWyGX3mNZzqsHSWfv3qLiU6HMpAoKiTymxbc9ztvaVw")

def generate_diy_guide(topic, problem_solution):
    prompt = f"""
    Schreibe eine hochqualitative, detaillierte Bauanleitung für Heimwerker zum Thema: {topic}.
    Hintergrund: {problem_solution}
    
    Struktur:
    1. H2: Warum dieses DIY-Gadget teure Produkte schlägt (Physik kurz erklären, Kosten-Nutzen-Vergleich).
    2. H2: Einkaufsliste / Materialliste.
    3. H2: Schritt-für-Schritt-Bauanleitung (sehr präzise, als würde ich daneben stehen).
    4. H2: Tipps zur Optimierung und Sicherheit.
    
    WICHTIG: Schreibe authentisch, praxisnah und vermeide typisches KI-Marketing-Blabla. 
    Markdown Format.
    """
    
    response = client.models.generate_content(
        model='gemini-3.1-flash-lite',
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    topic = input("DIY-Projekt Titel: ")
    context = input("Kurze Beschreibung/Hintergrund: ")
    
    print("\n--- GENERIERE ENTWURF... ---\n")
    content = generate_diy_guide(topic, context)
    
    # Füge das Astro-Layout automatisch hinzu
    final_content = f"""---
layout: ../../layouts/PostLayout.astro
title: "{topic}"
---

{content}
"""
    
    # Speichern direkt in den fertigen Post-Ordner, da es nun "fertig" ist
    os.makedirs("src/pages/posts", exist_ok=True)
    filename = f"src/pages/posts/{topic.replace(' ', '-').lower()}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_content)
    
    print(f"Artikel fertig generiert in: {filename}")
    print("Prüfe ihn kurz und pushe ihn dann zu GitHub für Vercel.")
