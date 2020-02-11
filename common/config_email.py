# coding=utf-8

import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime
import threading
import zipfile
import glob
import read_config as readconfig
from common.ReportHelper import MyRh



# ======== Reading web_config.ini setting ===========
localReadConfig = readconfig.ReadConfig()


class Email:
    def __init__(self):
        global host, user, password, port, sender, title, content

        host = localReadConfig.get_email("mail_host")
        user = localReadConfig.get_email("mail_user")
        password = localReadConfig.get_email("mail_pass")
        port = localReadConfig.get_email("mail_port")
        sender = localReadConfig.get_email("sender")
        title = localReadConfig.get_email("subject")
        content = localReadConfig.get_email("content")
        host = localReadConfig.get_email("mail_host")


        # 获取收件人列表
        self.value = localReadConfig.get_email("receiver")
        self.receiver = []
        for i in str(self.value).split("/"):
            self.receiver.append(i)

        # 定义邮件主题
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = "接口测试报告" + "" + date

        self.rh = MyRh.get_Rh()
        self.msg = MIMEMultipart('related')

    def config_header(self):
        '''
        定义邮件头，包括主题，发件人和收件人
        :return:
        '''
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)

    def config_content(self):
        '''
        邮件内容
        :return:
        '''
        f = open(os.path.join(readconfig.base_dir, 'support', 'emailStyle.txt'))
        content = f.read()
        f.close()
        content_plain = MIMEText(content, 'html', 'UTF-8')
        self.msg.attach(content_plain)
        self.config_image()

    def config_image(self):
        '''
        构造图片链接，配置邮件内容中使用的图像
        :return:
        '''
        image_path = os.path.join(readconfig.base_dir, 'support', 'LOGO-CF.png')
        fp = open(image_path, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # defined image id
        msgImage.add_header('Content-ID', '<image>')
        self.msg.attach(msgImage)

    def config_file(self):
        '''
        配置邮件附件
        :return:
        '''

        # if the file content is not null, then config the mail file
        if self.check_file():

            report_path = self.rh.get_result_path()
            zip_path = os.path.join(readconfig.base_dir, "result", "test_report.zip")

            # zip file
            files = glob.glob((report_path + '/*').replace("\\", "/"))
            f = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
            for file in files:
                # 修改压缩文件的目录结构
                f.write(file, '/report/'+os.path.basename(file))
            f.close()

            report_file = open(zip_path, 'rb').read()
            file_html = MIMEText(report_file, 'base64', 'utf-8')
            file_html['Content-Type'] = 'application/octet-stream'
            file_html['Content-Disposition'] = 'attachment; filename="test_report.zip"'
            self.msg.attach(file_html)

    def check_file(self):
        '''
        检查测试报告
        :return:
        '''
        report_path = self.rh.get_report_path()
        if os.path.isfile(report_path) and not os.stat(report_path) == 0:
            return True
        else:
            return False

    def send_email(self):
        """
        发送邮件
        :return:
        """
        self.config_header()
        self.config_content()
        self.config_file()
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.starttls()
            smtp.ehlo()
            smtp.login(user, password)
            smtp.sendmail(sender, self.receiver, self.msg.as_string())
            smtp.quit()
        except Exception as ex:
            print ex


class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():

        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email


if __name__=="__main__":
    email = MyEmail.get_email()
    email.config_file()








