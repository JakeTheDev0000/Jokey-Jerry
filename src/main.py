import joke_MGR
import discord

Token = open("src/token.txt", "r").read()
# inv link: https://discord.com/api/oauth2/authorize?client_id=1057475979011956738&permissions=515399735360&scope=bot

def main():
    client = discord.Client(intents=discord.Intents.all())
    immaculata = joke_MGR.immaculata()
    jake = joke_MGR.jake()
    beecie = joke_MGR.beecie()
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        message.content = message.content.lower()
    
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

            elif who == 'immaculata':
                await message.channel.send(immaculata.get_random_joke())
            elif who == 'jake':
                await message.channel.send(jake.get_random_joke())
            elif who == 'beecie':
                await message.channel.send(beecie.get_random_joke())

            else:
                await message.channel.send("I don't know that person")
                await message.channel.send("Try 'joke list' to see who I know")
    
    client.run(Token)

if __name__ == "__main__":
    main()