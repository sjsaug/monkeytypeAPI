import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Get your APE_KEY value from the environment variables (the .env you created)
load_dotenv()
ape_key = os.getenv('APE_KEY')

# Replace YOUR_APE_KEY with your Monkeytype authorization key
headers = {
    'Authorization': f'ApeKey {ape_key}'
}

# mode is the typing mode you want to get PBs for ie "time" or "words"
mode = "time"
# mode2 is the amount of time or words you want to get PBs for ie "60" or "15"
mode2= "15"

# Send a GET request to the Monkeytype API
response = requests.get(f'https://api.monkeytype.com/users/personalBests?mode={mode}&mode2={mode2}', headers=headers)

# Print the response content
    #print(response.content)

# Parse the response content as JSON
data = response.json()

# Print the JSON object
    #print(data)
    
# Print the different PBs received in the response
for pb in data['data']:

    # Convert the timestamp to a datetime object
    timestamp = datetime.fromtimestamp(pb['timestamp'] / 1000.0)
    print(f"Accuracy: {pb['acc']}")
    print(f"Consistency: {pb['consistency']}")
    print(f"Difficulty: {pb['difficulty']}")
    print(f"Lazy Mode: {pb['lazyMode']}")
    print(f"Language: {pb['language']}")
    print(f"Punctuation: {pb['punctuation']}")
    print(f"Raw WPM: {pb['raw']}")
    print(f"WPM: {pb['wpm']}")
    print(f"Timestamp: {timestamp}")
