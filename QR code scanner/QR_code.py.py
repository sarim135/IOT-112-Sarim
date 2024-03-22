import qrcode as qr
img = qr.make("03095134177")
img.save("my_qr_number.png")