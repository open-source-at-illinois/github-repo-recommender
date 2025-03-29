import requests
from http.client import OK

def get_top_repos(n):
    # GitHub API endpoint to search for repositories sorted by stars
    url = "https://api.github.com/search/repositories?q=stars:>=1&sort=stars&order=desc"
    
    # List to store the names and owners of repositories
    repos_info = []
    
    # Pagination: GitHub API returns results in pages, each page contains 30 results by default
    # We need to loop through pages to get the top 100
    # page = 1
    while len(repos_info) < n:
        response = requests.get(url, params={'per_page': 100})
        if response.status_code == OK:
            data = response.json()
            items = data.get('items', [])
            
            for repo in items:
                repo_name = repo['name']
                repo_owner = repo['owner']['login']
                repos_info.append((repo_name, repo_owner))
                
                # Stop if we've gathered 100 repositories
                # print(len(repos_info))
                if len(repos_info) >= n:
                    break
            
            if 'next' in response.links:
                url = response.links['next']['url']
            # rate_limit_remaining = response.content
            # print(rate_limit_remaining)
            # print(url)
            # url = urls[0].split(';')[0]
            # print(url)
            # break
            # page += 1  # Move to the next page for more results
        else:
            print(f"Failed to fetch repositories. Status code: {response.status_code}")
            break
    
    # Print the results
    for repo_name, repo_owner in repos_info:
        print(f"Repository: {repo_name}, Owner: {repo_owner}")
    
    return repos_info

repo_num = 1000
repos_data = get_top_repos(repo_num)
if len(repos_data) != repo_num:
    print(f'{len(repos_data)} fetched out of {repo_num} repos')
else:
    print('data fetched succesfully')

