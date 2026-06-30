import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# 이메일 설정
SMTP_SERVER = 'smtp.example.com'  # SMTP 서버 주소 (예: smtp.gmail.com)
SMTP_PORT = 587  # SMTP 포트 (예: 587)
USERNAME = ''  # 'squirrrabbit@gmail.com'
PASSWORD = 'kqxq mwap upvh oacc'  # 여러분의 이메일 비밀번호

# 인증서 발급 현황 다운로드 함수
def download_iscc_data():
    # 여기에 다운로드 로직 추가
    response = requests.get('https://iscc-system.org/certification/iscc-documents/')  # 실제 데이터 URL로 변경
    if response.status_code == 200:
        return response.json()  # JSON 데이터 반환
    return None

# 이메일 전송 함수
def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = USERNAME
    msg['To'] = 'squirrrabbit@gmail.com, hjkwon@kfq.or.kr'  # 수신자 이메일 주소

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(USERNAME, PASSWORD)
        server.send_message(msg)

# 메인 실행 로직
def main():
    iscc_data = download_iscc_data()
    if iscc_data:
        # 발급 현황과 만료일을 확인하여 이메일 내용 구성
        subject = "ISCC 인증서 발급 현황"
        body = "발급 현황:\n\n"
        
        # 인증서 데이터 가공 (예시: 발급 상태 출력)
        for certificate in iscc_data:
            if certificate['status'] == 'issued' and certificate['expiration_date'] < (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'):
                body += f"인증서 ID: {certificate['id']}, 만료일: {certificate['expiration_date']}\n"
        
        # 이메일 보내기
        send_email(subject, body)

# 스케줄링 로직 (예: 매주 또는 2주마다 실행)
if __name__ == "__main__":
    main()