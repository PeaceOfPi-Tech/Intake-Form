from flask import Flask,request,jsonify
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import letter
from RequestBody import RequestBody
from reportlab.lib.utils import simpleSplit

import json
import requests
import os

asset_protection = False
probate_intake = False
app = Flask(__name__)
app.debug = True
@app.route('/webhook', methods=['POST'])
def webhook():
    
    data = request.get_json()
    if data.get("contact_source") =="asset protection trust intake form":
        global asset_protection
        asset_protection = True
    elif data.get("contact_source") != "Online Case Eval. Submission":
        global probate_intake 
        probate_intake = True 

    formatted_data = RequestBody(data) 

    create_pdf(formatted_data) 
    send_pdf_to_zapier("output.pdf",formatted_data.attributes)

    os.remove("output.pdf") 
    return jsonify({"status": "ok", "data": data}),200


def create_pdf(data):
    font_name = "Helvetica"
    font_size = 12

    c = canvas.Canvas("output.pdf", pagesize=letter)
    c.drawImage("title.jpeg", 25,700)
    c.setFont(font_name, font_size)
    
    y = 680
    for key,value in data.items():
        if key == "Contact ID" or key == "contact_source":
            continue
        if y < 20:
            c.showPage()
            y = 750
        if isinstance(value, list):
            value = ", ".join(value)
            
        add_form_label(key,value,50,y,c)
       
        y -= 50
    c.showPage() 
    if asset_protection:
        for key,value in data.assetProtection.items():
            if y < 20:
                c.showPage()
                y = 750
            if isinstance(value, list):
                value = ", ".join(value)
            add_form_label(key,value,50,y,c)
            y -= 50
    if probate_intake:
        for key,value in data.probateIntake.items():
            if y < 20:
                c.showPage()
                y = 750
            if isinstance(value, list):
                value = ", ".join(value)
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
    field_value_str = str(field_value) if field_value is not None else ""
    text_width = c.stringWidth(field_value_str, font_name, font_size)

        

    fill_color = Color(0,0,0,alpha=0.5)
    c.setStrokeColor(fill_color)
    field_name = field_name + ":"
    #draw name
    c.drawString(x+4, y+5, field_name)
    #draw value
    if text_width > width -50:
        height = 50
        y_for_rect -= 25
        lines = simpleSplit(field_value_str, font_name, font_size,width)
        # used to make a biggere rectangle dependent on the number of lines
        for line in lines:
            c.drawString(x+4, y-17, line)
            y -= 10
            y_for_rect = y-50
            height += 10
        
        y-=50
    else:
        c.drawString(x+4, y-17, field_value_str)

    #draw rectangle
    c.roundRect(x, y_for_rect, width, height, radius, stroke=1, fill=0)

    

def send_pdf_to_zapier(pdf_path,customerData):
    customer_name = customerData.get("Full Name"," ")
    customer_email = customerData.get("Email"," ")
    contact_id = customerData.get("Contact ID"," ")
    
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
