print("Hii Pilot")
altitude = int(input("Enter the altitude:"))
if altitude <= 1000:
    if altitude == 1000:
        print("Hey Pilot your altitude is",altitude,"ft, you can land now.")
    else:
        print("Hey Pilot land your plane now,your altitude is",altitude,"ft.")
elif altitude < 5000:
    print("Hey Pilot your altitude is",altitude,"ft,pls come down to 1000 ft.")
else:
    print("Hey Pilot currently your altitude is",altitude,"ft,go around and try later.")
