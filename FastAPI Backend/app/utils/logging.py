import logging
import coloredlogs

# Configure logging
coloredlogs.install(
    level='INFO',  # Set the logging level
    fmt='%(levelname)s:     %(message)s - %(asctime)s',
    datefmt='%Y-%m-%d %H:%M:%S',  # Format for the timestamp
    field_styles={'levelname': {'bold': True, 'color': 'green'}},  # Color for the log level
)


# Create a logger instance
logger = logging.getLogger(__name__)