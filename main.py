import discord
from discord.ext import commands
import math
import json
import os

# Set up intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Data storage (Simplified for this example)
XP_DATA = {} 

def level_from_xp(xp):
    return int(math.floor(math.sqrt(xp / 100)))

@bot.event
async def on_message(message):
    if message.author.bot or not message.guild:
        return

    user_id = str(message.author.id)
    guild_id = str(message.guild.id)
    
    # Initialize user data
    if guild_id not in XP_DATA:
        XP_DATA[guild_id] = {}
    if user_id not in XP_DATA[guild_id]:
        XP_DATA[guild_id][user_id] = 0

    # Calculate levels
    before_xp = XP_DATA[guild_id][user_id]
    before_level = level_from_xp(before_xp)
    
    # Add XP
    XP_DATA[guild_id][user_id] += 20 
    
    after_level = level_from_xp(XP_DATA[guild_id][user_id])

    # LEVEL UP LOGIC
    if after_level > before_level:
        # Find the specific "level-up" channel by name
        level_channel = discord.utils.get(message.guild.text_channels, name="level-up")
        
        # If the channel exists, send the message there; otherwise, use the current channel
        target = level_channel if level_channel else message.channel
        
        embed = discord.Embed(
            title="🎉 Level Up!",
            description=f"{message.author.mention} reached **Level {after_level}**!",
            color=discord.Color.green()
        )
        await target.send(embed=embed)

    await bot.process_commands(message)

@bot.command()
async def rank(ctx, member: discord.Member = None):
    member = member or ctx.author
    xp = XP_DATA.get(str(ctx.guild.id), {}).get(str(member.id), 0)
    lvl = level_from_xp(xp)
    await ctx.send(f"📊 **{member.display_name}** is at Level {lvl} ({xp} XP).")

bot.run("YOUR_TOKEN_HERE")
