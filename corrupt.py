def corruption_check(file):
    try:
        with open(file, 'r') as file:
            rd = file.read(512)

        if rd:
            return False
        else:
            return True

    except IOError:
        return True


file = "my-draw_EPC.xml"

if corruption_check(file):
    print("File is Corrupt")

else:
    print("File is Valid")
