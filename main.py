import discord
import os
from webserver import keep_alive

TOKEN = os.environ['TOKEN']
my_secret = os.environ['TOKEN']

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

@client.event
async def on_member_join(member):
    account_age = (member.created_at).days

    if account_age <= 7:
        # change the 7 into wahtever you like the 7 is days, not month or minutes so choose according to date guys. like you date a girl for 7 days you wanna break her, ban her for being alt.
        await member.ban(reason='Potential alternate account')
        print(f'Banned alt account: {member}')


keep_alive()
client.run(TOKEN)
