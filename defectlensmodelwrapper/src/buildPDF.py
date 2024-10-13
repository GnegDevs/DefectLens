from fpdf import FPDF, Align
from datetime import date
import base64
import io

def buildPDF(id, pics, sernum):
    names = ["Крышка ноутбука", "Экран", "Клавиатура", "Нижний корпус"]
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("Lora", style="", fname="Lora-VariableFont_wght.ttf", uni=True)
    pdf.add_font("Lora", style="B", fname="Lora-Bold.ttf", uni=True)
    pdf.set_margins(top=25, left=15, right=15)
    pdf.set_font(family="Lora", style="B", size=20)

    pdf.cell(200, 10, txt=f"Протокол №{id}", ln=1, align="C")
    pdf.cell(200, 10, txt="о качестве ноутбука", ln=1, align="C")

    pdf.ln(10)
    pdf.set_font(family="Lora",  size=16)

    pdf.cell(200, 10, txt=f"Дата осмотра: {date.today().strftime("%d.%m.%Y")}", ln=1)
    pdf.cell(200, 10, txt="Модель ноутбука: _________________", ln=1)
    pdf.cell(200, 10, txt=f"Серийный номер: {sernum}",  ln=1)
    pdf.cell(200, 10, txt="ФИО осматривающего: ___________________________",  ln=1)
    pdf.cell(200, 10, txt="Контактные данные: ___________________________",  ln=1)

    pdf.ln(10)
    pdf.set_font(family="Lora",  size=20, style="B")

    pdf.cell(200, 10, txt="Результаты осмотра", ln=1, align="C")
    pdf.cell(200, 10, txt="нейросетью «DefectLens»", ln=1, align="C")
    pdf.ln(10)

    n = 0
    a = "КОНТРОЛЬ КАЧЕСТВА ПРОЙДЕН"
    for i in range(4):
        pdf.set_font(family="Lora", style="B", size=20)
        pdf.cell(200, 10, txt=f"{i+1}. {names[i]}", ln=1, align="C")

#        with open(pics[i][0], "rb") as imagefile:
#            convert = base64.b64encode(imagefile.read())
        decoded = io.BytesIO(base64.b64decode(pics[i][0]))

        pdf.ln(5)
        pdf.image(decoded, w=100, x=Align.C)
        pdf.ln(5)

        pdf.set_font(family="Lora", size=20, style="B")
        pdf.cell(200, 10, txt="Класс повреждения:", ln=1)
        pdf.set_font(family="Lora", size=20)
        pdf.cell(200, 10, txt=pics[i][1], ln=1)

        pdf.ln(30)

        if pics[i][1] != "Дефектов не обнаружено":
            n += 1
            a = "КОНТРОЛЬ КАЧЕСТВА НЕ ПРОЙДЕН"

    pdf.set_font(family="Lora", size=24)
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Количество дефектов: {n}/4", ln=1, align="C")
    pdf.cell(200, 10, txt=a, ln=1, align="C")

    pdf.set_font(family="Lora", size=20)
    pdf.ln(10)

    pdf.cell(200, 10, txt="Подпись осматривающего _________________", ln=1)
    pdf.cell(200, 10, txt=f"Дата осмотра {date.today().strftime("%d.%m.%Y")}", ln=1)

    return pdf

prompt = [["iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAELSURBVDhPbZK7asNAEEX3ZwWqhepVb0PSBwW1JgT8iWvOwFlugovLrGfmzMtqx3GMfd9L53mO2+2jhL/3PtZ1LT/CZwxt2zaqAMHHz9cMYoX0I4oBWYB4s7tJgvgAsAmg+/2zpsPXEliW5W0xphDED4glt1a4rmsmmWBHIEHFGsBwLQNWTpg3AOu4Ejk2qwkSchJ+k+y/gJ+O5Coa1A0sgoSwv8/v2QmZxwGBic0VABBdtMYs4uW9Gb4qwI4mWZlERRzloT3snIDq2ARcxf2FzUMtL4t4E7BbTkPc4n8mMPH/W8g3YPpo1nKvd8qDISA0P+VM9lMmCJh30fq2cRVgHwLAvhNKmyv23scLGG+YXNliKwQAAAAASUVORK5CYII=", "Дефектов не обнаружено", "гна гна"],
          ["iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAELSURBVDhPbZK7asNAEEX3ZwWqhepVb0PSBwW1JgT8iWvOwFlugovLrGfmzMtqx3GMfd9L53mO2+2jhL/3PtZ1LT/CZwxt2zaqAMHHz9cMYoX0I4oBWYB4s7tJgvgAsAmg+/2zpsPXEliW5W0xphDED4glt1a4rmsmmWBHIEHFGsBwLQNWTpg3AOu4Ejk2qwkSchJ+k+y/gJ+O5Coa1A0sgoSwv8/v2QmZxwGBic0VABBdtMYs4uW9Gb4qwI4mWZlERRzloT3snIDq2ARcxf2FzUMtL4t4E7BbTkPc4n8mMPH/W8g3YPpo1nKvd8qDISA0P+VM9lMmCJh30fq2cRVgHwLAvhNKmyv23scLGG+YXNliKwQAAAAASUVORK5CYII=", "Дефектов не обнаружено",  "гна гна"],
          ["iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAELSURBVDhPbZK7asNAEEX3ZwWqhepVb0PSBwW1JgT8iWvOwFlugovLrGfmzMtqx3GMfd9L53mO2+2jhL/3PtZ1LT/CZwxt2zaqAMHHz9cMYoX0I4oBWYB4s7tJgvgAsAmg+/2zpsPXEliW5W0xphDED4glt1a4rmsmmWBHIEHFGsBwLQNWTpg3AOu4Ejk2qwkSchJ+k+y/gJ+O5Coa1A0sgoSwv8/v2QmZxwGBic0VABBdtMYs4uW9Gb4qwI4mWZlERRzloT3snIDq2ARcxf2FzUMtL4t4E7BbTkPc4n8mMPH/W8g3YPpo1nKvd8qDISA0P+VM9lMmCJh30fq2cRVgHwLAvhNKmyv23scLGG+YXNliKwQAAAAASUVORK5CYII=", "Дефектов не обнаружено",  "гна гна"],
          ["iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAELSURBVDhPbZK7asNAEEX3ZwWqhepVb0PSBwW1JgT8iWvOwFlugovLrGfmzMtqx3GMfd9L53mO2+2jhL/3PtZ1LT/CZwxt2zaqAMHHz9cMYoX0I4oBWYB4s7tJgvgAsAmg+/2zpsPXEliW5W0xphDED4glt1a4rmsmmWBHIEHFGsBwLQNWTpg3AOu4Ejk2qwkSchJ+k+y/gJ+O5Coa1A0sgoSwv8/v2QmZxwGBic0VABBdtMYs4uW9Gb4qwI4mWZlERRzloT3snIDq2ARcxf2FzUMtL4t4E7BbTkPc4n8mMPH/W8g3YPpo1nKvd8qDISA0P+VM9lMmCJh30fq2cRVgHwLAvhNKmyv23scLGG+YXNliKwQAAAAASUVORK5CYII=", "Дефектов не обнаружено",  "гна гна"]]

buildPDF(1, prompt, 52).output("report.pdf")

