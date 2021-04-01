class Tweet:
    def __init__(self, id, screenname, username, created_at, text='', emojis='', 
                    replys=0, likes=0, retweets=0,image_links=None,tweet_url):
    self.id=id
    self.screenname=screenname
    self.username=username
    self.created_at=created_at
    self.text=text
    self.emojis=emojis
    self.replys=replys
    self.likes=likes
    self.retweets=retweets
    self.image_links=image_links
    self.tweet_url=tweet_url