from flask import Flask, make_response, request, render_template
import requests
import os

app = Flask(__name__)

FLAG = os.getenv("FLAG") 
FAKE = os.getenv("FAKE")

@app.route('/', methods=['GET', 'POST', 'HEAD', 'TRACE', 'OPTIONS', 'PUT', 'DELETE', 'PATCH', 'CONNECT', 'LINK', 'UNLINK', 'PURGE', 'LOCK', 'UNLOCK', 'PROPFIND', 'VIEW', 'FLAG'])
def index():
    if request.method == 'GET':
        response = make_response(render_template('index.html'))
        response.headers['X-Flag'] = FAKE
        return response
    elif request.method == 'POST':
        response = make_response(render_template('index.html'))
        response.headers['X-Flag'] = FAKE
        return response
    elif request.method == 'HEAD':
        return "", 200
    elif request.method == 'TRACE':
        return request.data, 200
    elif request.method == 'OPTIONS':
        return '', 200, {
            'Allow': 'GET, POST, HEAD, TRACE, OPTIONS, PUT, DELETE, PATCH, CONNECT, LINK, UNLINK, PURGE, LOCK, UNLOCK, PROPFIND, VIEW, FLAG',
            'Content-Length': '0'
        }
    elif request.method == 'PUT':
        return "PUT request received"
    elif request.method == 'DELETE':
        return "DELETE request received"
    elif request.method == 'PATCH':
        return "PATCH request received"
    elif request.method == 'CONNECT':
        return "CONNECT request received"
    elif request.method == 'LINK':
        return "LINK request received"
    elif request.method == 'UNLINK':
        return "UNLINK request received"
    elif request.method == 'PURGE':
        return "PURGE request received"
    elif request.method == 'LOCK':
        return "LOCK request received"
    elif request.method == 'UNLOCK':
        return "UNLOCK request received"
    elif request.method == 'PROPFIND':
        return "PROPFIND request received"
    elif request.method == 'VIEW':
        return "VIEW request received"
    elif request.method == 'FLAG':
        url = request.json.get('url')
        
        if not url:
            return "Send me a URL to visit...", 400

        try:
            response = requests.post(url, data={'flag': f'{FLAG}'})
            return response.text
        except requests.RequestException as e:
            return str(e), 500
    else:
        return "Method not allowed", 405

if __name__ == '__main__':
    app.run(debug=True, port=6969)
