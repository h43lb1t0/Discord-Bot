import discord
from discord.ext import commands, tasks
from discord.utils import get
from secret import token

client = commands.Bot(command_prefix='$')

tooken = token

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Welcome'))
    print('Welcome ready')

@client.event
async def on_member_join(member):
    userCount = len(client.users)
    channel = discord.utils.get(member.guild.channels, name='willkommen')
    embed=discord.Embed(title="Willkommen!", description=f"Schön dich hier bei uns zu sehen {member.mention}!\n du bist unser {userCount}. mitgllied. Gucke noch in <#758319692300419104> bevor du anfängst auf dem Server rumzustöbern :)")
    await channel.send(embed=embed)
    print('1')

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    print(payload.emoji.name)
    print(message_id)
    role = None
    if str(message_id) == '758651277667729418':
        print('message correct')
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == "❌":
            role = discord.utils.get(guild.roles, name='DM Nein')
            print('DM no')

        elif payload.emoji.name == '📩':
            role = discord.utils.get(guild.roles, name='DM Ja')
            print('DM yes')


    if str(message_id) == '758694471499251743':
        print('message correct')
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == '♂️':
            role = discord.utils.get(guild.roles, name='Männlich')
            print('male')

        elif payload.emoji.name == '♀️':
            role = discord.utils.get(guild.roles, name='Weiblich')
            print('female')

        elif payload.emoji.name == '🏳️‍🌈':
            role = discord.utils.get(guild.roles, name='Geschlecht: LGBTQ++')
            print('Geschlecht: LGBTQ++')

    if str(message_id) == '758695407886270544':
        print('message correct')
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == '0️⃣':
            role = discord.utils.get(guild.roles, name='14+')
            print('14+')

        elif payload.emoji.name == '1️⃣':
            role = discord.utils.get(guild.roles, name='16+')
            print('16+')

        elif payload.emoji.name == '2️⃣':
            role = discord.utils.get(guild.roles, name='18+')
            print('18+')


    if role is not None:
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

        if member is not None:
            print(member.roles)
            for i in member.roles:
                if str(message_id) == '758651277667729418':
                    if "DM Ja" in str(i):
                        print('remove Ja')
                        await member.remove_roles(discord.utils.get(guild.roles, name='DM Ja'))

                    elif "DM Nein" in str(i):
                        print('remove Nein')
                        await member.remove_roles(discord.utils.get(guild.roles, name='DM Nein'))

                    else:
                        await member.add_roles(role)

                elif str(message_id) == '758694471499251743':
                    if "Weiblich" in str(i):
                        print('remove weiblich')
                        await member.remove_roles(discord.utils.get(guild.roles, name='Weiblich'))

                    elif "Männlich" in str(i):
                        print('remove männlich')
                        await member.remove_roles(discord.utils.get(guild.roles, name='Männlich'))

                    elif "Geschlecht: LGBTQ+" in str(i):
                        print('remove Geschlecht: LGBTQ+')
                        await member.remove_roles(discord.utils.get(guild.roles, name='Geschlecht: LGBTQ+'))

                    else:
                        await member.add_roles(role)

                elif str(message_id) == '758695407886270544':
                    if "14+" in str(i):
                        print('14+')
                        await member.remove_roles(discord.utils.get(guild.roles, name='14+'))

                    elif "16+" in str(i):
                        print('16+')
                        await member.remove_roles(discord.utils.get(guild.roles, name='16+'))

                    elif "18+" in str(i):
                        print('18+')
                        await member.remove_roles(discord.utils.get(guild.roles, name='18+'))

                    else:
                        await member.add_roles(role)
    else:
        print('problem')







""" @client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    print(payload.emoji.name)
    print(message_id)
    role = None
    if str(message_id) == '758651277667729418':
        print('message correct')
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == "❌":
            role = discord.utils.get(guild.roles, name='DM Nein')
            print('DM no remoed')

        elif payload.emoji.name == '📩':
            role = discord.utils.get(guild.roles, name='DM Ja')
            print('DM yes removed')

        


    if role is not None:
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        if member is not None:
            await member.remove_roles(role)
    else:
        print('problem')
 """
client.run(tooken)