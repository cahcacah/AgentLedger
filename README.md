# AgentLedger

AgentLedger is a lightweight Python library for managing financial ledgers for autonomous agents.  
It provides a simple API to record transactions, query balances, and persist data to disk.

## Features
- Create and manage multiple agents
- Record credit and debit transactions with timestamps
- Query individual agent balances and full transaction history
- Export and import ledgers as JSON files
- Command‑line interface for quick interactions

## Installation
```bash
git clone https://github.com/yourname/AgentLedger.git
cd AgentLedger
pip install -r requirements.txt   # (requires only the standard library)
```

## Usage
```bash
# Add an agent
python main.py add-agent Alice

# Record a transaction
python main.py transact Alice 150.00 "Project payment"

# Show balance
python main.py balance Alice

# Export ledger
python main.py export ledger.json
```

## License
MIT License – feel free to use, modify, and distribute.