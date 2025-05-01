"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_devtoforemapiv1.tap import TapdevtoForemAPIV1

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "api-key": "your_api_key_here",  # Add the API key here
}


# Run standard built-in tap tests from the SDK:
TestTapdevtoForemAPIV1 = get_tap_test_class(
    tap_class=TapdevtoForemAPIV1,
    config=SAMPLE_CONFIG,
)


# TODO: Create additional tests as appropriate for your tap.
