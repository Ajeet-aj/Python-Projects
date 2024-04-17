# import modules
import qrcode


# Give any link to Generate QRcode
url = "https://replit.com/@ajeet9717865417"

# Give box-size or border 
qr = qrcode.QRCode(version=1,
               error_correction=qrcode.constants.ERROR_CORRECT_H,
               box_size=10, border=5)


qr.add_data(url)

qr.make(fit=True)

# fill any color to make QRcode beautiful
img=qr.make_image(fill_color="green",
                 back_color="white")


# Save QRcode to image png or jpg
img.save("Name of image.png")