file_name = input("File name: ")
if file_name.lower().strip().endswith(".gif"):
    print("image/gif")
elif file_name.lower().strip().endswith((".jpg","jpeg")):
    print("image/jpeg")
elif file_name.lower().strip().endswith(".png"):
    print("image/png")
elif file_name.lower().strip().endswith(".pdf"):
    print("application/pdf")
elif file_name.lower().strip().endswith(".txt"):
    print("text/plain")
elif file_name.lower().strip().endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
