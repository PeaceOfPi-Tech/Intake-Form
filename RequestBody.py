



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
            "Contact ID": data.get("contact_id"),
            "contact_source": data.get("contact_source")
        }
        self.assetProtection = {
            "Do you want to be cremated?": data.get("Do you want to be cremated?"),
            "Funeral or Burial Prearrangements?" : data.get("Funeral or Burial Prearrangements?"),
            "Beneficiary Names": data.get("Beneficiary Names. Please include: Percentages (or equally); Dates of Birth; and Relationship"),
            "Who do you want to serve as personal representative (executor) of your will?" : data.get("Who do you want to serve as personal representative (executor) of your will?"),
            "Relation": data.get("Relation"),
            "Upon your passing, who do you want to be the trustee of your trust?" : data.get("During your lifetime, you will be the trustee of your trust. A trustee manages and administers the trust. Upon your passing, who do you want to be the trustee of your trust?"),
            "Who do you want to serve as successor or alternate?" : data.get("If your trustee above predeceases you or cannot act, who do you want to serve as successor or alternate?"), 
            "Who do you want to make your legal and financial decisions?" : data.get("Who do you want to make your legal and financial decisions? (Your power of attorney)"),
            "Power of Attorney's Address & Phone Number": data.get("Power of Attorney's Address & Phone Number"),
            "Who do you want to make your healthcare decisions? (Your healthcare surrogate)" : data.get("Who do you want to make your healthcare decisions? (Your healthcare surrogate)"),
            "Who do you want to serve as successor?" : data.get("If your healthcare surrogate above predeceases you or cannot act, who do you want to serve as successor?"),
            "Income Beneficiaries": data.get("Income Beneficiaries - During your lifetime, you're the income beneficiary. Is there anyone else you want to give it during lifetime? (Distribution to these beneficiaries is not mandatory but permissible)"),
            "Principal Beneficiaries" : data.get("Principal Beneficiaries - You cannot be a principal beneficiary as that will cause loss of protection. Who would you like to be able to give some of the principal to?"),
            "Any Specific Requests" : data.get("Any specific bequests?"),
        }
        self.probateIntake = {
            "Decedent's Full Legal Name" : data.get("Decedent's Full Legal Name"),
            "County of Death or County of Property": data.get("County of Death or County of Property"),
            "Decedent's Residence/Address" : data.get("Decedent's Residence/Address"),
            "Decendent's City": data.get("Decendent's City"),
            "Decedent's Zip Code" : data.get("Decedent's Zip Code"),
            "Is it Homestead Property?" : data.get("Is it Homestead Property?"),
            "Is there a Mortgage on the Property": data.get("Is there a Mortgage on the Property"),
            "Date of Death": data.get("Date of Death"),
            "Is there a will?" : data.get("Is there a will?"),
            "Does the decedent have a surviving spouse?" : data.get("Does the decedent have a surviving spouse?"),
            "Does the decedent have children?" : data.get("Does the decedent have children?"),
            "If so, how many?" : data.get("If so, how many?"), 
            "Have all debts been paid?": data.get("Have all debts been paid?"),
            "What are the assets (in the Decedent's name) and their approximate value?": data.get("What are the assets (in the Decedent's name) and their approximate value?"),
            "# 1 - Name, Phone Number, Relation, & Email" : data.get("# 1 - Name, Phone Number, Relation, & Email"),
            "# 2 - Name, Phone Number, Relation, & Email" : data.get("# 2 - Name, Phone Number, Relation, & Email"),
            "# 3 - Name, Phone Number, Relation, & Email" : data.get("# 3 - Name, Phone Number, Relation, & Email"),
            "# 4 - Name, Phone Number, Relation, & Email" : data.get("# 4 - Name, Phone Number, Relation, & Email"),
            "Any other concerns or questions you want addressed at the meeting?" : data.get("Any other concerns or questions you want addressed at the meeting?"),
        }
    def items(self):
        return self.attributes.items() 
    def assetProtectionItems(self):
        return self.assetProtection.items()
