# Blackjack Helper

A command-line tool to help with blackjack strategy decisions. This tool implements basic blackjack strategy and provides recommendations based on your cards and the dealer's up card.

## Features

- Calculates hand values, properly handling aces
- Provides basic strategy recommendations
- Supports all standard blackjack actions (Hit, Stand, Double, Split)
- Handles soft hands (hands containing an ace)
- Handles pairs appropriately

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ArnaudCallea/Black-Jack-Helper.git
cd Black-Jack-Helper
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the program:
```bash
python blackjack_helper.py
```

Enter your cards when prompted:
- Use A for Ace
- Use 2-10 for number cards
- Use J, Q, K for face cards
- Separate multiple cards with spaces (e.g., "A 7")

The program will:
1. Calculate your hand value
2. Provide the recommended action based on basic strategy
3. Warn you if your hand is bust

## Example

```
Enter your cards (space-separated, e.g., 'A 7'): A 7
Enter dealer's up card: 6

Results:
Your hand value: 18
Recommended action: Double/Stand
```

## Strategy Implementation

The tool implements standard basic blackjack strategy, including:
- Hard hand strategy
- Soft hand strategy
- Pair splitting strategy
- Double down opportunities

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests!
