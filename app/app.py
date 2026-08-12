from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
	<h1>🚀 DevOps Showcase App</h1>
        <p>Deployed using Docker + Ansible + GitHub Actions</p>
    	<p>Built by: Omkar Bachche</p>
    	<p>Version 2.0 - Auto Deployed! 🎉</p>
    	'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
