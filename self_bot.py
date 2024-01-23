from __future__ import annotations

import discord
from discord.ext import commands

import config

bot = commands.Bot(
                    command_prefix=config.DEFAULT_PREFIX, 
                    self_bot=True, 
                    help_command=None
                    )

# Event triggers only once when bot ready or start 
@bot.event
async def on_ready():
    print(f"Ready to be {bot.user.name}!")
    
# Imp
async def self_check(ctx: commands.Context) -> bool:
    """This is a self check that bot id == user id or owner id."""
    if ctx.author.id == bot.user.id:
        return True
    return False

@commands.check(self_check)
@bot.command(description="This is an test command.")
async def test(ctx: commands.Context) -> None:
    """This is an test command, Just send `Hello` message when triggered."""
    await ctx.message.delete()
    # await ctx.send("Hello")
    print("Hello It's working...")
    
# Run the bot using bot tokn and use bot=False
bot.run(token=config.BOT_TOKEN, bot=False)




