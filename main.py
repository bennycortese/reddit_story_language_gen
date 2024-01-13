import praw
import csv
import openai

reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent='',
    username='',
    password=''
)

api_key = "YOUR_API_KEY_HERE"


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

def query_gpt(prompt, api_key):
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )

    return response.choices[0].text.strip()


def french_translation(input_text, api_key):
    # train LLM or use pretrained-LLM or neural network to do the french translation
    return query_gpt(input_text, api_key)
