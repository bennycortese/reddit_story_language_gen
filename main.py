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
        story.comments.replace_more(limit=None)
        for comment in story.comments.list():
            if comment.body:
                translated_comment = french_translation(comment.body)
                stories_content.append(translated_comment)
    return stories_content



def french_translation(input_text):
    # train LLM or use pretrained-LLM or neural network to do the french translation
