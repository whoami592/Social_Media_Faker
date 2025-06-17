import random
from faker import Faker
from datetime import datetime
import pyfiglet

# Initialize Faker
fake = Faker()

# Stylish ASCII banner
banner = pyfiglet.figlet_format("Social Media Faker")
print(banner)
print("Coded by Pakistani Ethical Hacker Mr Sabaz Ali Khan\n")

# Function to generate a fake social media profile
def generate_fake_profile():
    profile = {
        "username": fake.user_name(),
        "full_name": fake.name(),
        "email": fake.email(),
        "bio": fake.text(max_nb_chars=150),
        "location": fake.city(),
        "join_date": fake.date_this_decade(),
        "followers": random.randint(10, 10000),
        "following": random.randint(10, 5000)
    }
    return profile

# Function to generate a fake social media post
def generate_fake_post(username):
    post = {
        "username": username,
        "content": fake.text(max_nb_chars=280),
        "timestamp": fake.date_time_this_month(),
        "likes": random.randint(0, 1000),
        "retweets": random.randint(0, 500),
        "comments": random.randint(0, 200)
    }
    return post

# Main function to generate and display fake social media data
def main():
    print("="*50)
    print("Generating Fake Social Media Profile")
    print("="*50)
    
    # Generate a profile
    profile = generate_fake_profile()
    
    # Display profile details
    print(f"Username: {profile['username']}")
    print(f"Full Name: {profile['full_name']}")
    print(f"Email: {profile['email']}")
    print(f"Bio: {profile['bio']}")
    print(f"Location: {profile['location']}")
    print(f"Join Date: {profile['join_date']}")
    print(f"Followers: {profile['followers']}")
    print(f"Following: {profile['following']}")
    print("="*50)
    
    # Generate and display 3 fake posts
    print("\nGenerating Fake Posts")
    print("="*50)
    for i in range(3):
        post = generate_fake_post(profile['username'])
        print(f"Post {i+1}:")
        print(f"Username: {post['username']}")
        print(f"Content: {post['content']}")
        print(f"Posted on: {post['timestamp']}")
        print(f"Likes: {post['likes']}")
        print(f"Retweets: {post['retweets']}")
        print(f"Comments: {post['comments']}")
        print("-"*50)

if __name__ == "__main__":
    main()