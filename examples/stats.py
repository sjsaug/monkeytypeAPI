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

# Send a GET request to the Monkeytype API
response = requests.get(f'https://api.monkeytype.com/users/stats', headers=headers)

# Parse the response content as JSON
data = response.json()

# Convert the timeTyping value to minutes, hours, and days
time_typing = data['data']['timeTyping']
time_typing_minutes = time_typing / 60
time_typing_hours = time_typing / 3600
time_typing_days = time_typing / 86400

# Create percentCompleted
percentCompleted = data['data']['completedTests'] / data['data']['startedTests'] * 100
    
# Print the different stats received in the response
print(f"Started Tests: {data['data']['startedTests']}")
print(f"Completed Tests: {data['data']['completedTests']}")
print(f"Percent Completed: {percentCompleted}%")
print(f"Time Typing (minutes): {time_typing_minutes}")
print(f"Time Typing (hours): {time_typing_hours}")
print(f"Time Typing (days): {time_typing_days}")