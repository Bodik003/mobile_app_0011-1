import discord
from discord.ext import commands
from discord.ext.commands import Bot
import datetime
import pytz
import time
from PIL import Image
from discord.ext import tasks


Bot = commands.Bot(".")

@Bot.event
async def on_ready():
     change_status.start()

@Bot.command()
@commands.has_permissions(administrator=True)
async def schedule(ctx):
    for attach in ctx.message.attachments:
        await attach.save("schedule.png")
    # 1 day
    img1 = Image.open("schedule.png")
    new_crop1 = (0,0,214,298)
    img11 = img1.crop(new_crop1)
    img111 = Image.new(size=(214,298),mode="RGB")
    img111.paste(img11,(0,0,214,298))
    img111.save("schedule1.png")
    # 2 day
    img2 = Image.open("schedule.png")
    new_crop2 = (215,0,429,298)
    img22 = img2.crop(new_crop2)
    img222 = Image.new(size=(214,298),mode="RGB")
    img222.paste(img22,(0,0,214,298))
    img222.save("schedule2.png")
    # 3 day
    img3 = Image.open("schedule.png")
    new_crop3 = (430,0,644,298)
    img33 = img3.crop(new_crop3)
    img333 = Image.new(size=(214,298),mode="RGB")
    img333.paste(img33,(0,0,214,298))
    img333.save("schedule3.png")
    # 4 day
    img4 = Image.open("schedule.png")
    new_crop4 = (645,0,859,298)
    img44 = img4.crop(new_crop4)
    img444 = Image.new(size=(214,298),mode="RGB")
    img444.paste(img44,(0,0,214,298))
    img444.save("schedule4.png")
    # 5 day
    img5 = Image.open("schedule.png")
    new_crop5 = (0,300,214,598)
    img55 = img5.crop(new_crop5)
    img555 = Image.new(size=(214,298),mode="RGB")
    img555.paste(img55,(0,0,214,298))
    img555.save("schedule5.png")
    # 6 day
    img6 = Image.open("schedule.png")
    new_crop6 = (215,300,429,598)
    img66 = img6.crop(new_crop6)
    img666 = Image.new(size=(214,298),mode="RGB")
    img666.paste(img66,(0,0,214,298))
    img666.save("schedule6.png")
    # 7 day
    img7 = Image.open("schedule.png")
    new_crop7 = (430,300,644,598)
    img77 = img7.crop(new_crop7)
    img777 = Image.new(size=(214,298),mode="RGB")
    img777.paste(img77,(0,0,214,298))
    img777.save("schedule7.png")


# weekday 1
@Bot.command()
@commands.has_permissions(administrator=True)
async def an1(ctx, hh, mm):
    with open("test.txt", 'r') as f:
        get_all = f.readlines()
    with open("test.txt", 'w') as f:
        for i, line in enumerate(get_all, 1):
            if i == 1:
                f.writelines("hh1 = "+hh+"\n")
            else:
                f.writelines(line)
    with open("test.txt", 'r') as f:
        get_all = f.readlines()
    with open("test.txt", 'w') as f:
        for i, line in enumerate(get_all, 1):
            if i == 2:
                f.writelines("mm1 = " + mm + "\n")
            else:
                f.writelines(line)
# weekday 2
@Bot.command()
@commands.has_permissions(administrator=True)
async def an2(ctx, hh, mm):
    with open("test.txt", 'r') as f:
        get_all = f.readlines()
    with open("test.txt", 'w') as f:
        for i, line in enumerate(get_all, 1):
            if i == 3:
                f.writelines("hh2 = "+hh+"\n")
            else:
                f.writelines(line)
    with open("test.txt", 'r') as f:
        get_all = f.readlines()
    with open("test.txt", 'w') as f:
        for i, line in enumerate(get_all, 1):
            if i == 4:
                f.writelines("mm2 = " + mm + "\n")
            else:
                f.writelines(line)
# weekday 3
@Bot.command()
@commands.has_permissions(administrator=True)
async def an3(ctx, hh, mm):
    with open("test.txt", 'r') as f:
        get_all = f.readlines()
    with open("test.txt", 'w') as f:
        for i, line in enumerate(get_all, 1):
            if i == 5:
                f.writelines("hh3 = "+hh+"\n")
            else:
                f.writelines(line)
    with open("test.txt", 'r') as f:
        get_all = f.readlines()
    with open("test.txt", 'w') as f:
        for i, line in enumerate(get_all, 1):
            if i == 6:
                f.writelines("mm3 = " + mm + "\n")
            else:
                f.writelines(line)
# weekday 4
@Bot.command()
@commands.has_permissions(administrator=True)
async def an4(ctx, hh, mm):
    with open("test.txt", 'r') as f:
        get_all = f.readlines()
    with open("test.txt", 'w') as f:
        for i, line in enumerate(get_all, 1):
            if i == 7:
                f.writelines("hh4 = "+hh+"\n")
            else:
                f.writelines(line)
    with open("test.txt", 'r') as f:
        get_all = f.readlines()
    with open("test.txt", 'w') as f:
        for i, line in enumerate(get_all, 1):
            if i == 8:
                f.writelines("mm4 = " + mm + "\n")
            else:
                f.writelines(line)
# weekday 5
@Bot.command()
@commands.has_permissions(administrator=True)
async def an5(ctx, hh, mm):
    with open("test.txt", 'r') as f:
        get_all = f.readlines()
    with open("test.txt", 'w') as f:
        for i, line in enumerate(get_all, 1):
            if i == 9:
                f.writelines("hh5 = "+hh+"\n")
            else:
                f.writelines(line)
    with open("test.txt", 'r') as f:
        get_all = f.readlines()
    with open("test.txt", 'w') as f:
        for i, line in enumerate(get_all, 1):
            if i == 10:
                f.writelines("mm5 = " + mm + "\n")
            else:
                f.writelines(line)
# weekday 6
@Bot.command()
@commands.has_permissions(administrator=True)
async def an6(ctx, hh, mm):
    with open("test.txt", 'r') as f:
        get_all = f.readlines()
    with open("test.txt", 'w') as f:
        for i, line in enumerate(get_all, 1):
            if i == 11:
                f.writelines("hh6 = "+hh+"\n")
            else:
                f.writelines(line)
    with open("test.txt", 'r') as f:
        get_all = f.readlines()
    with open("test.txt", 'w') as f:
        for i, line in enumerate(get_all, 1):
            if i == 12:
                f.writelines("mm6 = " + mm + "\n")
            else:
                f.writelines(line)
# weekday 7
@Bot.command()
@commands.has_permissions(administrator=True)
async def an7(ctx, hh, mm):
    with open("test.txt", 'r') as f:
        get_all = f.readlines()
    with open("test.txt", 'w') as f:
        for i, line in enumerate(get_all, 1):
            if i == 13:
                f.writelines("hh7 = "+hh+"\n")
            else:
                f.writelines(line)
    with open("test.txt", 'r') as f:
        get_all = f.readlines()
    with open("test.txt", 'w') as f:
        for i, line in enumerate(get_all, 1):
            if i == 14:
                f.writelines("mm7 = " + mm + "\n")
            else:
                f.writelines(line)



# loop 1
@tasks.loop()
async def change_status():
    with open("test.txt", 'r') as file:
        for line in file:
            if "hh1" in line:
                hh1 = int(line.strip()[6:])
            if "mm1" in line:
                mm1 = int(line.strip()[6:])

            if "hh2" in line:
                hh2 = int(line.strip()[6:])
            if "mm2" in line:
                mm2 = int(line.strip()[6:])

            if "hh3" in line:
                hh3 = int(line.strip()[6:])
            if "mm3" in line:
                mm3 = int(line.strip()[6:])

            if "hh4" in line:
                hh4 = int(line.strip()[6:])
            if "mm4" in line:
                mm4 = int(line.strip()[6:])

            if "hh5" in line:
                hh5 = int(line.strip()[6:])
            if "mm5" in line:
                mm5 = int(line.strip()[6:])

            if "hh6" in line:
                hh6 = int(line.strip()[6:])
            if "mm6" in line:
                mm6 = int(line.strip()[6:])

            if "hh7" in line:
                hh7 = int(line.strip()[6:])
            if "mm7" in line:
                mm7 = int(line.strip()[6:])

                target_channel_id = 838112578126610434
                channel = Bot.get_channel(target_channel_id)
                weekday = datetime.datetime.today().isoweekday()
                now = datetime.datetime.now(tz=pytz.timezone('Europe/Moscow'))
                h = now.hour
                m = now.minute
                if weekday == 1 and h == hh1 and m == mm1:
                    await channel.send((discord.utils.get(channel.guild.roles, name="Announcements").mention),file = discord.File(fp = 'schedule1.png'))
                    time.sleep(61)

                if weekday == 2 and h == hh2 and m == mm2:
                    await channel.send((discord.utils.get(channel.guild.roles, name="Announcements").mention),file = discord.File(fp = 'schedule2.png'))
                    time.sleep(61)

                if weekday == 3 and h == hh3 and m == mm3:
                    await channel.send((discord.utils.get(channel.guild.roles, name="Announcements").mention),file = discord.File(fp = 'schedule3.png'))
                    time.sleep(61)

                if weekday == 4 and h == hh4 and m == mm4:
                    await channel.send((discord.utils.get(channel.guild.roles, name="Announcements").mention),file = discord.File(fp = 'schedule4.png'))
                    time.sleep(61)

                if weekday == 5 and h == hh5 and m == mm5:
                    await channel.send((discord.utils.get(channel.guild.roles, name="Announcements").mention),file = discord.File(fp = 'schedule5.png'))
                    time.sleep(61)

                if weekday == 6 and h == hh6 and m == mm6:
                    await channel.send((discord.utils.get(channel.guild.roles, name="Announcements").mention),file = discord.File(fp = 'schedule6.png'))
                    time.sleep(61)

                if weekday == 7 and h == hh7 and m == mm7:
                    await channel.send((discord.utils.get(channel.guild.roles, name="Announcements").mention),file = discord.File(fp = 'schedule7.png'))
                    time.sleep(61)


Bot.run('ODM4NDU0NTYzMzk5OTI1Nzky.YI7VqQ.POY-YF9hd9nda-Usq7DU0kyCoCs')