## Présentation d'un projet Python

Dans ce projet présenté à Bernard BONCHE, dans le cadre de la semaine d'examen du 27 Juin 2022, nous traiterons les notions suivantes : 

La modélisation 3D avec Blender

Les tokens non fongibles (ou NFT)

La programmation avec Python

Ce mini projet aura pour but de développer en python, dans le cadre d'une mission concrète avec un véritable projet à la clé, un système de génération de modèle 3D unique grâce à des textures stocké dans un dossier. 

Le but sera de récupérer un renard modéliser avec un style "Low Poly".
De créer ses textures en format png sous forme de petits carrés.
De générer autant de model 3D dans un dossier qu'il y'a de textures existantes.

Chaque renard générer devras posséder un format .glb pour pouvoir chargé le model sur le web avec la librairie adéquate, et devra également posséder un rendu image .png d'un rendu caméra.

Le tout devra être dispatché dans des dossiers séparés.

Ce projet servira à générer plus de 10 000 NFT avec un rendu 3D et tout cela d'un seul coup.


## Présentation de blender

Blender est un logiciel libre de modélisation, d’animation par ordinateur et de rendu en 3D, créé en 1998. Il est actuellement développé par la Fondation Blender.

Depuis 2019 le logiciel Blender est de plus en plus reconnu par les entreprises du secteur de l'animation 3D, comme Epic Games, Ubisoft et NVIDIA3,4,5.

Il propose des fonctions avancées de modélisation (dont la sculpture 3D, le texturage et dépliage UV, etc), d’animation 3D (rigging, blend shapes), et de rendu (sur GPU comme sur CPU). Il gère aussi le montage vidéo non linéaire, la composition, la création nodale de matériaux, ainsi que diverses simulations physiques telles que les particules, les corps rigides, les corps souples et les fluides. Ses capacités sont par ailleurs très extensibles, grâce à un système de greffons (addons).


## Les NFTs c'est quoi ? 

Un NFT, ou jeton non fongible en français, c’est un certificat numérique de propriété qui désigne un objet unique : une musique, une image ou un personnage de jeu vidéo. Ce document donne toutes les informations sur l’objet : son auteur, combien il l’a vendu, et à qui. 

De plus, seul son propriétaire peut le déchiffrer ou le modifier, car ce fichier utilise un langage secret et très sécurisé. Pour ça, il est enregistré sur Internet dans une sorte de grand livre de comptes ultraprotégé, la blockchain. Pour acheter un NFT, tout se fait en cryptomonnaie, de l’argent numérique qui s’échange uniquement en ligne.

Ces dernières années, des milliards d’euros ont été dépensés pour acheter des NFT. Un collage numérique géant ou un simple tweet ont ainsi été vendus plusieurs millions d’euros ! Avec ce nouveau système, les artistes peuvent présenter leurs œuvres numériques sur Internet et les vendre. Ils gagnent aussi plus d’argent, car la vente se fait directement avec l’acheteur. Cependant, des œuvres vendues très cher ne vaudront peut-être plus rien dans quelque temps… Et certains escrocs créent des NFT avec des images volées sur Internet. Aujourd’hui, les avis sont partagés sur l’avenir des NFT. Alors, idée de génie ou non, à chacun de se faire son opinion.

## Mon projet Blender associé à un script Python

1 - Installer blender
>tp-blender > 1 - Installateur blender

2 - Ouvrir le fichier Fox.blend
>tp-blender > sources > mesh

3 - Lancer le script Python

4 - Ouvrez un navigateur web et coller cette URL
>https://sandbox.babylonjs.com/

5 - Aller dans le dossier export
>tp-blender > sources > exports

6 - Faite glisser un à un les modèles générés en format .glb

Voyez que les renards changent en fonction de la texture  appliqué dans la boucle.

Vous êtes enfin prêt à créer des NFTs en 3D et à les générer !

