import time
import random
import logging
import datetime
from swap_bot import execute_swap, generate_swap_params

def swap_worker(network, networks, token_list, summary_logs, stop_event):
    """Worker function to perform swaps for a specific network."""
    logging.info(f"Starting swap worker for {network}")
    
    while not stop_event.is_set():
        try:
            source, destination, token_address, amount = generate_swap_params(token_list, networks)
            if source not in networks[network]["name"] and destination not in networks[network]["name"]:
                log_entry = f"{datetime.datetime.now()} - {network}: Skipped swap {source} -> {destination} (not involving this network)"
                summary_logs["skipped"].append(log_entry)
                logging.info(log_entry)
                time.sleep(random.randint(1800, 7200))
                continue

            success = execute_swap(source, destination, token_address, amount)
            if success:
                log_entry = f"{datetime.datetime.now()} - {network}: Successful swap {source} -> {destination}, Token: {token_address}, Amount: {amount}"
                summary_logs["successful"].append(log_entry)
                logging.info(log_entry)
            else:
                log_entry = f"{datetime.datetime.now()} - {network}: Failed swap {source} -> {destination}"
                summary_logs["errors"].append(log_entry)
                logging.error(log_entry)
        
        except Exception as e:
            log_entry = f"{datetime.datetime.now()} - {network}: Error during swap - {str(e)}"
            summary_logs["errors"].append(log_entry)
            logging.error(log_entry)
        
        time.sleep(random.randint(1800, 7200))

    logging.info(f"Stopping swap worker for {network}")
