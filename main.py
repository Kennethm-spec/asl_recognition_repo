import os
import base64
import numpy as np
from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__)

VIDEO_FOLDER = 'videos'
app.config['VIDEO_FOLDER'] = VIDEO_FOLDER
os.makedirs(VIDEO_FOLDER, exist_ok=True)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/recognize', methods=['POST'])
def recognize():
    data = request.get_json()
    img_data = base64.b64decode(data['image'])
    img_array = np.frombuffer(img_data, dtype=np.uint8)
    print(f'here is img_array -> {img_array}')
    print(f'{img_array.size}')
    # TODO: do somethign with image array
    sign = 'hello world'  # return hello world for now
    return jsonify({'sign': sign})

# Disable caching for CSS files
@app.route('/static/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path, cache_timeout=0)

# Disable caching for JS files
@app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path, cache_timeout=0)

if __name__ == '__main__':
    app.run(port=5003, debug=True)
