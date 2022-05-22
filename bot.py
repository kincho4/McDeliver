import time
import discord
from discord.ext import commands
import sqlite3
from flask import Flask, abort, request
import pyautogui
import pydirectinput
import random
from discord_components import Button, DiscordComponents
import json
# This file will be for the Discord bot that will recieve the coord info

client = commands.Bot(command_prefix=".")
DiscordComponents(client)

@client.event
async def on_ready():
    print("Bot ready")


@client.command()
async def shop(ctx):
    embed = discord.Embed(
        title="Shop", description="This is the shop where you will be able to buy items", color=0x00ff4c)
    embed.add_field(name="1: PvP Kit", value="10 credits", inline=True)
    embed.add_field(name="2: Survival Kit", value="10 credits", inline=True)
    embed.add_field(name="3: Greifing Kit", value="2 credits", inline=True)
    embed.add_field(name="4: Advanced Greifing Kit",
                    value="4.5 credits", inline=True)
    embed.add_field(name="5: Totem Kit", value="2 credits", inline=True)
    embed.add_field(name="6: Chorous Kit", value="0.5 credits", inline=True)
    embed.add_field(name="7: Pearl Kit", value="0.5 credits", inline=True)
    embed.add_field(name="8: Wool Kit", value="2 credits", inline=True)
    embed.add_field(name="9: Lavacast Kit", value="0.5 credits", inline=True)
    embed.add_field(name="10: Firework Kit", value="1.5 credits", inline=True)
    embed.set_footer(text="Do .view [Item-Number] and .buy [Item-Number]")
    await ctx.send(embed=embed)


@client.command()
async def view(ctx, Item_number):
    if Item_number == "1":
        embed = discord.Embed(title="PvP Kit", url="https://cdn.discordapp.com/attachments/880771101695832067/881627393595433020/PvP_Kit.png",
                              description="This is the best PvP kit that contains all the needed items.", color=0xff0000)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/880771101695832067/881627393595433020/PvP_Kit.png")
        embed.add_field(
            name="Diamond Sword [mending, unbreaking III, looting III, sweeping edge III, sharpness V]", value="1", inline=False)
        embed.add_field(
            name="Diamond Axe [silk touch, unbreaking III, sharpness V, mending, efficiency V]", value="1", inline=False)
        embed.add_field(
            name="Diamond Pickaxe [mending, fortune III, unbreaking III, efficiency V]", value="1", inline=False)
        embed.add_field(
            name="Bow [flame, infinity, unbreaking III, power V]", value="1", inline=False)
        embed.add_field(
            name="Diamond Helmet [aqua affinity, respiration III, protection IV, unbreaking III, mending]", value="2", inline=False)
        embed.add_field(
            name="Diamond Chestplate [unbreaking III, mending, protection III]", value="2", inline=False)
        embed.add_field(
            name="Diamond Leggings [unbreaking III, mending, protection III]", value="2", inline=False)
        embed.add_field(
            name="Diamond Boots [mending, depth strider III, unbreaking III, protection IV, feather falling IV]", value="2", inline=False)
        embed.add_field(name="Totem of Undying", value="6", inline=False)
        embed.add_field(name="Ender Chest", value="8", inline=False)
        embed.add_field(name="Ender Pearl", value="32", inline=False)
        embed.add_field(name="Arrow", value="64", inline=False)
        embed.add_field(name="Obsidian", value="64", inline=False)
        embed.add_field(name="End Crystal", value="64", inline=False)
        embed.add_field(name="Chorous Fruit", value="192", inline=False)
        await ctx.send(embed=embed)
    elif Item_number == "2":
        embed = discord.Embed(title="Survival Kit", url="https://cdn.discordapp.com/attachments/880771101695832067/881838046574698516/Survial.png",
                              description="This kit will get you started out and is ideal for if you die.", color=0x1e00ff)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/880771101695832067/881838046574698516/Survial.png")
        embed.add_field(
            name="Diamond sword [mending, unbreaking III, looting III, sweeping edge III, sharpness V]", value="1", inline=False)
        embed.add_field(
            name="Diamond Axe [silk touch, unbreaking III, sharpness V, mending, efficiency V]", value="1", inline=False)
        embed.add_field(
            name="Diamond Pickaxe [mending, fortune III, unbreaking III, efficiency V]", value="1", inline=False)
        embed.add_field(
            name="Diamond Pickaxe [mending, silk touch, unbreaking III, efficiency V]", value="1", inline=False)
        embed.add_field(
            name="Diamond Shovel [mending, silk touch, unbreaking III, efficiency V]", value="1", inline=False)
        embed.add_field(
            name="Shears [unbreaking III, mending, efficiency V]", value="1", inline=False)
        embed.add_field(
            name="Flint and Steel [mending, unbreaking III]", value="1", inline=False)
        embed.add_field(
            name="Fishing Rod [mending, unbreaking III, lure III, luck of the sea III]", value="1", inline=False)
        embed.add_field(
            name="Diamond Helmet [aqua affinity, respiration III, protection IV, unbreaking III, mending]", value="1", inline=False)
        embed.add_field(
            name="Diamond Chestplate [unbreaking III, mending, protection III]", value="1", inline=False)
        embed.add_field(
            name="Diamond Leggings [unbreaking III, mending, protection III]", value="1", inline=False)
        embed.add_field(
            name="Diamond Boots [mending, depth strider III, unbreaking III, protection IV, feather falling IV ", value="1", inline=False)
        embed.add_field(
            name="Elytra [unbreaking III, mending]", value="1", inline=False)
        embed.add_field(name="Enchanting Table", value="1", inline=False)
        embed.add_field(name="Totem of Undying", value="4", inline=False)
        embed.add_field(name="Bookshelf", value="15", inline=False)
        embed.add_field(name="Ender Chest", value="16", inline=False)
        embed.add_field(name="Firework Rocket", value="128", inline=False)
        embed.add_field(name="Chourus Fruit", value="128", inline=False)
        embed.add_field(name="Lapis Lazuli", value="192", inline=False)
        await ctx.send(embed=embed)
    elif Item_number == "3":
        embed = discord.Embed(title="Greifing Kit", url="https://cdn.discordapp.com/attachments/880771101695832067/881846289728405534/Greif_Kit.png",
                              description="This kit will give you the items to DESTROY anything from a small dirt house to a MEGA-mansion.", color=0xff8800)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/880771101695832067/881846289728405534/Greif_Kit.png")
        embed.add_field(name="Tnt", value="1664", inline=False)
        embed.add_field(
            name="Flint and Steel [mending, unbreaking III]", value="1", inline=False)
        await ctx.send(embed=embed)
    elif Item_number == "4":
        embed = discord.Embed(title="Advanced Greifing Kit", url="https://cdn.discordapp.com/attachments/942371061561962540/945293352180539392/Advanced_Greifing_Kit.png",
                              description="This kit will DESTROY anything with DOUBLE the power than the Greifing Kit. ", color=0xff8800)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/942371061561962540/945293352180539392/Advanced_Greifing_Kit.png")
        embed.add_field(name="Wither Skeleton Skull",
                        value="384", inline=False)
        embed.add_field(name="Soul Sand", value="512", inline=False)
        embed.add_field(name="TNT", value="768", inline=False)
        embed.add_field(
            name="Flint and Steel [mending, unbreaking III]", value="1", inline=False)
        await ctx.send(embed=embed)
    elif Item_number == "5":
        embed = discord.Embed(title="Totem Kit", url="https://cdn.discordapp.com/attachments/880771101695832067/881847685999624212/Totem_Kit.png",
                              description="Defy death with this totem kit!", color=0xeeff00)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/880771101695832067/881847685999624212/Totem_Kit.png")
        embed.add_field(name="Totem of Undying", value="27", inline=False)
        await ctx.send(embed=embed)
    elif Item_number == "6":
        embed = discord.Embed(title="Chorous Kit", url="https://cdn.discordapp.com/attachments/880771101695832067/881848628598169600/Chorous_Kit.png",
                              description="This kit will let you just teleport away when in danger!", color=0xff00f7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/880771101695832067/881848628598169600/Chorous_Kit.png")
        embed.add_field(name="Chorus fruit", value="1728", inline=False)
        await ctx.send(embed=embed)
    elif Item_number == "7":
        embed = discord.Embed(title="Pearl Kit", url="https://cdn.discordapp.com/attachments/880771101695832067/881849284893483048/Pearl_Kit.png",
                              description="This kit will give you all the ender pearls needed for escaping danger or quick transport.", color=0x3f6737)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/880771101695832067/881849284893483048/Pearl_Kit.png")
        embed.add_field(name="Ender Pearl", value="432", inline=False)
        await ctx.send(embed=embed)
    elif Item_number == "8":
        embed = discord.Embed(title="Wool Kit", url="https://cdn.discordapp.com/attachments/880771101695832067/881850287420235796/Wool_Kit.png",
                              description="This kit is perfect for builders who need a quick refill on wool", color=0x2bff00)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/880771101695832067/881850287420235796/Wool_Kit.png")
        embed.add_field(name="Red Wool", value="128", inline=False)
        embed.add_field(name="Orange Wool", value="128", inline=False)
        embed.add_field(name="Yellow Wool", value="128", inline=False)
        embed.add_field(name="Lime Wool", value="128", inline=False)
        embed.add_field(name="Green Wool", value="128", inline=False)
        embed.add_field(name="Cyan Wool", value="128", inline=False)
        embed.add_field(name="Light Blue Wool", value="128", inline=False)
        embed.add_field(name="Blue Wool", value="128", inline=False)
        embed.add_field(name="Purple Wool", value="128", inline=False)
        embed.add_field(name="Magenta Wool", value="128", inline=False)
        embed.add_field(name="Pink Wool", value="128", inline=False)
        embed.add_field(name="Black Wool", value="128", inline=False)
        embed.add_field(name="Gray Wool", value="64", inline=False)
        embed.add_field(name="Light Gray Wool", value="64", inline=False)
        embed.add_field(name="White Wool", value="64", inline=False)
        await ctx.send(embed=embed)
    elif Item_number == "9":
        embed = discord.Embed(title="Lavacast Kit", url="https://cdn.discordapp.com/attachments/880771101695832067/881852715750293525/Lavacast_Kit.png",
                              description="This is another good tool for destroying buildings and it topped up with everything you will need", color=0x999999)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/880771101695832067/881852715750293525/Lavacast_Kit.png")
        embed.add_field(name="Water Bucket", value="1", inline=False)
        embed.add_field(name="Lava bucket ", value="25", inline=False)
        embed.add_field(name="cobblesotne", value="64", inline=False)
        await ctx.send(embed=embed)
    elif Item_number == "10":
        embed = discord.Embed(title="Firework Kit", url="https://cdn.discordapp.com/attachments/880771101695832067/881854249946976346/Firework_Kit.png",
                              description="This kit is a long lasting top-up on firework rockets for your elytra", color=0x0db1f8)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/880771101695832067/881854249946976346/Firework_Kit.png")
        embed.add_field(name="Firework Rocket", value="1728", inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("That is not a valid item id. E.g. the item id of [PvP Kit] would be [1]")


@client.command()
@commands.has_permissions(administrator=True)
async def addcreds(ctx, duser, credamount):
    fltcredamnt = float(credamount)

    con = sqlite3.connect("credits.db")
    cur = con.cursor()

    dbcrdamt = cur.execute(
        f"SELECT creditamount FROM creds WHERE userid={duser}").fetchall()
    dbcrdamtr = float(dbcrdamt[0][0])

    cur.execute(
        f"UPDATE creds SET creditamount = {fltcredamnt+dbcrdamtr} WHERE userid={duser}")

    await ctx.send(f"SUCCESSFULLY ADDED {credamount} CREDITS TO {duser}")

    con.commit()
    con.close()


@client.command()
async def create_account(ctx):
    concr = sqlite3.connect("credits.db")
    curcr = concr.cursor()
    conit = sqlite3.connect("items.db")
    curit = conit.cursor()

    alrextstcr = curcr.execute(f"SELECT userid FROM creds WHERE userid={ctx.author.id}").fetchall()
    alrextstit = curit.execute(f"SELECT userid FROM items WHERE userid={ctx.author.id}").fetchall()
    if alrextstcr == []and alrextstit == []:
        curcr.execute(f"INSERT INTO creds VALUES ({ctx.author.id},0.00)")
        curit.execute(f'INSERT INTO items VALUES ({ctx.author.id},"")')
        await ctx.send("Account created successfully!")
    else:
        await ctx.send("Can not create account because your id is already on the database run .creds to see your balance and .inv to see your items.")
    conit.commit()
    conit.close()
    concr.commit()
    concr.close()


@client.command()
async def creds(ctx):
    con = sqlite3.connect("credits.db")
    cur = con.cursor()

    accdb = cur.execute(
        f"SELECT userid, creditamount FROM creds WHERE userid={ctx.author.id}").fetchall()

    embed = discord.Embed(color=0x319642)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="Username:", value=ctx.author.name, inline=False)
    embed.add_field(name="ID", value=accdb[0][0], inline=False)
    embed.add_field(name="Credits:", value=accdb[0][1], inline=False)
    await ctx.send(ctx.author.mention)
    await ctx.send(embed=embed)

    con.commit()
    con.close()


@client.command()
async def deliver(ctx, X, Y, Z, package):
    chars = "ABCDEFGHIGLKMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwyz1234567890"
    a = "".join(random.sample(chars,4))+"-"
    b = "".join(random.sample(chars,4))+"-"
    c = "".join(random.sample(chars,4))+"-"
    d = "".join(random.sample(chars,4))
    pack1x = "1340"
    pack1y = "80"
    pack1z = "-2451"
    coordscomb = int(X)+int(Y)+int(Z)
    delid = a+b+c+d
    delidpic = f"screenshots/{delid}.png"

    if package == "1":
        pyautogui.write(f't #goto {pack1x} {pack1y} {pack1z}', interval=0.25)
        time.sleep(0.5)
        pydirectinput.press("Enter")
        pack1suptd = int(pack1x)+int(pack1y)+int(pack1z)
        distance = abs(pack1suptd-coordscomb)
        estdeltime = distance/1.5 + 48
        data = {"account": "kinchomincho", "delid":delid,
                "dcoords": f"{X}, {Y}, {Z}", "esttime": str(estdeltime)}
    elif package == "2":
        pyautogui.write(f't #goto x, y , z', interval=0.25)
        time.sleep(0.5)
        pydirectinput.press("Enter")
    elif package == "3":
        pyautogui.write(f't #goto x, y , z', interval=0.25)
        time.sleep(0.5)
        pydirectinput.press("Enter")
    elif package == "4":
        pyautogui.write(f't #goto x, y , z', interval=0.25)
        time.sleep(0.5)
        pydirectinput.press("Enter")
    elif package == "5":
        pyautogui.write(f't #goto x, y , z', interval=0.25)
        time.sleep(0.5)
        pydirectinput.press("Enter")
    elif package == "6":
        pyautogui.write(f't #goto x, y , z', interval=0.25)
        time.sleep(0.5)
        pydirectinput.press("Enter")
    elif package == "7":
        pyautogui.write(f't #goto x, y , z', interval=0.25)
        time.sleep(0.5)
        pydirectinput.press("Enter")
    elif package == "8":
        pyautogui.write(f't #goto x, y , z', interval=0.25)
        time.sleep(0.5)
        pydirectinput.press("Enter")
    elif package == "9":
        pyautogui.write(f't #goto x, y , z', interval=0.25)
        time.sleep(0.5)
        pydirectinput.press("Enter")
    elif package == "10":
        pyautogui.write(f't #goto x, y , z', interval=0.25)
        time.sleep(0.5)
        pydirectinput.press("Enter")
    else:
        await ctx.send("That package does not exist")
    time.sleep(0.2)
    embed=discord.Embed(title=f"Delivery - {delid}", description="This is some info about your delivery. When the delivery is completed you will get a screenshot of the delivery with the coords.", color=0xa9e10e)
    embed.add_field(name="Delivery ID", value=data["delid"], inline=False)
    embed.add_field(name="Delivery Coords", value=data["dcoords"], inline=False)
    embed.add_field(name="Estimated Delivery Time (second)", value=data["esttime"]+" Sec", inline=False)
    embed.add_field(name="Estimated Delivery Time (Minuite)", value=str(int(data["esttime"])/60)+" Min", inline=False)
    embed.add_field(name="Estimated Delivery Time (Hour)", value=str(int(data["esttime"])/3600)+" Hour", inline=False)
    await ctx.author.send(embed=embed)
    time.sleep(15)
    pyautogui.write(f't #goto {X} {Y} {Z}', interval=0.25)
    time.sleep(0.5)
    pydirectinput.press("Enter")
    time.sleep(distance/1.5)
    pyautogui.write(f't #goto chest', interval=0.25)
    time.sleep(0.5)
    pydirectinput.press("Enter")
    time.sleep(30)
    pydirectinput.keyDown('shift')
    time.sleep(0.5)
    pydirectinput.click(680, 800)
    time.sleep(0.5)
    pydirectinput.keyUp('shift')
    time.sleep(0.5)
    chscreen = pyautogui.screenshot()
    chscreen.save("screenshots/"+delid+".png")
    time.sleep(0.2)
    await ctx.author.send(file=discord.File(delidpic))

@client.command()
async def inv(ctx):
    con = sqlite3.connect("items.db")
    cur = con.cursor()

    invitems = cur.execute("SELECT * FROM items").fetchall()
    
    embed1=discord.Embed(title=ctx.author.name)
    embed1.set_thumbnail(url=ctx.author.avatar_url)
    embed1.add_field(name="Pack 1", value="0", inline=False)
    embed1.add_field(name="Pack 2", value="0", inline=False)
    embed1.add_field(name="Pack 3", value="0", inline=False)
    embed1.add_field(name="Pack 4", value="0", inline=False)
    embed1.add_field(name="Pack 5", value="0", inline=False)
    embed1.set_footer(text="Page 1")

    embed2=discord.Embed(title=ctx.author.name)
    embed2.set_thumbnail(url=ctx.author.avatar_url)
    embed2.add_field(name="Pack 6", value="0", inline=False)
    embed2.add_field(name="Pack 7", value="0", inline=False)
    embed2.add_field(name="Pack 8", value="0", inline=False)
    embed2.add_field(name="Pack 9", value="0", inline=False)
    embed2.add_field(name="Pack 10", value="0", inline=False)
    embed2.set_footer(text="Page 2")

    await ctx.send(embed=embed1, components=[
        [Button(label="Next Page",style=3,emoji="➡",custom_id="button1")]
    ])
    interaction1 = await client.wait_for("button_click",check = lambda i: i.custom_id == "button1")
    await interaction1.send(embed=embed2, components=[Button(label="Previous Page",style=3,emoji="⬅",custom_id="button2")], ephemeral=False)
    interaction2 = await client.wait_for("button_click",check = lambda i: i.custom_id == "button2")
    await interaction2.send(embed=embed1, ephemeral=False)
    con.close()

@client.command()
async def buy(ctx,pack):
    concred = sqlite3.connect("credits.db")
    curcred = concred.cursor()

    creds = curcred.execute(f"SELECT creditamount FROM creds WHERE userid={ctx.author.id}").fetchall()
    concred.close()

    if pack == "1":
        price1 = 10.0
        newcredamount1 = float(creds[0][0])-price1

        if newcredamount1 >= 0:
            connewcred = sqlite3.connect("credits.db")
            curnewcred = connewcred.cursor()
            curnewcred.execute(f"UPDATE creds SET creditamount={newcredamount1} WHERE userid={ctx.author.id}")
            connewcred.commit()
            connewcred.close()

            coninvup = sqlite3.connect("items.db")
            curinvup = coninvup.cursor()
            packs = curinvup.execute(f"SELECT items FROM items WHERE userid={ctx.author.id}").fetchall()
            packsraw = packs[0][0]
            packsplit = packsraw.split(",")
            packsplitnew = packsplit.append("1")
            packlistnestr = ",".join(packsplitnew)
            curinvup.execute(f"UPDATE items SET items={packlistnestr} WHERE userid={ctx.author.id}")
            coninvup.commit()
            coninvup.close()


        else:
            await ctx.send("You dont have enough credits :(")
    elif pack == "2":
        price2 = 10.0
    elif pack == "3":
        price3 = 2.0
    elif pack == "4":
        price4 = 4.5
    elif pack == "5":
        price5 = 2.0
    elif pack == "6":
        price6 = 0.5
    elif pack == "7":
        price7 = 0.5
    elif pack == "8":
        price8 = 2.0
    elif pack == "9":
        price9 = 0.5
    elif pack == "10":
        price10 = 1.5
    else:
        await ctx.send("Thats not a valid package")
TOKEN=""
with open("data.json", "r") as tokenget:
    data = json.load(tokenget)
    for tokentrue in data["TOKEN"]:
        TOKEN += tokentrue 

client.run(TOKEN)
