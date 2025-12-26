# Satellite-Property-Valuation
NOTE: MAPBOX STATIC MAP API HAS BEEN USED SO GET THE API KEY OF THE SAME, AND USE GOOGLE COLLAB TO RUN THE FILES.


pk.eyJ1IjoiamhhLXBhcmlqYXQiLCJhIjoiY21qbjNmejJ5MHJ2cDNlcGlpZnc1eXF5YyJ9.azskqHRd1Wv8grAGv4bJSQ

Follow the process to get it running in your laptop:


Sign up for a free account at Mapbox and get an Access Token.


Create a google collab notebook.


Click the key icon (Secrets) in the left-hand sidebar of Collab.


Add a new secret with the name MAPBOX_ACCESS_TOKEN and paste your token as the value.


Toggle the Notebook access switch to "on" for that secret.

>>!git clone https://github.com/Parijat1072005/satellite-property-valuation


Select the runtime as t4 GPU.


inside the satellite-property-valuation, make a folder named data.
inside the data make three folders named raw, processed and satellite_images.
put the dataset files inside the raw folder.

>>!pip install -r satellite-property-valuation/requirements.txt


>>%run /content/satellite-property-valuation/src/data_fetcher.py


>>%run /content/satellite-property-valuation/src/preprocessing.ipynb


>>%run /content/satellite-property-valuation/src/model_training.ipynb


