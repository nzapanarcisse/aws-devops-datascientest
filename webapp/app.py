import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proven-FR - Provenderie</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #003366;
            color: white;
            padding: 20px;
            text-align: center;
        }
        nav {
            margin: 20px 0;
        }
        nav a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-weight: bold;
        }
        section {
            padding: 20px;
            margin: 10px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        footer {
            text-align: center;
            padding: 10px;
            background-color: #003366;
            color: white;
            position: relative;
        }
        .hero {
            background-image: url('https://via.placeholder.com/1200x400/003366/ffffff?text=Bienvenue+chez+Proven-FR');
            background-size: cover;
            color: white;
            text-align: center;
            padding: 60px 20px;
        }
        .hero h1 {
            font-size: 3em;
        }
        .products img {
            width: 100%;
            height: auto;
            border-radius: 5px;
        }
        .about {
            background-color: #ffe6e6;
            padding: 20px;
        }
    </style>
</head>
<body>

<header>
    <h1>Proven-FR</h1>
    <nav>
        <a href="#accueil">Accueil</a>
        <a href="#produits">Produits</a>
        <a href="#contact">Contact</a>
        <a href="#apropos">À propos de nous</a>
    </nav>
</header>

<section class="hero" id="accueil">
    <h1>Bienvenue chez Proven-FR</h1>
    <p>Votre expert en provenderie.</p>
</section>

<section class="products" id="produits">
    <h2>Nos Produits</h2>
    <p>Découvrez notre large gamme de produits de qualité pour vos animaux.</p>
    <img src="https://via.placeholder.com/600x300/ffcc00/000000?text=Produits+de+Qualité" alt="Produits de Proven-FR">
</section>

<section class="about" id="apropos">
    <h2>À propos de nous</h2>
    <p>Chez Proven-FR, nous nous engageons à fournir les meilleurs aliments pour vos animaux. Notre équipe d'experts travaille chaque jour pour garantir la qualité de nos produits.</p>
</section>

<section id="contact">
    <h2>Contactez-nous</h2>
    <p>Pour toute demande d'information, n'hésitez pas à nous contacter à l'adresse suivante : contact@provenfr.com.</p>
</section>

<footer>
    <p>&copy; 2024 Proven-FR - Tous droits réservés</p>
</footer>

</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
