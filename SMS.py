import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
	}

def sendMessage():

    email = os.getenv('google_email')
    pw = os.getenv('google_pw')
    cell = os.getenv('cell_number')
    sms_gateway = f'{cell}{carriers["tmobile"]}'
    smtp = "smtp.gmail.com"
    port = 587

    # This will start our email server
    server = smtplib.SMTP(smtp,port)
    # Starting the server
    server.starttls()
    # Now we need to login
    server.login(email,pw)

    """
    Create message
    """
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    # Make sure you add a new line in the subject
    msg['Subject'] = "3080 Live TEST \n"
    # Make sure you also add new lines to your body
    body = "BUY THE DIP \n www.gamestop.com/video-games/pc/components/graphics-cards/products/geforce-rtx-3080-10-gb-gddr6x-strix-graphic-card/11112926.html?condition=New"
    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(body, 'plain'))
    sms = msg.as_string()
    server.sendmail(email,sms_gateway,sms)
    # lastly quit the server
    server.quit()
