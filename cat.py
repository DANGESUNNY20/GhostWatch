from flask import Flask, jsonify, render_template_string
import subprocess
import threading

app = Flask(__name__)

# Store the most recent 500 logs to prevent memory overload
live_logs = []

def run_bash_script():
    while True:
        # Executes the real Linux SOC script
        process = subprocess.Popen(
            ['bash', 'collect_logs_2.sh'], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT, 
            text=True
        )
        
        current_category = "SYSTEM"
        
        for line in iter(process.stdout.readline, ''):
            line = line.strip()
            if not line:
                continue
                
            # Detect categories from the bash script output
            if "[+] ERROR" in line: current_category = "ERROR"
            elif "[+] WARNING" in line: current_category = "WARNING"
            elif "[+] SSH" in line: current_category = "SSH"
            elif "[+] SUDO" in line: current_category = "SUDO"
            elif "[+] AUTH" in line or "[+] PAM" in line or "FAILED PASSWORD" in line: current_category = "AUTH"
            elif "[ALERT]" in line: current_category = "ALERT"
            
            # Ignore ANSI color codes and borders
            elif not line.startswith("\033[") and not line.startswith("="):
                import datetime
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                live_logs.append({
                    "timestamp": timestamp,
                    "type": current_category,
                    "process": "system",
                    "message": line
                })
                
                if len(live_logs) > 500:
                    live_logs.pop(0)
                    
        process.wait()

@app.route('/')
def index():
    # Serve the frontend HTML
    with open('index.html', 'r') as f:
        return render_template_string(f.read())

@app.route('/api/logs')
def get_logs():
    return jsonify(live_logs)

if __name__ == '__main__':
    # Start the log collector in a background thread
    threading.Thread(target=run_bash_script, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
