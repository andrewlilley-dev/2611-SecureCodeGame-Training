import code

user = code.TaxPayer("Jeremy","password")

#Test Class
print(user)
print(user.username)
print(user.password_hash)

#Test Password Hasing
print(user.verify_password("password"))
print(user.verify_password("passwords"))

#Test profile picture
print(user.get_prof_picture(path="assets/prof_picture.png"))

#Test Tax Form
print(user.get_tax_form_attachment(path="assets/tax_form.pdf"))