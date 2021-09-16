from flask import Flask, render_template, request
import paho.mqtt.client as paho


def publish_data(topic, data):
    try:
        del client
    except:
        pass
    broker = "mqttdns.eastus.cloudapp.azure.com"
    client = paho.Client()
    client.connect(broker)
    client.publish(topic, data)
    client.disconnect()
    del client
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    if request.method == 'POST':
        topic = request.form['topic']
        publish_data(topic, '1')
        return render_template('start.html')

@app.route('/stop', methods=['POST'])
def stop():
    if request.method == 'POST':
        topic = request.form['topic']
        publish_data(topic, '0')
        return render_template('stop.html')
