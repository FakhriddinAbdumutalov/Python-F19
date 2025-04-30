from datetime import datetime
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nCreated At: {self.created_at}\nContent: {self.content}\n"
class Blog:
    def __init__(self):
        self.posts = []
    def add_post(self, title, content, author):
        post = Post(title, content, author)
        self.posts.append(post)
        print(f"Post '{title}' added.")
    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
        else:
            print("\nAll Posts:")
            for post in self.posts:
                print(post)
    def list_posts_by_author(self, author):
        posts_by_author = [post for post in self.posts if post.author == author]
        if not posts_by_author:
            print(f"No posts found by {author}.")
        else:
            print(f"\nPosts by {author}:")
            for post in posts_by_author:
                print(post)
    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                print(f"Post '{title}' deleted.")
                return
        print(f"Post '{title}' not found.")
    def edit_post(self, title, new_title=None, new_content=None):
        for post in self.posts:
            if post.title == title:
                if new_title:
                    post.title = new_title
                if new_content:
                    post.content = new_content
                print(f"Post '{title}' updated.")
                return
        print(f"Post '{title}' not found.")
    def latest_posts(self, n=5):
        sorted_posts = sorted(self.posts, key=lambda x: x.created_at, reverse=True)
        print(f"\nLatest {n} Posts:")
        for post in sorted_posts[:n]:
            print(post)
def main():
    blog = Blog()
    while True:
        print("\nBlog System")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. View Latest Posts")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            blog.add_post(title, content, author)
        elif choice == "2":
            blog.list_all_posts()
        elif choice == "3":
            author = input("Enter author name to list posts: ")
            blog.list_posts_by_author(author)
        elif choice == "4":
            title = input("Enter post title to delete: ")
            blog.delete_post(title)
        elif choice == "5":
            title = input("Enter post title to edit: ")
            new_title = input("Enter new title (or press Enter to keep the same): ")
            new_content = input("Enter new content (or press Enter to keep the same): ")
            blog.edit_post(title, new_title if new_title else None, new_content if new_content else None)
        elif choice == "6":
            n = int(input("Enter number of latest posts to display: "))
            blog.latest_posts(n)
        elif choice == "7":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
