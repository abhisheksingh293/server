from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint to serve files data
@app.route('/files', methods=['GET'])
def get_files():
    # Example data with GitHub raw URLs
    files = [
        {"name": "Chemistry Notes Chapter 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Chemistry"},
        {"name": "Chemistry Notes Chapter 2", "url": "https://raw.githubusercontent.com/username/repository/branch/path/to/chapter2.pdf", "category": "Chemistry"},
        {"name": "Physics Notes Chapter 1", "url": "https://raw.githubusercontent.com/username/repository/branch/path/to/chapter1.pdf", "category": "Physics"},
        {"name": "Physics Notes Chapter 2", "url": "https://raw.githubusercontent.com/username/repository/branch/path/to/chapter2.pdf", "category": "Physics"},
        {"name": "Chemistry Notes Chapter 3", "url": "https://raw.githubusercontent.com/username/repository/branch/path/to/chapter3.pdf", "category": "Chemistry_pyq"},
        {"name": "Physics Notes Chapter 3", "url": "https://raw.githubusercontent.com/username/repository/branch/path/to/chapter3.pdf", "category": "Physics"}
    ]
    return jsonify(files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
