import time
import threading
import logging
import datetime
from config import NETWORKS, WALLET_MNEMONIC, PRIVATE_KEY
from utils import fetch_token_list
from swap_worker import swap_worker

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Starting Testnet Swap Bot...")

    token_list = fetch_token_list("union-testnet-9")  # Default network, adjust as needed
    if not token_list:
        logging.error("Unable to fetch token list. Exiting.")
        return

    if not WALLET_MNEMONIC and not PRIVATE_KEY:
        logging.error("Wallet credentials not provided. Exiting.")
        return
    logging.info("Wallet imported successfully.")

    now = datetime.datetime.now()
    next_midnight = (now + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    run_duration = (next_midnight - now).total_seconds()
    logging.info(f"Bot will run for approximately {run_duration/3600:.2f} hours until final login at midnight.")

    summary_logs = {"successful": [], "skipped": [], "errors": []}
    stop_event = threading.Event()
    threads = []

    for network in NETWORKS.keys():
        thread = threading.Thread(target=swap_worker, args=(network, NETWORKS, token_list, summary_logs, stop_event))
        thread.start()
        threads.append(thread)

    time.sleep(run_duration)
    stop_event.set()

    for thread in threads:
        thread.join()

    logging.info("----- Final Summary Log at 00:00 AM -----")
    logging.info("Successful Transactions:")
    for entry in summary_logs["successful"]:
        logging.info(entry)
    logging.info("Skipped Transactions:")
    for entry in summary_logs["skipped"]:
        logging.info(entry)
    logging.info("Errors Encountered:")
    for entry in summary_logs["errors"]:
        logging.info(entry)

    logging.info("Closing sessions. Bot execution completed for the day.")

if __name__ == "__main__":
    main()
