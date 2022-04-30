# import qrcode

# link = "https://github.com/Atanas809"

# qr = qrcode.QRCode(
#     version=3,
#     box_size=3,
#     border=4)

qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='red')
img.save('qrcode001.png')
