# NII ARKU LARYEA/.
#nii.arku@azubiafrica.org | Group 10
plain_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
#plain text has already been defined as A-z.    
text = input("Enter plaintext message: ").upper()
#s defines the shift count
S = int(input("Choose the shift code: "))

encrypted = str()
#string is used so that program does not blow up.
# transverse the plain text
for i in text:
    updated_position = (plain_text.find(i)-S) % 26
    encrypted += plain_text[updated_position]

print(encrypted)

