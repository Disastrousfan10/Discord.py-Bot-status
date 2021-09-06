import discord
from discord.ext import commands
from discord.ext.commands.core import dm_only

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
	print("10")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online)

@client.command()
async def hello(ctx):
  await ctx.send("hi")

@client.command(aliases= ['purge','delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
   if amount == None:
       await ctx.channel.purge(limit=1000000)
   else:
       await ctx.channel.purge(limit=amount)

@client.command()
async def dm(ctx, user_id=None, *, args=None):
    if user_id != None and args != None:
        try:
            target = await client.fetch_user(user_id)
            await target.send(args)

            await ctx.channel.send("'" + args + "' sent to: " + target.name)

        except:
            await ctx.channel.send("Couldn't dm the given user.")
        

    else:
        await ctx.channel.send("You didn't provide a user's id and/or a message.")






client.run("ODg0MDU4MjM0MDc4NTExMTE1.YTS9ZA.1vL0sjyB-VJdE7krgJM3oPEDDUk")
