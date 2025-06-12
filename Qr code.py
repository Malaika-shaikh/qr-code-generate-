import qrcode

myqr = qrcode.make("https://www.behance.net/shaikhusama3")
myqr.save("myqr.png",scale = 8)
