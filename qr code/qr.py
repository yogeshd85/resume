import qrcode
img = qrcode.make('https://www.instagram.com/')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")