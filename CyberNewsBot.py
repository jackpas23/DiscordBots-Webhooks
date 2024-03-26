import requests
from bs4 import BeautifulSoup
import os
import discord
from dotenv import load_dotenv
from discord.ext import tasks
import nltk
import emoji
nltk.download('punkt')
#from nltk.tokenize import sent_tokenize
load_dotenv()
TOKEN = ('INPUT YOUR TOKEN')

GUILD = ('INPUT YOUR GUILD')
intents = discord.Intents.default()
intents.members = True 
intents.message_content = True
intents.messages = True
client = discord.Client(intents=intents)


@client.event
##triggers event
async def on_ready():
    myloop.start()
    
@tasks.loop(hours=4)
async def myloop():
    URL="https://thehackernews.com/"
    page=requests.get(URL)
    soup = BeautifulSoup(page.content,"html.parser")
    results = soup.find_all("div", class_="body-post clear")
    #URLs = soup.find_all("a", class_="story-link")
    #print(results)
    #titles=results.find_all("h2", class_="home-title")
    #print(results.prettify())
    for story in results:
        channel = client.get_channel(1207853113189339236)
        title_element=story.find("h2", class_="home-title")
        genre_element=story.find("span", class_="h-tags")
        desc_element=story.find("div", class_="home-desc")
        img_element=story.find("img",class_="home-img-src")
        #print(img_element)
        if img_element and img_element.has_attr('data-src'):
            img_url = img_element['data-src']
        else:
            img_url = None  # or a default image URL
        desc_text = desc_element.get_text(separator=' ').strip()
        description = nltk.tokenize.sent_tokenize(desc_text, language='english')
    
# Format the description
        if len(description) >= 2:
            formatted_description = f"{description[0]}{description[1]}"
        else:
            # Handle case where there's only one sentence or none
            formatted_description = '\n'.join(description)
        
        hyperlink_element=story.find("a", class_="story-link",)
        #print(hyperlink_element)
        link = hyperlink_element["href"] if hyperlink_element else "No link available"
        embed = discord.Embed(
            title=f"{emoji.emojize(':desktop_computer:')}{'  '}{title_element.text.strip()}{'  '}{emoji.emojize(':desktop_computer:')}",
            description=f"{'## '}{genre_element.text.strip()}\n\n*{formatted_description}*",
            url=link,  # This is the link you want to display.
            color=0x00ff00
        )
        embed.add_field(name="Learn More", value=f"[CLICK HERE TO LEARN MORE]({link})")
        embed.set_thumbnail(url=link)  # Optional: if you have a specific thumbnail image
        embed.set_image(url=img_url)
        #retStr = str("""```css\nThis is some colored Text```""")
        
        try:
            await channel.send(embed=embed)
        except Exception as e:
            print(f"An error occurred while sending the message: {e}")

        
       
        # print(title_element.text.strip())
        # print(link,'\n')
        # print(genre_element.text.strip(),'\n')
        # print(desc_element.text.strip(),'\n')
        # bot.py
    #channel = client.get_channel(1207853113189339236)    
   # await channel.send(title_element.text.strip())
    #print(title_element.text.strip())
    #print(genre_element.text.strip())
    #print(desc_element.text.strip())
    #print(link)

    @client.event
    async def on_error(event, *args, **kwargs):
        with open('err.log','a') as f:
            if event =='on_message':
                f.write(f'Unhandeled message: {args[0]}\n')
            else:
                raise

client.run(TOKEN)
