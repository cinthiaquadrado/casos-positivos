import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Supondo que você já tenha os resultados do join em 'casos_existentes'
casos_existentes = [
    {'grupo_assunto': 'Grupo A', 'numero_casos': 10},
    {'grupo_assunto': 'Grupo B', 'numero_casos': 5}
    # ... outros casos existentes ...
]

# Preparar os dados para o e-mail
email_body = "Casos existentes:\n"
for caso in casos_existentes:
    email_body += f"Grupo de Assunto: {caso['grupo_assunto']}, Número de Casos: {caso['numero_casos']}\n"

# Configurar informações de e-mail
sender_email = 'seu_email@gmail.com'
receiver_email = 'destinatario@email.com'
subject = 'Casos Existentes no Join do Alteryx'
body = email_body

# Configurar servidor SMTP do Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'seu_email@gmail.com'
smtp_password = 'sua_senha'

# Configurar e enviar o e-mail
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("E-mail enviado com sucesso!")
except Exception as e:
    print("Erro ao enviar o e-mail:", e)
finally:
    server.quit()
