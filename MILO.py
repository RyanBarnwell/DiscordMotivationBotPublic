import discord
import random
from discord.ext import commands
from flask import Flask
import threading

# Create Flask app(Used to have an HTTP server)
app = Flask(__name__)

#HTTP server routing for Render to utilize free hosting
@app.route("/")
def home():
    return "Bot is running!"

# Run Flask in a separate thread
def run_server():
    app.run(host="0.0.0.0", port=8080)
    
    
#enable intents
intents = discord.Intents.default()
#enable message content intent
intents.message_content = True

#set up bots
bot = commands.Bot(command_prefix="!", intents=intents)

# Define a simple command
@bot.command()
async def hello(ctx):
    randGreet = random.randint(1,6)
    if(randGreet == 1):
        await ctx.send(f"Hello, {ctx.author.name}! 👋")
    elif(randGreet == 2):
        await ctx.send(f"Howdy, {ctx.author.name}!")
    elif(randGreet == 3):
        await ctx.send(f"Salutations, {ctx.author.name}!")
    elif(randGreet == 4):
        await ctx.send(f"I WILL SMITE THEE, {ctx.author.name}!")
    elif(randGreet == 5):
        await ctx.send(f"How can I help, {ctx.author.name}?")
    elif(randGreet == 6):
        #Hi in binary
        await ctx.send(f"01001000 01101001, {ctx.author.name}! 👋")
    
@bot.command()
async def motivate(ctx):
    #import csv for motivations?
    randMot = random.randint(1,3)
    if(randMot == 1):
        await ctx.send(f"You've got this {ctx.author.name}!")
    elif(randMot == 2):
        await ctx.send(f"I believe in you {ctx.author.name}!")
    elif(randMot == 3):
        await ctx.send(f"Don't give up {ctx.author.name}!")
    
# Run the bot
bot.run("Key Here")
