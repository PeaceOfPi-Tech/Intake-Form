



class RequestBody:
    def __init__(self, data):
        self.attributes = {
            "Full Name": data.get("full_name"),
            "Email": data.get("email"),
            "Social Security Number": data.get("Social Security Number"),
            "Citizen": data.get("Resident/Citizenship Status"),
            "Phone": data.get("phone"),
            "Secondary Phone": data.get("Secondary Phone"),
            "Full Address": data.get("full_address"),
            "Full Address 2" : data.get("Address 2"),
            "Employment": data.get("Employment"),
            "Emergency Contact": data.get("Emergency Contact (Name, Relationship, Phone)"),
            "Marital Status": data.get("Marital Status"),
            "Spouse Name": data.get("Spouse/Partner Full Name"),
            "Spouse DOB": data.get("Spouse DOB"),
            "Spouse SSN": data.get("Spouse SSN"),
            "Spouse Address": data.get("Spouse Address"),
            "Spouse Number": data.get("Spouse Phone Number"),
            "Spouse Email": data.get("Spouse Email"),
            "Spouse Employment": data.get("Spouse Employment"),
            "Child Name" : data.get("Child Name"),
            "Child DOB": data.get("Child DOB"),
            "Child Status" : data.get("Child Status"),
            "Child (2) Name": data.get("Child (2) Name"),
            "Child (2) DOB": data.get("Child (2) DOB"),
            "Child (2) Status": data.get("Child (2) Status"),
            "Child (3) Name": data.get("Child (3) Name"),
            "Child (3) DOB": data.get("Child (3) DOB"),
            "Child (3) Status": data.get("Child (3) Status"),
            "How did you hear about us? Radio Type": data.get("How did you hear about us? Radio Type"),
            "Type of legal work you would like us to help with: Checkbox": data.get("Type of legal work you would like us to help with: Checkbox"),
            "Type of legal work you would like us to help with:": data.get("Type of legal work you would like us to help with:"),
            "More Detail/Notes": data.get("More Details/Notes"),
            "Contact ID": data.get("contact_id")

        }
    def items(self):
        return self.attributes.items() 

