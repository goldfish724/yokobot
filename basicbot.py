import discord
import asyncio
import csv
import yokocalc



client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!yoko'):
    	choice = "[ERROR] uh oh! Go yell at @cyphra!"
    	tmp = await client.send_message(message.channel, 'Calculating outfit...')
    	
    	
    	await client.edit_message(tmp, 'I recommend {}'.format(choice))


    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')



client.run('MzI1MzA0ODU1NzcyMjY2NDk3.DCW6yw.-x1RF4BWmI09517fZUJw5oZhLTQ')