from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def foo():
    data = json.loads(request.data)
    print(json.dumps(data, indent=4, sort_keys=True))
    if data["action"] == "closed_by_user" and data['alert']['rule']['security_severity_level'] == "critical":
        print(f"WARNING: A developer dismissed a critical alert for reason: { data['alert']['dismissed_reason'] }.")
    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4567)
