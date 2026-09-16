from datetime import datetime

def log_run():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"Run executed at: {now}\n"
    
    with open("log.txt", "a") as f:
        f.write(entry)
        
    print(f"Logged: {entry.strip()}")

if __name__ == "__main__":
    log_run()