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
        <title>Vente d'Ordinateurs</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f4f4f4;
            }
            header {
                background: #333;
                color: #fff;
                padding: 10px 0;
                text-align: center;
            }
            nav {
                margin: 20px 0;
            }
            nav a {
                margin: 0 15px;
                color: #fff;
                text-decoration: none;
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 18px;
            }
            .footer {
                margin-top: 20px;
                font-size: 14px;
                color: #666;
            }
            .gallery {
                display: flex;
                justify-content: space-around;
                flex-wrap: wrap;
            }
            .gallery img {
                width: 200px;
                height: auto;
                margin: 15px;
                border: 1px solid #ccc;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Bienvenue chez Computer Sales!</h1>
            <nav>
                <a href="#">Accueil</a>
                <a href="#">Produits</a>
                <a href="#">Contact</a>
            </nav>
        </header>
        <p>Nous sommes spécialisés dans la vente d'ordinateurs de haute qualité.</p>
        <p>Notre mission est de fournir les meilleurs ordinateurs pour tous vos besoins.</p>
        <p>Contactez-nous pour plus d'informations!</p>

        <div class="gallery">
            <img src="https://via.placeholder.com/200x150.png?text=Ordinateur+1" alt="Ordinateur 1">
            <img src="https://via.placeholder.com/200x150.png?text=Ordinateur+2" alt="Ordinateur 2">
            <img src="https://via.placeholder.com/200x150.png?text=Ordinateur+3" alt="Ordinateur 3">
            <img src="https://via.placeholder.com/200x150.png?text=Ordinateur+4" alt="Ordinateur 4">
        </div>

        <p class="footer">Hello world!</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
