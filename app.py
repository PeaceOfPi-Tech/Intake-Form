from flask import Flask,request,jsonify,redirect
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import letter
from RequestBody import RequestBody
from reportlab.lib.utils import simpleSplit
import json
import requests
import os
import uuid
import logging

#TODO: Change url is Gohiglevel automation tree to prod url
probate_intake = False
personal_injury = False
estatePlanning = False

app = Flask(__name__)
app.debug = True

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    #write data to a file
    formatted_data = RequestBody(data) 
    
    pdf_title = f"{formatted_data.attributes.get('Full Name','')} intakeform.pdf"

    create_pdf(formatted_data,pdf_title,"Client Intake Form") 
    send_pdf_to_zapier(pdf_title,formatted_data.attributes)
    os.remove(pdf_title)

    return jsonify({"status": "ok", "data": data}),200

@app.route('/webhook/general', methods=['POST'])
def webhook_general():
    global probate_intake,personal_injury,estatePlanning
    probate_intake,personal_injury,estatePlanning = False,False,False

    data = request.get_json()
    formatted_data = RequestBody(data) 
    
    pdf_title = f"{formatted_data.attributes.get('Full Name','')} General_Intake_Form.pdf"
    create_pdf(formatted_data,pdf_title,"Client Intake Form") 

    send_pdf_to_zapier(pdf_title,formatted_data.attributes)
    os.remove(pdf_title)

    return jsonify({"status": "ok", "data": data}),200

#probate intake form
@app.route('/webhook/probate', methods=['POST'])
def webhook_probate():
    global probate_intake,personal_injury,estatePlanning
    probate_intake,personal_injury,estatePlanning = False,False,False
    probate_intake = True

    data = request.get_json()
        
    formatted_data = RequestBody(data)
    pdf_title = f"{formatted_data.attributes.get('Full Name','')} Probate_Intake_Form.pdf"
    
    create_pdf(formatted_data,pdf_title,"Probate Intake Form")

    send_pdf_to_zapier(pdf_title,formatted_data.attributes)
    os.remove(pdf_title)

    return jsonify({"status": "ok", "data": data}),200 

#personal injury form
@app.route('/webhook/personalinjury', methods=['POST'])
def webhook_personal_injury():
    global probate_intake,personal_injury,estatePlanning
    probate_intake,personal_injury,estatePlanning = False,False,False

    personal_injury = True 

    data = request.get_json()
    formatted_data = RequestBody(data)
    
    pdf_title = f"{formatted_data.attributes.get('Full Name','')} Personal_Injury_Form.pdf"
    create_pdf(formatted_data,pdf_title, "Personal Injury Form")

    send_pdf_to_zapier(pdf_title,formatted_data.attributes)
    os.remove(pdf_title)

    return jsonify({"status": "ok", "data": data}),200 

@app.route('/webhook/estateplanning', methods=['POST'])
def webhook_estate_planning():
    global probate_intake,personal_injury,estatePlanning
    probate_intake,personal_injury,estatePlanning = False,False,False

    estatePlanning = True 

    data = request.get_json()
    formatted_data = RequestBody(data)
    
    pdf_title = f"{formatted_data.attributes.get('Full Name','')} Estate_Planning_Form.pdf"
    create_pdf(formatted_data,pdf_title, "Estate Planning Form")
    send_pdf_to_zapier(pdf_title,formatted_data.attributes)
    os.remove(pdf_title)

    return jsonify({"status": "ok", "data": data}),200 

def create_pdf(data,pdf_title,heading):
    font_name = "Helvetica"
    font_size = 12
    c = canvas.Canvas(pdf_title, pagesize=letter)
    c.drawImage("title.jpeg", 25,725,width=200,height=60)
    c.setFont(font_name, 28)
    c.drawString(300, 740, heading)
    c.setFont(font_name, font_size)
    
    y = 710
    margin_left_x = 20
    for key,value in data.items():
        if key == "Contact ID" or key == "contact_source":
            continue
        if y < 20:
            c.showPage()
            c.drawImage("title.jpeg", 25,725,width=200,height=60)
            y = 715
        if isinstance(value, list):
            value = ", ".join(value)
            
        y = add_form_label(key,value,margin_left_x,y,c)
       
        #y -= 50
        
    if estatePlanning:
        for key,value in data.estatePlanning.items():
            if y < 20:
                c.showPage()
                c.drawImage("title.jpeg", 25,725,width=200,height=60)
                y = 715
            if isinstance(value, list):
                value = ", ".join(value)
            y = add_form_label(key,value,margin_left_x ,y,c)
    elif probate_intake:
        for key,value in data.probateIntake.items():
            if y < 20:
                c.showPage()
                c.drawImage("title.jpeg", 25,725,width=200,height=60)
                y = 715
            if isinstance(value, list):
                value = ", ".join(value)
            y = add_form_label(key,value,margin_left_x,y,c)

    elif personal_injury:
        for key,value in data.personalInjury.items():
            if y < 20:
                c.showPage()
                c.drawImage("title.jpeg", 25,725,width=200,height=60)
                y = 715
            if isinstance(value, list):
                value = ", ".join(value)
            y = add_form_label(key,value,margin_left_x,y,c)

        for key,value in data.personalInjury_defendent.items():
            if y < 20:
                c.showPage()
                c.drawImage("title.jpeg", 25,725,width=200,height=60)
                y = 715
            if isinstance(value, list):
                value = ", ".join(value)
            y = add_form_label(key,value,margin_left_x,y,c)
    c.save()    

def add_form_label(field_name,field_value, x, y, c):
    width = 400
    height = 25 
    radius = 10
    y_for_rect = y-25

    font_name = "Helvetica"
    font_size = 12
    oversized = False

    field_value_str = str(field_value) if field_value is not None else ""
    text_width = c.stringWidth(field_value_str, font_name, font_size)

        

    fill_color = Color(0,0,0,alpha=0.5)
    c.setStrokeColor(fill_color)
    field_name = field_name + ":"
    #draw name
    c.drawString(x+4, y+5, field_name)
    #draw value
    oversized = text_width > width - 50
    if oversized:
        height = 50
        y_for_rect -= 25
        lines = simpleSplit(field_value_str, font_name, font_size,width + 75)
        # used to make a biggere rectangle dependent on the number of lines
        for line in lines:
            c.drawString(x+4, y-17, line)
            y -= 10
            y_for_rect = y-50
            height += 10

        width += 100
        y-=50
    else:
        c.drawString(x+4, y-17, field_value_str)

    #draw rectangle
    c.roundRect(x, y_for_rect, width, height, radius, stroke=1, fill=0)
    y-= 50
    return y

    

def send_pdf_to_zapier(pdf_path,customerData):
    customer_name = customerData.get("Full Name"," ")
    customer_email = customerData.get("Email"," ")
    contact_id = customerData.get("Contact ID"," ")
    phone_number = customerData.get("Phone"," ") 
    url = "https://hooks.zapier.com/hooks/catch/16299933/3p0pd3l/"
    with open(pdf_path, 'rb') as pdf:
        files = {'file': (
            pdf_path, pdf, 'application/pdf'
        )}
        data = {
            "full_name": customer_name,
            "email": customer_email,
            "contact_id": contact_id,
            "phone": phone_number,
        }
        response = requests.post(url, files=files,data = data)
        
        if response.status_code == 200:
            logger.info("PDF sent successfully")
            return jsonify({"status": "ok", "message": "PDF sent successfully"}), 200
        else:
            logger.info("Failed to send to zapier",response.status_code)
            return jsonify({"status": "error", "message": "Error while sending pdf"}), 500
        