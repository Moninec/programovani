pozdrav = "ahoj"

if pozdrav == "ahoj":
    print("ahoj")
elif pozdrav == "čau":
    print("čau")


match pozdrav:
    case "ahoj":
        print("ahoj")
    case "čau":
        print("čau")
    case "zdar":
        print("zdar")
    case _:
        print("huh?")