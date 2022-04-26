class Comment:

    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

# This is just example, you can change it to: input() and try with on your own!
comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)
