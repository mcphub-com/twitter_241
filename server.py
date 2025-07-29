import requests
from datetime import datetime
from typing import Union
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

mcp = FastMCP('twitter241')

@mcp.tool()
def get_user_by_username(username: Annotated[str, Field(description="")]) -> dict:
    '''Gets a user by username'''
    url = 'https://twitter241.p.rapidapi.com/user'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_users_by_ids(users: Annotated[str, Field(description="")]) -> dict:
    '''Get Users By IDs (Rest IDs)'''
    url = 'https://twitter241.p.rapidapi.com/get-users'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'users': users,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_users_by_ids_v2(users: Annotated[str, Field(description="")]) -> dict:
    '''Get Users By IDs V2'''
    url = 'https://twitter241.p.rapidapi.com/get-users-v2'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'users': users,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_user_replies(user: Annotated[str, Field(description="")],
                     count: Annotated[str, Field(description="")],
                     cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get User Replies By ID You can get the user(rest_id) query from "Get User By Username" endpoint'''
    url = 'https://twitter241.p.rapidapi.com/user-replies'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user': user,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_user_replies_v2(user: Annotated[str, Field(description="")],
                        count: Annotated[str, Field(description="")],
                        cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get User Replies By ID You can get the user(rest_id) query from "Get User By Username" endpoint'''
    url = 'https://twitter241.p.rapidapi.com/user-replies-v2'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user': user,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_user_media(user: Annotated[str, Field(description="")],
                   count: Annotated[str, Field(description="")],
                   cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get User Media By ID You can get the user(rest_id) query from "Get User By Username" endpoint'''
    url = 'https://twitter241.p.rapidapi.com/user-media'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user': user,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_user_tweets(user: Annotated[str, Field(description="")],
                    count: Annotated[str, Field(description="")],
                    cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get User Tweets By ID You can get the user(rest_id) query from "Get User By Username" endpoint'''
    url = 'https://twitter241.p.rapidapi.com/user-tweets'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user': user,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_user_followings(user: Annotated[str, Field(description="")],
                        count: Annotated[str, Field(description="")],
                        cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get User Followings By ID. You can get the user(rest_id) query from "Get User By Username" endpoint'''
    url = 'https://twitter241.p.rapidapi.com/followings'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user': user,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_user_following_ids(username: Annotated[str, Field(description="")],
                           count: Annotated[str, Field(description="Maximum count is 5000")],
                           cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''GET Following IDs by Username'''
    url = 'https://twitter241.p.rapidapi.com/following-ids'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_user_followers(user: Annotated[str, Field(description="")],
                       count: Annotated[str, Field(description="")],
                       cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get User Followers By ID. You can get the user(rest_id) query from "Get User By Username" endpoint'''
    url = 'https://twitter241.p.rapidapi.com/followers'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user': user,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_user_verified_followers(user: Annotated[str, Field(description="")],
                                count: Annotated[str, Field(description="")],
                                cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get User Verified Followers By ID. You can get the user(rest_id) query from "Get User By Username" endpoint'''
    url = 'https://twitter241.p.rapidapi.com/verified-followers'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user': user,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_user_followers_ids(username: Annotated[str, Field(description="")],
                           count: Annotated[str, Field(description="Maximum count is 5000")],
                           cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''GET Followers IDs by Username'''
    url = 'https://twitter241.p.rapidapi.com/followers-ids'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_highlights(user: Annotated[str, Field(description="")],
                   count: Annotated[str, Field(description="")],
                   cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get user highlights by ID'''
    url = 'https://twitter241.p.rapidapi.com/highlights'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user': user,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_post_comments(pid: Annotated[str, Field(description="")],
                      count: Annotated[str, Field(description="")],
                      cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get Post Comments By Post ID'''
    url = 'https://twitter241.p.rapidapi.com/comments'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'pid': pid,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_post_comments_v2(pid: Annotated[str, Field(description="")],
                         rankingMode: Annotated[str, Field(description="Relevance || Likes || Recency")] = None,
                         count: Annotated[str, Field(description="")] = None,
                         cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get Post Comments By Post ID V2'''
    url = 'https://twitter241.p.rapidapi.com/comments-v2'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'pid': pid,
        'rankingMode': rankingMode,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_post_quotes(pid: Annotated[str, Field(description="")],
                    count: Annotated[str, Field(description="")],
                    cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get Post Quotes By Post ID'''
    url = 'https://twitter241.p.rapidapi.com/quotes'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'pid': pid,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_post_retweets(pid: Annotated[str, Field(description="")],
                      count: Annotated[str, Field(description="")],
                      cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get Post Retweets By Post ID'''
    url = 'https://twitter241.p.rapidapi.com/retweets'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'pid': pid,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_tweet_details(pid: Annotated[str, Field(description="")]) -> dict:
    '''Get Tweet Details By Tweet ID'''
    url = 'https://twitter241.p.rapidapi.com/tweet'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'pid': pid,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_tweet_details_v2(pid: Annotated[str, Field(description="")]) -> dict:
    '''Get Tweet Details By Tweet ID'''
    url = 'https://twitter241.p.rapidapi.com/tweet-v2'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'pid': pid,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_tweets_details_by_ids(tweetIds: Annotated[str, Field(description="")]) -> dict:
    '''Get Tweets Details By Tweet IDs'''
    url = 'https://twitter241.p.rapidapi.com/tweet-by-ids'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tweetIds': tweetIds,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search_twitter_v2(type: Annotated[str, Field(description="")],
                      count: Annotated[str, Field(description="")],
                      query: Annotated[str, Field(description="")],
                      cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Search Twitter (Top, Latest, Videos, Photos and People)'''
    url = 'https://twitter241.p.rapidapi.com/search-v2'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
        'count': count,
        'query': query,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search_twitter(type: Annotated[str, Field(description="")],
                   count: Annotated[str, Field(description="")],
                   query: Annotated[str, Field(description="")],
                   cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Search Twitter (Top, Latest, Videos, Photos and People)'''
    url = 'https://twitter241.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
        'count': count,
        'query': query,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def autocomplete(value: Annotated[str, Field(description="")]) -> dict:
    '''Twitter Seach Query Autocomplete'''
    url = 'https://twitter241.p.rapidapi.com/autocomplete'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'value': value,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def space_details(id: Annotated[str, Field(description="")]) -> dict:
    '''Get Space Details By ID'''
    url = 'https://twitter241.p.rapidapi.com/spaces'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_organization_affiliates(user: Annotated[str, Field(description="")],
                                count: Annotated[str, Field(description="")],
                                cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get Organization Affiliates By ID You can get the user(rest_id) query from "Get User By Username" endpoint'''
    url = 'https://twitter241.p.rapidapi.com/org-affiliates'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user': user,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search_lists(query: Annotated[str, Field(description="")]) -> dict:
    '''Search lists'''
    url = 'https://twitter241.p.rapidapi.com/search-lists'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_list_details(listId: Annotated[str, Field(description="Get this value from \\\"lists[x].object_id\\\" returned from GET /search-lists Endpoint")]) -> dict:
    '''Get list details by listId'''
    url = 'https://twitter241.p.rapidapi.com/list-details'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'listId': listId,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_list_timeline(listId: Annotated[str, Field(description="Get this value from \\\"lists[x].object_id\\\" returned from GET /search-lists Endpoint")],
                      cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get list timeline by listId'''
    url = 'https://twitter241.p.rapidapi.com/list-timeline'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'listId': listId,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_list_followers(listId: Annotated[str, Field(description="")],
                       count: Annotated[str, Field(description="")] = None,
                       cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get List Followers by List ID'''
    url = 'https://twitter241.p.rapidapi.com/list-followers'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'listId': listId,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_list_members(listId: Annotated[str, Field(description="")],
                     count: Annotated[str, Field(description="")] = None,
                     cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get List Members by List ID'''
    url = 'https://twitter241.p.rapidapi.com/list-members'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'listId': listId,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search_community(query: Annotated[str, Field(description="")],
                     count: Annotated[str, Field(description="")],
                     cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Search community'''
    url = 'https://twitter241.p.rapidapi.com/search-community'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_community_topics() -> dict:
    '''Get Community Topics'''
    url = 'https://twitter241.p.rapidapi.com/community-topics'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def fetch_popular_community(topicId: Annotated[str, Field(description="Get this value from GET /community-topics")],
                            count: Annotated[str, Field(description="")],
                            cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Fetch Popular Community'''
    url = 'https://twitter241.p.rapidapi.com/fetch-popular-community'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'topicId': topicId,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_community_timeline(topicId: Annotated[str, Field(description="")] = None,
                           cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Explore Community Timeline'''
    url = 'https://twitter241.p.rapidapi.com/explore-community-timeline'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'topicId': topicId,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_community_members(communityId: Annotated[str, Field(description="")],
                          cusrsor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get Community Members by Community ID'''
    url = 'https://twitter241.p.rapidapi.com/community-members'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'communityId': communityId,
        'cusrsor': cusrsor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_community_moderators(communityId: Annotated[str, Field(description="")],
                             cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get Community Moderators by Community ID'''
    url = 'https://twitter241.p.rapidapi.com/community-moderators'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'communityId': communityId,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_community_tweets(communityId: Annotated[str, Field(description="")],
                         searchType: Annotated[str, Field(description="Default or Media")],
                         rankingMode: Annotated[str, Field(description="Relevance or Recency or Likes")] = None,
                         count: Annotated[str, Field(description="")] = None,
                         cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get Community Tweets by Community ID'''
    url = 'https://twitter241.p.rapidapi.com/community-tweets'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'communityId': communityId,
        'searchType': searchType,
        'rankingMode': rankingMode,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_community_about(communityId: Annotated[str, Field(description="")]) -> dict:
    '''Get Community About by Community Id'''
    url = 'https://twitter241.p.rapidapi.com/community-about'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'communityId': communityId,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_community_details(communityId: Annotated[str, Field(description="")]) -> dict:
    '''Get Community Details by Community ID'''
    url = 'https://twitter241.p.rapidapi.com/community-details'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'communityId': communityId,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search_job_locations(query: Annotated[str, Field(description="")]) -> dict:
    '''Suggest Job Locations'''
    url = 'https://twitter241.p.rapidapi.com/jobs-locations-suggest'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search_jobs(keyword: Annotated[str, Field(description="")],
                count: Annotated[str, Field(description="")],
                job_location_id: Annotated[str, Field(description="Get this value from GET /jobs-locations-suggest (Search Job Locations).")] = None,
                job_location_type: Annotated[str, Field(description="onsite,remote,hybrid. One of them or multiple values with comma as seperator")] = None,
                seniority_level: Annotated[str, Field(description="intern,entry_level,junior,mid_level,senior,lead,manager,executive. One of them or multiple values with comma as seperator")] = None,
                employment_type: Annotated[str, Field(description="full_time,full_time_contract,part_time,contract_to_hire. One of them or multiple values with comma as seperator")] = None,
                cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Search Jobs'''
    url = 'https://twitter241.p.rapidapi.com/jobs-search'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keyword': keyword,
        'count': count,
        'job_location_id': job_location_id,
        'job_location_type': job_location_type,
        'seniority_level': seniority_level,
        'employment_type': employment_type,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def job_details(jobId: Annotated[str, Field(description="Get this value from \\\\\\\"rest_id\\\\\\\" returned from GET /jobs-search Endpoint")]) -> dict:
    '''Get Job Details'''
    url = 'https://twitter241.p.rapidapi.com/job-details'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'jobId': jobId,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_available_trends_locations() -> dict:
    '''Get Available Trends Locations'''
    url = 'https://twitter241.p.rapidapi.com/trends-locations'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_trends_by_location(woeid: Annotated[str, Field(description="This value can be gotten from the Get Available Trends Locations endpoint.")],
                           exclude: Annotated[str, Field(description="Setting this value equal to hashtags will remove all hashtags from the response list.")] = None) -> dict:
    '''Get Trends By Location'''
    url = 'https://twitter241.p.rapidapi.com/trends-by-location'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'woeid': woeid,
        'exclude': exclude,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_user_likes(user: Annotated[str, Field(description="")],
                   count: Annotated[str, Field(description="")],
                   cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get User Likes By ID You can get the user(rest_id) query from "Get User By Username" endpoint'''
    url = 'https://twitter241.p.rapidapi.com/user-likes'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user': user,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_post_likes(pid: Annotated[str, Field(description="")],
                   count: Annotated[str, Field(description="")],
                   cursor: Annotated[str, Field(description="")] = None) -> dict:
    '''Get Post Likes By Post ID'''
    url = 'https://twitter241.p.rapidapi.com/likes'
    headers = {'x-rapidapi-host': 'twitter241.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'pid': pid,
        'count': count,
        'cursor': cursor,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")