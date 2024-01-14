import praw
import csv
from dotenv import load_dotenv
import os

load_dotenv()

client_id=os.getenv("CLIENT_ID")
client_secret=os.getenv("CLIENT_SECRET")
user_agent=os.getenv("USER_AGENT")
username=os.getenv("USERNAME_REDDIT")
password=os.getenv("PASSWORD")


reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)


api_key = "YOUR_API_KEY_HERE"


def story_grabber(num_stories):
    stories_content = []
    subreddit = reddit.subreddit('WritingPrompts')
    hottest_stories = subreddit.hot(limit=50)
    for story in hottest_stories:
        story.comments.replace_more(limit=None)
        for comment in story.comments.list():
            if comment.body and comment.score > 100 and len(comment.body) > 1000:
                translated_comment = french_translation(comment.body)
                stories_content.append(translated_comment)
    return stories_content

def eng_to_french(prompt):
    return prompt
