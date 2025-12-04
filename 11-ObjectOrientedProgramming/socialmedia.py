class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        for index, post in enumerate(self.posts, start = 1):
            print(f'{index}. {post}')
    
def main():
    johndoe = SocialMediaProfile("johndoe")

    johndoe.add_post("Hello World!")
    johndoe.add_post("Had a great time at park")
    johndoe.add_post("Whats up Nataie how are you?")

    johndoe.display_timeline()

if __name__ == "__main__":
    main()


