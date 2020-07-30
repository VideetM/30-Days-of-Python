from formatting import format_msg
from datetime import datetime
import sys
import requests

 
def send(name,website=None,versbose=False):
    if website != None:
        msg = format_msg(my_name=name,my_website=website)
    else :
        msg = format_msg(my_name=name)
    if versbose:
        print(name,website)

    #send message
    r = requests.get("http://httpbin.org/json")
    if r.status_code == 200:
        return r.json()
    else:
        print("There was a error")

if __name__ == "__main__":
    print(sys.argv)
    name ="Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    response = send(name, versbose=True)
    print(response)