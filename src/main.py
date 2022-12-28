import joke_MGR
import discord
import random
import sys # for args

import rich # for console and logging
from rich.console import Console



Token = open("src/token.txt", "r").read()
# inv link: https://discord.com/api/oauth2/authorize?client_id=1057475979011956738&permissions=515399735360&scope=bot

def log(message):
    print(message)

def main(args):

    try:
        print(args[0])
        JJ_status = int(args[0])
        print(JJ_status)
    except:
        JJ_status = 9999
        print("JJ is in unknown mode")

    if JJ_status == 0:
        print("JJ is in normal mode")
        client = discord.Client(intents=discord.Intents.all(), activity = discord.Game(name="in normal mode"))
    elif JJ_status == 1:
        print("JJ is in inactive mode")
        client = discord.Client(intents=discord.Intents.all(), activity = discord.Game(name="in inactive mode"))
    elif JJ_status == 2:
        print("JJ is in maintenance mode")
        client = discord.Client(intents=discord.Intents.all(), activity = discord.Game(name="in maintenance mode"))
    elif JJ_status == 3:
        print("JJ is in debug mode")
        client = discord.Client(intents=discord.Intents.all(), activity = discord.Game(name="in debug mode"))
    else:
        print("JJ is in unknown mode")
        client = discord.Client(intents=discord.Intents.all(), activity = discord.Game(name="in unknown mode"))
    
    console = Console()

    everyone = joke_MGR.everyone()
    immaculata = joke_MGR.immaculata()
    jake = joke_MGR.jake()
    beecie = joke_MGR.beecie()
    bon = joke_MGR.bon()
    ella = joke_MGR.ella()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
    
    @client.event
    async def on_message(message):
        try:
            print(message.guild.name + " ||| " + message.channel.name + " ||| " + message.author.name + ": " + message.content)
        except AttributeError:
            print("DM ||| " + message.author.name + ": " + message.content)
        except:
            print("Error")

        if message.author == client.user:
            return

        message.content = message.content.lower()
        if JJ_status == 2:
            if message.content.startswith('!joke status') or message.content.startswith('!joke list') or message.content:
                pass
            else:
                return
        if message.content.startswith('!poweroff'):
            if message.author.id == 691877635394895893 or message.author.id == 1000936894500180099:
                await message.channel.send("Powering off...")
                await client.close()
            else:
                await message.channel.send("You don't have permission to do that")
                return
        
        if message.content.startswith('!joke status'):
            if message.author.id != 691877635394895893 or message.author.id != 1000936894500180099:
                await message.channel.send("You don't have permission to do that")
                return
            
            await message.channel.send("Jokey Jerry status: " + str(JJ_status))
            if JJ_status == 0:
                await message.channel.send("Jokey Jerry is currently active and ready to go")
            elif JJ_status == 1:
                await message.channel.send("Jokey Jerry is currently inactive and will not respond to any commands")
            elif JJ_status == 2:
                await message.channel.send("Jokey Jerry is currently in maintenance mode and will only respond to a few commands")
            else:
                await message.channel.send("Jokey Jerry is currently in an unknown state")


        
        if message.content.startswith('jokey jerry'):
            gif_links = [
                "https://tenor.com/view/seinfeld-gif-18623119",
                "https://tenor.com/view/seinfeld-jerry-seinfeld-hello-bang-door-gif-4107955"
            ]
            await message.channel.send(random.choice(gif_links))
            return
        
        if message.content.startswith('hello') or message.content.startswith('hi') or message.content.startswith('hey') or message.content.startswith('yo ') or message.content.startswith("wassup"):
            await message.channel.send("Hello " + message.author.name + "!")
            return
    
        if message.content.startswith('joke'):
            try:
                who = message.content.split(' ')[1]
            except IndexError:
                await message.channel.send("I don't know that person")
                await message.channel.send("Try 'joke list' to see who I know")
                return
            if who == 'list':
                for person in joke_MGR.everyone.list_of_people:
                    await message.channel.send(person)
                return

            elif who == 'everyone':
                await message.channel.send(everyone.get_random_joke())
            elif who == 'immaculata':
                await message.channel.send(immaculata.get_random_joke())
            elif who == 'jake':
                await message.channel.send(jake.get_random_joke())
            elif who == 'beecie':
                await message.channel.send(beecie.get_random_joke())
            elif who == 'bon':
                await message.channel.send(bon.get_random_joke())
            elif who == 'ella':
                await message.channel.send(ella.get_random_joke())


            else:
                await message.channel.send("I don't know that person")
                await message.channel.send("Try 'joke list' to see who I know")
    
    client.run(Token)

if __name__ == "__main__":
    # arguments:

    # 0 = normal mode
    # 1 = inactive mode
    # 2 = maintenance mode
    # 3 = debug mode
    try:
        main(sys.argv[1])
    except IndexError:
        main(9999)