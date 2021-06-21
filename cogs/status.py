import discord
import speedtest
from discord.ext import commands

servers = []
threads = None

class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def status(self, ctx):
        embed = discord.Embed(
            title="Informations sur le bot :",
            color = discord.Color.blurple()
        )
        await ctx.send("Aquisition des informations requises en cours...")
        s = speedtest.Speedtest()
        s.get_servers(servers)
        s.get_best_server()
        embed.add_field(name="Vitesse de téléchargement :", value=f"{(round(s.download(threads=threads)))/1000000} mbps", inline=False)
        embed.add_field(name="Vitesse de téléversement :", value=f"{(round(s.upload(threads=threads)))/1000000} mbps", inline=False)
        embed.set_footer(text=f"Commande effectuée par {ctx.author}.", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(status(bot))