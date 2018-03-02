from twilio.rest import Client
from flask import Flask, request
from flask_slack import Slack

app = Flask(__name__)
slack = Slack(app)

account_sid = TWILIO_SID
auth_token = TWILIO_TOKEN

client = Client(account_sid, auth_token)

app.add_url_rule('/', view_func=slack.dispatch)

@slack.command('/text', token=SLACK_TOKEN,
               team_id=SLACK_TEAMID, methods=['POST'])

@app.route('/text', methods=['POST'])
def send_text(**kwargs):
	args = request.form.get('text', '').split(' ', 1)
	client.messages.create(
	 	to=args[0], from_=TWILIO_PHONE_NUM,
	 	body=args[1])
	
	return 'Text Sent'

if __name__ == '__main__':
	app.run()