CARD_VALUES = {
    'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10
}

def calculate_hand_value(cards):
    """Calculate the value of a hand, handling aces properly."""
    value = sum(CARD_VALUES[card] for card in cards)
    aces = cards.count('A')
    
    # Adjust for aces if we're over 21
    while value > 21 and aces > 0:
        value -= 10  # Convert ace from 11 to 1
        aces -= 1
    
    return value

def get_basic_strategy(player_cards, dealer_card):
    """Return basic strategy recommendation."""
    value = calculate_hand_value(player_cards)
    
    # Handle pairs
    if len(player_cards) == 2 and player_cards[0] == player_cards[1]:
        return get_pair_strategy(player_cards[0], dealer_card)
    
    # Handle soft hands (with ace)
    if 'A' in player_cards:
        return get_soft_hand_strategy(value, dealer_card)
    
    # Handle hard hands
    return get_hard_hand_strategy(value, dealer_card)

def get_pair_strategy(pair_card, dealer_card):
    """Basic strategy for pairs."""
    dealer_value = CARD_VALUES[dealer_card]
    
    if pair_card == 'A' or pair_card == '8':
        return 'Split'
    elif pair_card in ['2', '3', '7']:
        return 'Split' if dealer_value <= 7 else 'Hit'
    elif pair_card in ['4', '5', '10', 'J', 'Q', 'K']:
        return 'Hit' if pair_card == '4' else 'Double/Hit' if pair_card == '5' else 'Stand'
    elif pair_card == '6':
        return 'Split' if dealer_value <= 6 else 'Hit'
    elif pair_card == '9':
        return 'Split' if dealer_value not in [7, 10, 11] else 'Stand'
    return 'Hit'

def get_soft_hand_strategy(value, dealer_card):
    """Basic strategy for soft hands (with ace)."""
    dealer_value = CARD_VALUES[dealer_card]
    
    if value >= 20:
        return 'Stand'
    elif value == 19:
        return 'Double/Stand' if dealer_value == 6 else 'Stand'
    elif value == 18:
        if dealer_value <= 6:
            return 'Double/Stand'
        elif dealer_value <= 8:
            return 'Stand'
        return 'Hit'
    elif value == 17:
        return 'Double/Hit' if 3 <= dealer_value <= 6 else 'Hit'
    elif value == 16:
        return 'Double/Hit' if 4 <= dealer_value <= 6 else 'Hit'
    elif value == 15:
        return 'Double/Hit' if 4 <= dealer_value <= 6 else 'Hit'
    elif value == 14:
        return 'Double/Hit' if 5 <= dealer_value <= 6 else 'Hit'
    return 'Hit'

def get_hard_hand_strategy(value, dealer_card):
    """Basic strategy for hard hands."""
    dealer_value = CARD_VALUES[dealer_card]
    
    if value >= 17:
        return 'Stand'
    elif value >= 13:
        return 'Stand' if dealer_value <= 6 else 'Hit'
    elif value == 12:
        return 'Stand' if 4 <= dealer_value <= 6 else 'Hit'
    elif value == 11:
        return 'Double/Hit'
    elif value == 10:
        return 'Double/Hit' if dealer_value <= 9 else 'Hit'
    elif value == 9:
        return 'Double/Hit' if 3 <= dealer_value <= 6 else 'Hit'
    return 'Hit'

def main():
    print("\nWelcome to Blackjack Helper!")
    print("Enter cards as: A, 2-10, J, Q, or K")
    print("Type 'quit' to exit\n")
    
    while True:
        # Get player's cards
        player_input = input("\nEnter your cards (space-separated, e.g., 'A 7'): ").strip().upper()
        if player_input.lower() == 'quit':
            break
            
        player_cards = player_input.split()
        if not all(card in CARD_VALUES for card in player_cards):
            print("Invalid cards! Please use: A, 2-10, J, Q, or K")
            continue
            
        # Get dealer's card
        dealer_input = input("Enter dealer's up card: ").strip().upper()
        if dealer_input.lower() == 'quit':
            break
            
        if dealer_input not in CARD_VALUES:
            print("Invalid dealer card! Please use: A, 2-10, J, Q, or K")
            continue
            
        # Calculate and display results
        hand_value = calculate_hand_value(player_cards)
        recommendation = get_basic_strategy(player_cards, dealer_input)
        
        print("\nResults:")
        print(f"Your hand value: {hand_value}")
        print(f"Recommended action: {recommendation}")
        
        if hand_value > 21:
            print("Warning: Your hand is bust!")

if __name__ == '__main__':
    main()
