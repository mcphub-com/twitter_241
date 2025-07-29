# Aigeon AI Twitter 241

## Project Description

Aigeon AI Twitter 241 is a Python-based server application designed to interact with Twitter data through a series of API endpoints. The application provides a suite of tools to retrieve various types of user-related information from Twitter, such as user details, tweets, media, and social connections. This project leverages the FastMCP server framework to expose these functionalities as tools that can be easily accessed and utilized.

## Features Overview

- Retrieve Twitter user information by username or user IDs.
- Access user tweets, media, and replies.
- Explore user social connections, including followers and followings.
- Support for paginated data retrieval using cursors.
- Integration with a third-party API for data access.

## Main Features and Functionality

The Aigeon AI Twitter 241 server provides several key functionalities for interacting with Twitter data:

1. **User Information Retrieval**: Fetch detailed information about a Twitter user using their username or user ID.
2. **Tweets and Media Access**: Obtain a user's tweets and media content, with support for pagination.
3. **Social Connections**: Retrieve information about a user's followers, followings, and verified followers.
4. **Replies and Interactions**: Access a user's replies and interactions on Twitter.

## Main Functions Description

Below is a description of the main functions provided by the Aigeon AI Twitter 241 server, including their parameters:

### `get_user_by_username`

- **Description**: Retrieves information about a Twitter user based on their username.
- **Parameters**:
  - `username`: The Twitter username of the user.

### `get_users_by_ids`

- **Description**: Fetches information for multiple users using their Twitter IDs.
- **Parameters**:
  - `users`: A comma-separated string of user IDs.

### `get_users_by_ids_v2`

- **Description**: An alternative method to retrieve user information by IDs.
- **Parameters**:
  - `users`: A comma-separated string of user IDs.

### `get_user_replies`

- **Description**: Retrieves replies made by a user, identified by their user ID.
- **Parameters**:
  - `user`: The user ID.
  - `count`: The number of replies to retrieve.
  - `cursor`: (Optional) Cursor for pagination.

### `get_user_replies_v2`

- **Description**: An alternative method to retrieve user replies.
- **Parameters**:
  - `user`: The user ID.
  - `count`: The number of replies to retrieve.
  - `cursor`: (Optional) Cursor for pagination.

### `get_user_media`

- **Description**: Retrieves media content posted by a user.
- **Parameters**:
  - `user`: The user ID.
  - `count`: The number of media items to retrieve.
  - `cursor`: (Optional) Cursor for pagination.

### `get_user_tweets`

- **Description**: Fetches tweets posted by a user.
- **Parameters**:
  - `user`: The user ID.
  - `count`: The number of tweets to retrieve.
  - `cursor`: (Optional) Cursor for pagination.

### `get_user_followings`

- **Description**: Retrieves the list of users followed by a specified user.
- **Parameters**:
  - `user`: The user ID.
  - `count`: The number of followings to retrieve.
  - `cursor`: (Optional) Cursor for pagination.

### `get_user_following_ids`

- **Description**: Retrieves the IDs of users followed by a specified user.
- **Parameters**:
  - `username`: The Twitter username of the user.
  - `count`: The maximum number of IDs to retrieve (up to 5000).
  - `cursor`: (Optional) Cursor for pagination.

### `get_user_followers`

- **Description**: Fetches the list of followers for a specified user.
- **Parameters**:
  - `user`: The user ID.
  - `count`: The number of followers to retrieve.
  - `cursor`: (Optional) Cursor for pagination.

### `get_user_verified_followers`

- **Description**: Retrieves verified followers of a specified user.
- **Parameters**:
  - `user`: The user ID.
  - `count`: The number of verified followers to retrieve.
  - `cursor`: (Optional) Cursor for pagination.

This README provides a comprehensive overview of the Aigeon AI Twitter 241 project, detailing its capabilities and the functionalities of its main components.