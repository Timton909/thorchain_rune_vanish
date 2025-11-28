import requests, time

def rune_vanish():
    print("THORChain — RUNE Vanish Detector (> 100k RUNE single outbound)")
    seen = set()
    while True:
        r = requests.get("https://thornode.ninerealms.com/thorchain/outbounds")
        for outbound in r.json()[:30]:
            txid = outbound.get("tx_id") or outbound.get("id")
            if not txid or txid in seen: continue
            seen.add(txid)

            amount = int(outbound.get("amount", 0)) / 1e8
            if amount >= 100_000:
                chain = outbound["chain"]
                to = outbound.get("to_address", "unknown")[:16]
                print(f"RUNE VANISHED\n"
                      f"{amount:,.0f} RUNE sent out to {chain}\n"
                      f"To: {to}...\n"
                      f"TxID: {txid}\n"
                      f"https://viewblock.io/thorchain/tx/{txid}\n"
                      f"{'-'*60}")
        time.sleep(3.5)

if __name__ == "__main__":
    rune_vanish()
