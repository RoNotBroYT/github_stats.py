import requests
import json

def get_github_stats(username):
    # GitHub API endpoint for user information
    url = f"https://api.github.com/users/{RoNotBroYT}"
    
    # Sending GET request to the GitHub API
    response = requests.get(url)
    
    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        # Parsing JSON response
        data = response.json()
        
        # Extracting relevant information
        public_repos = data['public_repos']
        followers = data['followers']
        following = data['following']
        
        # Printing the stats
        print(f"GitHub Stats for {RoNotBroYT}:")
        print(f"Public Repositories: {public_repos}")
        print(f"Followers: {followers}")
        print(f"Following: {following}")
    else:
        print(f"Error fetching GitHub stats. Status code: {response.status_code}")

# Main function to fetch and display GitHub stats
if __name__ == "__main__":
    username = "RoNotBroYT"
    get_github_stats(RoNotBroYT)
