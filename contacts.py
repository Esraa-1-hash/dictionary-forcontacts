#create a dictionary called CONTACTS.
contacts={"Esraa": "123456789",
          "Mohamed": "789456123",
          "Zain": "147258369"}
print("The contacts in the dictionary are:", contacts)
#Adding three contacts.
contacts={"Esraa": "123456789",
          "Mohamed": "789456123",
          "Zain": "147258369"}
contacts["Mariem"] = "852963741"
contacts["Sohila"] = "1594786328"
contacts["Soha"] = "826459713"
print("The contacts in the dictionary became:" ,contacts)
for name in contacts:
   print("name", name)
   #The user can search for a contact by name
contacts={"Esraa": "123456789",
          "Mohamed": "789456123",
          "Zain": "147258369",
          "Mariem":"852963741",
           "Sohila":  "1594786328",
           "Soha": "826459713"}
print("the contact of Zain is " ,contacts["Zain"])