import code

user = code.TaxPayer("Jeremy","password")

#Test Class
print(user)
print(user.username)
print(user.password)

#Test profile picture
print(user.get_prof_picture(path="assets/prof_picture.png"))

#Test Tax Form
print(user.get_tax_form_attachment(path="assets/tax_form.pdf"))