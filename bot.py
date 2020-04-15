import praw
import re, os, time, random
reddit = praw.Reddit(client_id='secret',
					client_secret='secret',
					user_agent='therealsaucebot by u/sutterismine',
					username='therealsaucebot',
					password='pass')
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       print(posts_replied_to)
       posts_replied_to = list(filter(None, posts_replied_to))
subreddit = reddit.subreddit('all')
while True:
    for comment in subreddit.stream.comments():
        if comment.id not in posts_replied_to:
            if re.search(r"^(S|s)auce(\?)?$", comment.body):
                randomNum = random.randint(1, 9)
                randomDec = random.randint(1, 99)
                print('post found')
                try:
                    comment.reply(f'''Found the [sauce!](https://www.youtube.com/watch?v=K8DBs0QLqq4)
(This took {randomNum}.{randomDec} ms)                    
I am a bot, and this action was performed automatically.''')    
                    print('reply successful to:' + str(comment.author))
                    posts_replied_to.append(comment.id)
                    with open("posts_replied_to.txt", "w") as f:
                        for post_id in posts_replied_to:
                            f.write(post_id + "\n")
                    print('waiting for ratelimit')                    
                    time.sleep(480)
                except Exception as E:
                    print(E)
                    break
    continue
