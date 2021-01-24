import discord
from discord.ext import commands, tasks
from discord.utils import get
from secret import token2

from random import choice

client = commands.Bot(command_prefix='$')

x = 'x'

tooken = token2

class Player():
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)
        print(self.players)
    
    def random_player(self):
        return choice(self.players)

class Game():
    def __init__(self):
        self.start = True

    def gameStart(self):
        embed=discord.Embed(title='Wahrheit oder Plicht', description='Bei Wahrheit oder Pflicht (WoP) geht es darum, dass ein Spieler von mir (Bot) ausgewählt wird und dann entscheiden muss ob er Wahrheit nimmt und damit eine Frage beantworten muss, oder ob er Pflicht nimt wobei er dann eine Aufgabe ausführen muss.')
        embed.add_field(name='Spiek Administration', value='Spiel Starten:  `$start`\nSpiel benenden: `$stop game`\n Anderen Spieler hinzufügen: `$add `spieler per @ makieren\n sich selbst dem Spielhinzufügen: `$add-me`', inline=True)
        embed.add_field(name='Spielbefehle', value='Nächste Runde: `$spin`\nSpieler überspringen: `$skip`\n Neue aufgabe: `x`', inline=False)
        embed.set_footer(text='WoPBot')
        return embed

game = Game()
player = Player()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Wahrheit oder Pflicht'))
    channel = client.get_channel('758341649624465448')
    await channel.send(channel, embed=game.gameStart())
    print('main ready')



@client.command(aliases=['start'])
async def start_game(ctx):
    await ctx.send(embed=game.gameStart()) 



@client.command(aliases=['add-me'])
async def add_me(ctx):
    member =  ctx.message.author.mention
    player.players.append(member)
    print(player.players)
    
@client.command()
async def add(ctx,*, member):
    player.players.append(member)
    print(player.players)

@client.command()
async def random(ctx):
    embed=discord.Embed(title='Spieler')
    embed.add_field(name='Zufälliger Spieler:', value=choice(player.players), inline=True)
    embed.add_field(name='Alle Spieler:', value=player.players, inline=False)
    
    await ctx.send(embed=embed)
    #await ctx.send(f'random player: {choice(player.players)}')
    

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


client.run(tooken)