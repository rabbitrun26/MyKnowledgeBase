import subprocess

def sync_with_bat():
    subprocess.run(["C:\\MyKnowledgeBase\\backup.bat"], check=True)

if __name__ == "__main__":
    sync_with_bat()

