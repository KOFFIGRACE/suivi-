import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Suivi Santé IMC",
    page_icon="🏥",
    layout="wide"
)

# CSS personnalisé pour améliorer l'interface
st.markdown("""
<style>
    /* Styles généraux */
    .main {
        background-color: #f5f7fa;
        padding: 2rem;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* En-tête principal */
    .main-header {
        color: #2c3e50;
        font-size: 2.5rem !important;
        font-weight: 700;
        margin-bottom: 1.5rem;
        text-align: center;
        padding-bottom: 1rem;
        border-bottom: 3px solid #3498db;
    }
    
    /* Sous-titres */
    .section-header {
        color: #3498db;
        font-size: 1.5rem !important;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-left: 0.5rem;
        border-left: 4px solid #3498db;
    }
    
    /* Cartes pour contenir les résultats */
    .result-card {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
    }
    
    /* Affichage de l'IMC */
    .imc-display {
        font-size: 2.2rem !important;
        font-weight: 700;
        text-align: center;
        color: #2c3e50;
        margin: 1rem 0;
    }
    
    /* Statut IMC */
    .imc-status {
        font-size: 1.3rem !important;
        text-align: center;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.5rem auto;
        max-width: 200px;
    }
    
    .status-underweight {
        background-color: #3498db;
        color: white;
    }
    
    .status-normal {
        background-color: #2ecc71;
        color: white;
    }
    
    .status-overweight {
        background-color: #f39c12;
        color: white;
    }
    
    .status-obese {
        background-color: #e74c3c;
        color: white;
    }
    
    /* Menu et formulaire */
    .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: white;
    }
    
    /* Plans de repas */
    .meal-card {
        background-color: #f8f9fa;
        border-left: 4px solid #3498db;
        padding: 0.8rem;
        margin-bottom: 0.8rem;
        border-radius: 5px;
    }
    
    .meal-title {
        font-weight: 600;
        color: #2c3e50;
    }
    
    /* Recommandations */
    .recommendation {
        background-color: #ebf5fb;
        border-radius: 5px;
        padding: 1rem;
        margin-top: 1rem;
        border-left: 4px solid #3498db;
    }
    
    .recommendation-title {
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    /* Alertes et statuts */
    .status-alert {
        padding: 1rem;
        border-radius: 5px;
        margin-top: 1rem;
    }
    
    .alert-warning {
        background-color: #fcf3cf;
        border-left: 4px solid #f1c40f;
    }
    
    .alert-success {
        background-color: #d4efdf;
        border-left: 4px solid #2ecc71;
    }
    
    /* Bouton */
    .stButton>button {
        background-color: #3498db;
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        width: 100%;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #2980b9;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Titre principal
st.markdown("<h1 class='main-header'>Suivi et recommandations personnalisées pour l'IMC et la santé</h1>", unsafe_allow_html=True)

# Création de colonnes pour l'interface
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-header'>Informations personnelles</h2>", unsafe_allow_html=True)
    
    # Informations personnelles de base
    genre = st.selectbox("Genre", ["Femme", "Homme"])
    age = st.number_input("Âge", min_value=10, max_value=100, step=1)
    taille = st.number_input("Taille (m)", min_value=1.0, max_value=2.5, step=0.01, value=1.70)
    poids = st.number_input("Poids (kg)", min_value=20, max_value=200, step=1, value=70)
    
    # Pression artérielle
    st.markdown("<h3 style='color: #3498db; font-size: 1.2rem;'>Pression artérielle</h3>", unsafe_allow_html=True)
    pression_syst = st.number_input("Pression Systolique", min_value=90, max_value=180, step=1, value=120)
    pression_diast = st.number_input("Pression Diastolique", min_value=50, max_value=120, step=1, value=80)
    
    # Niveau d'activité
    st.markdown("<h3 style='color: #3498db; font-size: 1.2rem;'>Niveau d'activité</h3>", unsafe_allow_html=True)
    activite_physique = st.selectbox("Niveau d'activité quotidienne", ["Faible", "Moyenne", "Élevée"])
    heures_sport = st.slider("Heures de sport par semaine", min_value=0, max_value=14, step=1)
    
    # Habitudes de vie
    st.markdown("<h3 style='color: #3498db; font-size: 1.2rem;'>Habitudes de vie</h3>", unsafe_allow_html=True)
    boissons_gazeuses = st.radio("Consommation de boissons gazeuses", ["Oui", "Non"])
    consommation_alcool = st.radio("Consommation d'alcool", ["Oui", "Non"])
    fumer = st.radio("Tabagisme", ["Oui", "Non"])
    classe_sociale = st.selectbox("Classe sociale", ["Faible", "Moyenne", "Élevée"])
    
    # Variables spécifiques au genre
    if genre == "Femme":
        st.markdown("<h3 style='color: #3498db; font-size: 1.2rem;'>Objectifs spécifiques</h3>", unsafe_allow_html=True)
        prendre_poids = st.radio("Souhaitez-vous prendre du poids ?", ["Oui", "Non"])
        si_developper_bassin = st.radio("Souhaitez-vous développer votre bassin et vos hanches ?", ["Oui", "Non"])
    
    if genre == "Homme":
        st.markdown("<h3 style='color: #3498db; font-size: 1.2rem;'>Objectifs spécifiques</h3>", unsafe_allow_html=True)
        objectif_sport = st.selectbox("Quel est votre objectif sportif ?", ["Développer les abdos", "Développer les épaules", "Forme générale"])
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Bouton pour effectuer la prédiction
    calculate_button = st.button("Calculer l'IMC et obtenir mes recommandations")

# Colonne de résultats
with col2:
    if calculate_button:
        # Calcul de l'IMC
        if taille > 0:
            imc = poids / (taille ** 2)
            
            # Détermination de la catégorie IMC
            if imc < 18.5:
                categorie_imc = "Sous-poids"
                status_class = "status-underweight"
            elif 18.5 <= imc < 25:
                categorie_imc = "Poids normal"
                status_class = "status-normal"
            elif 25 <= imc < 30:
                categorie_imc = "Surpoids"
                status_class = "status-overweight"
            else:
                categorie_imc = "Obésité"
                status_class = "status-obese"
            
            # Affichage des résultats IMC
            st.markdown("<div class='result-card'>", unsafe_allow_html=True)
            st.markdown("<h2 class='section-header'>Résultats de votre IMC</h2>", unsafe_allow_html=True)
            st.markdown(f"<p class='imc-display'>IMC: {imc:.1f} kg/m²</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='imc-status {status_class}'>{categorie_imc}</p>", unsafe_allow_html=True)
            
            # Interprétation et conseils généraux selon l'IMC
            interpretations = {
                "Sous-poids": "Votre IMC indique que vous êtes en sous-poids. Il est important d'augmenter votre apport calorique avec des aliments nutritifs et de consulter un professionnel de santé.",
                "Poids normal": "Félicitations ! Votre IMC est dans la fourchette normale. Continuez à maintenir une alimentation équilibrée et une activité physique régulière.",
                "Surpoids": "Votre IMC indique un léger surpoids. Envisagez d'augmenter votre activité physique et d'ajuster votre alimentation pour atteindre un poids plus sain.",
                "Obésité": "Votre IMC indique une obésité. Il est recommandé de consulter un professionnel de santé pour établir un plan personnalisé de perte de poids."
            }
            
            st.markdown(f"<p style='margin-top:1rem;'>{interpretations[categorie_imc]}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Plans alimentaires recommandés
            st.markdown("<div class='result-card'>", unsafe_allow_html=True)
            st.markdown("<h2 class='section-header'>Plan alimentaire recommandé</h2>", unsafe_allow_html=True)
            
            repas = {
                "Sous-poids": {
                    "Faible": {"Petit-déjeuner": "Attiéké avec sauce graine", "Déjeuner": "Foutou avec poisson braisé", "Dîner": "Riz gras avec viande"},
                    "Moyenne": {"Petit-déjeuner": "Couscous avec légumes", "Déjeuner": "Poulet braisé avec riz et légumes", "Dîner": "Salade de poisson"},
                    "Élevée": {"Petit-déjeuner": "Porridge avec baies et noix", "Déjeuner": "Filet de poisson avec légumes grillés", "Dîner": "Riz au lait et fruits frais"}
                },
                "Poids normal": {
                    "Faible": {"Petit-déjeuner": "Pain complet avec œufs", "Déjeuner": "Riz et sauce légumes", "Dîner": "Grillades de poisson et légumes"},
                    "Moyenne": {"Petit-déjeuner": "Yaourt nature et fruits", "Déjeuner": "Salade avec poulet grillé", "Dîner": "Soupe de légumes"},
                    "Élevée": {"Petit-déjeuner": "Smoothie vert et céréales", "Déjeuner": "Poisson au four avec légumes", "Dîner": "Soupe de légumes avec graines"}
                },
                "Surpoids": {
                    "Faible": {"Petit-déjeuner": "Pap avec lait", "Déjeuner": "Salade avec poulet grillé", "Dîner": "Poisson et légumes vapeur"},
                    "Moyenne": {"Petit-déjeuner": "Smoothie avec légumes", "Déjeuner": "Fruits et yaourt nature", "Dîner": "Poulet grillé et légumes"},
                    "Élevée": {"Petit-déjeuner": "Avoine avec fruits", "Déjeuner": "Quinoa avec légumes cuits", "Dîner": "Poisson et salade"}
                },
                "Obésité": {
                    "Faible": {"Petit-déjeuner": "Salade de fruits", "Déjeuner": "Soupe de légumes", "Dîner": "Poisson avec légumes"},
                    "Moyenne": {"Petit-déjeuner": "Smoothie de légumes", "Déjeuner": "Salade avec vinaigrette légère", "Dîner": "Poisson grillé"},
                    "Élevée": {"Petit-déjeuner": "Porridge de quinoa", "Déjeuner": "Légumes vapeur avec poulet", "Dîner": "Salade verte"}
                }
            }
            
            for repas_type, contenu in repas[categorie_imc][classe_sociale].items():
                st.markdown(f"""
                <div class='meal-card'>
                    <span class='meal-title'>{repas_type}:</span> {contenu}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Recommandations spécifiques
            st.markdown("<div class='result-card'>", unsafe_allow_html=True)
            st.markdown("<h2 class='section-header'>Recommandations personnalisées</h2>", unsafe_allow_html=True)
            
            # Recommandations selon genre et objectifs
            if genre == "Femme":
                if prendre_poids == "Oui":
                    st.markdown("""
                    <div class='recommendation'>
                        <p class='recommendation-title'>Conseils pour prendre du poids sainement</p>
                        <ul>
                            <li>Augmentez votre apport calorique avec des aliments nutritifs</li>
                            <li>Privilégiez les protéines de qualité (poisson, œufs, volaille, légumineuses)</li>
                            <li>Ajoutez des bonnes graisses à vos repas (avocat, huile d'olive, noix)</li>
                            <li>Pratiquez des exercices de musculation 3 fois par semaine</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                
                if si_developper_bassin == "Oui":
                    st.markdown("""
                    <div class='recommendation'>
                        <p class='recommendation-title'>Conseils pour développer le bassin et les hanches</p>
                        <ul>
                            <li>Concentrez-vous sur les exercices ciblant le bas du corps (squats, fentes, hip thrust)</li>
                            <li>Consommez suffisamment de protéines pour favoriser la croissance musculaire</li>
                            <li>Incluez des aliments riches en acides gras essentiels (poisson, avocat, noix)</li>
                            <li>Pratiquez ces exercices 3-4 fois par semaine pour des résultats optimaux</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
            
            if genre == "Homme":
                if objectif_sport == "Développer les abdos":
                    st.markdown("""
                    <div class='recommendation'>
                        <p class='recommendation-title'>Programme pour développer les abdominaux</p>
                        <ul>
                            <li>Réduisez votre pourcentage de graisse corporelle avec du cardio</li>
                            <li>Pratiquez des exercices variés pour les abdos (crunchs, planches, relevés de jambes)</li>
                            <li>Consommez des protéines maigres pour renforcer vos muscles</li>
                            <li>Limitez les aliments transformés et riches en sucres</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                elif objectif_sport == "Développer les épaules":
                    st.markdown("""
                    <div class='recommendation'>
                        <p class='recommendation-title'>Programme pour développer les épaules</p>
                        <ul>
                            <li>Intégrez des exercices de presse militaire, élévations latérales et frontales</li>
                            <li>Travaillez toutes les parties du deltoïde (avant, milieu, arrière)</li>
                            <li>Consommez suffisamment de protéines (1.6-2g par kg de poids corporel)</li>
                            <li>Assurez-vous de récupérer adéquatement entre les séances</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                elif objectif_sport == "Forme générale":
                    st.markdown("""
                    <div class='recommendation'>
                        <p class='recommendation-title'>Programme pour améliorer la forme générale</p>
                        <ul>
                            <li>Combinez entraînements cardio et musculation</li>
                            <li>Pratiquez des exercices poly-articulaires (squat, soulevé de terre, tractions)</li>
                            <li>Suivez une alimentation équilibrée riche en protéines, fruits et légumes</li>
                            <li>Visez 3-5 séances d'entraînement par semaine</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Recommandations spécifiques à l'obésité
            if categorie_imc == "Obésité":
                st.markdown("""
                <div class='recommendation'>
                    <p class='recommendation-title'>Recommandations spéciales pour l'obésité</p>
                    <ul>
                        <li>Consultez un médecin avant de commencer tout régime ou programme d'exercice</li>
                        <li>Suivez un régime hypocalorique supervisé par un professionnel</li>
                        <li>Commencez par des activités à faible impact comme la marche ou la natation</li>
                        <li>Fixez-vous des objectifs réalistes et progressifs</li>
                        <li>Envisagez un suivi psychologique pour vous aider dans votre démarche</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Évaluation de la fragilité
            st.markdown("<div class='result-card'>", unsafe_allow_html=True)
            st.markdown("<h2 class='section-header'>Évaluation de votre santé cardiovasculaire</h2>", unsafe_allow_html=True)
            
            if pression_syst < 90 or pression_diast < 50:
                st.markdown("""
                <div class='status-alert alert-warning'>
                    <p><strong>Attention :</strong> Votre pression artérielle est inférieure aux valeurs recommandées.</p>
                    <p>Il est conseillé de consulter un médecin avant de commencer tout programme d'exercice intensif.</p>
                    <p><strong>Recommandations :</strong></p>
                    <ul>
                        <li>Mangez des aliments riches en fer et en vitamines</li>
                        <li>Hydratez-vous régulièrement tout au long de la journée</li>
                        <li>Privilégiez les activités physiques modérées comme la marche</li>
                        <li>Évitez les changements brusques de position pour prévenir les étourdissements</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class='status-alert alert-success'>
                    <p><strong>Bonne nouvelle :</strong> Votre pression artérielle se situe dans les valeurs normales.</p>
                    <p>Vous pouvez suivre les recommandations adaptées à votre catégorie d'IMC et à vos objectifs personnels.</p>
                    <p>Pensez à maintenir de bonnes habitudes de vie pour préserver votre santé cardiovasculaire.</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        else:
            st.error("Veuillez entrer des valeurs valides pour la taille et le poids.")
    else:
        # Message d'accueil quand aucun calcul n'a été effectué
        st.markdown("""
        <div style="padding: 3rem; text-align: center; color: #3498db; background-color: white; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
            <img src="https://www.svgrepo.com/show/13656/heart.svg" width="100" style="margin-bottom: 1rem;">
            <h2 style="color: #2c3e50; margin-bottom: 1rem;">Bienvenue dans votre application de suivi de santé</h2>
            <p style="color: #7f8c8d; font-size: 1.1rem;">Complétez les informations dans le formulaire et cliquez sur le bouton "Calculer" pour obtenir des recommandations personnalisées pour améliorer votre santé.</p>
        </div>
        """, unsafe_allow_html=True)

# Pied de page
st.markdown("""
<div style="margin-top: 2rem; text-align: center; padding: 1rem; color: #7f8c8d; font-size: 0.9rem;">
    © 2025 Application de Suivi Santé IMC | Développée pour fournir des recommandations personnalisées
</div>
""", unsafe_allow_html=True)