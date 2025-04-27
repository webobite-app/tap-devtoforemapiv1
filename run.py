from tap_devtoforemapiv1.tap import TapdevtoForemAPIV1
from target_jsonl.target import TargetJSONL  # Replace with actual import if different
from singer_sdk.helpers._util import read_json
import io

# Tap config
tap_config = {
    "api_key": ""
}

# Target config
target_config = {
    "destination_path": "./output",  # Customize path
    "format": "jsonl"
}

# Create tap and target instances
tap = TapDevToForemAPIV1(config=tap_config)
target = TargetJSONL(config=target_config)

# Discover and sync streams
tap_discovered_catalog = tap.discover_catalog()

# Activate the streams you want (you can also filter here)
for stream in tap.get_selected_streams(tap_discovered_catalog):
    for message in stream.sync():
        # Write each Singer message (RECORD, STATE, SCHEMA)
        target._write_message(message)
