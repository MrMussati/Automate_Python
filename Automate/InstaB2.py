#importar as biblioteca
from instabot import Bot, utils
import time

bot = Bot()
bot.login(username=" dailyofgrow@gmail.com", password=" Cannabis1533") 
time.sleep = 5
# coletar o nome das pessaos que voce segue mas te seguem de volta 
file = utils.file("followers.txt")

non_followers = set(bot.following) - set(bot.followers) - set(bot.friends)
non_followers = list(non_followers)
non_followers_names = []


for user in non_followers:
    non_followers_names.append(bot.get_username_from_user_id(user)) 
    non_followers_names.append(non_followers_names)
    print(non_followers_names)
    bot.small_delay()



    #salvar nun text
file.save_list(non_followers_names, "non_followers.txt")


time.sleep(5)   

bot.upload_photo("C:/Users/Usuario/Desktop/Python/Automation_project/IMG_20210909_155544.jpg", caption="Teste de automação com python") 

