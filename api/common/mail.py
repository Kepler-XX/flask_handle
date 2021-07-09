import smtplib
from email.mime.text import MIMEText

FROMADDR = ''
PASSWORD = ''


def send_mail(content, toaddr, subject=''):
    """
    发送邮件
    @param subject: 邮件主题
    @param content: 邮件内容
    @param toaddr: 接收邮箱账号列表，群发
    @return:
    """
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = subject
    message['From'] = FROMADDR
    try:
        server = smtplib.SMTP_SSL('smtp.yeah.net', 465)
        server.login(FROMADDR, PASSWORD)
        server.sendmail(FROMADDR, toaddr, message.as_string())
        server.quit()
        return True
    except Exception as e:
        return False


if __name__ == '__main__':
    res = send_mail('girl is god', ['', ''])
    print(res)
