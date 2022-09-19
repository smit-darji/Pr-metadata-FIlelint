import os
from github import Github

GITHUB_TOKEN = (os.environ.get('GITHUB_TOKEN'))
def post_pr_comment (github_client, invalid_file_names, invalid_directory_names):
  gh = Github(GITHUB_TOKEN)
  repo = gh.repository(user, repo_name)
  pr = repo.create_pull(description, base, from_branch, detailed)
  issue = repo.issue(pr.number)
  issue.create_comment("test")
  print(invalid_file_names)
  print(invalid_directory_names)
  # 