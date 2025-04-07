import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Wallet credentials
WALLET_MNEMONIC = os.getenv("WALLET_MNEMONIC")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

if not WALLET_MNEMONIC and not PRIVATE_KEY:
    raise ValueError("Either WALLET_MNEMONIC or PRIVATE_KEY must be set in .env")

# Define supported networks with token lists and RPC endpoints
NETWORKS = {
    "bbn-test-5": {
        "name": "Babylon Testnet",
        "tokens": ["USDT", "BBN", "UNO"],
        "token_list_url": "https://unionlabs.github.io/token-lists/babylon.babylon-testnet-1/tokenlist.json",
        "rpc_endpoint": "https://rpc.testnet.babylonchain.io"  # Example RPC, replace with actual
    },
    "elgafar-1": {
        "name": "Stargaze Testnet",
        "tokens": ["STARS", "UNO", "mkUSD"],
        "token_list_url": "https://unionlabs.github.io/token-lists/stargaze.elgafar-1/tokenlist.json",
        "rpc_endpoint": "https://rpc.elgafar-1.stargaze.io"  # Example RPC, replace with actual
    },
    "stride-internal-1": {
        "name": "Stride Testnet",
        "tokens": ["STRD"],
        "token_list_url": "https://unionlabs.github.io/token-lists/stride.stride-internal-1/legacy-tokenlist.json",
        "rpc_endpoint": "https://rpc.stride-internal-1.stride.zone"  # Example RPC, replace with actual
    },
    "union-testnet-9": {
        "name": "Union Testnet",
        "tokens": ["USDT", "mkUSD", "UNO"],
        "token_list_url": "https://unionlabs.github.io/token-lists/union.union-testnet-9/tokenlist.json",
        "rpc_endpoint": "https://rpc.testnet.union.build"  # Example RPC, replace with actual
    },
}
