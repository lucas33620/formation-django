from django.shortcuts import render
from datetime import datetime

# Exemple d'articles simulés
def index(request):
    articles = [
        {"titre": "Bienvenue sur mon blog Django", "contenu": "Voici mon premier article ! 🎉", "date": datetime(2025, 4, 1)},
        {"titre": "Comprendre les vues Django", "contenu": "Une vue est une fonction ou classe qui retourne une réponse...", "date": datetime(2025, 4, 2)},
    ]
    return render(request, "blog/index.html", {
        "articles": articles,
        "year": datetime.now().year
    })

def article(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f"blog/article_{numero_article}.html", {"article": article})
    else :
        return render(request, f"blog/article_not_found.html")
