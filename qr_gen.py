import qrcode
while True:

    data = input("enter the link: ")
    if data.lower() == "exit":
        break

    qr = qrcode.make(data)

    qr.save(input("name the file: "))

    print("qr code created successfully")
