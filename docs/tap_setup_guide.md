# Tap Setup Guide for `tap-devtoforemapiv1`

## Overview
`tap-devtoforemapiv1` is a Singer tap that supports multiple content management system extractors, built with the Meltano Tap SDK. This guide outlines the steps to set up and run any of the supported extractors.

## Supported Extractors

1. **Dev.to Extractor**
   - Extracts content from Dev.to platform
   - Supports articles, comments, and tags

2. **WordPress Extractor**
   - Extracts content from WordPress sites
   - Supports posts, categories, comments, and media files

3. **Hashnode Extractor**
   - Extracts content from Hashnode platform
   - Supports articles, comments, tags, and statistics

## Setup Instructions

### 1. Install the Tap
```bash
pipx install .
```

### 2. Configure Environment Variables
Create a `.env` file in the project root with the appropriate configuration for your chosen extractor:

#### Dev.to Extractor
```bash
TAP_DEVTOFOREMAPIV1_API_KEY=your_api_key
TAP_DEVTOFOREMAPIV1_USERNAME=your_username
TAP_DEVTOFOREMAPIV1_START_DATE=2023-01-01T00:00:00Z
TAP_DEVTOFOREMAPIV1_BLOG_SLUG=your_blog_slug
TAP_DEVTOFOREMAPIV1_INCLUDE_COMMENTS=true
TAP_DEVTOFOREMAPIV1_INCLUDE_TAGS=true
```

#### WordPress Extractor
```bash
TAP_WORDPRESS_USERNAME=your_username
TAP_WORDPRESS_PASSWORD=your_password
TAP_WORDPRESS_BASE_URL=https://your-wordpress-site.com
TAP_WORDPRESS_START_DATE=2023-01-01T00:00:00Z
TAP_WORDPRESS_INCLUDE_CATEGORIES=true
TAP_WORDPRESS_INCLUDE_COMMENTS=true
TAP_WORDPRESS_INCLUDE_MEDIA=true
```

#### Hashnode Extractor
```bash
TAP_HASHNODE_USERNAME=your_username
TAP_HASHNODE_API_KEY=your_api_key
TAP_HASHNODE_BLOG_SLUG=your_blog_slug
TAP_HASHNODE_START_DATE=2023-01-01T00:00:00Z
TAP_HASHNODE_INCLUDE_COMMENTS=true
TAP_HASHNODE_INCLUDE_TAGS=true
TAP_HASHNODE_INCLUDE_STATS=true
```

### 3. Run the Extractor
Choose the extractor you want to run:

```bash
# Run Dev.to extractor
meltano run tap-devtoforemapiv1 target-jsonl

# Run WordPress extractor
meltano run tap-wordpress target-jsonl

# Run Hashnode extractor
meltano run tap-hashnode target-jsonl
```

## Configuration Management

### Configuration Files
Each extractor has its own configuration file in the `configs` directory:
- `devto.yml` - For Dev.to extractor
- `wordpress.yml` - For WordPress extractor
- `hashnode.yml` - For Hashnode extractor

These files use the environment variables defined in the `.env` file.

### Override Settings
You can override specific settings using Meltano config commands:

```bash
# Set specific configuration
meltano config tap-devtoforemapiv1 set start_date "{{ env.TAP_DEVTOFOREMAPIV1_START_DATE }}"

# View current configuration
meltano config tap-devtoforemapiv1 list
```

## Common Errors and Solutions

### Error: Missing Configuration
- **Description**: The error indicates that a required property is missing.
- **Solution**: Ensure all required environment variables are set in the `.env` file and match the extractor you're trying to run.

### Error: Authentication Failed
- **Description**: The extractor fails to authenticate with the API.
- **Solution**: Verify that your API credentials are correct and have the necessary permissions.

### Error: Invalid Date Format
- **Description**: The start_date configuration is not in the correct format.
- **Solution**: Ensure the start_date is in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ

## Common Errors and Solutions

### Error: Command Not Found
- **Description**: The command `tap-devtoforemapiv1` is not recognized.
- **Solution**: Ensure the tap is installed using `pipx` and that the installation was successful.

### Error: Missing API Key
- **Description**: The error indicates that the `'api-key'` is a required property.
- **Solution**: Ensure that the API key is defined in the `.env` file and that the `meltano.yml` file references it correctly.

### Error: 404 Client Error
- **Description**: The request to the API endpoint returns a 404 error.
- **Solution**: Check the `path` in the `streams.py` file. Ensure it is set correctly without a leading slash:
  ```python
  path = "api/articles"
  ```

### Error: NoneType Received
- **Description**: The tap encounters a `NoneType` error when trying to access the API key.
- **Solution**: Ensure that the API key is referenced correctly in the `streams.py` file:
  ```python
  headers = {"api-key": self.config.get("api-key")}
  ```

## Conclusion
Following these steps should help you successfully set up and run the `tap-devtoforemapiv1`. If you encounter any further issues, refer to the Meltano documentation or community for additional support.
