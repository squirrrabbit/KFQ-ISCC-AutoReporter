import smtplib
from email.message import EmailMessage
from config import *

# report.py에서 생성한 엑셀 파일
EXCEL_FILE = "ISCC_Korea_Report.xlsx"

# report.py에서 생성한 HTML 읽기
with open("summary.html", "r", encoding="utf-8") as f:
    html_body = f.read()

msg = EmailMessage()

msg["Subject"] = "[KFQ] ISCC Korea Weekly Report"
msg["From"] = WORKS_EMAIL
msg["To"] = "hjkwon@kfq.or.kr, jypark@kfq.or.kr"

# HTML 메일
msg.set_content("HTML을 지원하는 메일 프로그램에서 확인해주세요.")
msg.add_alternative(html_body, subtype="html")

# 엑셀 첨부
with open(EXCEL_FILE, "rb") as f:
    msg.add_attachment(
        f.read(),
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=EXCEL_FILE
    )

# 메일 발송
with smtplib.SMTP_SSL("smtp.worksmobile.com", 465) as smtp:
    smtp.login(WORKS_EMAIL, WORKS_PASSWORD)
    smtp.send_message(msg)

print("메일 발송 완료!")