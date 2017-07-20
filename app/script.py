from flask import Flask, render_template, request, send_file
from geopy.geocoders import Nominatim
import pandas

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def index():
    return render_template("index.html")

@app.route("/success", methods = ['POST'])
def success():
    if request.method == 'POST':
        file = request.files["files"]
        try:
            df = pandas.read_csv(file)
            gc = Nominatim()
            df["coordinates"] = df["Address"].apply(gc.geocode)
            df["Latitude"] = df["coordinates"].apply(lambda x: x.latitude if x != None else None)
            df["Longitude"] = df["coordinates"].apply(lambda x: x.longitude if x != None else None)
            df = df.drop("coordinates", 1)
            df.to_csv("uploads/geocoded.csv", index=None)
            return render_template("index.html", text = df.to_html(), btn ="download.html")
        except:
            return render_template("index.html", text = "File not properly structured")

@app.route("/download-file/")
def download():
    return send_file("uploads/geocoded.csv", attachment_filename='yourfile.csv', as_attachment=True)

if __name__ == '__main__':
    app.debug = True
    app.run()
