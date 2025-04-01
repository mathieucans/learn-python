My journey in python 
===

# Installation de l'environnement

Install un environnement local au répertoire pour pas tout niker
```python3 -m venv ./.venv```

Active l'environnement
```. ./.venv/bin/activate```

# Configure intelij

1 - Ouvrir la fenêtre de configuration du projet    
![Configure-Intellij.png](docs/1-Configure-Intellij.png)
Ou menu file > Project structure

2 - Ajouter un SDK python

![2-Add-python-sdk.png](docs/2-Add-python-sdk.png)

3 - Choisir un interpréteur python 
![3-Select-python-interpreter.png](docs/3-Select-python-interpreter.png)

⚠ Ne pas choisir virtual env et bien choisir le binaire python et pas pip :-)

4 - Sélectionner interpreter pour le projet

![4-select-python-sdk.png](docs/4-select-python-sdk.png)

# Setup

Run the following command : 
```pip install -r requirements.txt```

# To clean up installed modules
```pip freeze | xargs pip uninstall -y```

