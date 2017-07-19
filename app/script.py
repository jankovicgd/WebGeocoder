from flask import Flask, render_template, request, send_file
import pandas

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def index():
    return render_template("index.html")

@app.route("/success", methods = ['POST'])
def success():
    if request.method == 'POST':
        file = request.files["files"]
        content = file.read()
        print(file)
        print(content)
        return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
