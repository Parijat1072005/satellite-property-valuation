import os
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from dotenv import load_dotenv
from tqdm import tqdm

# Load environment variables
load_dotenv()
MAPBOX_TOKEN = os.getenv("MAPBOX_ACCESS_TOKEN")

# Configuration for Mapbox
SAVE_DIR = "data/satellite_images/"
ZOOM = 17
WIDTH, HEIGHT = 400, 400

# --- SETUP RETRY STRATEGY ---
# total=5 means it will try 6 times in total (1 original + 5 retries)
retry_strategy = Retry(
    total=5,
    backoff_factor=1, # Wait 1s, 2s, 4s, 8s, 16s between retries
    status_forcelist=[429, 500, 502, 503, 504],
    raise_on_status=False, # Don't crash if final retry also fails
    connect=5 # Specifically retries on DNS/Connection errors
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)

def download_satellite_image(lat, lon, property_id):
    file_path = os.path.join(SAVE_DIR, f"{property_id}.jpg")
    
    # Check if image already exists (Resumption Logic)
    if os.path.exists(file_path):
        return

    # Mapbox coordinates are LON, LAT
    url = f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/{lon},{lat},{ZOOM}/{WIDTH}x{HEIGHT}"
    
    params = {
        "access_token": MAPBOX_TOKEN,
        "attribution": "false",
        "logo": "false"
    }

    try:
        # CRITICAL CHANGE: Use 'session.get' instead of 'requests.get'
        response = session.get(url, params=params, timeout=15)
        
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
        else:
            print(f"\nError {response.status_code} for ID {property_id}")
            
    except Exception as e:
        # This will catch the Errno 11001 if all 5 retries fail
        print(f"\nFailed to resolve/connect for ID {property_id}: {e}")

def main():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    # Load local data
    try:
        df = pd.read_excel("data/raw/train(1).xlsx")
    except FileNotFoundError:
        print("Error: train(1).xlsx not found in data/raw/")
        return
    
    print(f"Starting/Resuming download for {len(df)} images...")
    
    # Process rows
    for _, row in tqdm(df.iterrows(), total=df.shape[0]):
        download_satellite_image(row['lat'], row['long'], row['id'])

if __name__ == "__main__":
    main()