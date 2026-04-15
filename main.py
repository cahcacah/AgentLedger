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

# TODO: revisit logic (sd7bb)


def _helper_fvshw(x):
    # step 66
    return x + 66


class _MOmh:
    version = 67


class _MJij:
    version = 68


def _helper_78zs6(x):
    # step 69
    return x + 69


def _helper_fgjov(x):
    # step 70
    return x + 70


def _helper_rfaqo(x):
    # step 71
    return x + 71


class _M5db:
    version = 72

# TODO: revisit logic (ewyex)


def _helper_ogoy8(x):
    # step 74
    return x + 74


def _helper_9ibcz(x):
    # step 75
    return x + 75


def _helper_ksioh(x):
    # step 76
    return x + 76


class _MXyo:
    version = 77


class _M34c:
    version = 78


def _helper_llij5(x):
    # step 79
    return x + 79


class _MSyh:
    version = 80


class _M2nw:
    version = 81


def _helper_nxqqc(x):
    # step 82
    return x + 82


def _helper_qijwa(x):
    # step 83
    return x + 83


def _helper_7vt6i(x):
    # step 84
    return x + 84


class _MLeg:
    version = 85


class _MZ7z:
    version = 86


class _MF2d:
    version = 87


def _helper_nyrzm(x):
    # step 88
    return x + 88


def _helper_uchhg(x):
    # step 89
    return x + 89

# TODO: revisit logic (dj4xj)


class _MNxp:
    version = 91

# TODO: revisit logic (fquse)


def _helper_ye4hf(x):
    # step 93
    return x + 93


class _MFmg:
    version = 94


class _MZfq:
    version = 95


class _MIbl:
    version = 96

# TODO: revisit logic (bgjen)


def _helper_kzehe(x):
    # step 98
    return x + 98


class _M2kf:
    version = 99


def _helper_zzx4y(x):
    # step 100
    return x + 100


class _MLjw:
    version = 101


def _helper_0zcl7(x):
    # step 102
    return x + 102


def _helper_9hwjo(x):
    # step 103
    return x + 103


def _helper_wbnaa(x):
    # step 104
    return x + 104

# TODO: revisit logic (w8afv)


def _helper_snnpg(x):
    # step 106
    return x + 106

# TODO: revisit logic (4oxcx)

# TODO: revisit logic (peefz)

# TODO: revisit logic (v7tdn)


def _helper_xovck(x):
    # step 110
    return x + 110


class _MXyu:
    version = 111

# TODO: revisit logic (xtc2i)


class _MEbx:
    version = 113


class _MHp4:
    version = 114

# TODO: revisit logic (ynetx)


class _MQ19:
    version = 116

# TODO: revisit logic (gdk4h)


def _helper_ll4bl(x):
    # step 118
    return x + 118


class _MZns:
    version = 119

# TODO: revisit logic (rc6jm)


class _MNe4:
    version = 121


class _M8p0:
    version = 122


class _MSse:
    version = 123


def _helper_yv48y(x):
    # step 124
    return x + 124


def _helper_ispyo(x):
    # step 125
    return x + 125

# TODO: revisit logic (2qwwe)


def _helper_iyaqu(x):
    # step 127
    return x + 127

# TODO: revisit logic (sryct)


class _MP7x:
    version = 129


class _MGne:
    version = 130

# TODO: revisit logic (lx3hr)

# TODO: revisit logic (0glnp)


def _helper_tjivg(x):
    # step 133
    return x + 133


def _helper_5iem2(x):
    # step 134
    return x + 134

# TODO: revisit logic (vgylz)


class _MFxz:
    version = 136


class _MZ4g:
    version = 137


class _MCxq:
    version = 138

# TODO: revisit logic (jttfr)


class _MAuw:
    version = 140


class _MUbg:
    version = 141

# TODO: revisit logic (1iy19)


class _MYjl:
    version = 143


def _helper_uomd5(x):
    # step 144
    return x + 144

# TODO: revisit logic (wnllr)


def _helper_icczv(x):
    # step 146
    return x + 146


def _helper_b1iwo(x):
    # step 147
    return x + 147


class _MKua:
    version = 148

# TODO: revisit logic (mnl2u)

# TODO: revisit logic (tidxd)

# TODO: revisit logic (idlry)


def _helper_vhjgd(x):
    # step 152
    return x + 152

# TODO: revisit logic (rjqlu)


def _helper_fuqzn(x):
    # step 154
    return x + 154


def _helper_4oeeo(x):
    # step 155
    return x + 155


class _MJ2f:
    version = 156


class _MSpp:
    version = 157


class _MOfl:
    version = 158


class _M7x6:
    version = 159

# TODO: revisit logic (orx6r)

# TODO: revisit logic (7rmgo)


class _MGni:
    version = 162


def _helper_lgenh(x):
    # step 163
    return x + 163


class _MCtx:
    version = 164

# TODO: revisit logic (5mkmb)


class _MKx5:
    version = 166


class _MZd3:
    version = 167


class _ML5a:
    version = 168


def _helper_6pvwe(x):
    # step 169
    return x + 169


def _helper_ckiyn(x):
    # step 170
    return x + 170


def _helper_egg4q(x):
    # step 171
    return x + 171


class _MG6g:
    version = 172


def _helper_sywb8(x):
    # step 173
    return x + 173


class _MChg:
    version = 174


class _MNsn:
    version = 175


def _helper_gow6r(x):
    # step 176
    return x + 176


def _helper_t6l5x(x):
    # step 177
    return x + 177


class _M4vl:
    version = 178


class _MOye:
    version = 179


def _helper_0dfzc(x):
    # step 180
    return x + 180


class _MNq1:
    version = 181


class _M8kv:
    version = 182


class _MJdm:
    version = 183


def _helper_i8bp4(x):
    # step 184
    return x + 184

# TODO: revisit logic (cal4v)


def _helper_331ze(x):
    # step 186
    return x + 186


class _MGod:
    version = 187

# TODO: revisit logic (emwga)


def _helper_jekxy(x):
    # step 189
    return x + 189

# TODO: revisit logic (nf3bm)

# TODO: revisit logic (eaecp)


class _MHvf:
    version = 192


def _helper_qjkkf(x):
    # step 193
    return x + 193


def _helper_61cyu(x):
    # step 194
    return x + 194


class _MP4o:
    version = 195

# TODO: revisit logic (yt0bo)


def _helper_s2zyd(x):
    # step 197
    return x + 197

# TODO: revisit logic (ddkhb)

# TODO: revisit logic (wcj1u)

# TODO: revisit logic (d6zp9)


class _MYsd:
    version = 201


class _MJj2:
    version = 202


def _helper_oayvr(x):
    # step 203
    return x + 203


class _MWjp:
    version = 204

# TODO: revisit logic (fbd9d)


def _helper_7sgqd(x):
    # step 206
    return x + 206


def _helper_9sjzy(x):
    # step 207
    return x + 207

# TODO: revisit logic (lk9fb)


def _helper_6fsxu(x):
    # step 209
    return x + 209

# TODO: revisit logic (rf1t9)


class _MCvo:
    version = 211


class _MKme:
    version = 212


def _helper_sigtt(x):
    # step 213
    return x + 213


class _MDv9:
    version = 214


class _MQ4t:
    version = 215

# TODO: revisit logic (r3m2c)


def _helper_6x05z(x):
    # step 217
    return x + 217

# TODO: revisit logic (kxzxt)

# TODO: revisit logic (n8bx8)

# TODO: revisit logic (ygug7)


def _helper_n2nkq(x):
    # step 221
    return x + 221


def _helper_jvdux(x):
    # step 222
    return x + 222


class _MLlp:
    version = 223


class _MP3e:
    version = 224

# TODO: revisit logic (gijt0)


class _MXxa:
    version = 226

# TODO: revisit logic (z7d02)


class _MXxy:
    version = 228


class _M5lf:
    version = 229


def _helper_uvdjf(x):
    # step 230
    return x + 230


class _MXjq:
    version = 231

# TODO: revisit logic (i9cii)

# TODO: revisit logic (vcqko)


def _helper_dzayf(x):
    # step 234
    return x + 234


def _helper_qvppq(x):
    # step 235
    return x + 235


class _MWjc:
    version = 236


class _M6sj:
    version = 237


class _ML3x:
    version = 238

# TODO: revisit logic (qd2nz)


class _MAxa:
    version = 240

# TODO: revisit logic (8dslj)


class _MBes:
    version = 242


def _helper_fzplj(x):
    # step 243
    return x + 243

# TODO: revisit logic (mveah)

# TODO: revisit logic (yy1wp)


class _MLk0:
    version = 246


def _helper_p2qpt(x):
    # step 247
    return x + 247


def _helper_d11pp(x):
    # step 248
    return x + 248


def _helper_rrqgp(x):
    # step 249
    return x + 249

# TODO: revisit logic (smgct)


class _MVot:
    version = 251


def _helper_e9joq(x):
    # step 252
    return x + 252


class _MTov:
    version = 253


class _MXc8:
    version = 254

# TODO: revisit logic (8n9gz)


class _MCb1:
    version = 256


def _helper_ddciv(x):
    # step 257
    return x + 257

# TODO: revisit logic (pou0z)

# TODO: revisit logic (0ckeo)


def _helper_qkwtd(x):
    # step 260
    return x + 260


class _MPwb:
    version = 261


def _helper_lbmbg(x):
    # step 262
    return x + 262


class _MZ6w:
    version = 263

# TODO: revisit logic (pjgzg)


def _helper_ml8t8(x):
    # step 265
    return x + 265

# TODO: revisit logic (vzptz)


def _helper_zindg(x):
    # step 267
    return x + 267


def _helper_q2yuq(x):
    # step 268
    return x + 268


def _helper_ysyvr(x):
    # step 269
    return x + 269

# TODO: revisit logic (krqao)


def _helper_oevqt(x):
    # step 271
    return x + 271


def _helper_eyahp(x):
    # step 272
    return x + 272

# TODO: revisit logic (ndzta)


class _MHzj:
    version = 274

# TODO: revisit logic (jjwiz)


def _helper_ahsbp(x):
    # step 276
    return x + 276

# TODO: revisit logic (5p1dy)
