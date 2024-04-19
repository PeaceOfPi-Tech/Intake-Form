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

asset_protection = False
probate_intake = False
app = Flask(__name__)
app.debug = True

@app.route('/webhook', methods=['POST'])
def webhook():
    access_token_2 = "a6bd077b-02ea-47d9-94e6-4dfcc33d9ed9"
    access_token = "2092060b-b7b3-492a-abb9-5e305f41dfb3"
    location_id = "yPsOXmmCcVaa9JZxtxU3"
    custom_field_id = "{{ contact.intake_form }}"

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

    #send_pdf_to_gohighlevel("output.pdf",formatted_data.attributes,access_token_2,location_id,custom_field_id)
    os.remove("output.pdf") 
    return jsonify({"status": "ok", "data": data}),200


def create_pdf(data):
    font_name = "Helvetica"
    font_size = 12

    c = canvas.Canvas("output.pdf", pagesize=letter)
    c.drawImage("title.jpeg", 25,725,width=200,height=60)
    c.setFont(font_name, font_size)
    
    y = 710
    margin_left_x = 20
    for key,value in data.items():
        if key == "Contact ID" or key == "contact_source":
            continue
        if y < 20:
            c.showPage()
            y = 750
        if isinstance(value, list):
            value = ", ".join(value)
            
        y = add_form_label(key,value,margin_left_x,y,c)
       
        #y -= 50

    if asset_protection:
        for key,value in data.assetProtection.items():
            if y < 20:
                c.showPage()
                y = 750
            if isinstance(value, list):
                value = ", ".join(value)
            y = add_form_label(key,value,margin_left_x ,y,c)
            #y -= 50

    if probate_intake:
        for key,value in data.probateIntake.items():
            if y < 20:
                c.showPage()
                y = 750
            if isinstance(value, list):
                value = ", ".join(value)
            y = add_form_label(key,value,margin_left_x,y,c)
            #y -= 50

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
            print("PDF sent successfully")
            return jsonify({"status": "ok", "message": "PDF sent successfully"}), 200
        else:
            print("Failed to send to zapier",response.status_code)
            return jsonify({"status": "error", "message": "Error while sending pdf"}), 500
        

def send_pdf_to_gohighlevel(pdf_path, customerData, access_token, location_id, custom_field_id):
    url = 'https://services.leadconnectorhq.com/forms/upload-custom-files'
    
    # Construct headers and query parameters
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Version': '2021-07-28'
    }
    
    params = {
        'contactId': customerData.get("Contact ID"," "),
        'locationId': location_id
    }
    
    # Generate a random file ID (UUID)
    file_id = uuid.uuid4()
    
    # Prepare the files dictionary using the custom field and file ID
    file_key = f'{custom_field_id}_{file_id}'
    files = {
        file_key: ('filename.pdf', open(pdf_path, 'rb'), 'application/pdf')
    }
    
    # Send the POST request
    response = requests.post(url, headers=headers, params=params, files=files)
    
    # Close the file after sending
    files[file_key][1].close()
    
    # Check response
    if response.status_code == 200:
        print("PDF uploaded successfully")
    else:
        print("Failed to upload PDF:", response.status_code, response.text)

    return response

if __name__ == '__main__':
    app.run(debug=True)
