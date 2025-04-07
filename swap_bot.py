import time
import random
from cosmpy.aerial.client import LedgerClient
from cosmpy.aerial.wallet import LocalWallet
from cosmpy.aerial.tx import Transaction
from config import NETWORKS, PRIVATE_KEY
from token_list import fetch_token_list
from utils import get_token_address

def generate_swap_params(token_list, networks):
    """Generate randomized swap parameters with a valid token address."""
    source_dict, destination_dict = random.sample(list(networks.values()), 2)
    source, destination = source_dict["name"], destination_dict["name"]
    token_symbol = random.choice(networks[source_dict["name"]]["tokens"])
    token_address = get_token_address(token_list, source, token_symbol)
    amount = round(random.uniform(1, 10), 2)
    return source, destination, token_address, amount

def execute_swap(source, destination, token_address, amount, retries=3):
    """Execute a real swap transaction on the blockchain."""
    wallet = LocalWallet.from_private_key(PRIVATE_KEY)
    source_rpc = NETWORKS[source]["rpc_endpoint"]
    client = LedgerClient(source_rpc)

    for attempt in range(retries):
        try:
            tx = Transaction()
            tx.add_transfer(destination, token_address, f"{amount}utoken")  # Adjust denomination as needed
            tx.sign(wallet)
            result = client.broadcast_tx(tx)
            print(f"Transaction Successful! Tx Hash: {result.tx_hash}")
            return True
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(5)  # Wait before retry
    print("Swap failed after all retries.")
    return False

if __name__ == "__main__":
    token_list = fetch_token_list("union-testnet-9")  # Default network
    if token_list:
        for _ in range(20):  # Execute 20 transactions per network daily
            source, destination, token, amount = generate_swap_params(token_list, NETWORKS)
            execute_swap(source, destination, token, amount)
            time.sleep(random.randint(1800, 7200))  # Random delay between 30 mins to 2 hours
