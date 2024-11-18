from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

# Path to your Streamlit script
STREAMLIT_APP_PATH = "path_to_streamlit_app.py"

@app.route("/")
def home():
    # Render an HTML template with an iframe to the Streamlit app
    return render_template("index.html")  # You'll create this template in Step 3

def run_streamlit():
    """Run the Streamlit app in a subprocess with network accessibility."""
    # Modify the command to allow external network access (0.0.0.0)
    streamlit_command = f"streamlit run {STREAMLIT_APP_PATH} --server.port=8501 --server.address=0.0.0.0"
    subprocess.Popen(streamlit_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == "__main__":
    # Run the Streamlit app as a subprocess
    run_streamlit()
    # Start Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)  # Listen on all network interfaces (0.0.0.0)
