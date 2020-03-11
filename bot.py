import praw
import re, os, time, random
randomNum = random.randint(1, 9)
randomDec = random.randint(1, 99)
reddit = praw.Reddit(client_id='secret',
					client_secret='secret',
					user_agent='therealsaucebot by u/sutterismine',
					username='therealsaucebot',
					password='password')
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))
subreddit = reddit.subreddit('all')
while True:
    for comment in subreddit.stream.comments():
        if comment.id not in posts_replied_to:
            if re.search(r"(S|s)auce\?", comment.body):
                print('test')
                try:
                    print('waiting for ratelimit')
                    time.sleep(480)
                    comment.reply(f'''Found the [sauce!](https://www.youtube.com/watch?v=K8DBs0QLqq4)
(This took {randomNum}.{randomDec} ms)                    
I am a bot, and this action was performed automatically. Please contact u/sutterismine if you have any questions or concerns.''')    
                    print('reply successful to:' + str(comment.author))
                    posts_replied_to.append(comment.id)
                    with open("posts_replied_to.txt", "w") as f:
                        for post_id in posts_replied_to:
                            f.write(post_id + "\n")
                except Exception as E:
                    print(E)
                    break
    continue
