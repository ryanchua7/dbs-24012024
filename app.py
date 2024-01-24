from flask import Flask,request,render_template 

app = Flask(__name__)
#Load all my objects into app

@app.route("/" , methods=["Get","POST"]) #Run this decorator first, before u run the function index, need to run this first. 
def index(): 
    if request.method == "POST" : 
        rate = float(request.form.get("rate")) #force it to a number, cast it to float. text to number
        return(render_template("<html>.html",result = (rate*-50.6)+90.2))
    else:
        return(render_template("<html>.html",result = "waiting for to key in the exchange rate"))
    
if __name__ == "__main__":
    app.run()
