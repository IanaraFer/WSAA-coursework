import requests

# Step 1: Shuffle the deck
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url)
if response.status_code == 200:
    deck = response.json()
    deck_id = deck['deck_id']  # Get the deck_id
else:
    print("Error shuffling the deck")
    exit()

# Step 2: Draw 5 cards
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(draw_url)
if response.status_code == 200:
    cards = response.json()['cards']
else:
    print("Error drawing cards")
    exit()

# Step 3: Print the value and suit of each card
print("Your hand of 5 cards:")
for card in cards:
    print(f"{card['value']} of {card['suit']}")
