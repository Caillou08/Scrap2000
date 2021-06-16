from __future__ import unicode_literals
import discord
import youtube_dl
from discord.ext import commands
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

class ytdl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ytdl(self, ctx, url=None, musicformat=None):
        embed=discord.Embed(
            title=f"Résultat du téléchargement de {ctx.author.mention} :",
            color=discord.Color.blurple()
        )
        if url == None or format == None:
            embed.add_field(name="Erreur !", value="Veuillez indiquer un url ainsi qu'un format valide !")
            await ctx.send(embed=embed)
        else : 
            ydl_opts = {
                "format": f"{musicformat}",
                    "outtmpl": f"{ctx.author}.%(ext)s",
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            upload_file_list = [f"{ctx.author}.{musicformat}"]
            for upload_file in upload_file_list:
                gfile = drive.CreateFile({"parents": [{"id": "19a--FCDfFLXpkSbENE1Lliu8fyS2clVh"}]})
                gfile.SetContentFile(upload_file)
                gfile.Upload()
            await ctx.send("Test")
            
def setup(bot):
    bot.add_cog(ytdl(bot))
            