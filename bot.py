import discord
import responses
from responses import DISCORD_TOKEN

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = DISCORD_TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("READY")


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        # if str(message.author) == "pjewett#9599":
        #     return

        await send_message(message, str(message.content), is_private=False)

    client.run(TOKEN)
