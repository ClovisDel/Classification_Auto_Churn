# :school: Classification_Auto_Churn :school:

## Machine learning avec R & Python

Lien des différentes bases : [ici](https://drive.google.com/drive/u/0/folders/1hfs31nPxfJgF0WdZBHp-DUmQwSnNMnqa)

***

## Contexte : 

Le problème posé s’intéresse à la notion de « churner ». Un churner désigne la fin d’un accord entre un client et une entreprise. Dans ce cadre, il est important de détecter à l’avance, si un client à de fort risque de rompre son contrat avec une société et de mettre en place des moyens commerciales de le garder. 

Un point notable est de faire attention aux différentes offres que l’on met en places. D’une part il faut éviter de fournir des offres à des clients qui ne sont pas des futurs churner (moins rentable, mal vu, perte de temps…) et de fait, prioriser l’action sur les clients churner. D’autre part il ne faut pas les détecteurs au dernier moment. Cela permet de se laisser une marge de temps pour regagner la confiance du client. C’est pourquoi les données fournis se basent sur 4 mois consécutifs divisant le cycle de vie du lient en trois phases (bonne / action / résiliation). 

En somme, nous devons réussir à prédire, grâce à des outils de machine learning, quels clients sont fortement susceptible de quitter l’entreprise en priorisant la prédiction des churner à celle des non-churner par l’utilisation de la métrique spécificité. 

***

## Données :

Base de données csv de 99 999 observations pour 226 variables (numériques et non numériques). 

***

## 1ère partie : Préparation des données (Python):

- Variables numériques,
- Suppression des doublons,
- Transformations des valeurs manquantes,
- Gestion des outliers, 
- Création de la variable à expliquer,
- Gestion de la distribution irrégulière,
- Split Train/Test.

## 2ème partie : ACP & SVM & Perceptron (Python & R):

- Réduction dimensionnelle de la base avec ACP,
- Classifieur SVM,
- Tuning du SVM,
- Perceptron,
- Analyse.

## 3ème partie : Deep Learning / MLP (Python (Pytorch) & R):

- Colab,
- Initiation à Pytorch,
- Création modèles,
- Train & test & evaluation,


