from flask import Flask, render_template

app=Flask(__name__)
# app.run(host='0.0.0.0',port=120) we can change IP and port number but mostly we use which is
# provided by defualt
#app Routing --> means mapping the  URLs to a specific function and that function helps to display content or webpage.
#www.example.com/ --> home page
#www.example.com/aboutus --> about page
#    url        /end point

# to bind a functon to a URL path we can use the app.route decorator.
#Syntax: @app.route('EndPoint')
#def FunctionName():
# return "Messege"


# @app.route('/')
# def home():
#     return "home.html"

# @app.route('/about')
# def aboutUS():
#     return "about us"
# @app.route('/contact')
# def con():
#     return "contact us"




#render_template() --> used to redirect on html web page

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def con():
    return render_template('contact.html')

app.run(debug=True)




