from flask import Flask, render_template, request, jsonify
import requests								#make http calls to server

app= Flask(__name__)

MODEL_SERVER_URL = "http://host.docker.internal:6000/describe"

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():								#forwading to the server
	image = request.files["image"]

	response = requests.post(
	MODEL_SERVER_URL,
	files={"image": (image.filename, image.stream, image.mimetype)}
	)

	if response.status_code != 200:					#error handling
		return jsonify({"error": "Model server error"}), 502

	return jsonify(response.json())		            

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5001, debug=True)

