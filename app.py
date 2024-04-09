from flask import Flask,request,jsonify
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import letter
from RequestBody import RequestBody
from reportlab.lib.utils import simpleSplit

import json
import requests

app = Flask(__name__)
app.debug = True
@app.route('/webhook', methods=['POST'])
def webhook():
    
    data = request.get_json()
    formatted_data = RequestBody(data) 

    create_pdf(formatted_data) 
    send_pdf_to_zapier("output.pdf",formatted_data.attributes)
    return jsonify({"status": "ok", "data": data}),200


def create_pdf(data):
    font_name = "Helvetica"
    font_size = 12
    
    #Insert image into pdf on the top left corne
    try:
        c = canvas.Canvas("output.pdf", pagesize=letter)
        c.drawImage("title.jpeg", 25,700)
        c.setFont(font_name, font_size)
    except Exception as e:
        print("Error: ", e)
        return jsonify({"status": "error", "message": "Error while creating pdf"}), 500
    
    y = 680
    for key,value in data.items():
        if y < 20:
            c.showPage()
            y = 750
        add_form_label(key,value,50,y,c)
        y -= 50

    c.save()    

def add_form_label(field_name,field_value, x, y, c):
    
    width = 500
    height = 25 
    radius = 10
    y_for_rect = y-25
    font_name = "Helvetica"
    font_size = 12
    text_width = c.stringWidth(field_value, font_name, font_size)
    if field_name == "More Detail/Notes":
        height = 50
        y_for_rect -= 25

    fill_color = Color(0,0,0,alpha=0.5)
    c.setStrokeColor(fill_color)
    field_name = field_name + ":"
    c.drawString(x+4, y+5, field_name)

    if text_width > 400:
        lines = simpleSplit(field_value, font_name, font_size,width)
        # used to make a biggere rectangle dependent on the number of lines
        for line in lines:
            c.drawString(x+4, y-17, line)
            y -= 10
            y_for_rect = y-50
            height += 10
    else:
        c.drawString(x+4, y-17, field_value)

    c.roundRect(x, y_for_rect, width, height, radius, stroke=1, fill=0)

def send_pdf_to_zapier(pdf_path,customerData):
    customer_name = customerData.get("Full Name")
    customer_email = customerData.get("Email")
    contact_id = customerData.get("Contact ID")
    print("customer name: ",customer_name)
    print("customer email: ",customer_email)
    url = "https://hooks.zapier.com/hooks/catch/16299933/3p0pd3l/"
    with open(pdf_path, 'rb') as pdf:
        files = {'file': (
            pdf_path, pdf, 'application/pdf'
        )}
        data = {
            "full_name": customer_name,
            "email": customer_email,
            "contact_id": contact_id,
        }
        response = requests.post(url, files=files,data = data)
        
        if response.status_code == 200:
            print("PDF sent successfully")
            return jsonify({"status": "ok", "message": "PDF sent successfully"}), 200
        else:
            print("Failed to send to zapier",response.status_code)
            return jsonify({"status": "error", "message": "Error while sending pdf"}), 500
if __name__ == '__main__':
    app.run(debug=True)
