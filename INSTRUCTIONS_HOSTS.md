# Configuration du nom de domaine mission.malagasy.mg

Pour que votre application soit accessible via le nom de domaine `mission.malagasy.mg` en local, vous devez ajouter une entrée dans votre fichier hosts.

## Instructions pour Windows

1. Ouvrez le Bloc-notes en tant qu'administrateur
   - Recherchez "Bloc-notes" dans le menu Démarrer
   - Faites un clic droit sur "Bloc-notes" et sélectionnez "Exécuter en tant qu'administrateur"

2. Ouvrez le fichier hosts
   - Dans le Bloc-notes, allez dans Fichier > Ouvrir
   - Naviguez vers `C:\Windows\System32\drivers\etc`
   - Changez le filtre de fichiers de "Documents texte (*.txt)" à "Tous les fichiers (*.*)"
   - Sélectionnez le fichier `hosts` et cliquez sur Ouvrir

3. Ajoutez la ligne suivante à la fin du fichier:
   ```
   127.0.0.1 mission.malagasy.mg
   ```

4. Enregistrez le fichier
   - Allez dans Fichier > Enregistrer

5. Redémarrez Docker et votre navigateur

## Vérification

Après avoir effectué ces modifications, vous devriez pouvoir accéder à votre application via:

```
http://mission.malagasy.mg/
```

## Note importante

Cette configuration est uniquement pour le développement local. En production, vous devrez configurer correctement les DNS pour que le nom de domaine `mission.malagasy.mg` pointe vers l'adresse IP de votre serveur.