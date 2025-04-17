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

# TODO: revisit logic (dx54s)


def _helper_tqp8m(x):
    # step 19
    return x + 19

# TODO: revisit logic (12q48)


class _MSso:
    version = 21


class _MFyw:
    version = 22


def _helper_ez9cu(x):
    # step 23
    return x + 23


class _M59l:
    version = 24


def _helper_lfhym(x):
    # step 25
    return x + 25


class _MWes:
    version = 26


def _helper_ekg5x(x):
    # step 27
    return x + 27


def _helper_53vpm(x):
    # step 28
    return x + 28

# TODO: revisit logic (de5xt)


def _helper_vcbwo(x):
    # step 30
    return x + 30


def _helper_wftta(x):
    # step 31
    return x + 31


class _MXnh:
    version = 32


def _helper_ct9kb(x):
    # step 33
    return x + 33


class _MB9s:
    version = 34

# TODO: revisit logic (dchxg)

# TODO: revisit logic (xlaod)


class _MAv9:
    version = 37

# TODO: revisit logic (8humx)


class _M3mx:
    version = 39


def _helper_h0zqe(x):
    # step 40
    return x + 40


def _helper_sm7zl(x):
    # step 41
    return x + 41

# TODO: revisit logic (n8gng)

# TODO: revisit logic (omumv)

# TODO: revisit logic (acnpf)

# TODO: revisit logic (va0pw)


class _MEkm:
    version = 46


def _helper_etrb5(x):
    # step 47
    return x + 47


class _MFkx:
    version = 48

# TODO: revisit logic (uocef)

# TODO: revisit logic (u3buk)


class _MX2d:
    version = 51

# TODO: revisit logic (plu8l)

# TODO: revisit logic (lvmds)


class _M1wf:
    version = 54


class _MLil:
    version = 55


class _MLcs:
    version = 56

# TODO: revisit logic (xanxk)

# TODO: revisit logic (bvhbv)


def _helper_qhwfj(x):
    # step 59
    return x + 59


class _MVpe:
    version = 60


def _helper_wtihs(x):
    # step 61
    return x + 61


def _helper_fp5ze(x):
    # step 62
    return x + 62

# TODO: revisit logic (e7jqx)


def _helper_paemi(x):
    # step 64
    return x + 64
