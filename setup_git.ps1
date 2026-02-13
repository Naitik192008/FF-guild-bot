# setup_git.ps1

Write-Host "Initializing Git Repository..." -ForegroundColor Cyan
git init

Write-Host "Adding all files..." -ForegroundColor Cyan
git add .

Write-Host "Committing changes..." -ForegroundColor Cyan
git commit -m "Initial commit of Free Fire Bot Suite"

Write-Host "`nGit Repository Initialized!" -ForegroundColor Green
Write-Host "-------------------------------------------------------"
Write-Host "NEXT STEPS TO DEPLOY LIKE A PRO:" -ForegroundColor Yellow
Write-Host "1. Go to GitHub.com and create a new PUBLIC repository."
Write-Host "2. Copy the URL of your new repository (e.g., https://github.com/yourname/my-bot.git)"
Write-Host "3. Run the following command in this terminal (replace the URL):"
Write-Host "   git remote add origin <YOUR_REPO_URL>"
Write-Host "4. Push your code:"
Write-Host "   git push -u origin master"
Write-Host "-------------------------------------------------------"
Write-Host "AFTER PUSHING:" -ForegroundColor Yellow
Write-Host "1. Go to Railway.app or Render.com"
Write-Host "2. Click 'New Project' -> 'Deploy from GitHub repo'"
Write-Host "3. Select your 'my-bot' repository."
Write-Host "4. It will automatically build and deploy your Docker container!"
Write-Host "-------------------------------------------------------"
