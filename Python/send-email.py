# 寄送 Email 的程式
# 準備訊息物件設定
import email.message
msg=email.message.EmailMessage()
msg["From"]="a107221202@mail.shu.edu.tw"
msg["To"]="u10807001@go.utaipei.edu.tw"
msg["Subject"]="黃魚腥味"
# 寄送純文字的內容
msg.set_content("請尊重，你才沒內涵")
# 寄送比較多種式的內容(html)
# msg.add.alternative("<ch3>")優惠券</h3>滿五百送一百",subtype="html")
# 連線到 SMTP Sever. 驗證寄件人身分發送郵件
import smtplib
sever=smtplib.SMTP_SSL("smtp.gmail.com",465)
sever.login("u10807001@go.utaipei.edu.tw","N226126352")
sever.send_message(msg)
sever.close()