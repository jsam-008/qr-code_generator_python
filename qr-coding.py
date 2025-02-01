import qrcode

# Ask the user to enter the text
text = input("Enter the text to generate QR code: ")

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(text)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill="black", back_color="white")

# Save the QR code image
img.save("qrcode.png")

# Show the QR code
img.show()

print("QR Code generated and saved as 'qrcode.png'!")
