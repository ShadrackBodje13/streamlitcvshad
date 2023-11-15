#Projet de CV

#Librairies
import streamlit as st

# Titre
st.title('Mon CV interactif')

# Menu déroulant dans la barre latérale pour la navigation
menu_options = ['INFORMATIONS PERSONNELLES', 'EXPERIENCE PROFESSIONNELLE', 'FORMATION', 'HARD SKILLS', "SOFT SKILLS", "CENTRES D'INTERET", "CERTIFICATIONS"]
choice = st.sidebar.selectbox('Section CV', menu_options)

# Informations personnelles
if choice == 'INFORMATIONS PERSONNELLES':
    st.header('INFORMATIONS PERSONNELLES')
    

    st.subheader('Nom')
    st.write('Shadrack BODJE')
    st.subheader('Adresse')
    st.write('Île de France, France')
    st.subheader('E-mail')
    st.write('shadrackemmanuel.bodje@ynov.com')

    with open("cv_shadrack_bodje_chef_de_projet.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Télécharger CV Shadrack",
                    data=PDFbyte,
                    file_name="cv_shadrack_bodje_chef_de_projet.pdf",
                    mime='application/octet-stream')
    
    
    # Ajouter des liens avec des icônes pour LinkedIn et GitHub
    st.markdown("""
        <a href="https://www.linkedin.com/in/shadrack-bodje-37a0b9183/" target="_blank" title="Visitez mon profil Linkedin"><img src="https://img.icons8.com/color/48/000000/linkedin.png"/></a>
        <a href="https://github.com/ShadrackBodje13/" target="_blank" title="Visitez mon profil GitHub"><img src="https://img.icons8.com/ios-filled/50/000000/github.png"/></a>
    """, unsafe_allow_html=True)
    
# Lien de téléchargement du CV


# Expérience professionnelle
if choice == 'EXPERIENCE PROFESSIONNELLE':
    st.header('EXPERIENCE PROFESSIONNELLE')
    st.subheader('CHEF DE PROJET / PRODUCT OWNER - BNP Paribas')
    st.subheader('Septembre 2022 - Now')
    st.write('V3C : analyse,  pilotage de la réalisation et des évolutions de l’asset Vision 360 Client Corporate ainsi qu’au suivi du run, en collaboration avec les équipes IT')
    st.write('INSIDE : Elaboration des leads prédictifs mise en oeuvre par la data science IA en collaboration avec les metiers concernés')
    st.write('CRM GDCC: Participer aux projets de conception et de réalisation du Customer Relationship Management (CRM) Corporate dans ses dimensions Gestion des Opportunités et du Fonds de Commerce')
    st.write("CRM Mon Fonds de Commerce : Visualisation de chaque IFC pour Chaque chargé d'affaire en fonction de son CAF et suivi des activités pour le CAE")

    st.subheader('DEVELOPPEUR BACKEND - Axians')    
    st.subheader('Octobre 2021 - Juillet 2022')
    st.write('Dashboard pour les entreprises du pôle : Possibilité de voir les dossiers traités, en cours, archivés, non attribués, resolus...')
    st.write('Scripts Python : Conversion documents words html en pdf, automatisation de tâches')
    
    st.subheader('DEVELOPPEUR Web - CGM Metaux')    
    st.subheader('Juin - Juillet 2021')
    st.write('Modification page html')
    st.write('Boite à idées avec Google forms')

# Éducation
if choice == 'FORMATION':
    st.header('FORMATION')
    st.subheader('Expert informatique et systèmes d’information – Niveau 7 | Data Engineer & Data Scientist')
    st.write('Paris Ynov Campus')
    st.write('Septembre 2019 - Septembre 2024')

    st.subheader('Ingenieur logiciel')
    st.write('Mastere Data Engineer & Data Scientist')
    st.write('Intech')
    st.write('Mars 2019 - Juillet 2019')
    
    st.subheader('Ecole Preparatoire Science de la sante')
    st.write('Tronc Commun Medecine')
    st.write('Université Nangui Abrogoua')
    st.write('Fevrier 2017 - Janvier 2019')
    
    st.subheader('Baccalaureat D - Maths Physique Chimie SVT')
    st.write('Cours Secondaire Methodiste Cocody')
    st.write('Septembre 2015 - juin 2016')




# Compétences
if choice == 'HARD SKILLS':
    st.header('HARD SKILLS')
    st.write('Suivi de projet')
    st.write('Jira Trello, Gant,Kanban')
    st.write('Méthode Agile Scrum, DevOps')
    st.write('Connaissance pratique du langage SQL, Python, JavaScript,HTML et CSS')
    st.write('Connaissance pratique Machine Learning & Deep Learning')
    st.write('DataIku')
    st.write('Outils collaboratif Google')
    st.write('Microsoft office')
    st.write('CMS : Wordpress, Drupal')
    st.write('Canva')
    st.write('SEO | UX|UI design')

    
if choice == 'SOFT SKILLS':
    st.header('SOFT SKILLS')
    st.write('Leadership')
    st.write('Gestion')
    st.write('Curiosité')
    st.write('Bon relationnel et communiquant')
    st.write('Motivation & Réactivité')
    st.write("Travail d'équipe et adaptation")
    st.write('Implication')
    st.write('Organisation et rigueur')
    st.write('Pédagogie et autonomie')
    st.write("Esprit d'analyse et de synthèse")




# Loisirs et centres d'intérêt
if choice == "CENTRES D'INTERET":
    st.header("CENTRES D'INTERET")
    st.write('Gestion de projet')
    st.write('Data')
    st.write('Management')
    st.write('Football')


# Section supplémentaire
if choice == 'CERTIFICATIONS':
    st.header('CERTIFICATIONS')
    st.markdown("""
        <a href="https://verify.skilljar.com/c/n6ikjfrjn7cd" target="_blank" style="text-decoration: none;">Dataiku - Machine Learning Practicioner</a>
    """, unsafe_allow_html=True)
    st.markdown("""
        <a href="https://verify.skilljar.com/c/pcatrtdih98x" target="_blank" style="text-decoration: none;">Dataiku - Advanced designer</a>
    """, unsafe_allow_html=True)
    st.markdown("""
        <a href="https://verify.skilljar.com/c/n6ikjfrjn7cd" target="_blank" style="text-decoration: none;">Dataiku - Core designer</a>
    """, unsafe_allow_html=True)

    st.markdown("""
        <a href="https://verify.skilljar.com/c/n6ikjfrjn7cd" target="_blank" style="text-decoration: none;">Dataiku - Core designer</a>
    """, unsafe_allow_html=True)
    st.write('Google ateliers numeriques')

