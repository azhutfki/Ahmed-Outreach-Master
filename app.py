from flask import Flask, request, jsonify

app = Flask(__name__)

target_groups = {
    "model": "site:.com intitle:model",
    "artist": "site:.com intitle:artist",
    # ... other target groups and their respective Google Dorks
}

def generate_search_url(target_group, location):
    dork = target_groups[target_group]
    search_url = f"https://www.google.com/search?q={dork}+{location}"
    return search_url

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    target = data['target']
    location = data['location']
    search_url = generate_search_url(target, location)
    return search_url

if __name__ == '__main__':
    app.run(debug=True)
