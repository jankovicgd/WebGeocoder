from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route("/")
def index():
    if request.method == 'POST':
        file = request.files["files"]
        content = file.read()
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
