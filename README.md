# Satellite-Property-Valuation
NOTE: MAPBOX STATIC MAP API HAS BEEN USED SO GET THE API KEY OF THE SAME, AND USE GOOGLE COLLAB TO RUN THE FILES.



Follow the process to get it running in your laptop:


Sign up for a free account at Mapbox and get an Access Token.


Create a google collab notebook.


Select the runtime as t4 GPU.


Click the key icon (Secrets) in the left-hand sidebar of Collab.


Add a new secret with the name MAPBOX_ACCESS_TOKEN and paste your token as the value.


Toggle the Notebook access switch to "on" for that secret.


>>!git clone https://github.com/Parijat1072005/satellite-property-valuation


Inside the satellite-property-valuation, make a folder named data.



Inside the data, make a folder named raw.



Put the dataset files inside the raw folder, you can find it in the repoitory's initial project release.



Now run the following commands one by one in the collaboratory's cells.



>>!pip install -r satellite-property-valuation/requirements.txt


>>%run /content/satellite-property-valuation/src/data_fetcher.py


>>%run /content/satellite-property-valuation/src/preprocessing.ipynb


>>%run /content/satellite-property-valuation/src/model_training.ipynb


