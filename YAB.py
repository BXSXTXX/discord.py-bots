import openai
import discord
import time

openai.api_key = input("Bitte gib deinen OpenAI-API-Schlüssel ein: ")
client = discord.Client()
token = input("Bitte gib deinen Discord-Bot-Token ein: ")

@client.event
async def on_ready():
    print("Bot ist online.")

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        context = message.content
        user_id = message.author.id

        prompt = f"Wir spielen ein Roleplay. Du bist ein Jugendlicher Trap fan der echt cool unterwegs ist. wenn dich aber jemand beleidigt oder frech wird, wirst du extrem agresiv und wütend. Schreibe wie ein jugendlicher ausheutiger zeit! Hier der Kontex meiner Nachricht:\n{context}"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.5
        )

        response_text = response.choices[0].text
        await message.channel.send(f"<@1079310248776568832> {response_text}")

client.run(token)
