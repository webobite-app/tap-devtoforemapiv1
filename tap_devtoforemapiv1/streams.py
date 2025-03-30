from singer_sdk import Stream, RESTStream
from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class ArticlesStream(RESTStream):
    """DEV.to articles stream"""
    name = "articles"
    path = "/articles"
    primary_keys = ["id"]
    replication_key = "published_at"
    records_jsonpath = "$[*]"
    
    @property
    def url_base(self) -> str:
        return "https://dev.to/api"
    
    def get_url_params(self, context, next_page_token):
        params = {
            "page": 1,
            "per_page": 1000
        }
        if next_page_token:
            params["page"] = next_page_token
        return params
    
    def get_next_page_token(self, response, previous_token):
        data = response.json()
        if len(data) == 1000:  # If max per_page reached
            return (previous_token or 1) + 1
        return None
    
    schema = PropertiesList(
        Property("id", IntegerType),
        Property("title", StringType),
        Property("description", StringType),
        Property("published_at", DateTimeType),
        Property("slug", StringType),
        Property("body_markdown", StringType),
        # Add more fields from API response
    ).to_dict()
    
    def prepare_request(self, context, next_page_token):
        headers = {"api-key": self.config.get("api-key")}
        request = super().prepare_request(context, next_page_token)
        request.headers.update(headers)
        return request