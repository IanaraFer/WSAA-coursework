import requests

try:
    # Step 1: Shuffle the deck
    shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(shuffle_url)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    deck = response.json()
    deck_id = deck.get('deck_id')  # Safely get 'deck_id'
    if not deck_id:
        print("Error: 'deck_id' not found in the response.")
        exit()
except requests.exceptions.RequestException as e:
    print(f"Error shuffling the deck: {e}")
    exit()

try:
    # Step 2: Draw 5 cards
    draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
    response = requests.get(draw_url)
    response.raise_for_status()
    cards = response.json().get('cards')  # Safely get 'cards'
    if not cards:
        print("Error: 'cards' not found in the response.")
        exit()
    # Process the cards (e.g., print them)
    for card in cards:
        print(f"{card['value']} of {card['suit']}")
except requests.exceptions.RequestException as e:
    print(f"Error drawing cards: {e}")
    exit()