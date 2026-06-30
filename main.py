import subprocess

print("=" * 50)
print("KFQ ISCC AutoReporter")
print("=" * 50)

print("1. Downloading latest ISCC data...")
subprocess.run(["py", "downloader.py"], check=True)

print("2. Creating report...")
subprocess.run(["py", "report.py"], check=True)

print("3. Sending email...")
subprocess.run(["py", "mail.py"], check=True)

print("=" * 50)
print("All tasks completed successfully!")
print("=" * 50)