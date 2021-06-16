import discord
import os
import asyncio
from discord.ext import commands
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

class deezerdl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def deezerdl(self, ctx, url=None, musicformat=None):
        embed=discord.Embed(
            title=f"Résultat du téléchargement de `{ctx.author}` :",
            color=discord.Color.blurple()
        )
        if url == None or format == None:
            embed.add_field(name="Erreur !", value="Veuillez indiquer un url ainsi qu'un format valide !")
            await ctx.send(embed=embed)
        else : 
            await ctx.send("Téléchargement en cours, cela peut prendre plusieurs minutes...")
            os.system(f"python3 -m deemix {url} -b {musicformat} --portable")   
            upload_file_list = [f"DeezerDL.{musicformat}"]
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
            embed.set_footer(text=f"Commande effectuée par {ctx.author}, ce lien sera supprimer dans 5 minutes", icon_url=ctx.author.avatar_url)
            os.remove(f"./DeezerDL.{musicformat}")
            await ctx.send(embed=embed)
            await asyncio.sleep(300)
            gfile.Delete()
            print(f"Fichier de {ctx.author} supprimé du GDrive")

def setup(bot):
    bot.add_cog(deezerdl(bot))
                    
