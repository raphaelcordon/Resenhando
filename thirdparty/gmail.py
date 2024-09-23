from email.message import EmailMessage
from smtplib import SMTP_SSL


class EmailPassword:
    def __init__(self, email_address, name, password):
        msg = EmailMessage()
        msg['Subject'] = 'Resenhando, reset de senha'
        msg['From'] = 'Resenhando'
        msg['To'] = email_address
        msg.set_content(f"Olá {name}, aqui é do time da Resenhando.\n\n"
                        f"Sua nova senha é '{password}'.\n "
                        f"Ao se logar no site você será redirecionado para alterá-la.\n\n"
                        f"Esperamos vê-lo em breve para novas resenhas. :)\n\n"
                        f"http://resenhando.herokuapp.com")

        with SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('cordonraphael@gmail.com', 'gkbucljtatzgjlbm')
            smtp.send_message(msg)

# piuxeaxjwrqifhcw
