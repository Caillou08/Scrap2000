from __future__ import unicode_literals
import discord
import youtube_dl
import asyncio
import os
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
            title=f"Résultat du téléchargement de `{ctx.author}` :",
            color=discord.Color.blurple()
        )
        if url == None or format == None:
            embed.add_field(name="Erreur !", value="Veuillez indiquer un url ainsi qu'un format valide !")
            await ctx.send(embed=embed)
        else : 
            await ctx.send("Téléchargement en cours, cela peut prendre plusieurs minutes...")
            if musicformat == "mp4": 
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
                permission = gfile.InsertPermission({
                        'type': 'anyone',
                        'value': 'anyone',
                        'role': 'reader'})
            embed.add_field(name="Téléchargement terminé !", value=f"Format : {musicformat}", inline=False)
            embed.add_field(name="Lien :", value=gfile['alternateLink'], inline=False)
            embed.set_footer(text=f"Commande effectuée par {ctx.author}, ce lien sera supprimer dans 5 minutes.", icon_url=ctx.author.avatar_url)
            os.remove(f"./{ctx.author}.{musicformat}")
            await ctx.send(embed=embed)
            await asyncio.sleep(300)
            gfile.Delete()
            print(f"Fichier de {ctx.author} supprimé du GDrive")

def setup(bot):
    bot.add_cog(ytdl(bot))
            