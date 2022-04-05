# Tipologia_PRA1 - WebScrapper de rutes a Cataluña

## Introducció

L'objectiu d'aquest codi és implementar un WebScrapping sobre la popular pàgina web de rutes Wikiloc. La consulta està preparada per a executar un webscrapping de les 1500 millors rutes, ordenades per ranking de popularitat / qualitat. La informació que ens mostra el buscador és la següent:

![image](https://user-images.githubusercontent.com/37300782/161796482-ac52b381-0518-42c1-9b54-f53a797915ca.png)

## robots.txt

S'ha fet un anàlisi de l'arxiu robots.txt, que s'adjunta a continuació, i no presenta cap limitació:

    User-Agent: *
    Allow: /
    Disallow: /*_full.jpg$
    Disallow: /wikiloc/companionRequest.do
    Disallow: /wikiloc/tr.do
    Disallow: /wikiloc/map.do
    Disallow: /wikiloc/geocode.do
    Disallow: /cdn-cgi/
    Sitemap: https://ca.wikiloc.com/sitemap.xml

## Contingut

El fitxer dataset resultant inclou un llistat de rutes amb els següents paràmetres:

| Atribut         | Descripció                                          |
|-----------------|-----------------------------------------------------|
| Nom de la ruta            | Senderisme, Bicicleta, running,...|
| Tipus d'activitat     | Municipi més proper a l'inici de la ruta|
| Punt d'inici | Distància total de la ruta |
| Distància          | Factor de qualitat FIFA del jugador|
| Desnivell positiu             | Desnivell positiu acomulat de la ruta|
| Ranking de wikiloc   | Ranking de Wikiloc (sobre 100) basat en la qualitat de la ruta per paràmetres de la web (descripció, imatges, explicació,...)|
| Ranking d'usuaris    | Puntuació d'altres usuaris a la ruta (sobre 5)|
| URL Imatge1                | Primera imatge de la ruta|
| URL Imatge2                | Segona imatge de la ruta|
| URL Imatge3                | Tercera imatge de la ruta|

## Agraïments

Les dades han estat obtingudes de la web de rutes Wikiloc

## Motivació

Es poden realitzar multiples estudis amb la informació que conté el dataset

  - Extraure informació sobre el tipus de ruta preferit de la població a Catalunya
  - Definir àrees geogràfiques on està més valorades les rutes naturals
  - Extraure conclusions en base a distància i elevació, i classificar les rutes amb paràmetres de 'duresa' per comparar les puntuacions

## Llicència

La llicència escollida per a aqquest projecte ha estat la llicència CC BY-SA 4.0 License, pels motius següents

  - Es permet la lliure distribució o copia del material que es proveeix per qualsevol motiu, inclosos motius comercials
  - S'ha d'acreditar el nom del creador de les dades, indicant si s'han fet canvis al conjunt de dades.
  - Si es modifica o es transformen les dades del dataset, s'han de distribuir les modificacions sota la mateixa llicència plantejada.

