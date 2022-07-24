import json
import sys
import pandas as pd
import pygit2 as pg
from datetime import datetime
import os
from definitions import GIT_PATH, REPO_URL

""" reads the GitHub repository commits and places them into a pandas DataFrame """

def getCommits(repository):
    repo = pg.Repository(repository)
    commits = []
    i=0
    for commit in repo.walk(repo.head.target, pg.GIT_SORT_TIME):
        #date, hash,message
        commits.append([datetime.utcfromtimestamp(commit.commit_time).strftime('%Y-%m-%d %H:%M:%S'),
                    commit.hex,
                    commit.message])
        i+=1
    return(commits)

def make_clickable(val):
    
    path = "<a href=%s/commit/%s>%s</a>"%(REPO_URL,val,val[:8])
    return path

def get_changelog():
    
    cm = getCommits(GIT_PATH)
    df = pd.DataFrame(cm,columns=['Date','Commit', 'log'])
   
    #make hash linkeable to the webpage.
    s = df.style.format({"hash": lambda x:make_clickable(x)}).hide_index()
    out = s.set_table_attributes('class="mystyle"').to_html()
    return df