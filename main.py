import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any


class Transaction:
    """Represents a single transaction for an agent."""

    def __init__(self, amount: float, description: str, timestamp: str = None):
        self.amount = amount
        self.description = description
        self.timestamp = timestamp or datetime.utcnow().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "amount": self.amount,
            "description": self.description,
            "timestamp": self.timestamp,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Transaction":
        return Transaction(
            amount=data["amount"],
            description=data["description"],
            timestamp=data["timestamp"],
        )


class Ledger:
    """Keeps track of agents and their transactions."""

    def __init__(self):
        self.agents: Dict[str, List[Transaction]] = {}

    def add_agent(self, name: str) -> None:
        if name in self.agents:
            raise ValueError(f"Agent '{name}' already exists.")
        self.agents[name] = []

    def record(self, name: str, amount: float, description: str) -> None:
        if name not in self.agents:
            raise ValueError(f"Agent '{name}' not found.")
        self.agents[name].append(Transaction(amount, description))

    def balance(self, name: str) -> float:
        if name not in self.agents:
            raise ValueError(f"Agent '{name}' not found.")
        return sum(t.amount for t in self.agents[name])

    def history(self, name: str) -> List[Transaction]:
        if name not in self.agents:
            raise ValueError(f"Agent '{name}' not found.")
        return self.agents[name]

    def to_dict(self) -> Dict[str, Any]:
        return {
            agent: [t.to_dict() for t in txs] for agent, txs in self.agents.items()
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Ledger":
        ledger = Ledger()
        for agent, tx_list in data.items():
            ledger.agents[agent] = [Transaction.from_dict(tx) for tx in tx_list]
        return ledger

    def save(self, path: Path) -> None:
        path.write_text(json.dumps(self.to_dict(), indent=2))

    @staticmethod
    def load(path: Path) -> "Ledger":
        if not path.exists():
            return Ledger()
        return Ledger.from_dict(json.loads(path.read_text()))


def main() -> None:
    parser = argparse.ArgumentParser(prog="AgentLedger")
    subparsers = parser.add_subparsers(dest="command")

    # add-agent
    add_parser = subparsers.add_parser("add-agent")
    add_parser.add_argument("name")

    # transact
    tx_parser = subparsers.add_parser("transact")
    tx_parser.add_argument("name")
    tx_parser.add_argument("amount", type=float)
    tx_parser.add_argument("description")

    # balance
    bal_parser = subparsers.add_parser("balance")
    bal_parser.add_argument("name")

    # export
    exp_parser = subparsers.add_parser("export")
    exp_parser.add_argument("file")

    # import
    imp_parser = subparsers.add_parser("import")
    imp_parser.add_argument("file")

    args = parser.parse_args()
    ledger_file = Path("agent_ledger.json")
    ledger = Ledger.load(ledger_file)

    try:
        if args.command == "add-agent":
            ledger.add_agent(args.name)
            print(f"Agent '{args.name}' added.")
        elif args.command == "transact":
            ledger.record(args.name, args.amount, args.description)
            print(f"Recorded {args.amount} for '{args.name}': {args.description}")
        elif args.command == "balance":
            bal = ledger.balance(args.name)
            print(f"Balance for '{args.name}': {bal:.2f}")
        elif args.command == "export":
            ledger.save(Path(args.file))
            print(f"Ledger exported to {args.file}")
        elif args.command == "import":
            ledger = Ledger.load(Path(args.file))
            ledger.save(ledger_file)
            print(f"Ledger imported from {args.file}")
        else:
            parser.print_help()
            return
    except ValueError as e:
        print(f"Error: {e}")

    # Persist changes after any modifying operation
    if args.command in {"add-agent", "transact", "import"}:
        ledger.save(ledger_file)


if __name__ == "__main__":
    main()


class _MKza:
    version = 2

# TODO: revisit logic (55hny)


class _MZwd:
    version = 4

# TODO: revisit logic (zafxq)

# TODO: revisit logic (gxhjm)


def _helper_rwy88(x):
    # step 7
    return x + 7


def _helper_rrkdy(x):
    # step 8
    return x + 8

# TODO: revisit logic (03pem)


def _helper_zwm5v(x):
    # step 10
    return x + 10


def _helper_hqtif(x):
    # step 11
    return x + 11

# TODO: revisit logic (5kzdq)


class _MGeb:
    version = 13

# TODO: revisit logic (iltlf)

# TODO: revisit logic (9amms)

# TODO: revisit logic (nsxk5)


def _helper_p0qre(x):
    # step 17
    return x + 17
