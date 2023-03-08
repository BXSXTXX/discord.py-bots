import openai
import discord
import time

# Benutzereingabe für OpenAI-API-Schlüssel und Discord-Bot-Token in der Konsole abfragen
openai.api_key = input("Bitte gib deinen OpenAI-API-Schlüssel ein: ")
client = discord.Client()
token = input("Bitte gib deinen Discord-Bot-Token ein: ")
user_id = input("Bitte gib die ID des Nutzers ein, der gepingt werden soll: ")

# Variable zum Speichern des letzten Befehlszeitpunkts
last_command_time = time.time()

@client.event
async def on_message(message):
    # Zugriff auf die globale Variable last_command_time
    global last_command_time

    # Prüfen, ob der Bot gepingt wurde
    if client.user.mentioned_in(message):
        # Den Kontext des Nachrichteninhalts erhalten
        context = message.content

        # Prüfen, ob der Nutzer, der die Nachricht gesendet hat, der ausgewählte Nutzer ist
        if str(message.author.id) == user_id:
            # Prüfen, ob seit dem letzten Befehl mindestens 5 Sekunden vergangen sind
            if time.time() - last_command_time >= 5:
                # Generiere eine Beleidigung mit GPT-3
                prompt = f"Wir spielen ein Roleplay. Du bist ein Jugendlicher Gangster Boy der voll krass unterwegs ist. Du wirst schnell ausfällig. Hier der Kontex meiner Nachricht:\n{context}"
                response = openai.Completion.create(
                    engine="davinci",
                    prompt=prompt,
                    max_tokens=100,
                    n=1,
                    stop=None,
                    temperature=0.5,
                    model="text-davinci-003"
                )

                # Sende die Beleidigung als Nachricht im selben Kanal
                response_text = response.choices[0].text
                await message.channel.send(f"<@{user_id}> {response_text}")

                # Aktualisiere den Zeitpunkt des letzten Befehls
                last_command_time = time.time()

# Verbindung zum Discord-Client herstellen
client.run(token)
