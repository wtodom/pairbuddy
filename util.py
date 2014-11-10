from __future__ import print_function
import json


def json_to_table(pairing_json):
	html = '<table class="table"><thead><tr><td>table</td><td>player 1</td><td>player 2</td></tr></thead><tbody>'
	with open(pairing_json, 'r') as f:
		data = json.loads(f.read())
		for i, table in enumerate(data['tables']):
			players = table["players"]
			html += '<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>'.format(
				i + 1, 
				players[0],
				players[1]
				)
		html += '</tbody></table>'
	return html


print(json_to_table('example.json'))