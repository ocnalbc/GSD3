from flask import Flask, jsonify, make_response, abort, url_for, request

from scrape import construct_entries

app = Flask(__name__)

entries = construct_entries()

@app.route('/api/v1.0/entries/all', methods=['GET'])
def get_entries():
    return jsonify({'entries': [make_public_entry(entry) for entry in entries]})

def make_public_entry(entry):
    new_entry = {}
    for field in entry:
        if field != 'id':
            new_entry[field] = entry[field]
    return new_entry

@app.route('/api/v1.0/entries', methods=['GET'])
def get_entry():
    area_code = request.args.get('area')
    entry = [entry for entry in entries if entry['area'] == area_code]
    if len(entry) == 0:
        abort(404)
    return jsonify({'entries': entry})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)