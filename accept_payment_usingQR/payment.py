import qrcode # install qrcode library using pip install qrcode

# take UPI ID as input
upi_id = input("Enter your UPI ID: ")

# upi://pay?pa=upi_id&pn=Name&mc=MerchantCode&tid=TransactionID&tr=TransactionRefID&tn=Note&am=Amount&cu=Currency

# define the UPI URL based on UPI ID and payment app 
phonepe_url = f"upi://pay?pa={upi_id}&pn=Name&mc=MerchantCode&tid=TransactionID&tr=TransactionRefID&tn=Note&am=Amount&cu=Currency"
googlepay_url = f"upi://pay?pa={upi_id}&pn=Name&mc=MerchantCode&tid=TransactionID&tr=TransactionRefID&tn=Note&am=Amount&cu=Currency"
paytm_url = f"upi://pay?pa={upi_id}&pn=Name&mc=MerchantCode&tid=TransactionID&tr=TransactionRefID&tn=Note&am=Amount&cu=Currency"

# QR code 
phonepe_qr = qrcode.make(phonepe_url)
googlepay_qr = qrcode.make(googlepay_url)
paytm_qr = qrcode.make(paytm_url)

# save the QR code
phonepe_qr.save("phonepe.png")
googlepay_qr.save("googlepay.png")
paytm_qr.save("paytm.png")

print("QR codes generated successfully.")

# show the QR code (Install PIL/pillow library for displaying the QR code)
phonepe_qr.show()
googlepay_qr.show()
paytm_qr.show()
