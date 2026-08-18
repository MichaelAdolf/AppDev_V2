(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> git add .
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> git commit -m "Centralize database configuration"
[main 5379ab0] Centralize database configuration
 19 files changed, 108 insertions(+), 35 deletions(-)
 create mode 100644 .dockerignore
 create mode 100644 Dockerfile
 create mode 100644 settings.database_url
 create mode 100644 src/stockmind/shared/config/database.py
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> git push
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/MichaelAdolf/stockmind-platform.git/'
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
