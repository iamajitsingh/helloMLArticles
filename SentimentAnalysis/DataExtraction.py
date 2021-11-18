import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets_list = []

# Scraping data and append tweets to list
for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper('united nations since:2020-07-30 until:2021-11-03').get_items()):
    if i > 100000:
        break
    tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.likeCount, tweet.user.displayname, tweet.lang])

# Creating the dataframe, Export .csv file
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Like Count', 'Display Name', 'Language'])
tweets_df.to_csv('united_nations.csv')

