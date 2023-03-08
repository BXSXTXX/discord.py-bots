import openai
import discord
import time

openai.api_key = input("Bitte gib deinen OpenAI-API-Schlüssel ein: ")
client = discord.Client()
token = input("Bitte gib deinen Discord-Bot-Token ein: ")
user_id = input("Bitte gib die ID des Nutzers ein, der gepingt werden soll: ")

last_command_time = time.time()

@client.event
async def on_message(message):
    global last_command_time

    if client.user.mentioned_in(message):
        context = message.content

        if str(message.author.id) == user_id:
            if time.time() - last_command_time >= 5:
                prompt = f"Wir spielen ein Roleplay. Du bist ein Jugendlicher Gangster Boy der voll krass unterwegs ist. Du wirst schnell ausfällig. Hier der Kontex meiner Nachricht:\n{context}"
                response = openai.Completion.create(
                	model="text-davinci-003",
    			prompt=prompt,
    			max_tokens=100,
    			n=1,
    			stop=None,
    			temperature=0.5
                )

                response_text = response.choices[0].text
                await message.channel.send(f"<@{user_id}> {response_text}")

                last_command_time = time.time()

client.run(token)
