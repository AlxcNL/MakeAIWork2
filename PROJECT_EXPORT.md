# Export van project

<ol>

<li>

Paden aanpassen

chmod +x convert_path.py && ./convert_path.py "relative\path\to\model"

<ul>

<li>In VsCode selecteer je het bestand met de rechtermuisknop en kies je 'Copy Relative Path'</li>
<li>Pas het pad aan als het om een sub-directory of juist hoger gelegen directory gaat</li>
<li>Test de start-scripts vanuit een (git bash) terminal</li>

</ul>

</li>
<br>

<li>
Pycache verwijderen

```bash
rm -r {project_directory}/__pycache__
```
</li>

<li> 
Map p2 aanmaken en daarin alle code en data kopieren

```bash
mkdir p2 && cp -r {project_directory} p2/
```

Map p2 toevoegen en committen met git

```bash
git add p2 && git commit -m "Deliverable Periode 2"
```

</li>

<li>

Git export van p2 maken

```bash
git archive -o "../{voornaam}_{achternaam}.zip" HEAD:p2
```

</li>

<li>

Testen en uploaden

<ol>

<li>p2.zip op een adere locatie uitpakken en testen</li>

<li>p2.zip uploaden naar eigen Teams kanaal -> Deliverables periode 2

</li>

</ol>
