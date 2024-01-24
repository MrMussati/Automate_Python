import os
import time

## color
yellow = '\033[1;33m'
green = '\033[1;32m'
white = '\033[1;37m'

##  apresentar o chatbot

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(green + f'{os.linesep}{nome}, CBD will not get you high in any quantity or dose because it is not psychotropic. Psychotropic simply means a psychoactive effect that has intoxicating qualities. THC, which is another compound found in cannabis, is the compound responsible for the psychotropic effects associated with hemp and cannabis, and you won’t find it above 0.0% in Vitality CBD products..{os.linesep}' + white)

        time.sleep(1)
        

  
    elif resposta == '2':
        print (green + f'{os.linesep}{nome}, We’re proud to say that none of our CBD products are tested on animals and are completely cruelty free. This includes all of our CBD oils and even our premium CBD creams in the Infused range. Our Infused CBD range and other topicals are still completely safe and suitable for use on even the most sensitive skin and without any animal testing.{os.linesep}'+ white)
    

        time.sleep(1)
        



    elif resposta == '3':
        print(green + f'{os.linesep}{nome},Based on our own research and listening to customers, the most satisfied users took a 70mg dose for 21 days straight. Consistency is key to CBD, so give it a go for 21 days; if you are still unsure then contact our CBD mentors who will be happy to advise you further.{os.linesep}' + white)

        time.sleep(1)
        


    elif resposta == '4':
        print(green + f'{os.linesep}{nome}, Daily dose is the most important factor when considering satisfaction with CBD, rather than the strength of the CBD oil. Our most satisfied customers take 70mg daily consistently over the course of 21 days or more. For this reason, we recommend using a 2400mg or 4800mg CBD oil as this gives you 34 or 64 daily doses, respectively. {os.linesep}'+ white)

        time.sleep(1)
        


    elif resposta == '5': 
        print(green + f'{os.linesep}{nome}, Always speak to your doctor before taking CBD alongside any medication. Even though CBD can’t be discussed in relation to medicinal properties due to its current legal status, it still interacts with the human body in ways which need to be considered.The most significant manner in which CBD needs to be considered in relation to medication is its inhibition of the enzyme P450. Essentially, this means that certain medications arent able to be metabolised as fast as before, so you’ll need to be a little more careful with your dosages. If that sounds concerning, bear in mind that it’s the exact same effect that grapefruit has on your enzymes. That’s why certain medication will advise you to not eat grapefruit whilst taking it. In fact, you can use that as a good baseline to know whether it’s advisable to take CBD with it. By inhibiting the production of P450, the most widespread effect is that certain drugs and medication will linger in the bloodstream longer. Since this is difficult to predict with any precision, it’s best to check with your doctor about any potential interactions.{os.linesep}' + white)
        
        time.sleep(1)
        
    else:
        print(white + 'Just Type only 1,2,4 and 5 ')    


def start():
    ##  apresentar o chatbot
    print(white + 'Hi! Welcome to INSANA FLOR CHAT')    
    
    ## pedir o email 
    nome = input (white + 'Type your name:')


    ## pedir o email 
    email = input (white + 'Type your email:')

    while True :
        ## oferecer o menu de opcoes 
        resposta = input ( f'What would you like to know today?{os.linesep}[1] - Will CBD get me high?{os.linesep}[2] - Are CBD products tested on animals?{os.linesep}[3] - I have been using CBD for a week now, why is it not working?{os.linesep}[4] - What strength CBD would you recommend?{os.linesep}[5] - Can I use CBD with medication?{os.linesep}----- INSANA FLOR CHAT ------{os.linesep}' )
        # Processar a resposta enviada
        processar_resposta(resposta, nome)
        
        time.sleep(1)

if __name__ == '__main__':
    start()
