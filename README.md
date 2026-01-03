# Satellite Imagery-Based Property Valuation
## Project Overview
This project implements a Multimodal Deep Learning pipeline designed to estimate residential property values by combining traditional house specifications with spatial environmental context captured from satellite imagery.

While traditional valuation models rely solely on tabular data (e.g., number of bedrooms, square footage), this model integrates high-resolution satellite tiles to "see" neighborhood quality, proximity to amenities, and green cover. By fusing these two distinct data modalities, the model captures visual nuances that are often missing from standard real estate spreadsheets.

## Key Objectives
**Automated Data Acquisition**: Programmatically fetch satellite imagery using the Mapbox Static Images API for thousands of properties.

**Multimodal Fusion**: Develop a neural network that processes images via a Convolutional Neural Network (CNN) and tabular data via a Multi-Layer Perceptron (MLP).

**Explainable AI (XAI)**: Utilize Grad-CAM (Gradient-weighted Class Activation Mapping) to visualize which visual features (like parks or road density) drive the model's price predictions.

**Performance Benchmarking**: Compare the multimodal model against a tabular-only Random Forest baseline to measure the "value add" of visual data.

## Technical Architecture
**The system utilizes a Late-Fusion Architecture**:

***Image Branch***: A pre-trained ResNet18 model acts as a feature extractor, converting satellite tiles into high-dimensional visual embeddings.

***Tabular Branch***: A dense MLP processes features such as sqft_living, grade, and condition.

***Concatenation Layer***: The outputs from both branches are "glued" together into a single feature vector.

***Regression Head***: A final series of fully connected layers outputs the predicted property price.

## Setup instructions:
NOTE: MAPBOX STATIC MAP API HAS BEEN USED SO GET THE API KEY OF THE SAME, AND USE GOOGLE COLLAB TO RUN THE FILES.



Follow the process to get it running in your laptop:


Sign up for a free account at Mapbox "https://console.mapbox.com/account/access-tokens/" and get an Access Token.


Create a google colab notebook.


Select the runtime as t4 GPU.


Click the key icon (Secrets) in the left-hand sidebar of Colab.


Add a new secret with the name MAPBOX_ACCESS_TOKEN and paste your token as the value.


Toggle the Notebook access switch to "on" for that secret.


>>!git clone https://github.com/Parijat1072005/satellite-property-valuation


Inside the satellite-property-valuation, make a folder named data.



Inside the data, make a folder named "raw" and another folder named "processed".



Put the dataset files inside the raw folder, you can find it in the repoitory's initial project release.



Now run the following commands one by one in the colaboratory's cells.



>>%cd satellite-property-valuation 



>>!pip install -r requirements.txt


>>%run src/data_fetcher.py


>>%run src/preprocessing.ipynb


>>%run src/model_training.ipynb


