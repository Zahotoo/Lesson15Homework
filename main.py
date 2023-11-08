#Homework
#So you know that on the internet certain codes have certain meanings for example 404= "Page not found".
# I want you to make a function called errorcode(x) that tells you the meaning of the error for example errorcode(404) prints "page not found".
# You do not need to do it for ALL the codes, but do it for SOME of the codes. Try to do at least 5 codes.

x = int(input("Please enter an error code, I can tell you the code's meaning. "))
def errorcode(x):
    match x:
        case 403:
            print("Page forbidden.")
        case 404:
            print("Page not found.")
        case 502:
            print("Bad Gateway")
        case 503:
            print("Service Unavailabe")
        case 406:
            print("Not Acceptable")
#TESTING
#errorcode(403)
#errorcode(404)
#errorcode(502)
#errorcode(503)
#errorcode(406)

errorcode(x)

quit()

