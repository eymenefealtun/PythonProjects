import pyqrcode

url = input("enter url in order to generate the qr code: ")

qr_code = pyqrcode.create(url);
qr_code.svg('qrcode.svg',scale=5);