import smtplib
from email.mime.text import MIMEText

class SendMail:
    global send_user, from_addr, from_addr_password, to_addr, smtp_server, server_port
    send_user = "925795403@qq.com"
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '925795403@qq.com'
    from_addr_password = 'pjdwrojzmtwrbcbd'

    # 收信方邮箱
    to_addr = 'zhixiao.liang@fanli.com'
    reciver_list = ["zhixiao.liang@fanli.com", "136388682@qq.com"]

    # 发信服务器
    smtp_server = 'smtp.qq.com'
    server_port = 465

    def send_mail(self, reciver_list, subject, content):
        user = "python发件人:<" + from_addr + ">"
        msg = MIMEText(content, _subtype='plain', _charset='utf-8')
        # 邮件标题
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addr
        # msg['To'] = ';'.join(reciver_list)

        try:
            send_server = smtplib.SMTP_SSL(smtp_server, server_port)  # 邮件服务器及端口号
            send_server.login(from_addr, from_addr_password)
            send_server.sendmail(from_addr, to_addr, msg.as_string())
            print("发送成功")
        except send_server.SMTPException as e:
            print("发送失败")
        finally:
            send_server.close()


if __name__ == '__main__':
    test = SendMail()
    test.send_mail('', 'test', 'testestset')