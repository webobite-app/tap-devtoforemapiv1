"""devtoForemAPIV1 tap class."""

from __future__ import annotations

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
# from tap_devtoforemapiv1 import streams
from tap_devtoforemapiv1.streams import (
    ArticlesStream
)

STREAM_TYPES: List[Stream] = [
    ArticlesStream
]

class TapdevtoForemAPIV1(Tap):
    """devtoForemAPIV1 tap class."""

    name = "tap-devtoforemapiv1"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api-key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            title="API Key",
            description="The token to authenticate against the API service",
        ),
        # th.Property(
        #     "project_ids",
        #     th.ArrayType(th.StringType),
        #     required=True,
        #     title="Project IDs",
        #     description="Project IDs to replicate",
        # ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
    ).to_dict()

    def discover_streams(self):
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [ArticlesStream(self)]


if __name__ == "__main__":
    TapdevtoForemAPIV1.cli()
