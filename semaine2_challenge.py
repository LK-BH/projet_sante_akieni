# ============================================================
# AKIENI ACADEMY — Projet Santé Publique
# Semaine 2 — Challenge Entreprise : Demande Urgente du DSS
# ============================================================

# --- DONNEES BRUTES ---
# Hôpital de Kinkala
budget_kinkala = 12_500_000
consultations_kinkala = 1847
hospitalisations_kinkala = 312
deces_kinkala = 8
lits_total_kinkala = 45
lits_occupes_kinkala = 41
medecins_kinkala = 3
population_kinkala = 85_000

# CMS de Vindza
budget_vindza = 6_800_000
consultations_vindza = 923
hospitalisations_vindza = 87
deces_vindza = 2
lits_total_vindza = 20
lits_occupes_vindza = 14
medecins_vindza = 1
population_vindza = 42_000

# Hôpital de Kindamba
budget_kindamba = 9_200_000
consultations_kindamba = 1234
hospitalisations_kindamba = 201
deces_kindamba = 11
lits_total_kindamba = 35
lits_occupes_kindamba = 33
medecins_kindamba = 2
population_kindamba = 67_000

# --- CALCULS KPIs ---
# Kinkala
cout_moyen_kinkala = round(budget_kinkala / (consultations_kinkala + hospitalisations_kinkala), 2)
taux_occupation_kinkala = round(lits_occupes_kinkala / lits_total_kinkala * 100, 1)
densite_medicale_kinkala = round(medecins_kinkala / population_kinkala * 1000, 2)
taux_mortalite_kinkala = round(deces_kinkala / hospitalisations_kinkala * 100, 2)

# Vindza
cout_moyen_vindza = round(budget_vindza / (consultations_vindza + hospitalisations_vindza), 2)
taux_occupation_vindza = round(lits_occupes_vindza / lits_total_vindza * 100, 1)
densite_medicale_vindza = round(medecins_vindza / population_vindza * 1000, 2)
taux_mortalite_vindza = round(deces_vindza / hospitalisations_vindza * 100, 2)

# Kindamba
cout_moyen_kindamba = round(budget_kindamba / (consultations_kindamba + hospitalisations_kindamba), 2)
taux_occupation_kindamba = round(lits_occupes_kindamba / lits_total_kindamba * 100, 1)
densite_medicale_kindamba = round(medecins_kindamba / population_kindamba * 1000, 2)
taux_mortalite_kindamba = round(deces_kindamba / hospitalisations_kindamba * 100, 2)

# --- AFFICHAGE RAPPORT ---
print("=== RAPPORT COMPARATIF — Département du Pool ===")
print(f"{'Hôpital':25} {'Coût moyen/patient':20} {'Occupation (%)':15} {'Densité médicale':20} {'Taux mortalité (%)':20}")
print("-"*100)

print(f"{'Hôpital de Kinkala':25} {cout_moyen_kinkala:>20,.2f} {taux_occupation_kinkala:>15} {densite_medicale_kinkala:>20} {taux_mortalite_kinkala:>20}")
print(f"{'CMS de Vindza':25} {cout_moyen_vindza:>20,.2f} {taux_occupation_vindza:>15} {densite_medicale_vindza:>20} {taux_mortalite_vindza:>20}")
print(f"{'Hôpital de Kindamba':25} {cout_moyen_kindamba:>20,.2f} {taux_occupation_kindamba:>15} {densite_medicale_kindamba:>20} {taux_mortalite_kindamba:>20}")

print("\nALERTES CRITIQUES")
if taux_mortalite_kinkala > 2.0 or densite_medicale_kinkala < 0.05:
    print(f" ALERTE : Hôpital de Kinkala est en situation critique (Mortalité {taux_mortalite_kinkala}% / Densité {densite_medicale_kinkala}).")
if taux_mortalite_vindza > 2.0 or densite_medicale_vindza < 0.05:
    print(f" ALERTE : CMS de Vindza est en situation critique (Mortalité {taux_mortalite_vindza}% / Densité {densite_medicale_vindza}).")
if taux_mortalite_kindamba > 2.0 or densite_medicale_kindamba < 0.05:
    print(f" ALERTE : Hôpital de Kindamba est en situation critique (Mortalité {taux_mortalite_kindamba}% / Densité {densite_medicale_kindamba}).")

# --- BONUS ---
budget_total = budget_kinkala + budget_vindza + budget_kindamba
cout_medecins_5 = 5 * 1_200_000 * 3  # 3 hôpitaux, 5 médecins chacun
print("\nBONUS")
if budget_total >= cout_medecins_5:
    print(f" Le budget total ({budget_total:,} FCFA) suffit pour financer 5 médecins par hôpital.")
else:
    print(f" Le budget total ({budget_total:,} FCFA) est insuffisant pour 5 médecins par hôpital.")
