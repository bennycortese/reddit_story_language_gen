import praw
import csv

reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent='',
    username='',
    password=''
)



def story_grabber(num_stories):
    subreddit = reddit.subreddit('WritingPrompts')
    hottest_stories = subreddit.hot(limit=50)
    for story in hottest_stories:
        print(story)



def french_translation(input_text):
    # train LLM or use pretrained-LLM or neural network to do the french translation
