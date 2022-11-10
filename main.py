import discord
from discord.ext import commands, tasks
from asyncio import sleep
import random
import interactions
import datetime
import asyncio
import os
import httpx
from random import choice, randint
from discord.utils import get
from dotenv import load_dotenv
import requests
from requests import get
import json
import sys

shit = []

pp = ["**8=D**","**8==D**","**8===D**","**8====D**","**8=====D**","**8======D**"]
ben = ["Yes?","No","Ugh","NaNaNa","HoHoHo","Ben?"]
bella = ["Yes?","No","Bruh","NaNaNa","*laughs*","Bella?"]
killmessages = [" died.", " died from cringe."," saw floppa r34", " posted memes in #general", " took the L.", " got rickrolled by a free bobux link.", " got cancelled on Twitter."," got ratio'd on Twitter."," got caught in 4K"," ragequitted."," went to Brazil.", " got ratio'd"," got [Content Deleted]", " died because yes.", " got yeeted."," got permbanned.", " posted cringe 💀"," choked to death on a fortune cookie"," said deez nuts in 2022 💀"," got catfished by a 69 year old man."," said 'amogus' in 2022 💀"," got rejected by their crush."," found out what poison was."," choked on their spit."," hugged a bee hive"," stuck his pp in a electrical socket"," had explosive diarrhea after eating taco bell."," dabbed in 2022."," bought Stitch Face"," said amogus is still funny"," forgot how to breath 💀"," became emo"," became a TikToker"," became a dream stan"," downloaded Twitter"," went on twitter.com"," went to freerobux.com"," called amogus sussy imposter at 3AM"]

TOKEN = os.getenv("TOKEN")

bot = interactions.Client(token=TOKEN, disable_sync=False)
bot.requests = httpx.AsyncClient()

load_dotenv()

def admin_list():
    def predicate(ctx):
        list = [898358037239201812]  # ENTER YOUR USER ID HERE
        return ctx.message.author.id in list

    return commands.check(predicate)

@bot.event
async def on_ready():
    print("Bot Online!!!")
    with open("funny2.txt", "r") as f:
        file_lines1 = f.readlines()
    for line1 in file_lines1:
        shit.append(str(line1.strip()))
    print(f"{len(shit)} listed users!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot: return
    else:
        if str(message.author.id) in shit:
            await message.delete()
            await message.channel.send(message.author.mention + "<:troll:988139019869241444>")

@bot.command(
    name="hello",
    description="A friendly hello from the bot"
)
async def hello(ctx: interactions.CommandContext):
    await ctx.send(f"Hi {ctx.author.mention}!")

@bot.command(
    name="uwu",
    description="Use if ur a Furry"
)
async def uwu(ctx: interactions.CommandContext):
    await ctx.send("ew stfu u fucking furry")

@bot.command(
    name="die",
    description="Make Me kms"
)
async def die(ctx: interactions.CommandContext):
    await ctx.send("NEVER!!!")

@bot.command(
    name="ufat",
    description="Call the bot fat",
)
async def ufat(ctx: interactions.CommandContext):
    await ctx.send("ik u aint talking 💀💀💀")

@bot.command(
    name="ampro",
    description="Tell the bot that you're pro"
)
async def ampro(ctx: interactions.CommandContext):
    await ctx.send("i smell 🧢")

@bot.command(
    name="deez",
    description="Tell the bot a funi joke"
)
async def deez(ctx: interactions.CommandContext):
    await ctx.send("not funny")

@bot.command(
    name="imgay",
    description="Come out as Gay"
)
async def imgay(ctx: interactions.CommandContext):
    await ctx.send("alr cool now leave me alone")

@bot.command(
    name="gayrate",
    description="gay rate someone",
    options = [
        interactions.Option(
            name="user",
            description="who u want to rate",
            type=interactions.OptionType.USER,
            required=True,
        ),
    ],
)
async def gayrate(ctx: interactions.CommandContext, user: discord.Member):
 await ctx.send(f"{user.mention} is {random.randrange(101)}% gay")

@bot.command(
    name="ratio",
    description="ratio someone",
		    options = [
        interactions.Option(
            name="user",
            description="person you want to ratio",
            type=interactions.OptionType.USER,
            required=True,
        ),
    ],
)
async def ratio(ctx: interactions.CommandContext, user:
discord.Member):
    await ctx.send(f"{user.mention} L + don’t care + didn’t ask + cry about it + who asked + stay mad + get real + mald, seethe, cope harder + incorrect + hoes mad + pound sand + basic skill issue + typo + ur dad left + you fell off + no u + the audacity + triggered + repelled + get a life + ok and? + cringe + go outside + touch grass + kick rocks + think again + not based + not funny didn’t laugh + get good + reported + small pp + ur allergic to sunlight + GG! + get rekt + trolled + your loss + muted + banned + kicked + permaban + useless + i slept with ur mom + redpilled + i said it better + tiktok fan + get a life + unsubscribed + plundered + go tell reddit + talk nonsense + you're a full time discord mod + you’re* + grammar issue + nerd + get clapped + go outside + bleach + lol + gay + retard + autistic + reported + ask deez + ez clap + straight cash + idgaf + stay mad + youre lost + you “re” + stay pressed + reverse double take back + pedophile + cancelled + don't give a damn + get a job + dumb kid + sussy baka + get blocked + mad free + freer than air + furry + rip bozo + you're a (insert stereotype) + slight_smile + aired + cringe again + mad cuz bad + my pronouns are xe, xem & xyr + irrelevant + deal with it + screencapped your bio + karen/kyle + jealous + you're deaf + balls + i'll be right back + go ahead whine about it + eat paper + you lose + your problem + no one cares + log off + don't care even more + sex offender + sex defender + get religion + NFT owner + you make bad memes + problematic + fall in line + dog water + you are going to my cringe comp + you failed kindergarten + you have a anime profile picture + an* + fatherless + motherless + sisterless + brotherless + orphan + catch some bitches + I don't care about your opinion + genshin player + you dress like garbage + 日 amogus + get fucked + queued + put some thought into what you're going to do with that + stfu + go to bed + yes, i'm taller than you + I win BOZO")

@bot.command(
    name="uwontbelievewhathappens",
    description="OMG U WONT BELIEVE WHAT HAPPENS1!1!1!11!!1"
)
async def uwontbelievewhathappens(ctx: interactions.CommandContext):
    await ctx.send("https://youtu.be/fujCdB93fpw")

@bot.command(
    name="stfu",
    description="Stfu."
)
async def stfu(ctx: interactions.CommandContext):
    await ctx.send("https://cdn.discordapp.com/attachments/841451660059869194/958183891536056380/MemeFeedBot.mov")

@bot.command(
    name="invite",
    description="Invite The Bot"
)
async def invite(ctx: interactions.CommandContext):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=1038499921776619531&permissions=8&scope=applications.commands%20bot")


@bot.command(
    name="amogus",
    description="idk what to put here 💀"
)
async def amogus(ctx: interactions.CommandContext):
    await ctx.send("cringy ass mf 💀💀💀")

@bot.command(
    name="whois",
    description="Get personal info about someone in your server",
		    options = [
        interactions.Option(
            name="user",
            description="Who you want info on",
            type=interactions.OptionType.USER,
            required=True,
        ),
    ],
)
async def whois(ctx: interactions.CommandContext, user: discord.Member):
	await ctx.send(f"{user.mention}'s information IP: 69.420.68.419, Credit Card Info: Mastercard, {user.mention}, 2326081951108557, 08/2025, CVV: 397, Phone Number: 1234567890, Address: 123 Sesame Street, Neighbors: Elmo & Cookie Monster")

@bot.command(
    name="eightball",
    description="Ask 8ball a question",
	    options = [
        interactions.Option(
            name="text",
            description="What you want to ask 8ball",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def eightball(ctx: interactions.CommandContext, text: str):

    eightball_responses = [

        '**Hell no.**',

        '**It is not looking too likely.**',

        '**Probably not LOL.**',

			  '**Fuck you >:(**'

        '**It is quite possible.**',

        '**Definitely.**',

        '**Maybe so.**',

			  '**Of course.**',
    ]
    await ctx.channel.send(f"{ctx.author.mention}'s answer: {random.choice(eightball_responses)}")


@bot.command(
    name="summon",
    description="Summon the Bot"
)
async def summon(ctx: interactions.CommandContext):
    await ctx.send(f"Fuck off {ctx.author.mention}! Im sleeping, Bitch!")
    

@bot.command(
    name="console",
    description='print("Hello World!")'
)
async def console(ctx: interactions.CommandContext):
   message = await ctx.send("H")
   await message.edit(content=f"He")
   await asyncio.sleep(1.7)
   await message.edit(content="Hel")
   await asyncio.sleep(1.7)
   await message.edit(content=f"Hell")
   await asyncio.sleep(1.7)
   await message.edit(content="Hello")
   await asyncio.sleep(1.7)
   await message.edit(content=f"Hello W")
   await asyncio.sleep(1.7)
   await message.edit(content="Hello Wo")
   await asyncio.sleep(1.7)
   await message.edit(content=f"Hello Wor")
   await asyncio.sleep(1.7)
   await message.edit(content="Hello Worl")
   await asyncio.sleep(1.7)
   await message.edit(content=f"Hello World")
   await message.edit(content=f"Hello World!")
   await asyncio.sleep(1)
   await message.edit(content=f"Hello World")
   await asyncio.sleep(1.7)
   await message.edit(content="Hello Worl")
   await asyncio.sleep(1.7)
   await message.edit(content=f"Hello Wor")
   await asyncio.sleep(1.7)
   await message.edit(content="Hello Wo")
   await asyncio.sleep(1.7)
   await message.edit(content=f"Hello W")
   await asyncio.sleep(1.7)
   await message.edit(content="Hello ")
   await asyncio.sleep(1.7)
   await message.edit(content=f"Hell")
   await asyncio.sleep(1.7)
   await message.edit(content="Hel")
   await asyncio.sleep(1.7)
   await message.edit(content=f"He")
   await asyncio.sleep(0.7)
   await message.edit(content=f"H")
   await asyncio.sleep(0.7)
   await message.edit(content=f"⠀")

@bot.command(
    name="cat",
    description="c a t"
)
async def cat(ctx: interactions.CommandContext):
   message = await ctx.send("A package has Arrived!")
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""Hi...
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""Hi...
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""Hi...
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")		
   await asyncio.sleep(2.0)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""Hi...
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")		
   await asyncio.sleep(2.0)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""Hi...
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")		
   await asyncio.sleep(2.0)
	

@bot.command(
    name="nuke",
    description="nuke someones house",
		    options = [
        interactions.Option(
            name="user",
            description="Person you want to Nuke",
            type=interactions.OptionType.USER,
            required=True,
        ),
    ],
)
async def nuke(ctx: interactions.CommandContext, user: discord.Member):
   message = await ctx.send(f" {ctx.author.mention} has put a nuke in {user.mention}'s House, it will go off in **5**")
   await asyncio.sleep(3.5)
   await message.edit(content=f"**4**")
   await asyncio.sleep(1.5)
   await message.edit(content="**3**")
   await asyncio.sleep(1.5)
   await message.edit(content=f"**2**")
   await asyncio.sleep(1.5)
   await message.edit(content="**1**")
   await asyncio.sleep(1.5)
   await message.edit(content="https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831")
   await asyncio.sleep(1.7)
   await message.edit(content="**BOOM**")
   await asyncio.sleep(3)
   await message.edit(content=f"Rest in pieces {user.mention}")
   await asyncio.sleep(3)
   await message.edit(content=f"they will be missed")
   await asyncio.sleep(3)  

@bot.command(
    name="iq",
    description="Check someones IQ 🤓",
		    options = [
        interactions.Option(
            name="user",
            description="person you want to rate",
            type=interactions.OptionType.USER,
            required=True,
        ),
    ],
)
async def iq(ctx: interactions.CommandContext, user: discord.Member):
  await ctx.send(f"{user.mention} has {random.randrange(101)} IQ")


@bot.command(
    name="coolrate",
    description="Check someones coolness 😎",
		    options = [
        interactions.Option(
            name="user",
            description="person you want to rate",
            type=interactions.OptionType.USER,
            required=True,
        ),
    ],
)
async def coolrate(ctx: interactions.CommandContext, user: discord.Member):
  await ctx.send(f"{user.mention} is {random.randrange(101)}% cool")


@bot.command(
    name="dumbrate",
    description="Check someones dumbness",
		    options = [
        interactions.Option(
            name="user",
            description="person you want to rate",
            type=interactions.OptionType.USER,
            required=True,
        ),
    ],
)
async def dumbrate(ctx: interactions.CommandContext, user: discord.Member):
  await ctx.send(f"{user.mention} is {random.randrange(101)}% dumb")

@bot.command(
    name="pprate",
    description="Check someones pp size",
	    options = [
        interactions.Option(
            name="user",
            description="person you want to rate",
            type=interactions.OptionType.USER,
            required=True,
        ),
    ],
)
async def pprate(ctx: interactions.CommandContext, user: discord.Member):
  await ctx.send(f"{user.mention} pp size is {random.choice(pp)}")

@bot.command(
    name="bitchesrate",
    description="see if someone will get bitches",
		    options = [
        interactions.Option(
            name="user",
            description="idk what to put here 💀",
            type=interactions.OptionType.USER,
            required=True,
        ),
    ],
)
async def bitchesrate(ctx: interactions.CommandContext, user: discord.Member):
  await ctx.send(f"{user.mention} is {random.randrange(101)}% bitchless")

@bot.command(
    name="customcat",
    description="c u s t o m  c a t",
	    options = [
        interactions.Option(
            name="text",
            description="What you want to say on top of the cat",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def customcat(ctx: interactions.CommandContext, text: str):
   message = await ctx.send("A package has Arrived!")
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""{text}
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""{text}
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""{text}
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")		
   await asyncio.sleep(2.0)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""{text}
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")		
   await asyncio.sleep(2.0)
   await message.edit(content=f"""
ຸ 　　　＿＿_＿＿
    　／　／　  ／|"
    　|￣￣￣￣|　|
    　|　　　　|／
    　￣￣￣￣""")
   await asyncio.sleep(2.0)
   await message.edit(content=f"""{text}
    　   　∧＿∧＿_
    　／(´･ω･`)  ／＼
    ／|￣￣￣￣|＼／
    　|　　　　|／
    　￣￣￣￣""")		
   await asyncio.sleep(2.0)

@bot.command(
    name="furryrate",
    description="see if someone is a furry or not",
		    options = [
        interactions.Option(
            name="user",
            description="idk what to put here 💀",
            type=interactions.OptionType.USER,
            required=True,
        ),
    ],
)
async def furryrate(ctx: interactions.CommandContext, user: discord.Member):
  await ctx.send(f"{user.mention} is {random.randrange(101)}% a furry")


@bot.command(
    name="kill",
    description="kill someone",
		    options = [
        interactions.Option(
            name="user",
            description="person u want to kill",
            type=interactions.OptionType.USER,
            required=True,
        ),
    ],
)
async def kill(ctx, user: discord.Member):
 await ctx.send(user.mention + random.choice(killmessages))

@bot.command(
    name="flashingconsole",
    description='print ("flashing text")',
			    options = [
        interactions.Option(
            name="text",
            description="What u want to say",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def flashingconsole(ctx: interactions.CommandContext, text: str):
   message = await ctx.send(f"{text}")
   await message.edit(content=f"⠀⠀⠀")
   await asyncio.sleep(1.7)
   await message.edit(content=f"{text}")
   await asyncio.sleep(1.7)
   await message.edit(content=f"⠀⠀⠀")
   await asyncio.sleep(1.7)
   await message.edit(content=f"{text}")
   await asyncio.sleep(1.7)
   await message.edit(content=f"⠀⠀⠀")
   await asyncio.sleep(1.7)
   await message.edit(content=f"{text}")
   await asyncio.sleep(1.7)
   await message.edit(content=f"⠀⠀⠀")
   await asyncio.sleep(1.7)
   await message.edit(content=f"{text}")
   await asyncio.sleep(1.7)
   await message.edit(content=f"⠀⠀⠀")
   await message.edit(content=f"{text}")
   await asyncio.sleep(1.7)  

@bot.command(
    name="echo",
    description="Make me say whatever u want ",
			    options = [
        interactions.Option(
            name="text",
            description="What u want to me to say",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def echo(ctx: interactions.CommandContext, text: str):
	await ctx.send(f"**{text}**")

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.command(
    name="restart",
    description='restarts the bot (ADMIN ONLY)'
)
async def restart(ctx):
    id = str(ctx.author.id)
    if id == '898358037239201812':
        await ctx.send('Restarting...')
        restart_bot()
    else:
        await ctx.send("You dont have sufficient permmisions to perform this action!")

@bot.command(
    name="created",
    description='shows when the bot was created'
)
async def created(ctx: interactions.CommandContext):
        await ctx.send("Zalcus Bot Has Existed Since **November 5th 2022**")

@bot.command(
    name="quote",
    description='get a quote',
)
async def quote(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote_ = json_data[0]['q'] + " ~ " + json_data[0]['a']
    await ctx.send(quote_)

@bot.command(
    name="retardrate",
    description="retard rate someone",
    options = [
        interactions.Option(
            name="user",
            description="who u want to rate",
            type=interactions.OptionType.USER,
            required=True,
        ),
    ],
)
async def retardrate(ctx: interactions.CommandContext, user: discord.Member):
 await ctx.send(f"{user.mention} is {random.randrange(101)}% a retard")

@bot.command(
    name="cringerate",
    description="cringe rate someone",
    options = [
        interactions.Option(
            name="user",
            description="who u want to rate",
            type=interactions.OptionType.USER,
            required=True,
        ),
    ],
)
async def cringerate(ctx: interactions.CommandContext, user: discord.Member):
 await ctx.send(f"{user.mention} is {random.randrange(101)}% cringe")

@bot.command(
    name="reverse",
    description='reverse any text',
			options = [
        interactions.Option(
            name="text",
            description="what u want to reverse",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def reverse(ctx, *, text: str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"{t_rev}")

@bot.command(
    name="quandale dingle lore",
    description="found this on reddit lmao"
)
async def quandaledinglelore(ctx):
    await ctx.send("What's up guys! It's Quandale Dingle here! RUUEHEHEHEHEHEEHE I have been arrested for multiple crimes AHHHHHHHHHHHHH including: Battery on a police officer WHAT, Grand theft, Declaring war on Italy, and public indecency RUHEHEHEEHEHEHEHEHEHEHE. I will be escaping prison on, MARCH 28TH! After that.... I WILL TAKE OVER THE WORLD")
	
bot.start()
