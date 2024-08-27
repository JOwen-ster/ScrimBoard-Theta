'''Scrim Command'''

import discord
from discord import app_commands
from discord.ext import commands
import logging


class ScrimError(Exception):
    pass


class Scrim(commands.cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.guild_only()
    async def scrim(self, interaction: discord.Interaction):
        pass



