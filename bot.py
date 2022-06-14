import discord
import random
import pyjokes

# Can't Display Token

client = discord.Client()

@client.event
async def on_ready():
    print("The bot has logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user :
        return

    if message.channel.name == 'welcome-and-rules':
        if user_message.lower() == 'hello':
            greetings = ["ki khobor ?", "Long Time !!!", "What's Up buddy ?"]
            hellos = ["Adios", "Hi"]
            val = random.randint(0, len(greetings))
            j = random. randint(0, len(hellos))

            await message.channel.send(f'{hellos[j]} {username}!! + {greetings[val]} ')
            return
        elif user_message.lower() == 'bye':
            byes = ["Adieu", "Sayonara", "Bye"]
            r = random.randint(0, len(byes))
            await message.channel.send(f'{byes[r]} {username}, see you later!!!')
            return
        elif user_message.lower() == '!joke':
            await message.channel.send('Here is the joke:')
            joke = pyjokes.get_joke(language='en', category='neutral')
            await message.channel.send(joke)
            return

    if user_message.lower() == '!hibot':
        await message.channel.send(f'Hello {username} !, ei bot tar puro functionality explore korar icche thakle, "welcome-and-rules" channel tae explore korte parish')
        return


client.run(TOKEN)





