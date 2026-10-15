import qrcode   

#Taking UPI as input from user
upi_id = input("Enter your UPI ID: ")   

#upi://pay?pa=UPI_id&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=Message

#Defining the payment URL baSed on the UPI ID and the payment app 
#you can modify these URLs based on the payment apps you want to support

phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipiente%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipiente%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipiente%20Name&mc=1234"


# Generating QR codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)   
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Saving the QR codes as image files
phonepe_qr.save("phonepe_qr.png")   
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

# Displaying the QR codes(you may need to install an image viewer or use a library like PIL/Pillow to display the images)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

## qr code should be scannable by the respective payment apps, allowing users to make payments directly to the specified UPI ID.