from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/images", StaticFiles(directory="Image"), name="images")
app.mount("/static", StaticFiles(directory="static"), name="static")

def blue_sanguine_style_page(title, active, main_content,):
    nav = {
        "Accueil": "/",
        "Projets Personnel": "/projets-perso",
        "Projets Professionnel": "/projets-pro",
        "Carrière": "/carriere",
    }
    nav_html = '<nav class="nav"><ul>'
    for name, url in nav.items():
        cls = "active" if name == active else ""
        nav_html += f'<li><a href="{url}" class="{cls}">{name}</a></li>'
    nav_html += '</ul></nav>'
    banner_html = f'''
    <div class="banner center-banner">
      <h1>Andréas Aucher</h1>
      <div class="desc">
        Âgé de 20 ans, passionné de photographie, j’en ai fait mon activité professionnelle et une passion depuis quatre ans, en m’améliorant constamment.<br><br>
        En tant qu’amoureux des animaux et de la nature, je suis adhérent à l’ASPAS et à la Brigade de Protection des Animaux. J’explore aussi intensivement l’informatique, notamment la programmation et l’assemblage d’ordinateurs.<br><br>
        Côté professionnel, j’ai débuté dans le secteur commercial : expériences variées, création et emploi en entreprise. Début 2025, je me suis engagé dans l’aide aux usagers et le service public ; dorénavant, mon projet professionnel est de rejoindre la Gendarmerie nationale.
      </div>
      <div style="text-align:right; font-size:1em; margin-top:18px;">
        Contact : <a href="mailto:aucher.andreas@gmail.com" style="color:#ffd6b1;">aucher.andreas@gmail.com</a>
    </div>
    </div>
    '''
    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>{title} -By Andréas Aucher</title>
        <link rel="stylesheet" href="/static/style.css" />
    </head>
    <body>
        <header>{nav_html}</header>
        {banner_html if active=="Accueil" else ""}
        <main>
        {main_content}
        </main>
        <footer>© 2025 By Andréas Aucher</footer>
    </body>
    </html>
    """

@app.get("/", response_class=HTMLResponse)
async def accueil():
    content = ""
    return blue_sanguine_style_page("Accueil", "Accueil", content)

@app.get("/projets-perso", response_class=HTMLResponse)
async def projets_perso():
    content = '''
    <section class="projects-horizontal">
      <!-- Cadre portfolio à gauche -->
      <div class="portfolio">
        <h2>Portfolio Photo</h2>
        <div class="portfolio-grid">
          ''' + ''.join(
              f'''<a href="/images/portfolio/image{i}.JPG" target="_blank">
                     <img src="/images/portfolio/image{i}.JPG" alt="Photo {i}">
                 </a>'''
              for i in range(1, 11)
          ) + '''
        </div>
      </div>
      <!-- Cadre ordinateur à droite -->
      <div class="computer-info">
        <h2>Mon Ordinateur</h2>
        <p>Présentation détaillée de l’ordinateur que je construis, avec ses caractéristiques, composants, et évolutions.</p>
        <ul>
          <li>Processeur : Intel Core i5-12600K</li>
          <li>Carte graphique : NVIDIA RTX 4060 TI</li>
          <li>Mémoire RAM : 16 Go DDR5</li>
          <li>Stockage 1 : SSD 1 To</li>
          <li>Stockage 2 : SSD NVMe 456 Go</li>
          <li>Stockage 3 : SSD 240 Go</li>
          <li>Stockage 4 : HDD 2 To</li>
          <li>Refroidissement : Watercooling NZXT Z73</li>
          <li>Boîtier : NZXT H510 Elite</li>
          <li>Alimentation : 1000W 80 plus Platinium</li>
        </ul>
      </div>
    </section>
    '''
    return blue_sanguine_style_page("Projets Personnel", "Projets Personnel", content)


@app.get("/projets-pro", response_class=HTMLResponse)
async def projets_pro():
    content = '''
    <section class="projets-bloc">
  <!-- Partie intro et projets (textes) -->
  <h2>Mes projets professionnels</h2>
  <div>
    <h3>Gendarmerie Nationale</h3>
    <p>Mon projet principal est d’intégrer la Gendarmerie nationale.  
          Pour cela, je me prépare activement aux différentes épreuves du concours en utilisant des outils spécialisés.</p>
    <h3>Concours Formation</h3>
    <p>J’utilise “Concours Formation” pour m’entraîner aux tests psychotechniques.  
          Cet outil m’aide à améliorer ma rapidité, ma logique et mes capacités d’analyse, indispensables pour réussir les épreuves.
    </p>
    <h3>G pour Gendarme Prépa</h3>
    <p>J’utilise aussi “G pour Gendarme Prépa” qui est une plateforme complète pour se préparer au concours, avec des fiches pratiques, des quiz, et des conseils.  
          C’est un support fondamental pour structurer ma préparation et optimiser mes chances de réussite.</p>
  </div>
  <!-- Tableau activités et écoles -->
  <table class="projets-tableau">
    <tr>
      <th>Sport</th>
      <th>Écoles de Gendarmerie</th>
    </tr>
    <tr>
      <td>
        <strong>Mardi & Jeudi :</strong> cardio par tapis de course et vélo en salle de sport<br>
        <strong>Samedi :</strong> musculation diversifiée
      </td>
      <td>
        Je me renseigne sur les écoles de gendarmerie à <b>Chaumont</b>, <b>Tulle</b>, <b>Montluçon</b>. <br>
        J’ai lu en détail tous les livrets d’accueil pour gendarme adjoint volontaire, ce qui m’a permis de bien comprendre leur fonctionnement et exigences.
      </td>
    </tr>
  </table>
  <!-- Préparation de stage -->
  <div style="margin-top:28px;">
    <h3>Préparation de stage</h3>
    <p>
      Je prépare actuellement un stage dans une gendarmerie locale afin de découvrir concrètement les réalités du métier sur le terrain.
    </p>
  </div>
</section>
    '''
    return blue_sanguine_style_page("Projets Professionnel", "Projets Professionnel", content)


@app.get("/carriere", response_class=HTMLResponse)
async def carriere():
    content = '''
    <section style="max-width:900px; margin:auto; background:rgba(35,36,59,0.9); border-radius:16px; padding:32px; box-shadow:0 6px 28px #000d; color:#f0f0f5;">
      <h2 style="font-size:2.2em; font-weight:700; margin-bottom:32px; border-bottom: 2px solid #d35400; padding-bottom: 10px;">Carrière détaillée & Diplômes</h2>

      <article style="margin-bottom:40px;">
        <h3 style="font-size:1.6em; color:#ffbb66; margin-bottom:16px;">Expériences professionnelles</h3>
        <div style="margin-left:12px;">
          <h4 style="margin-bottom:8px; font-weight:700;">Service Civique – Sous-préfecture de Lodève</h4>
          <p><em>Février 2025 – Aujourd’hui</em></p>
          <ul style="line-height:1.6; font-size:1.1em;">
            <li>Accueil et sens du contact avec le public dans un cadre administratif.</li>
            <li>Organisation rigoureuse de missions variées pour assurer un service fluide.</li>
            <li>Travail en équipe, polyvalence et grande capacité d’adaptation.</li>
            <li>Maîtrise des outils informatiques nécessaires aux fonctions.</li>
            <li>Gestion efficace de situations diverses et respect strict des procédures.</li>
            <li>Discrétion et sens profond du service public.</li>
          </ul>
        </div>

        <div style="margin-left:12px; margin-top:24px;">
          <h4 style="margin-bottom:8px; font-weight:700;">Extra – Charcutier traiteur, E.Leclerc</h4>
          <p><em>Décembre 2023 – Mars 2024</em></p>
          <p>Travail intensif en charcuterie avec respect des normes d’hygiène et qualité, ainsi que relation client chaleureuse et efficace.</p>
        </div>

        <div style="margin-left:12px; margin-top:24px;">
          <h4 style="margin-bottom:8px; font-weight:700;">Photographe Entrepreneur</h4>
          <p><em>Mai 2023 – Octobre 2023</em></p>
          <p>Gestion complète de projets photographiques en indépendant, de la prise de vue à la post-production, en optimisant la relation client.</p>
        </div>
      </article>

      <article style="margin-bottom:40px;">
        <h3 style="font-size:1.6em; color:#ffbb66; margin-bottom:16px;">Diplômes & Formations</h3>
        <ul style="line-height:1.6; font-size:1.1em;">
          <li><b>Titre professionnel Agent de maintenance du bâtiment</b> – AFPA Saint Etienne, diplômé en 2024</li>
          <li><b>Habilitation électrique B2V</b> – AFPA Saint Etienne, réussite en décembre 2023</li>
          <li><b>Diplôme national du brevet</b> – Collège Bois de la Rive, obtenu en 2020</li>
        </ul>
      </article>

      <article style="margin-bottom:24px;">
        <h3 style="font-size:1.6em; color:#ffbb66; margin-bottom:16px;">Compétences & Divers</h3>
        <p>Polyvalent et curieux, je développe des compétences variées : photographie, programmation, mixologie, audiovisuel, airsoft.</p>
        <p>Maîtrise avancée des logiciels : LibreOffice suite, Canva, Google Suite, Adobe Acrobat.</p>
        <p>Membre engagé dans la vie associative, notamment à la Brigade de Protection des Animaux (BPA) et à l’ASPAS.</p>
      </article>

      <div style="text-align:center; margin-top:48px;">
        <a href="/images/CV%20Andréas%20Aucher.PDF" download style="background:#d35400; color:#fff; padding:16px 36px; border-radius:10px; font-weight:700; text-decoration:none; box-shadow:0 5px 20px #c04000;">
          Télécharger mon CV complet (PDF)
        </a>
      </div>
    </section>
    '''
    return blue_sanguine_style_page("Carrière", "Carrière", content)
