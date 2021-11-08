import smtplib
import os
import mimetypes
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

i = str(input('Введите ID ученика '))

x = True
while x == True:
    # Проверка наличия ID
    try:
        text_file = open('bin/users/user_' + str(i) + '.txt', 'r') # Попытка открытие файла с данными
    except FileNotFoundError:
        os.system('cls')
        i = str(input('Ученика с таким ID нет. Пожалуйста, введите корректный номер '))
    else:
        x = False

addr_from = 'email'  # Адресат
password = 'password'  # Пароль
addr_to = str(input('Введите Ваш email: '))  # Получатель

msg = MIMEMultipart()  # Создаем сообщение
msg['From'] = addr_from  # Адресат
msg['To'] = addr_to  # Получатель
msg['Subject'] = 'Данные ученика с ID ' + i  # Тема сообщения

body = 'Полная информация об ученике с ID ' + i  # Текст сообщения
msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст

filepath = 'bin/users/user_' + i + '.txt'  # Имя файла в абсолютном или относительном формате
filename = os.path.basename(filepath)  # Только имя файла

ctype, encoding = mimetypes.guess_type(filepath)  # Определяем тип файла на основе его расширения
maintype, subtype = ctype.split('/', 1)  # Получаем тип и подтип

with open(filepath) as fp:  # Открываем файл для чтения
    file = MIMEText(fp.read(), _subtype=subtype)  # Используем тип MIMEText
    fp.close()  # После использования файл обязательно нужно закрыть

file.add_header('Content-Disposition', 'attachment', filename=filename)  # Добавляем заголовки
msg.attach(file)  # Присоединяем файл к сообщению

server = smtplib.SMTP('smtp.mail.ru', 587)  # Создаем объект SMTP
server.starttls()  # Начинаем шифрованный обмен по TLS
server.login(addr_from, password)  # Получаем доступ
server.send_message(msg)  # Отправляем сообщение
server.quit()  # Выходим
