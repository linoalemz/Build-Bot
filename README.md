Clone the Repository
```bash
git clone https://github.com/linoalemz/Build-Bot.git
```
```bash
cd Build-Bot
```
Create .env
```bash
nano .env
```
```bash
WALLET_MNEMONIC="your testnet mnemonic here"
PRIVATE_KEY="your testnet private key here"
```
Install Dependencies
```bash
pip install -r requirements.txt
```
Troubleshooting:
If pip fails, try pip3 install -r requirements.txt.
Ensure cosmpy installs correctly (pip install cosmpy).

Run the Bot
```bash
python main.py
```

Expected Output: Logs showing swap attempts, successes, or errors.
Check blockchain explorers (e.g., Union Testnet explorer) for tx hashes.
Troubleshooting:
RPC Errors: Verify RPC endpoints are live.
Insufficient Funds: Ensure your wallet has test tokens.



