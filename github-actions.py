from github import Github
import os

def post_pr_comment (invalid_file_names, invalid_directory_names):
  g = Github("access_token")