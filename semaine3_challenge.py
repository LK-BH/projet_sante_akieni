# ============================================================
# AKIENI ACADEMY — Projet Santé Publique
# Semaine 3 — Challenge Entreprise : Rapport Sanitaire
# ============================================================

# --- DONNEES DES HOPITAUX ---
chu_lits_totaux, chu_lits_occ, chu_medecins, chu_ruptures, chu_alertes = 320, 298, 47, 2, 2
pn_lits_totaux, pn_lits_occ, pn_medecins, pn_ruptures, pn_alertes = 180, 143, 22, 0, 1
dol_lits_totaux, dol_lits_occ, dol_medecins, dol_ruptures, dol_alertes = 95, 91, 8, 1, 2
owa_lits_totaux, owa_lits_occ, owa_medecins, owa_ruptures, owa_alertes = 45, 32, 3, 3, 0
imp_lits_totaux, imp_lits_occ, imp_medecins, imp_ruptures, imp_alertes = 20, 19, 1, 2, 1

# --- FONCTIONS ---
def taux_occupation(lits_occ, lits_totaux):
    return round((lits_occ / lits_totaux) * 100, 1)

def niveau_global(nb_ruptures, nb_alertes, nb_medecins, taux_occ):
    if (nb_ruptures >= 2) or (taux_occ > 95):
        return "[CRITIQUE]"
    elif (nb_ruptures >= 1) or (taux_occ > 85) or (nb_alertes >= 2 and nb_medecins < 5):
        return "[PREOCCUPANT]"
    else:
        return "[SATISFAISANT]"

def recommandation(niveau):
    if niveau == "[CRITIQUE]":
        return "Mobiliser la réserve nationale PNA"
    elif niveau == "[PREOCCUPANT]":
        return "Renforcer la logistique et suivi rapproché"
    else:
        return "Maintenir le suivi standard"

def ligne_hopital(nom, lits_occ, lits_totaux, nb_medecins, nb_ruptures, nb_alertes):
    occ = taux_occupation(lits_occ, lits_totaux)
    niveau = niveau_global(nb_ruptures, nb_alertes, nb_medecins, occ)
    return f"  {nom:<25} {occ:>5}%   {nb_ruptures}R + {nb_alertes}A    {niveau}"

# --- RAPPORT ---
print("="*65)
print("  TABLEAU DE BORD SANITAIRE — MINISTERE DE LA SANTE")
print("  Date : 16 janvier 2026  |  Pour le Conseil des Ministres")
print("="*65)
print("  HOPITAL                    OCCUPATION   ALERTES    NIVEAU GLOBAL")

print(ligne_hopital("CHU Brazzaville", chu_lits_occ, chu_lits_totaux, chu_medecins, chu_ruptures, chu_alertes))
print(ligne_hopital("Hopital Pointe-Noire", pn_lits_occ, pn_lits_totaux, pn_medecins, pn_ruptures, pn_alertes))
print(ligne_hopital("Hopital Dolisie", dol_lits_occ, dol_lits_totaux, dol_medecins, dol_ruptures, dol_alertes))
print(ligne_hopital("Hopital Owando", owa_lits_occ, owa_lits_totaux, owa_medecins, owa_ruptures, owa_alertes))
print(ligne_hopital("CMS Impfondo", imp_lits_occ, imp_lits_totaux, imp_medecins, imp_ruptures, imp_alertes))

print("-"*65)

# --- BILAN NATIONAL ---
total_ruptures = chu_ruptures + pn_ruptures + dol_ruptures + owa_ruptures + imp_ruptures
total_critiques = sum([
    1 if niveau_global(chu_ruptures, chu_alertes, chu_medecins, taux_occupation(chu_lits_occ, chu_lits_totaux)) == "[CRITIQUE]" else 0,
    1 if niveau_global(pn_ruptures, pn_alertes, pn_medecins, taux_occupation(pn_lits_occ, pn_lits_totaux)) == "[CRITIQUE]" else 0,
    1 if niveau_global(dol_ruptures, dol_alertes, dol_medecins, taux_occupation(dol_lits_occ, dol_lits_totaux)) == "[CRITIQUE]" else 0,
    1 if niveau_global(owa_ruptures, owa_alertes, owa_medecins, taux_occupation(owa_lits_occ, owa_lits_totaux)) == "[CRITIQUE]" else 0,
    1 if niveau_global(imp_ruptures, imp_alertes, imp_medecins, taux_occupation(imp_lits_occ, imp_lits_totaux)) == "[CRITIQUE]" else 0
])

print(f"  {total_critiques} hopitaux sur 5 en situation CRITIQUE")
print(f"  {total_ruptures} ruptures de stock identifiées à l'échelle nationale")
print(f"  RECOMMANDATION PRIORITAIRE : Mobiliser la réserve nationale PNA")
print("="*65)
