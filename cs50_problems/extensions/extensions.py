user_input = input("File name: ").lower().strip()

match user_input:
    case user_input if user_input.endswith(".gif"):
        print("image/gif")
    case user_input if user_input.endswith(".jpg") or user_input.endswith(".jpeg"):
        print("image/jpeg")
    case user_input if user_input.endswith(".png"):
        print("image/png")
    case user_input if user_input.endswith(".pdf"):
        print("application/pdf")
    case user_input if user_input.endswith(".txt"):
        print("text/plain")
    case user_input if user_input.endswith(".zip"):
        print("application/zip")
    case _:
        print("application/octet-stream")