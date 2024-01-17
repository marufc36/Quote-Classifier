from flask import Flask, render_template, request
from gradio_client import Client

app = Flask(__name__)
client = Client("https://mmchowdhury-quote-classifier.hf.space/--replicas/tklcl/")

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        input_text = request.form['text']
        prediction = predict_tags(input_text)
        return render_template("index.html", input_text=input_text, prediction=prediction)
    else:
        return render_template("index.html")

def predict_tags(input_text):
    # Call the Hugging Face API using Gradio client
    result = client.predict(
        input_text,
        api_name="/predict"
    )

    # Extract only the labels from the response
    labels = [confidence['label'] for confidence in result['confidences']]

    # Update the result dictionary to include the labels
    result.update({"labels": labels, "quote": input_text})

    return result

if __name__ == "__main__":
    app.run(debug=True)
