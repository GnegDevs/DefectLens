from flask import Flask, send_file
import requests
from buildPDF import buildPDF
from yoloModel import get_yolo_predictions

app = Flask(__name__)

def processPhoto(bytea):
    return get_yolo_predictions(bytea)

def process(id, byteas, serial):
    toProcess = list()
    for bytea in byteas:
        toProcess.append(processPhoto(bytea))
    
    # toProcess = [[byteas[0], "Царапина"], [byteas[1], "Дефектов не обнаружено"], [byteas[2], "Проблемы с клавишами"], [byteas[3], "Царапина"], ]

    pdf = buildPDF(id, toProcess, serial)
    pdf.output("report.pdf")
    return pdf


@app.route("/defectlensmodel/api/v1/ping", methods=["GET"])
def pingController():
    return "ok"

@app.route("/defectlensmodel/api/v1/process/<int:id>", methods=["GET"])
def processorController(id):
    response = requests.get(f"http://localhost:8080/defectlens/api/v1/record/{id}").json()
    toProcess = list()
    for key, value in response.items():
        if key != "id" and value != "":
            toProcess.append(value)
    process(response["id"], toProcess, response["serial"])
    return "ok"


@app.route("/defectlensmodel/api/v1/process/download")
def sendPDF():
    path = "report.pdf"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True, port=5000)
