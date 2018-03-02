from twilio.rest import Client
from flask import Flask, request
from flask_slack import Slack

app = Flask(__name__)
slack = Slack(app)

account_sid = "AC3f035b264d9174b0ba9fadc6239f316a"
auth_token = "8d160eacf3bd250cd85342ba50a7009b"

client = Client(account_sid, auth_token)

app.add_url_rule('/', view_func=slack.dispatch)

@slack.command('/text', token='xoxp-175140767184-175736449491-322880991601-af5995a489a6d2888830a68eefbf0532',
               team_id='T5544NK5E', methods=['POST'])

@app.route('/text', methods=['POST'])
def send_text(**kwargs):
	args = request.form.get('text', '').split(' ', 1)
	client.messages.create(
	 	to=args[0], from_="+12064880703",
	 	body=args[1])
	
	return 'Text Sent'

if __name__ == '__main__':
	app.run()