import praw
import csv
from dotenv import load_dotenv
import os
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
from typing import Iterable, List
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import DataLoader, Dataset
from timeit import default_timer as timer
from torch.nn import Transformer
from torch import Tensor
from sklearn.model_selection import train_test_split
from tqdm.auto import tqdm
import torch.nn as nn
import torch
import torch.nn.functional as F
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

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
