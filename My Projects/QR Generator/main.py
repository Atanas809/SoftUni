# That's my qr generator project
# You can try it out with your own link and make QR code!

import qrcode

link = "https://github.com/Atanas809"

qr = qrcode.QRCode(
    version=3,
    box_size=3,
    border=4)

qr.add_data(link)
qr.make(fit=True)
