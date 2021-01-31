from requests import get
import pandas as pd
from bs4 import BeautifulSoup as BS
import os
import re

def get_article_text(url):
    headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent
    response = get(url, headers=headers)
    soup = BS(response.content, 'html.parser')
    
    title = soup.title.text
    article = soup.main.article.text.replace('\xa0', ' ')
    
    return title, article

def get_codeup_blogs():
    sites = [
    'https://codeup.com/codeups-data-science-career-accelerator-is-here/',
    'https://codeup.com/data-science-myths/',
    'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/',
    'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/',
    'https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/']
    
    articles = [{'title' : get_article_text(site)[0],
             'body'  : get_article_text(site)[1]} for site in sites]
    
    return articles

def get_codeup_blogs_text():
    sites = [
    'https://codeup.com/codeups-data-science-career-accelerator-is-here/',
    'https://codeup.com/data-science-myths/',
    'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/',
    'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/',
    'https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/']
    
    articles = [get_article_text(site)[1] for site in sites]
    
    return articles


def get_articles_from_topic(url):
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BS(response.content, 'html.parser')
    output = []
    articles = soup.select(".news-card")
    for article in articles: 
        title = article.select("[itemprop='headline']")[0].get_text()
        body = article.select("[itemprop='articleBody']")[0].get_text()
        author = article.select(".author")[0].get_text()
        published_date = article.select(".time")[0]["content"]
        category = response.url.split("/")[-1]
        article_data = {
            'title': title,
            'body': body,
            'category': category,
            'author': author,
            'published_date': published_date,
        }
        output.append(article_data)
    return output


def get_news_articles():
    urls = [
        "https://inshorts.com/en/read/business",
        "https://inshorts.com/en/read/sports",
        "https://inshorts.com/en/read/technology",
        "https://inshorts.com/en/read/entertainment"
    ]
    output = []
    for url in urls:
        output.extend(get_articles_from_topic(url))
    df = pd.DataFrame(output)
    df.to_csv('inshorts_news_articles.csv')
    return output