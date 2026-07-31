import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("Detailed info for debugging")
logging.info("Pipeline started")
logging.warning("Missing city value — filling with Unknown")
logging.error("Failed to cast total to float")
logging.critical("Database connection lost — pipeline cannot continue")


records = [
    {'order_id': 1, 'total': '150.00'},
    {'order_id': 2, 'total': 'INVALID'},
    {'order_id': 3, 'total': '89.99'},
    {'order_id': 4, 'total': '-50.00'},
    {'order_id': 5, 'total': '300.00'},
]


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pipeline.log'),
        logging.StreamHandler()          # also print to terminal
    ]
)

# What log level is used when a record fails type casting?

# What log level is used when a record has a negative total?

# How many INFO messages appear in the output?

# Add one more logger.info() call before the for loop and one after — what would you put there that's useful?

