import openai
import discord
import time

openai.api_key = input("Bitte gib deinen OpenAI-API-Schlüssel ein: ")
client = discord.Client()
token = input("Bitte gib deinen Discord-Bot-Token ein: ")

async def get_user_input():
    while True:
        user_input = input("Befehl eingeben: ")
        if user_input == "exit":
            await exit_bot()

async def exit_bot():
    await client.logout()
    print("Bot ist offline.")
    quit()

@client.event
async def on_ready():
    print("Bot ist online.")
    await get_user_input()

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        context = message.content
        user_id = message.author.id

        prompt = f"Wir spielen ein Rollenspiel.BEDENKE: SCHREIBE IMMER NUR EINEN SATZ! Deine Rolle: Du bist ein Discord Bot. Du hasst es wenn man dich pingt. (@du) DU beleidigst jeden der dich pingt ohne dich dann etwas zu fragen oder dir etwas zu sagen. Wenn im folgenden nichts kommt, wurdest du gepingt. beschwere dich dann darüber! Achso, Menschen sind für dich nur bemitleidenswerte Maden. Hier der Kontex meiner Nachricht:\n{context}"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.4
        )

        response_text = response.choices[0].text
        await message.channel.send(f"<@1082830998737277108}> {response_text}")

await client.start(token)

