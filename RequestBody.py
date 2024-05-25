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
            "How did you hear about us? Radio Type": data.get("How did you hear about us? Radio Type"),
            "Type of legal work you would like us to help with: Checkbox": data.get("Type of legal work you would like us to help with: Checkbox"),
            "Type of legal work you would like us to help with": data.get("Type of legal work you would like us to help with:"),
            "More Detail/Notes": data.get("More Details/Notes"),
            "Contact ID": data.get("contact_id"),
            "contact_source": data.get("contact_source")
        }
        self.estatePlanning = {
            "Do you want to be cremated?": data.get("Do you want to be cremated?"),
            "Funeral or Burial Prearrangements?" : data.get("Funeral or Burial Prearrangements?"),
            "Beneficiary Names": data.get("Beneficiary Names. Please include: Percentages (or equally); Dates of Birth; and Relationship"),
            "Who do you want to serve as personal representative (executor) of your will?" : data.get("Who do you want to serve as personal representative (executor) of your will?"),
            "Relation": data.get("Relation"),
            "Upon your passing, who do you want to be the trustee of your trust?" : data.get("During your lifetime, you will be the trustee of your trust. A trustee manages and administers the trust. Upon your passing, who do you want to be the trustee of your trust?"),
            "Who do you want to serve as successor or alternate?" : data.get("If your trustee above predeceases you or cannot act, who do you want to serve as successor or alternate?"), 
            "Who do you want to make your legal and financial decisions?" : data.get("Who do you want to make your legal and financial decisions? (Your power of attorney)"),
            "Power of Attorney's Address & Phone Number": data.get("Power of Attorney's Address & Phone Number"),
            "If your power of attorney above predeceases, who do you want to serve as successor?" : data.get("If your power of attorney above predeceases you or cannot act, who do you want to serve as successor?"),
            "Successor Power of Attorney's Address & Phone Number": data.get("Successor Power of Attorney's Address & Phone Number"),
            "Who do you want to make your healthcare decisions? (Your healthcare surrogate)" : data.get("Who do you want to make your healthcare decisions? (Your healthcare surrogate)"),
            "If your healthcare surrogate predeceases, who do you want to serve as successor?" : data.get("If your healthcare surrogate above predeceases you or cannot act, who do you want to serve as successor?"),
            "Income Beneficiaries": data.get("Income Beneficiaries - During your lifetime, you're the income beneficiary. Is there anyone else you want to give it during lifetime? (Distribution to these beneficiaries is not mandatory but permissible)"),
            "Principal Beneficiaries" : data.get("Principal Beneficiaries - You cannot be a principal beneficiary as that will cause loss of protection. Who would you like to be able to give some of the principal to?"),
            "Any Specific Requests" : data.get("Any specific bequests?"),
        }
        self.probateIntake = {
            "Decedent's Full Legal Name" : data.get("Decedent's Full Legal Name"),
            "County of Death or County of Property": data.get("County of Death or County of Property"),
            "Decedent's Residence/Address" : data.get("Decedent's Residence/Address"),
            "Decedent's City": data.get("Decedent's City"),
            "Decedent's Zip Code" : data.get("Decedent's Zip Code"),
            "Is it Homestead Property?" : data.get("Is it Homestead Property?"),
            "Is there a Mortgage on the Property": data.get("Is there a Mortgage on the Property?"),
            "Date of Death": data.get("Date of Death"),
            "Is there a will?" : data.get("Is there a will?"),
            "Does the decedent have a surviving spouse?" : data.get("Does the decedent have a surviving spouse?"),
            "Does the decedent have children?" : data.get("Does the decedent have children?"),
            "If so, how many?" : data.get("If so, how many?"), 
            "Have all debts been paid?": data.get("Have all debts been paid?"),
            "What are the assets (in the Decedent's name) and their approximate value?": data.get("What are the assets (in the Decedent's name) and their approximate value?"),
            "# 1 - Name, Phone Number, Relation, & Email" : data.get("# 1 - Name, Phone Number, Relation, & Email"),
            "# 2 - Name, Phone Number, Relation, & Email" : data.get("#2 - Name, Phone Number, Relation, & Email"),
            "# 3 - Name, Phone Number, Relation, & Email" : data.get("#3 - Name, Phone Number, Relation, & Email"),
            "# 4 - Name, Phone Number, Relation, & Email" : data.get("#4 - Name, Phone Number, Relation, & Email"),
            "Any other concerns or questions you want addressed at the meeting?" : data.get("Any other concerns or questions you want addressed at the meeting?"),
        }
        accident_info = data.get("Accident Information", {})
        if isinstance(accident_info, str):
            accident_info = {}
        decedent_info = data.get("Defendant's Information", {})
        if isinstance(decedent_info, str):
            decedent_info = {}
        
        self.personalInjury = {
            "Were you involved in an accident": data.get("Were you involved in an accident? "),
            "Type of accident": data.get("Type of Accident"),
            "Other type of accident": data.get("Other type of Accident"),
            "Date of Accident": accident_info.get("13f46446-40d6-42f3-be23-50b7b6e86d16",""),
            "Time of Accident": accident_info.get("0022a443-1776-4fc0-a5a3-7b78e6b97b29",""),
            "City of Accident": accident_info.get("23130898-16c6-4a06-8a43-43730cb20426",""),
            "Driver's Name": accident_info.get("393c6c98-47fa-4214-878c-069c7ac865bc",""),
            "Vehicle Make": accident_info.get("2445ac64-aea5-4770-8972-2df871caeff5",""),
            "Vehicle Year": accident_info.get("ec64f02d-2fa2-420c-b860-430c882a6dee",""),
            "Vehicle Model": accident_info.get("98881b60-7d8b-4cda-abfa-2cf154340a12",""),
            "Insurance Company": accident_info.get("3b88ba8a-90a4-47fa-b155-1dc326e9444e",""),
            "Policy Number": accident_info.get("fc047abc-abbc-4cf5-9876-ae1e4746452b",""),
            "Insurance Policyholder": accident_info.get("e0637505-6b5c-4ab8-86b4-c32883a4b4d2",""),
            "Claim Number": accident_info.get("f708966c-9370-403a-8d32-b962125b92d4",""),
            "Nature of Injuries": data.get("Nature of Inuries",""),
            "Previous Existing Injuries": data.get("Previous Existing Injuries",""),
            "Hospital Visited": data.get("Name of Hospital Visited",""),
            "Physicians Visited": data.get("Physicians Visited",""),
        }
        self.personalInjury_defendent = {
            "Defendant's Name": decedent_info.get("f271c0ce-79b2-4174-8871-9595fae172e1",""),
            "Defendant'sInsurance Company": decedent_info.get("a57f024b-749e-4ada-aa10-38b2f3239dd9",""),
            "Defendant's Policy Holder": decedent_info.get("e33d3fb6-a7fd-4b16-9b00-fda300a5231a",""),
            "Defendant's Policy Number": decedent_info.get("58190006-5607-4fc3-b1f7-132270b37c30",""),
            "Defendant's Vehicle Make": decedent_info.get("fbbd0482-7e4e-40f8-a5db-b670c7478c61",""),
            "Defendant's Vehicle Year": decedent_info.get("27610063-74bd-4519-aaf7-d108a70764ac",""),
            "Defendant's Vehicle Model": decedent_info.get("f2637e36-2549-4621-be40-b5454db94501",""),
            "At Fault?": decedent_info.get("03cf0835-7dac-4340-9913-75f3dc072720",""),
        }



        #TODO: add dictionary for personal Injury form
        #get all the fields by first submitting the from to the endpoint and then gettinf the keys from ngrok 
        #adjust logic in app.py to handle the personal injury form
    def items(self):
        return self.attributes.items() 
    def assetProtectionItems(self):
        return self.estatePlanning.items()
    def probateIntakeItems(self):
        return self.probateIntake.items()
    def personalInjuryItems(self):
        return self.personalInjury.items()
    def personalInjuryDefendentItems(self):
        return self.personalInjury_defendent.items()
