import os
import discord
from discord.ext import commands
from discord import app_commands

from botserver import server_on

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())



# Bot even
# คำสั่ง Bot พร้อมใช้งาน

@bot.event
async def on_ready():
    print("Bot Online!")
    await bot.tree.sync()

# แจ้งคนเข้า-ออก Server

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1290632414166519891) # channel id
    text = f"ควายหลุดเข้ามาเพิ่มแล้ว {member.mention}!"

    emmbed = discord.embed(title = 'ควายหลุดเข้ามาเพิ่มแล้ว',
                       description = text,
                       color = 0x66FFFF)

    await channel.send(text) # ส่งข้อความไปที่ห้อง
    await  channel.send(embed=emmbed) # ส่ง embed ไปที่ห้อง
    #await member.send(text)  # ส่งข้อความไปที่คนเข้ามา

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1290632414166519891) # channel id
    text = f"เลิกควายสักทีนะ {member.name}!"
    await channel.send(text) # ส่งข้อความไปที่ห้อง
    #await member.send(text)  # ส่งข้อความไปที่คนเข้ามา


#คำสั่ง chat bot
@bot.event
async def on_message(message):
    channel = bot.get_channel(1290638096609710222) # channel id
    mes = message.content # ดึงข้อความที่ถูกส่งมา
    if mes == 'Hello':
        await message.channel.send("มึงคนไทยป่าววะ") # ส่งกลับไปที่ห้องนั้น
    elif mes == 'สวัสดี':
        await message.channel.send("Hello โทษทีกูเด็กอินเตอร์") # ตอบกลับไปที่เดิม
    elif  mes == 'ควาย':
        await message.channel.send("มึงสิควาย")
    elif  mes == 'กินเบียร์มั้ย':
        await message.channel.send("เจอกัน IF Camping")
    elif   mes == 'กินเหล้ามั้ย':
        await message.channel.send("ชอบกินเบียร์มากกว่า หรือเหล้าขาวดี")
    elif   mes == 'รีวิวคุณซี':
        await  message.channel.send("ไอแคระ หัดมาเรียนบ้าง อย่าเล่นแต่Fivem")
    elif   mes == 'รีวิวคุณแม็ก':
        await  message.channel.send("แอบเมียดูดพอต นิสัยไม่ดี")
    elif    mes == 'รีวิวคุณไอซ์':
        await  message.channel.send("ดัดฟันเสร็จแล้วยิ้มไม่หยุด เรียนดี แต่กินเหล้าเบียร์ดีกว่า")
    elif     mes == 'รีวิวคุณแฟ้ม':
        await   message.channel.send("ติดแมว ส่วนเหล้าเบียร์ติดพอๆกัน ชอบจะล่อแต่วานเพื่อนนิฮาย")
    elif mes == 'ทำไมเป็นรูปกูอะไอบอท':
        await message.channel.send("ถามพ่อมึงดู ไอแคระ")
    elif mes == 'ควย':
        await message.channel.send("แล้วมึงควยไร")

    await bot.process_commands(message)
    # ทำคำสั่ง Event ก่อน แล้วจึงไปทำคำสั่ง Bot Command ต่อ

# /////////////// COMMANDS  /////////////////
# คำสั่ง Commands

@bot.command()
async def Hello(ctx):
    await  ctx.send(f"Hi {ctx.author.name}!")

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

# ถ้าต้องการมีหลาย Command  ต้องใช้ @bot.command() มากกว่า 1 ครั้ง

# Slash commands
@bot.tree.command(name = 'hibot', description = 'Replies with Hi')
async def testcommand(interaction):
     await interaction.response.send_message("ดีจ้า กูบอทมึงเอง")

# Bot รับค่าจาก User
@bot.tree.command(name='name')
@app_commands.describe(name = "มึงชื่ออะไร?")
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"Hello {name}")

# Embeds
@bot.tree.command(name='help', description='Bot command')
async def helpcommand(interaction):
    emmbed = discord.Embed(title='Help me! - Bot Commands',
                           description='Bot Commands',
                           color= 0x66FFFF,
                           timestamp= discord.utils.utcnow())
    # ใส่ข้อมูล
    emmbed.add_field(name='/hello1', value='Hello Commands', inline=True)
    emmbed.add_field(name='/hello2', value='Hello Commands', inline=True)
    emmbed.add_field(name='/hello3', value='Hello Commands', inline=False)
    # Set ชื่อผู้เขียน เช่น คนสร้างบอท แปะลิ้งก์ช่องทางของตัวเองได้
    emmbed.set_author(name='Author', url='https://www.youtube.com/watch?v=arxJvcQX7Rk',  icon_url='https://images.indianexpress.com/2024/02/YouTube-YouTube-1.jpg')
    # ใส่รูปเล็ก-ใหญ่
    emmbed.set_thumbnail(url='https://scontent-bkk1-1.xx.fbcdn.net/v/t39.30808-6/457648228_3219541168183460_8019237736004853319_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=6ee11a&_nc_eui2=AeEcEC6pd273N5ncmLtIR3j039Qs2Tn_uSDf1CzZOf-5IBabagxd92w9z1end7zr3JyiQXbtFsawLzmn3z-Hsz1D&_nc_ohc=UI4bDJ0AdPIQ7kNvgHeyv61&_nc_ht=scontent-bkk1-1.xx&_nc_gid=ABYVBA3DlyWUYVgPwkvj_ly&oh=00_AYAB2idRAh04AdK9ZOmp53Sm0gt2s0JevzT3uC7-KYgkMQ&oe=6701B2B0')
    emmbed.set_image(url='https://scontent-bkk1-1.xx.fbcdn.net/v/t39.30808-6/296285349_2583131785157738_1404869072572791856_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeEVORfTrfdZ-nTyDzpt90Fl6J7KZZ6YZiDonsplnphmILnvLTTRPmZxjbSyaNqv8QssFDSpmSEQhmPJrbjqpuuW&_nc_ohc=pjKHTmOGgukQ7kNvgFJbgRw&_nc_ht=scontent-bkk1-1.xx&_nc_gid=AhU7-ATLUtbGmf5qImg-BR2&oh=00_AYAgL5QcKHwXE-c2jKOCWO605lYWdo0nPewutSt0RZYuLg&oe=6701C4F0')
    # Footer หรือเนื้อหาส่วนท้าย
    emmbed.set_footer(text='Bot Commands', icon_url='https://scontent-bkk')

    await interaction.response.send_message(embed = emmbed)

server_on()

bot.run(os.getenv('TOKEN'))