# MIT License

# Copyright (c) 2022 Jacob O'Bbrien

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import datetime
import joke_MGR
import discord
import random
import sys # for args
import time
import os

import rich # for console and logging
from rich.console import Console

# experimental
from time import sleep

from rich.align import Align
from rich.text import Text
from rich.panel import Panel


# CAN ONLT BE RUN ON JAKE'S PC AND ON A LINUX MACHINE (OR A UNIX MACHINE)
global Token # token is stored in a file called token.txt 
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
        print("rich console is initializing...")
        print("rich console is initialized and ready to use\ntaking over console output now...")
        time.sleep(0.005)
        console.print(Align.center(Panel(Text("JOKEY JERRY IS ACTIVATED", style="bold red")), vertical="middle"))
        console.rule("[bold red]CONNECTED TO DISCORD")
    
    @client.event
    async def on_message(message):

        try:
            console.log(message.guild.name + " ||| " + message.channel.name + " |||[blue i] " + message.author.name + ":[green bold]" + message.content)
        except AttributeError:
            print("DM ||| " + message.author.name + ": " + message.content)
        except:
            print("Error")

        if message.author == client.user:
            return

        message.content = message.content.lower()
            
        if JJ_status == 2:
            if message.content.startswith('!joke') or message.content.startswith('!halt') or message.content.startswith('!poweroff') or message.content.startswith('!shutdown') or message.content.startswith('!restart'):
                pass
            else:
                return

        if message.content.startswith('!halt'):
            if message.author.id == 691877635394895893 or message.author.id == 1000936894500180099:
                try:
                    message.content = message.content.replace("!halt ", "")
                    await message.channel.send("pausing for " + message.content + " seconds\n I will respond to all your commands after that time")
                    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the timer go down, " + message.author.name + " halted me"))
                    with console.screen(style="bold white on blue") as screen:
                        for count in range(int(message.content), 0, -1):
                            text = Align.center(
                                Text.from_markup(f"[blink]TO STOP ME, TERMINATE THE PROGRAM\nHalted for...[/blink]\n{count}", justify="center"),
                                vertical="middle",
                            )
                            screen.update(Panel(text))
                            sleep(1)
                        
                        if JJ_status == 0:
                            await client.change_presence(activity=discord.Game(name="in normal mode"))
                        elif JJ_status == 1:
                            await client.change_presence(activity=discord.Game(name="in inactive mode"))
                        elif JJ_status == 2:
                            await client.change_presence(activity=discord.Game(name="in maintenance mode"))
                        elif JJ_status == 3:
                            await client.change_presence(activity=discord.Game(name="in debug mode"))
                        else:
                            await client.change_presence(activity=discord.Game(name="in unknown mode"))
                except ValueError:
                    console.log("[red bold blink i]Error in !halt")
                    await message.channel.send("Error in !halt, make sure you have a number (sec) after the command")
                except:
                    console.log("[red bold blink i]Error in !halt")
                    await message.channel.send("Error in !halt, make sure you have a number (sec) after the command")

        if message.content.startswith('!restart') or message.content.startswith("!r"):
            if message.author.id == 691877635394895893 or message.author.id == 1000936894500180099:
                if JJ_status == 2 or JJ_status == 3:
                    await message.channel.send("Restarting...")
                    await message.channel.send("have a good day!\n\nMADE BY JAKE (MESSYCODE) AND IMMACULATA (IMMACULATA RODRIGO)\nTHIS SOFTWARE IS LICENSED UNDER THE MIT LICENSE\nMADE ON DEC 28 2022, AT (ALL DAY)\nVERSION:9999\n")
                    await message.channel.send("TIME OF RESTART: " + str(datetime.datetime.now()))
                else:
                    await message.channel.send("Sending task to restart...\nthis might take 5 seconds to 10")
                    await message.channel.send("TIME OF RESTART: " + str(datetime.datetime.now()))
                
                command = "python3 src/main.py " + str(JJ_status)
                print(command)
                os.system(command)
                exit(0)
                    


        if message.content.startswith('!shutdown') or message.content.startswith('!poweroff'):
            if message.author.id == 691877635394895893 or message.author.id == 1000936894500180099:
                if JJ_status == 2 or JJ_status == 3:
                    await message.channel.send("Powering off...")
                    await message.channel.send("have a good day!\n\nMADE BY JAKE (MESSYCODE) AND IMMACULATA (IMMACULATA RODRIGO)\nTHIS SOFTWARE IS LICENSED UNDER THE MIT LICENSE\nMADE ON DEC 28 2022, AT (ALL DAY)\nVERSION:9999\n")
                    await message.channel.send("TIME OF SHUTDOWN: " + str(datetime.datetime.now()))
                else:
                    await message.channel.send("Goodbye " + message.author.name + "\ndont forget about me...")
                    await message.channel.send("time of death of instance: " + str(datetime.datetime.now()))

                console.print("[black bold on blue]\n\nhave a good day!\n\nMADE BY JAKE (MESSYCODE) AND IMMACULATA (IMMACULATA RODRIGO)\nTHIS SOFTWARE IS LICENSED UNDER THE MIT LICENSE\nMADE ON DEC 28 2022, AT (ALL DAY)\nVERSION:9999\n", justify="center")
                console.print("TIME OF SHUTDOWN: " + str(datetime.datetime.now()), justify="center", style="bold red blink on black")

                with console.screen(style="bold white on red") as screen:
                    for count in range(1000, 0, -1):
                        text = Align.center(
                            Text.from_markup(f"[blink]Shutting down in...[/blink]\n{count}", justify="center"),
                            vertical="middle",
                        )
                        screen.update(Panel(text))
                        sleep(0.00001)

                console.rule("[bold red]DISCONNECTED FROM DISCORD")
                await client.close()
                exit()
            else:
                await message.channel.send("You don't have permission to do that")
                return
        
        if message.content.startswith('!joke status'):
            if message.author.id == 691877635394895893 or message.author.id == 1000936894500180099:
                await message.channel.send("Jokey Jerry status: " + str(JJ_status))
                if JJ_status == 0:
                    await message.channel.send("Jokey Jerry is currently active and ready to go")
                elif JJ_status == 1:
                    await message.channel.send("Jokey Jerry is currently inactive and will not respond to any commands")
                elif JJ_status == 2:
                    await message.channel.send("Jokey Jerry is currently in maintenance mode and will only respond to a few commands")
                elif JJ_status == 3:
                    await message.channel.send("Jokey Jerry is currently in debug mode and will only respond to commands ONLY from the developer")
                else:
                    await message.channel.send("Jokey Jerry is currently in an unknown state")
            else:
                await message.channel.send("You don't have permission to do that")
                return


        
        if message.content.startswith('jokey jerry'):
            gif_links = [
                "https://tenor.com/view/seinfeld-gif-18623119",
                "https://tenor.com/view/seinfeld-jerry-seinfeld-hello-bang-door-gif-4107955",
                "https://tenor.com/view/jerry-seinfeld-popcorn-yeah-gif-26383058",
                "https://tenor.com/view/seinfeld-jerry-seinfeld-glasses-awkward-gif-4195909",
                "https://tenor.com/view/jerry-seinfeld-i-like-the-way-you-think-gif-14890068",
                "https://tenor.com/view/yes-seinfeld-truth-buddy-kramer-gif-23789643",
                "https://tenor.com/view/kramer-seinfeld-kramer-seinfeld-god-help-us-leave-quickly-gif-23488572",
            ]
            await message.channel.send(random.choice(gif_links))
            return
        
        if message.content.startswith('hello') or message.content.startswith('hi') or message.content.startswith('hey') or message.content.startswith('yo ') or message.content.startswith("wassup"):
            await message.channel.send("HELLO " + message.author.name + "!")
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

    @client.event
    async def on_message_delete(message):
        console.print(f'[red bold blink i]message: \"{message.content}\" by {message.author} was deleted in {message.channel}',justify="center")
    
    @client.event
    async def on_message_edit(message_before, message_after):
        console.print(f'[blue bold blink i]message: \"{message_before.content}\" by {message_before.author} was edited to \"{message_after.content}\" in {message_after.channel}',justify="center")

    try:
        global Token
        client.run(Token)
        #write token to file src/last_token.txt
        with open("src/last_token.txt", "w") as f:
            f.write(Token)
    except Exception as e:
        print(e)
        print("\n\nNOT A VALID TOKEN\nTRYING LAST KNOWN TOKEN\nIF THAT DOESNT WORK, THEN REST THE TOKEN\n")
        try:
            with open("src/last_token.txt", "r") as f:
                Token = f.read()

            try:
                client.close()
                client.run(Token)
                with open("src/token.txt", "w") as f:
                    f.write(Token)
            except Exception as e:
                print("\n\nNOT A VALID LAST KNOWN TOKEN\n"+str(e))
        except Exception as e:
            print("NO LAST KNOWN TOKEN FOUND\nPLEASE RESET TOKEN\n"+str(e))

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