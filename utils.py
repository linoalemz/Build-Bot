import logging

def get_token_address(token_list, network_name, token_symbol):
    """Retrieve the token address for a given symbol and network from the token list."""
    if not token_list or "tokens" not in token_list:
        logging.error("Invalid token list provided.")
        return None
    
    for token in token_list["tokens"]:
        if token.get("symbol") == token_symbol and network_name in token.get("address", ""):
            return token["address"]
    
    logging.warning(f"Token {token_symbol} not found for network {network_name}.")
    return None

def fetch_token_list(network_key=None):
    """Wrapper around token_list.fetch_token_list with fallback."""
    from token_list import fetch_token_list as fetch
    if network_key:
        return fetch(network_key)
    return fetch("union-testnet-9")
