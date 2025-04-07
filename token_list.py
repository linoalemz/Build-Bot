import requests
import logging
import random

# Token list URLs for each network (moved to config.py, kept here for reference)
TOKEN_LIST_URLS = {
    "union-testnet-9": "https://unionlabs.github.io/token-lists/union.union-testnet-9/tokenlist.json",
    "stargaze-testnet": "https://unionlabs.github.io/token-lists/stargaze.elgafar-1/tokenlist.json",
    "stride-testnet": "https://unionlabs.github.io/token-lists/stride.stride-internal-1/legacy-tokenlist.json",
    "babylon-testnet": "https://unionlabs.github.io/token-lists/babylon.babylon-testnet-1/tokenlist.json",
}

logging.basicConfig(level=logging.INFO)

def fetch_token_list(network):
    """Fetch available tokens from the specified network's token list."""
    token_list_url = TOKEN_LIST_URLS.get(network)

    if not token_list_url:
        logging.error(f"No token list URL found for network: {network}")
        return None

    try:
        response = requests.get(token_list_url)
        response.raise_for_status()
        token_list = response.json()
        logging.info(f"Token list successfully fetched for {network}.")
        return token_list
    except requests.RequestException as e:
        logging.error(f"Error fetching token list for {network}: {e}")
        return None

def get_token_balance():
    """Simulate retrieving a token balance by generating a random amount."""
    return round(random.uniform(1000, 5000), 2)  # Random balance between 1000 and 5000

if __name__ == "__main__":
    network = "union-testnet-9"  # Example: Fetching tokens for Union Testnet 9
    tokens = fetch_token_list(network)
    
    if tokens:
        print(f"Fetched tokens for {network}:")
        for token in tokens.get("tokens", []):
            symbol = token.get("symbol")
            address = token.get("address")
            balance = get_token_balance()
            print(f"Token: {symbol}, Address: {address}, Balance: {balance}")
