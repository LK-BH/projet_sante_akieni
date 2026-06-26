# ============================================================ 
# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy 
# Ce fichier centralise toutes les constantes et variables metier 
# Il sera enrichi chaque semaine jusqu'a S24 
# ============================================================ 
# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ======== 
TAUX_EUR_FCFA = 655.957 
TAUX_USD_FCFA = 600.0 
SEUIL_OMS_DENSITE_MEDICALE = 2.3    
# medecins pour 1000 habitants 
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # pourcentage minimum OMS
SEUIL_MORTALITE_ALERTE = 2.0        # % deces / hospitalisations 
SEUIL_RUPTURE_STOCK_JOURS = 30      # jours minimum de stock 
DEPARTEMENTS_CONGO = [              # 12 departements officiels 
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette', 
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala', 
    'Niari', 'Plateaux', 'Pool', 'Sangha' 
] 
 
# === SECTION B : VARIABLES DES 5 HOPITAUX =================== 
# Hopital 1 — CHU de Brazzaville 
h1_nom              = 'CHU de Brazzaville' 
h1_ville            = 'Brazzaville' 
h1_departement      = 'Brazzaville' 
h1_type             = 'CHU' 
h1_nb_lits          = 320 
h1_nb_lits_occupes  = 284 
h1_nb_medecins      = 47 
h1_nb_infirmiers    = 123 
h1_population_zone  = 1_800_000 


# Hopital 2 — Hôpital Général Pointe-Noire
h2_nom = "Hôpital Général Pointe-Noire"
h2_ville = "Pointe-Noire"
h2_departement = "Pointe-Noire"
h2_type = "Hôpital Général"
h2_nb_lits = 250
h2_nb_lits_occupes = 190
h2_nb_medecins = 35
h2_nb_infirmiers = 98
h2_population_zone = 1_200_000

# Hopital 3 — Hôpital de Dolisie
h3_nom = "Hôpital de Dolisie"
h3_ville = "Dolisie"
h3_departement = "Niari"
h3_type = "Hôpital de district"
h3_nb_lits = 180
h3_nb_lits_occupes = 140
h3_nb_medecins = 22
h3_nb_infirmiers = 65
h3_population_zone = 450_000

# Hopital 4 — Hôpital de district Owando
h4_nom = "Hôpital de district Owando"
h4_ville = "Owando"
h4_departement = "Cuvette"
h4_type = "Hôpital de district"
h4_nb_lits = 120
h4_nb_lits_occupes = 95
h4_nb_medecins = 15
h4_nb_infirmiers = 40
h4_population_zone = 300_000

# Hopital 5 — Centre de santé de Impfondo
h5_nom = "Centre de santé de Impfondo"
h5_ville = "Impfondo"
h5_departement = "Likouala"
h5_type = "Centre de santé"
h5_nb_lits = 80
h5_nb_lits_occupes = 60
h5_nb_medecins = 10
h5_nb_infirmiers = 25
h5_population_zone = 200_000
# ... (completer pour les 4 autres hopitaux) 
 
# === SECTION C : VARIABLES DES 5 MEDICAMENTS ================ 
# TODO : Declarer les 5 medicaments essentiels 
m1_nom = "Artemether-Lumefantrine"
m1_quantite = 500
m1_seuil_rupture = 100
m1_cout_unitaire_fcfa = 2500.0

m2_nom = "Amoxicilline"
m2_quantite = 800
m2_seuil_rupture = 150
m2_cout_unitaire_fcfa = 500.0

m3_nom = "Paracétamol"
m3_quantite = 1200
m3_seuil_rupture = 200
m3_cout_unitaire_fcfa = 100.0

m4_nom = "SRO (sels de réhydratation orale)"
m4_quantite = 600
m4_seuil_rupture = 120
m4_cout_unitaire_fcfa = 300.0

m5_nom = "Vaccin antipaludéen"
m5_quantite = 400
m5_seuil_rupture = 80
m5_cout_unitaire_fcfa = 15000.0

# === SECTION D : CALCULS D'INITIALISATION =================== 
# TODO : Calculer les KPIs globaux initiaux 
population_totale = (
    h1_population_zone + h2_population_zone +
    h3_population_zone + h4_population_zone + h5_population_zone
)
nb_medecins_total = (
    h1_nb_medecins + h2_nb_medecins +
    h3_nb_medecins + h4_nb_medecins + h5_nb_medecins
)
densite_medicale_nationale = round(nb_medecins_total / population_totale * 1000, 2)

taux_occupation_moyen = round(
    ((h1_nb_lits_occupes / h1_nb_lits) +
     (h2_nb_lits_occupes / h2_nb_lits) +
     (h3_nb_lits_occupes / h3_nb_lits) +
     (h4_nb_lits_occupes / h4_nb_lits) +
     (h5_nb_lits_occupes / h5_nb_lits)) / 5 * 100, 1
)

valeur_stock_medicaments = (
    m1_quantite * m1_cout_unitaire_fcfa +
    m2_quantite * m2_cout_unitaire_fcfa +
    m3_quantite * m3_cout_unitaire_fcfa +
    m4_quantite * m4_cout_unitaire_fcfa +
    m5_quantite * m5_cout_unitaire_fcfa
)

# === SECTION E : RAPPORT D'INVENTAIRE ======================= 
# TODO : Afficher le rapport initial du systeme de sante 
print("=" * 70)
print(" RAPPORT INITIAL DU SYSTÈME DE SANTÉ — SEMAINE 2 ")
print("=" * 70)
print(f"Densité médicale nationale : {densite_medicale_nationale} médecins / 1000 habitants")
print(f"Taux d'occupation moyen    : {taux_occupation_moyen}%")
print(f"Valeur totale stock médocs : {valeur_stock_medicaments:,.0f} FCFA")

print("\n--- Hôpitaux suivis ---")
print("H1 :", h1_nom)
print("H2 :", h2_nom)
print("H3 :", h3_nom)
print("H4 :", h4_nom)
print("H5 :", h5_nom)

print("\n--- Médicaments essentiels ---")
print("-", m1_nom)
print("-", m2_nom)
print("-", m3_nom)
print("-", m4_nom)
print("-", m5_nom)

#-------------Semaine 3------------
# === SECTION F : Classification automatique des stocks médicaments ===
if m1_quantite <= m1_seuil_rupture:
    m1_statut = "RUPTURE CRITIQUE"
elif m1_quantite <= m1_seuil_rupture * 1.5:
    m1_statut = "ALERTE STOCK"
elif m1_quantite <= m1_seuil_rupture * 2.0:
    m1_statut = "STOCK LIMITE"
else:
    m1_statut = "STOCK NORMAL"

if m2_quantite <= m2_seuil_rupture:
    m2_statut = "RUPTURE CRITIQUE"
elif m2_quantite <= m2_seuil_rupture * 1.5:
    m2_statut = "ALERTE STOCK"
elif m2_quantite <= m2_seuil_rupture * 2.0:
    m2_statut = "STOCK LIMITE"
else:
    m2_statut = "STOCK NORMAL"

if m3_quantite <= m3_seuil_rupture:
    m3_statut = "RUPTURE CRITIQUE"
elif m3_quantite <= m3_seuil_rupture * 1.5:
    m3_statut = "ALERTE STOCK"
elif m3_quantite <= m3_seuil_rupture * 2.0:
    m3_statut = "STOCK LIMITE"
else:
    m3_statut = "STOCK NORMAL"

if m4_quantite <= m4_seuil_rupture:
    m4_statut = "RUPTURE CRITIQUE"
elif m4_quantite <= m4_seuil_rupture * 1.5:
    m4_statut = "ALERTE STOCK"
elif m4_quantite <= m4_seuil_rupture * 2.0:
    m4_statut = "STOCK LIMITE"
else:
    m4_statut = "STOCK NORMAL"

if m5_quantite <= m5_seuil_rupture:
    m5_statut = "RUPTURE CRITIQUE"
elif m5_quantite <= m5_seuil_rupture * 1.5:
    m5_statut = "ALERTE STOCK"
elif m5_quantite <= m5_seuil_rupture * 2.0:
    m5_statut = "STOCK LIMITE"
else:
    m5_statut = "STOCK NORMAL"

# === SECTION G : Classification occupation hôpitaux ==========
# Hôpital 1 — CHU Brazzaville
h1_taux_occ = round(h1_nb_lits_occupes / h1_nb_lits * 100, 1)
if h1_taux_occ > 95:
    h1_statut_occ = "CRITIQUE"
elif h1_taux_occ > 85:
    h1_statut_occ = "ÉLEVÉ"
elif h1_taux_occ < 60:
    h1_statut_occ = "SOUS-UTILISÉ"
else:
    h1_statut_occ = "OPTIMAL"

# Hôpital 2 — Pointe-Noire
h2_taux_occ = round(h2_nb_lits_occupes / h2_nb_lits * 100, 1)
if h2_taux_occ > 95:
    h2_statut_occ = "CRITIQUE"
elif h2_taux_occ > 85:
    h2_statut_occ = "ÉLEVÉ"
elif h2_taux_occ < 60:
    h2_statut_occ = "SOUS-UTILISÉ"
else:
    h2_statut_occ = "OPTIMAL"

# Hôpital 3 — Dolisie
h3_taux_occ = round(h3_nb_lits_occupes / h3_nb_lits * 100, 1)
if h3_taux_occ > 95:
    h3_statut_occ = "CRITIQUE"
elif h3_taux_occ > 85:
    h3_statut_occ = "ÉLEVÉ"
elif h3_taux_occ < 60:
    h3_statut_occ = "SOUS-UTILISÉ"
else:
    h3_statut_occ = "OPTIMAL"

# Hôpital 4 — Owando
h4_taux_occ = round(h4_nb_lits_occupes / h4_nb_lits * 100, 1)
if h4_taux_occ > 95:
    h4_statut_occ = "CRITIQUE"
elif h4_taux_occ > 85:
    h4_statut_occ = "ÉLEVÉ"
elif h4_taux_occ < 60:
    h4_statut_occ = "SOUS-UTILISÉ"
else:
    h4_statut_occ = "OPTIMAL"

# Hôpital 5 — Impfondo
h5_taux_occ = round(h5_nb_lits_occupes / h5_nb_lits * 100, 1)
if h5_taux_occ > 95:
    h5_statut_occ = "CRITIQUE"
elif h5_taux_occ > 85:
    h5_statut_occ = "ÉLEVÉ"
elif h5_taux_occ < 60:
    h5_statut_occ = "SOUS-UTILISÉ"
else:
    h5_statut_occ = "OPTIMAL"

# === SECTION H : Classification couverture vaccinale (NEW S3) ===

# Brazzaville
brazzaville_taux = round(418500 / 450000 * 100, 1)
if brazzaville_taux < 50:
    brazzaville_statut = "ZONE CRITIQUE"
elif brazzaville_taux < 80:
    brazzaville_statut = "ZONE A RISQUE"
elif brazzaville_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    brazzaville_statut = "ZONE INSUFFISANTE"
else:
    brazzaville_statut = "ZONE OPTIMALE"

# Pointe-Noire
pn_taux = round(229600 / 280000 * 100, 1)
if pn_taux < 50:
    pn_statut = "ZONE CRITIQUE"
elif pn_taux < 80:
    pn_statut = "ZONE A RISQUE"
elif pn_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    pn_statut = "ZONE INSUFFISANTE"
else:
    pn_statut = "ZONE OPTIMALE"

# Pool
pool_taux = round(54000 / 120000 * 100, 1)
if pool_taux < 50:
    pool_statut = "ZONE CRITIQUE"
elif pool_taux < 80:
    pool_statut = "ZONE A RISQUE"
elif pool_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    pool_statut = "ZONE INSUFFISANTE"
else:
    pool_statut = "ZONE OPTIMALE"

# Sangha
sangha_taux = round(35700 / 85000 * 100, 1)
if sangha_taux < 50:
    sangha_statut = "ZONE CRITIQUE"
elif sangha_taux < 80:
    sangha_statut = "ZONE A RISQUE"
elif sangha_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    sangha_statut = "ZONE INSUFFISANTE"
else:
    sangha_statut = "ZONE OPTIMALE"

# === SECTION I : Rapport d'état global avec alertes (NEW S3) ===
print("\n--- Statuts des Médicaments ---")
print(m1_nom, ":", m1_statut)
print(m2_nom, ":", m2_statut)
print(m3_nom, ":", m3_statut)
print(m4_nom, ":", m4_statut)
print(m5_nom, ":", m5_statut)

print("\n--- Occupation des Hôpitaux ---")
print(h1_nom, ":", h1_taux_occ, "% ->", h1_statut_occ)
print(h2_nom, ":", h2_taux_occ, "% ->", h2_statut_occ)
print(h3_nom, ":", h3_taux_occ, "% ->", h3_statut_occ)
print(h4_nom, ":", h4_taux_occ, "% ->", h4_statut_occ)
print(h5_nom, ":", h5_taux_occ, "% ->", h5_statut_occ)

print("\n--- Couverture Vaccinale ---")
print("Brazzaville :", brazzaville_taux, "% ->", brazzaville_statut)
print("Pointe-Noire :", pn_taux, "% ->", pn_statut)
print("Pool :", pool_taux, "% ->", pool_statut)
print("Sangha :", sangha_taux, "% ->", sangha_statut)

# Compteurs d'alertes médicaments
nb_ruptures_critiques = 0
nb_alertes_stock = 0

if m1_statut == "RUPTURE CRITIQUE":
    nb_ruptures_critiques += 1
elif m1_statut == "ALERTE STOCK":
    nb_alertes_stock += 1

if m2_statut == "RUPTURE CRITIQUE":
    nb_ruptures_critiques += 1
elif m2_statut == "ALERTE STOCK":
    nb_alertes_stock += 1

if m3_statut == "RUPTURE CRITIQUE":
    nb_ruptures_critiques += 1
elif m3_statut == "ALERTE STOCK":
    nb_alertes_stock += 1

if m4_statut == "RUPTURE CRITIQUE":
    nb_ruptures_critiques += 1
elif m4_statut == "ALERTE STOCK":
    nb_alertes_stock += 1

if m5_statut == "RUPTURE CRITIQUE":
    nb_ruptures_critiques += 1
elif m5_statut == "ALERTE STOCK":
    nb_alertes_stock += 1

# Compteurs hôpitaux
nb_hopitaux_critiques = 0
if h1_statut_occ == "CRITIQUE":
    nb_hopitaux_critiques += 1
if h2_statut_occ == "CRITIQUE":
    nb_hopitaux_critiques += 1
if h3_statut_occ == "CRITIQUE":
    nb_hopitaux_critiques += 1
if h4_statut_occ == "CRITIQUE":
    nb_hopitaux_critiques += 1
if h5_statut_occ == "CRITIQUE":
    nb_hopitaux_critiques += 1

# Compteurs zones vaccinales
nb_zones_critiques = 0
nb_zones_risque = 0

if brazzaville_statut == "ZONE CRITIQUE":
    nb_zones_critiques += 1
elif brazzaville_statut == "ZONE A RISQUE":
    nb_zones_risque += 1

if pn_statut == "ZONE CRITIQUE":
    nb_zones_critiques += 1
elif pn_statut == "ZONE A RISQUE":
    nb_zones_risque += 1

if pool_statut == "ZONE CRITIQUE":
    nb_zones_critiques += 1
elif pool_statut == "ZONE A RISQUE":
    nb_zones_risque += 1

if sangha_statut == "ZONE CRITIQUE":
    nb_zones_critiques += 1
elif sangha_statut == "ZONE A RISQUE":
    nb_zones_risque += 1

# Rapport global
print("=" * 70)
print(" RAPPORT GLOBAL — SEMAINE 3 ")
print("=" * 70)
print(f"Médicaments en rupture critique : {nb_ruptures_critiques}")
print(f"Médicaments en alerte stock     : {nb_alertes_stock}")
print(f"Hôpitaux en saturation critique : {nb_hopitaux_critiques}")
print(f"Zones vaccinales critiques      : {nb_zones_critiques}")
print(f"Zones vaccinales à risque       : {nb_zones_risque}")
print("-" * 70)
print("Résumé exécutif :")
if nb_ruptures_critiques > 0 or nb_hopitaux_critiques > 0 or nb_zones_critiques > 0:
    print("La situation sanitaire nationale nécessite une mobilisation immédiate.")
elif nb_alertes_stock > 0 or nb_zones_risque > 0:
    print("La situation est préoccupante, un suivi rapproché est recommandé.")
else:
    print("La situation est globalement satisfaisante, maintien du suivi standard.")
print("=" * 70)
