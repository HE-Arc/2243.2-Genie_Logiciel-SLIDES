# CLAUDE.md — dépôt 2243.2-Genie_Logiciel-SLIDES

Slides du cours 2243.2 Génie logiciel (HE-Arc), en reveal.js, publiées sur GitHub Pages (`HE-Arc/2243.2-Genie_Logiciel-SLIDES`).
La tâche type est la **migration d'un chapitre** PDF/PPTX vers reveal.js.

## Règles

- **La forme change, pas le contenu.** Ne pas reformuler, ajouter, retirer ou réordonner du contenu sans demande explicite.
- **Coquilles et erreurs : les signaler, ne pas les corriger** sans validation (le chapitre 3 a gardé ses coquilles, le chapitre 7 les a corrigées à la demande).
- **Ne jamais commiter ni pousser.** Benoît commite lui-même. Pour `git status` / `git diff`, utiliser `git -c core.autocrlf=true` (sinon tous les fichiers paraissent modifiés à cause des fins de ligne).
- En cas de doute sur un choix de forme, faire le choix le plus proche du chapitre de référence et **le noter dans le compte rendu** (« choix non validés »).

## Structure

- `TO_MIGRATE/` : sources à migrer (`2243.2_NN_Titre.pdf` et souvent `.pptx`). Ne pas les déplacer ni les supprimer.
- `NN_Titre.html` : un fichier par chapitre (ex. `07_Intro_CMake_et_Ninja.html`).
- `medias/` : images, noms en minuscules et explicites (`usecase_include.png`, `cmake_logo.png`).
- `index.html` : liste des chapitres ; ajouter une entrée « N. Titre » par chapitre migré.
- `dist/theme/hearc.css` : thème HE-Arc.

## Recette de migration d'un chapitre

1. **Lire le chapitre de référence** : le dernier chapitre déjà migré (numéro le plus proche en dessous). Reprendre son en-tête, sa config et son code JS tels quels.
2. **Lire la source** : le PDF fait foi pour le contenu et l'ordre. Le PPTX sert à récupérer les images (en meilleure qualité) et les SVG. Les **slides masquées du PPTX** (absentes du PDF) ne sont pas migrées : les lister dans le compte rendu. Regarder les notes du PPTX (souvent vides).
3. **Créer `NN_Titre.html`** avec les conventions :
   - en-tête « 2243.2 Génie Logiciel - 2026-2027 », thème `hearc.css`, logos du chapitre de référence ;
   - config Reveal : 1920×1080, `slideNumber: 'c/t'`, sans transition ;
   - slide de titre avec la liste des sections ;
   - une pile verticale par section ;
   - titres `h2` préfixés du numéro de section quand le PDF numérote (« 3.2 Méthodes en cascade », sans tiret) ; sous-titres en `<h3><highlight>` ;
   - balises `<highlight>`, `<error>`, `<success>` ; colonnes `container` / `col-left` / `col-right` ;
   - typographie française (espaces avant `: ; ? !`, guillemets « »).
4. **Schémas** : redessiner en SVG généré par JS plutôt qu'en capture, en réutilisant le code existant :
   - feuille de route « Vue d'ensemble » (même code que les chapitres précédents) ;
   - flèche du cycle de vie avec `data-active` pour surligner la phase (slides « Rappel ») ;
   - arbres de modules avec `data-nodes`.
   Les graphiques simples (camembert, tableau) sont refaits en SVG/HTML avec les valeurs et couleurs de la source.
5. **Images** : extraire du PPTX (préférer les SVG d'origine aux PNG de repli), sinon du PDF avec `pdfimages`. Les ranger dans `medias/`.
6. **Code** : les captures de code deviennent du texte copiable dans des blocs de code.
7. **`index.html`** : ajouter l'entrée du chapitre.
8. **Site du cours** (dépôt voisin `2243.2-Genie_Logiciel`, Hugo) : dans `content/docs/cours/NN_Titre.md`, remplacer le shortcode `pdf` par le shortcode `slides`, plus le lien « Version imprimable (faire CTRL+P) » vers `NN_Titre.html?print-pdf` (avec `.html`). Ne pas toucher au reste de la page (exercices, liens).

## Vérification (obligatoire avant de dire « fini »)

- Ouvrir le chapitre avec Playwright : aucune erreur dans la console.
- Faire une capture de **chaque** slide (ou l'export `?print-pdf`) et une planche de contrôle.
- Vérifier sur chaque slide : rien ne dépasse les 1080 px de haut, rien ne chevauche le logo, les schémas JS s'affichent.
- Compter les slides : même nombre que les pages du PDF, sauf fusion notée dans le compte rendu.

## Compte rendu de fin

Terminer par un compte rendu court :
- fichiers créés ou modifiés (slides, `medias/`, `index.html`, page du site) ;
- nombre de slides / nombre de pages du PDF ;
- schémas redessinés, images extraites ;
- écarts de forme par rapport à la source ;
- **choix non validés** (à trancher par Benoît) ;
- coquilles repérées et non corrigées ;
- slides masquées non migrées.
