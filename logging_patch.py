# logging_patch.py
import logging

# Set root logger to INFO (not DEBUG - we only want DEBUG for trading endpoints)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Get a logger for this module
logger = logging.getLogger(__name__)

# Enable DEBUG only for trading-related modules
trading_targets = [
    "routers.trading",
    "services.accounts_service",
    "utils.logging_decorator",
    "utils.connector_manager",
    "services.orders_recorder",
    "services.funding_recorder",
    "hummingbot.connector.client_order_tracker",  # ← ADD THIS
    "hummingbot.connector.derivative",            # ← ADD THIS for connector warnings
]

for name in trading_targets:
    logging.getLogger(name).setLevel(logging.DEBUG)

logger.info("⚡ DEBUG logging enabled for trading endpoints only")
