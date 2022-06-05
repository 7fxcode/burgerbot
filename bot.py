import asyncio
import datetime
import random
import discord

from discord import Option
from discord.ext.commands import cooldown, BucketType
from discord.ext import commands

prefix = '>'
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')
now = datetime.datetime.now()
time = now.strftime('%H:%M:%S')

@bot.event
async def on_ready():
    guilds = await bot.fetch_guilds(limit=150).flatten()
    print('[{}] Neugestartet und eingeloggt als {}!'.format(time, bot.user))
    print('[{}] Momentan bin ich {} Gilde*n!'.format(time, len(list(bot.guilds))))
    print(guilds)
    await bot.change_presence(status=discord.Status.idle,activity=discord.Game(name='.gg/7fx | >help'))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(':rage: Bitte gebe alle nötigen Argumente an!\n`>help 1`')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(':rage: Du hast nicht genügend Rechte um diesen Befehl auszuführen!')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(':rage: Bitte gebe einen gültigen Befehl an!')
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(':japanese_ogre: Langsamer Sportsfreund! Warte mal **{}** Sekunden.'.format(round(error.retry_after)))
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! Latenz beträgt {}ms'.format(round(bot.latency)))


@bot.command()
async def help(ctx, page : int):
    if page == 1:
        em = discord.Embed(title='Sequence - Hilfe',
                       description='Willkommen, hier findest du alle Befehle die du brauchst!\n\n__**Information**__\n> Die Befehle sind in Kategorien sortiert damit man sie besser Zuordnen kann und es übersichtlicher ist.\n\n__**Moderation**__\n`>ban <member> <grund>` - ⛔ Sperre ein Mitglied aus der Gilde\n`>kick <member> <grund>` - 🦵 Werfe ein Mitglied aus der Gilde\n`>warn <member>` - ⚠️ Verwarne ein Mitglied, Work in Progress also nicht benutzen!\n`+clear <anzahl>` - ❌ Lösche eine bestimmte Anzahl an Nachrichten\n\n__**Utility**__\n`>rpstart <yes | nein>` - 🎩 Roleplay starten lassen!\n`>poll <titel> <nachricht>` - 📈 Abstimmung starten!\n`>suggestion <thema> <beschreibung>` - ✊ Schlage etwas vor, für Hilfe sehe unten! \n`>extrahelp suggestion` - ❓ Hilfe für den Suggestion Befehl!\n`>announce <titel> <beschreibung>` - 📢 Schreibe eine Ankündigung!\n`>serverinfo` - ℹ️ Lasse dir Information über die Gilde anzeigen.\n\n__**Fun**__\n`>freundlich` - 😀 Der Bot ist freundlich zu dir!\n`>netflix <serien | filme | count>` - 📺 Netflix Serien & Film Generator\n`>userinfo <member>` - 👤 Zeige die wichtigen Informationen eines Members an.\n`>wop <member>` - 🙋‍♂ Spiele Wahrheit oder Pflicht mit dem Member!\n`>wuerfel` - 🎲 Werfe einen Würfel!\n`>gaymeter <member | None>` - 🏳️‍🌈 Teste ob jemand gay ist!\n`>lovemeter <member1> <member2>` - 💘 Teste zu wieviel % sich 2 Member lieben :)\n`>whois <member | None>` - ❔ Wer bin ich? (Filter)\n`>affenpocken` - 🐒 Finde heraus wer Affenpocken hat :)\n`>invite` - ✉️ Trete dem Discord des Coders bei\n`>quiz` - 🤚 Starte ein Quiz, WIP!\n`>pp <member>` - 🍆 PeePee Size Generator, D:\n`>slap <member>` - 🤚 Schlage ein Mitglied der Gilde\n`>kiss <member>` - 💞 Küsse ein Mitglied aus der Gilde\n`>kos <member>` - 💋🤚 Spiele Kiss or Slap mit einem Mitglied\n`>hug <member>` - 🫂 Umarme ein Mitglied aus der Gilde, Cute!\n`>usernamegen` - 👥 Generiere einen Zufälligen Benutzernamen '               ,
                       color=0xff790a)
        em.set_author(icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096',
                  name='Sequence')
        em.set_footer(text='Made by 7fx#1159 | >help')
        await ctx.send(embed=em)
    else:
        await ctx.send(':rage: Bitte gebe eine gültige Seite an!')
        return

@bot.command()
async def extrahelp(ctx, sub):
        em = discord.Embed(title='Sequence - Suggestion Hilfe',
                            description='> Um im Titel mehrere Wörter einzusetzen kannst du **Unterstriche & Bindestriche** verwenden.\n> Dies würde dann so aussehen: `>suggestion Leben_lassen Hallo, bitte Leben lassen!`',
                            color=0xff790a)
        em.set_author(
            icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096',
            name='Sequence')
        em.set_footer(text='Made by 7fx#1159 | >help')
        await ctx.send(embed=em)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = None):
  await member.ban(reason = reason)
  emb = discord.Embed(title='Der Banhammer hat gesprochen!',
                description=':hammer: Das   Mitglied {} wurde soeben ausgeschlossen!\n**Grund:** {}'.format(member.mention, reason), color=0xff790a)
  emb.set_author(name='Sequence', icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
  emb.set_footer(text='Made by 7fx#1159 | >help')
  await ctx.send(embed=emb)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    em = discord.Embed(title='Jemand wurde rausgeworfen!',
                       description=':leg: Das   Mitglied {} wurde soeben rausgeworfen!\n**Grund:** {}'.format(member.mention, reason), color=0xff790a)
    em.set_author(name='Sequence',icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    em.set_footer(text='Made by 7fx#1159 | >help')
    await ctx.send(embed=em)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    em = discord.Embed(title='Nachrichten gelöscht!',
                       description=f':white_check_mark: Erfolgreich **{amount}** Nachrichten erfolgreich gelöscht!',
                       color=0xff790a)
    em.set_author(name='Sequence',
                  icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    em.set_footer(text='Made by 7fx#1159 | >help')
    await ctx.send(embed=em)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def rpstart(ctx, ping):
    em=discord.Embed(title='Roleplay Start',description='Das RP hat nun begonnen, hüpfe auf den Server und spiele Roleplay!',color=0xff790a)
    em.set_author(name='Sequence',
                  icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    em.set_footer(text='Made by 7fx#1159 | >help')
    if ping == 'ja':
        await ctx.send(embed=em)
        await ctx.send('<@981895367840903218>')
    elif ping == 'nein':
        await ctx.send(embed=em)
        return
    else:
        await ctx.send(':rage: Bitte gebe ein ob ich pingen soll oder nicht!')
        return

@bot.command()
@commands.has_permissions(manage_messages=True)
async def poll(ctx, title, *, desc):
    em=discord.Embed(title="{} - {}'s Abstimmung".format(title, ctx.author.name),
                     description='{}'.format(desc),
                     color=0xff790a)
    em.set_author(name='Sequence',
                  icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    em.set_footer(text='Made by 7fx#1159 | >help')
    mes = await ctx.send(embed=em)
    await mes.add_reaction('👍')
    await mes.add_reaction('👎')

@bot.command()
async def freundlich(ctx):
    await ctx.send(':sob: Tut mir leid, leider weiß ich nicht was freundlich sein ist...')

serien = ['Stranger Things', 'Haus des Geldes', 'All of us are Dead', 'Top Boy', 'Naruto', 'Schnelles Geld', 'Tokyo Ghoul', 'The Seven Deadly Sins', 'Pet Girl', 'Riverdale']
filme = ['Jumanji', 'Your Name', '365 Days', 'Ready Player One', 'Passenger', 'Die Bestimmung 1', 'Die Bestimmung 2', 'Die Bestimmung 3', 'Run', 'The Silence']

@bot.command()
async def netflix(ctx, arg):
  if arg == 'serien':
    em=discord.Embed(title='Gute Netflix Serien 2022',
    description=f'Serie: {random.choice(serien)}',
    color=0xff790a)
    em.set_author(name='Sequence',icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    em.set_footer(text='.gg/7fx | >help')
    await ctx.send(embed=em)
  elif arg == 'filme':
    emb=discord.Embed(title='Gute Netflix Filme 2022',
    description='Film: {}'.format(random.choice(filme)),
    color=0xff790a)
    emb.set_author(name='Sequence',icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    emb.set_footer(text='.gg/7fx | >help')
    await ctx.send(embed=emb)
  elif arg == 'count':
    embe=discord.Embed(title='Netflix Serien & Filme',
    description='**Serien:** `{}`\n**Filme:** `{}`'.format(len(serien), len(filme)),
    color=0xff790a)
    embe.set_author(name='Sequence',icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    embe.set_footer(text='.gg/7fx | >help')
    await ctx.send(embed=embe)
  else:
      await ctx.send(':rage: Bitte gebe ein gültiges Argument an!')

@bot.command()
async def code(ctx):
    embe = discord.Embed(title='ER:LC Server Code',description='**Code:** `ulle`',color=0xff790a)
    embe.set_author(name='Sequence',icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    embe.set_footer(text='.gg/7fx | >help')
    await ctx.send(embed=embe)

@bot.command()
async def userinfo(ctx, member: discord.Member=None):
    if member == None:
        member = ctx.author

        embed = discord.Embed(title=f"Userinfo für {member.name}", description=f"Das ist die Userinfo von dem User {member.mention}.", color=0xff790a)
        embed.add_field(name='Discord Username', value=member.name)
        embed.add_field(name='Nickname', value=member.display_name)
        embed.add_field(name='ID', value=member.id)
        embed.add_field(name="Server beigetreten:", value=member.joined_at.strftime("%d/%m/%y, %H:%M:%S"))
        embed.add_field(name="Discord beigetreten:", value=member.created_at.strftime("%d/%m/%y, %H:%M:%S"))
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name=member.name, icon_url=member.avatar_url)
        embed.set_footer(text=f'Executed by {ctx.author}')
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f"Userinfo für {member.name}", description=f"Das ist die Userinfo von dem User {member.mention}", color=0xff790a)
        embed.add_field(name='Discord Username', value=member.name)
        embed.add_field(name='Nickname', value=member.display_name)
        embed.add_field(name='ID', value=member.id)
        embed.add_field(name="Server beigetreten:", value=member.joined_at.strftime("%d/%m/%y, %H:%M:%S"))
        embed.add_field(name="Discord beigetreten:", value=member.created_at.strftime("%d/%m/%y, %H:%M:%S"))
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name=member.name, icon_url=member.avatar_url)
        embed.set_footer(text='.gg/7fx | >help')
        await ctx.send(embed=embed)

wopfragen = ['Hast du schonmal etwas geklaut?', 'Mit wie viel Jahren wurdest du getauft?', 'Hast du viele Freunde?', 'Magst du deine Familie oder deine Freunde mehr?',
             'Bist du ein Einzelkind?', 'Was ist deine Lieblingsfarbe?', 'Was war dein letzter Traum an den du dich erinnerst?', 'Was war dein schönstes Date?',
             'Wonach hast du als letztes gegoogelt?', 'Von wem hast du deinen letzten Korb bekommen?', 'Welches ist dein aktuelles Lieblingslied?', 'Hast du schon mal eine Straftat begangen?',
             'Mit wem würdest du am liebsten einen Urlaub verbringen?', 'Was war dein schlimmstes Date?', 'Was ist das peinlichste, was du je gemacht hast?', 'Was hältst du für deine beste Eigenschaft? Und was ist die schlechteste?',
             'Verrate mir ein Geheimnis aus deiner Kindheit.', 'Was ist das Mutigste, das du je getan hast?', 'Wovon träumst du beim Schlafen am häufigsten?', 'Wenn du illegal dein Geld verdienen würdest, womit würdest du es verdienen?',
             'Womit kann man dich am meisten beeindrucken?', 'Was war der größte Fehler deines Lebens?', 'In wen warst du bis jetzt am heftigsten verknallt?', 'Was ist für dich der größte Abturner, den es gibt?',
             'Wen hast du schon mal vorgegeben zu mögen – obwohl du ihn/sie total doof findest? ', 'Hast du noch Gefühle für dein*n Ex?', 'Was kannst du bei einem Date gar nicht ab? ',
             'Wer ist deiner Meinung nach die Diva eurer Gruppe?', 'Schläfst du noch mit Kuscheltieren?']

@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def wop(ctx, member : discord.Member):

    def check(m):
        return m.author == member

    await ctx.send(':question: {} Möchtest du **Wahrheit oder Pflicht** spielen?\n(j)a (n)ein?'.format(member.mention))
    msg1 = await bot.wait_for('message', check=check)
    if msg1.author == member and msg1.channel == ctx.channel and msg1.content == 'j':
        await ctx.send('**Wahrheit oder Pflicht!** {}\n{}'.format(member.mention, random.choice(wopfragen)))
    else:
        return

    msg = await bot.wait_for('message', check=check)
    if msg.author == member and msg.channel == ctx.channel:
        await ctx.send('Okay, danke fürs mitspielen!')
    else:
        return

@bot.command()
async def suggestion(ctx, thema, *, besch):
    em=discord.Embed(title="{} - {}'s Vorschlag".format(thema, ctx.author.name),
                     description='{}'.format(besch),
                     color=0xff790a)
    em.set_author(name='Sequence',icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    em.set_footer(text='.gg/7fx | >help')
    mes = await ctx.send(embed=em)
    await mes.add_reaction('👍')
    await mes.add_reaction('👎')

@bot.command()
async def wuerfel(ctx):
    await ctx.send(':game_die: Du hast eine **{}** gewürfelt!'.format(random.randint(1, 6)))

@bot.command()
@commands.has_permissions(manage_messages=True)
async def announce(ctx, title,  *, desc):
    em=discord.Embed(title="{} - {}'s Ankündigung".format(title, ctx.author.name),
                     description='{}'.format(desc),
                     color=0xff790a)
    em.set_author(name='Sequence',icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    em.set_footer(text='.gg/7fx | >help')
    await ctx.send(embed=em)

@bot.command()
async def gaymeter(ctx, member: discord.Member=None):
    if member == None:
        member = ctx.author
        em=discord.Embed(title='Gayometer v1',
                     description=':rainbow_flag: {} ist zu {}% gay! :joy_cat:'.format(member.mention, random.randint(0, 100)),
                     color=0xff790a)
        em.set_author(name='Sequence',
                  icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
        em.set_footer(text='.gg/7fx | >help')
        em.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=em)
    else:
        emb = discord.Embed(title='Gayometer v1',
                           description=':rainbow_flag: {} ist zu {}% gay! :joy_cat:'.format(member.mention,
                                                                                            random.randint(0, 100)),
                           color=0xff790a)
        emb.set_author(name='Sequence',
                      icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
        emb.set_footer(text='.gg/7fx | >help')
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=emb)

@bot.command()
async def lovemeter(ctx, member: discord.Member, member2: discord.Member):
        em = discord.Embed(title='Loveometer v1',
                           description=':heart: {} und {} lieben sich zu {}% :flushed:!'.format(member.mention, member2.mention, random.randint(0, 100)),
                           color=0xff790a)
        em.set_author(name='Sequence',icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
        em.set_footer(text='.gg/7fx | >help')
        em.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=em)

@bot.command()
async def serverinfo(ctx):
    em=discord.Embed(title='Serverinfo von {}'.format(ctx.guild.name),
                     description='Dies ist die Serverinfo für {}'.format(ctx.guild.name),
                     color=0xff790a)
    em.set_author(name='Sequence',icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    em.set_footer(text='.gg/7fx | >help')
    em.set_thumbnail(url=ctx.guild.icon_url)
    em.add_field(name='Server Name', value=ctx.guild.name)
    em.add_field(name='Server ID', value=ctx.guild.id)
    em.add_field(name='Mitglieder', value=ctx.guild.member_count)
    em.add_field(name='Boosts', value=ctx.guild.premium_subscription_count)
    em.add_field(name='Nitro Level', value=ctx.guild.premium_tier)
    em.add_field(name='Beschreibung', value=ctx.guild.description)
    em.add_field(name='Erstellt am', value=ctx.guild.created_at)
    em.add_field(name='Owner', value=f'<@{ctx.guild.owner_id}>')
    await ctx.send(embed=em)

whoislist = ['Panda', 'Giraffe', 'Pikachu', 'Naruto', 'Sasuke', 'Berlin (Haus des Geldes)', 'Annabelle', 'Rio', 'Affe',
             'Hodenkobold', 'Mega Ritter', 'Ballon', 'Demogorgon', 'Chief Hopper', 'Don Hwon', 'Programmiersprache', 'Pekka',
             'Mini Pekka', 'Faultier', 'Moderator', 'Tier', 'Mensch', 'Monster', 'Pflanze', 'Persicher Adler', 'Bulgarischer Vogel',
             'Mexikanischer Dealer', 'Random', 'Hund', 'Katze', 'Mind Flayer', 'Joe', 'Mama', 'Papa', 'Deine Mutter', 'Lucio',
             'Rapper',' Hybrid', 'Fortnite Battlepass']

@bot.command()
async def whois(ctx, member : discord.Member=None):
    if member == None:
        member = ctx.author
        em=discord.Embed(title='Wer bin ich..?',
                     description=random.choice(whoislist),
                     color=0xff790a)
        em.set_author(name=member.name,
              icon_url=member.avatar_url)
        em.set_footer(text='.gg/7fx | >help')
        em.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=em)
    else:
        emb = discord.Embed(title='Wer bin ich..?',
                       description=random.choice(whoislist),
                       color=0xff790a)
        emb.set_author(name=member.name,
                  icon_url=member.avatar_url)
        emb.set_footer(text='.gg/7fx | >help')
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=emb)

@bot.command()
async def invite(ctx):
    em=discord.Embed(title='Hauptdiscord',
                     description='💞 **1k+ Member!**\nhttps://discord.gg/7fx :)',
                     color=0xff790a)
    em.set_author(name='Sequence',
               icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    em.set_footer(text='.gg/7fx | >help')
    await ctx.send(embed=em)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member, *, reason):
    em=discord.Embed(title='Warn #{}'.format(member.name),
                     description='Das Mitglied {} wurde verwarnt!\n**Grund:** {}'.format(member.mention, reason),
                     color=0xff790a)
    em.set_author(name='Sequence',
               icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    em.set_footer(text='.gg/7fx | >help')
    await ctx.send(embed=em)

@bot.command()
async def affenpocken (ctx):
    await ctx.send('Hat <@723977115342602331>')

@bot.command()
async def quiz(ctx):

    def check(m):
        return m.channel ==  ctx.channel

    await ctx.send(':question: **Welches Quiz soll ich starten?**\n\n:one: | Gameboy\n:two: | Monalisa')
    time1 = await bot.wait_for('message', check=check)

    if time1.content == '1':
        await ctx.send('Wann wurde der erste Gameboy erbaut?\n\n:one: | 1989\n:two: | 1992\n:three: | 1976')
        time2 = await bot.wait_for('message', check=check)
    else:
        ctx.send(':rage: Bitte gebe 1 oder 2 an!')

    if time2.content == '1':
        await ctx.send('Richtig, versuch nun ein anderes quiz!')
        return
    elif time2.content == '2':
        await ctx.send('Falsch, arbeite mehr an deinem Allgemeinwissen!')
        return
    elif time2.content == '3':
        await ctx.send('Falsch, arbeite mehr an deinem Allgemeinwissen!')
        return
    else:
        await ctx.send('Bitte gebe entweder :one:, :two: oder :three: an!')
        return

    await ctx.send('Wann wurde die Monalisa gemalt?\n\n:one: | 1989\n:two: | 1992')

    if time1.content == '2':
        time1 = await bot.wait_for('message', check=check)
    else:
        ctx.send(':rage: Bitte gebe 1 oder 2 an!')

    time3 = await bot.wait_for('message', check=check)

    if time3.content == '1':
        await ctx.send('Richtig, versuch nun ein anderes quiz!')
    elif time3.content == '2':
        await ctx.send('Falsch, arbeite mehr an deinem Allgemeinwissen!')
    else:
        await ctx.send('Bitte gebe entweder :one: oder :two: an!')

pps = ['8=D', '8==D', '8===D', '8====D', '8=====D', '8======D', '8=======D', '8========D',
       '8==========D', '8===========D', '8============D']

@bot.command()
async def pp(ctx, member: discord.Member=None):
    if member == None:
        member = ctx.author
        em=discord.Embed(title='PP Size',
                         description="{}'s PeePee:\n{}".format(member.mention, random.choice(pps)),
                         color=0xff790a)
        em.set_author(name='Sequence',
                      icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
        em.set_footer(text='.gg/7fx | >help')
        em.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=em)
    else:
        emb = discord.Embed(title='PeePee Size',
                           description="{}'s PeePee:\n{}".format(member.mention, random.choice(pps)),
                           color=0xff790a)
        emb.set_author(name='Sequence',
                      icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
        emb.set_footer(text='.gg/7fx | >help')
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=emb)

@bot.command()
async def slap(ctx, member : discord.Member=None):
    em=discord.Embed(title='{} wurde geslapped!'.format(member.display_name),
                     description='🤚 Das Mitglied {} hat {} geschlagen, RIP BOZO :joy_cat:'.format(ctx.author.mention, member.mention),
                     color=0xff790a)
    em.set_author(name='Sequence',icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    em.set_footer(text='.gg/7fx | >help')
    em.set_image(url='https://c.tenor.com/yJmrNruFNtEAAAAC/slap.gif')
    await ctx.send(embed=em)

@bot.command()
async def kiss(ctx, member : discord.Member=None):
    em=discord.Embed(title='{} hat {} geküsst!'.format(ctx.author.name, member.name),
                     description='💞 Das Mitglied {} hat {} geküsst! Cute 💘'.format(ctx.author.mention, member.mention),
                     color=0xff790a)
    em.set_author(name='Sequence',icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    em.set_footer(text='.gg/7fx | >help')
    em.set_image(url='https://c.tenor.com/wPzIJLI3IeQAAAAC/kiss-hot.gif')
    await ctx.send(embed=em)

@bot.command()
async def hug(ctx, member : discord.Member=None):
    em=discord.Embed(title='{} hat {} umarmt!'.format(ctx.author.name, member.name),
                     description='💞 Das Mitglied {} hat {} umarmt! Cute 💘'.format(ctx.author.mention, member.mention),
                     color=0xff790a)
    em.set_author(name='Sequence',icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    em.set_footer(text='.gg/7fx | >help')
    em.set_image(url='https://c.tenor.com/OXCV_qL-V60AAAAC/mochi-peachcat-mochi.gif')
    await ctx.send(embed=em)


@bot.command()
async def kos(ctx, member : discord.Member):

    def check(m):
        return m.author == member

    await ctx.send(':kiss: {} Würdest du {} **(K)issen** oder **(S)lappen**?'.format(member.mention, ctx.author.mention))
    msg1 = await bot.wait_for('message', check=check)
    if msg1.author == member and msg1.channel == ctx.channel and msg1.content == 'K':
        await ctx.send('{} Du wurdest von {} geküsst, ulala! 💘'.format(ctx.author.mention, member.mention))
    elif msg1.author == member and msg1.channel == ctx.channel and msg1.content == 'S':
        await ctx.send('{} Du wurdest von {} geslapped, F BOZO! 🤡'.format(ctx.author.mention, member.mention))
    else:
        return

Start = ['sweaty', 'rainy', 'drilla', 'trigger', 'glock', 'freezed', 'razer', 'lean', 'may',
'dev', 'haunted', 'gen', 'really', 'fr', 'fx', 'slava', 'dynamic', 'slice', 'traced', 'epic',
'boolean', 'ideal', 'undefined', 'dead', 'right']

End = ['grave', 'proof', 'west', 'forest', 'fluid', 'project', 'supreme', 'ukraini', 'dev',
'stranger', 'erase', 'rend', 'ridical', 'angle', 'tribe', 'frozen', 'defined', 'razor', 'synapse',
'log', 'dreamer', 'indeed', 'bash']

@bot.command()
async def usernamegen(ctx):
    em=discord.Embed(title=':no_entry: Username Generator',
                     description='Generiere einen Benutzernamen für {}...'.format(ctx.author.mention),
                     color=0xff790a)
    em.add_field(name='Benutzername', value=random.choice(Start) + random.choice(End))
    em.set_author(name='Sequence',
                  icon_url='https://cdn.discordapp.com/avatars/982276578094501938/91e2e67e72f04ae099b1ac3654024229.png?size=4096')
    em.set_footer(text='.gg/7fx | >help')
    await ctx.send(embed=em)

from config import TOKEN
bot.run(TOKEN)
