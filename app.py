#import flask library
from flask import Flask, request,render_template

#s2 create a flask object and pass __name__
app= Flask(__name__)

Notes=[]

#s3 create a route and bind it to a function
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=="POST":
        Note=request.form.get("Note")
        if Note:
             Notes.append(Note)
    return render_template("home_page.html",Notes=Notes)

#s4 Run the application
if __name__=='__main__':
    app.run(debug=True)