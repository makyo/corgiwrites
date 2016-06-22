class User():
    stories = list(Story)
    username
    password
    email

class Story():
    title
    genre
    summary
    wordcounts = list(WordCountEntry)
    status = str #in progress, up for market, accepted
    submissions = list(Submission)

class Submission():
    market = Market
    status = string # accepted, rejected, waiting
    date = datetime

class Market():
    name
    url
    genre
    wordcount

class WordCountEntry():
    wordcount = int
    date = datetime
