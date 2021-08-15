import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

import read_file

metaConf = read_file.getMetaConfig()
[receivers, attachmentNames] = read_file.readReceiversByExecl()
# 设置登录及服务器信息
mail_host = metaConf['host']
mail_username = metaConf['username']
# 密码(部分邮箱为授权码)
mail_password = metaConf['password']
sender = metaConf['username']
# receivers = ['18217023823@163.com', '782216385@qq.com']



# 添加一个 txt 文件附件
# with open('assets/files/abc.txt', 'r') as h:
#     content2 = h.read()
# # 设置 txt 参数
# part2 = MIMEText(content2, 'plain', 'utf-8')
# # 附件设置内容类型，方便起见，设置为二进制流
# part2['Content-Type'] = 'application/octet-stream'
# # 设置附件头，添加文件名
# part2['Content-Disposition'] = 'attachment;filename="abc.txt"'

# 添加一个 execl 文件附件
# with open('assets/files/receivers.xlsx', 'rb') as h:
#     xlsxContent = h.read()
# # 设置 txt 参数
# attachmentXlsx = MIMEText(xlsxContent, 'base64', 'utf-8')
# # 附件设置内容类型，方便起见，设置为二进制流
# attachmentXlsx['Content-Type'] = 'application/octet-stream'
# # 设置附件头，添加文件名
# attachmentXlsx['Content-Disposition'] = 'attachment;filename="receivers.xlsx"'

# # 添加照片附件
# with open('assets/files/1.jpg', 'rb') as fp:
#     picture = MIMEImage(fp.read())
#     # 与 txt 文件设置相似
#     picture['Content-Type'] = 'application/octet-stream'
#     picture['Content-Disposition'] = 'attachment;filename="1.jpg"'

def main_email(receiver):
	# 设置 email 信息
	# 添加一个 MIMEMultipart 类，处理正文及附件
	message = MIMEMultipart()
	message['From'] = sender
	message['To'] = receiver
	# message['To'] = receivers[0]
	# 设置标题
	with open('assets/title.txt', 'r') as f:
		message['Subject'] = f.read()

	# 添加主体内容
	with open('assets/main.txt', 'r') as f:
		content = f.read()
	main = MIMEText(content, 'plain', 'utf-8')

	# # 将内容附件到邮件主体中
	message.attach(main)
	return message

def add_excel(emailMultipart, name):
	with open('assets/files/'+name, 'rb') as h:
		xlsxContent = h.read()
	# 设置 txt 参数
	xlsx = MIMEText(xlsxContent, 'base64', 'utf-8')
	# 附件设置内容类型，方便起见，设置为二进制流
	xlsx['Content-Type'] = 'application/octet-stream'
	# 设置附件头，添加文件名
	xlsx['Content-Disposition'] = 'attachment;filename='+name
	emailMultipart.attach(xlsx)


# # 将内容附件到邮件主体中
# message.attach(email_main)
# message.attach(attachmentXlsx)
# message.attach(picture)

if __name__ == '__main__':
	# 登录并发送
	try:
		# smtpObj = smtplib.SMTP() # 非 ssl 使用 port=25
		# smtpObj.connect(mail_host, 25)
		smtpObj = smtplib.SMTP_SSL(mail_host, 465)
		# smtpObj.set_debuglevel(1)
		smtpObj.login(mail_username, mail_password)
		for idx, receiver in enumerate(receivers):
			file_name = attachmentNames[idx]
			msg = main_email(receiver)
			add_excel(msg, file_name)
			smtpObj.sendmail(sender, receiver, msg.as_string())
		
		print('success')
		smtpObj.quit()
	except smtplib.SMTPException as e:
		print('error', e)

# https://segmentfault.com/a/1190000019773700