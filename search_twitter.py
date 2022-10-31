import json
import os
import requests
import time

def searchTwitter(query, tweet_fields, user_fields, next_token, bearer_token):
    
    headers = {"Authorization": f"Bearer {bearer_token}"}
    if next_token is not None:
        url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&{tweet_fields}&{user_fields}&next_token={next_token}"
    else:
        url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&{tweet_fields}&{user_fields}"

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 429:
        print("Request limit reached.")
        time.sleep(sec=1800)
        response = requests.request("GET", url, headers=headers)


    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

    return response.json()
