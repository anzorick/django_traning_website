import requests



token = '5632017300:AAEcljLU0CpgYMQ7G3rhoNcKve7QEa5GAJo'
chat_id = '-851492043'
text = 'Test_2'



def sendTelegram():
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text
        })

sendTelegram()    
