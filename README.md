# Umbrella - Multipurpose Discord Bot

236 commands across moderation, leveling, economy, music, games, fun, utility and more.

## Setup
1. Create a `.env` file and put your Discord token in it:
   ```
   DISCORD_TOKEN=your-token-here
   ```
2. Install deps: `pip install -r requirements.txt`
3. Run: `python main.py`

## Required Discord intents
Enable these in the Discord Developer Portal under your bot's "Bot" tab:
- MESSAGE CONTENT INTENT
- SERVER MEMBERS INTENT
- (PRESENCE intent not required)

## Required system packages
- Python 3.10+
- ffmpeg (only required for music commands - !play, !skip, etc.)

## Commands
Use `!help` in Discord to see all 236 commands grouped by category, or `!help <command>` for details on any single command.

## Railway Deployment

### Quick Deploy
1. Push your code to a GitHub repository
2. Go to [Railway](https://railway.app/) and create a new project
3. Select "Deploy from GitHub repo" and choose your repository
4. Railway will automatically detect the configuration files

### Environment Variables
After deployment, add your environment variable in Railway:
- Go to your project → Variables tab
- Add: `DISCORD_TOKEN` with your bot token value

### Important Notes
- The bot runs as a **worker** process (not a web server)
- **ffmpeg** is included for music commands
- Data files (XP, economy, warnings) will persist in Railway's ephemeral storage
- For permanent data storage, consider using Railway's database services

### Files for Railway
- `Procfile` - Defines the worker process
- `runtime.txt` - Specifies Python version
- `railway.json` - Railway configuration
- `nixpacks.toml` - Build configuration with ffmpeg
- `.railwayignore` - Files to exclude from deployment
