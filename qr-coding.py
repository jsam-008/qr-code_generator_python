import qrcode
text = input("Enter the text to generate QR code: ")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(text)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

img.save("qrcode.png")

img.show()

print("QR Code generated and saved as 'qrcode.png'!")
