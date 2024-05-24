from flask import Flask, render_template,request,url_for,redirect,session
import pymongo ,bcrypt
import urllib.parse

# Escape username and password according to RFC 3986
username = urllib.parse.quote_plus("i21ma055")
password = urllib.parse.quote_plus("Registration@dbmongo123")


app = Flask(__name__)
app.secret_key = 'testing'
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.fdcvxqm.mongodb.net/")
db = client.get_database('total_recodrs')

records = db.register


@app.route("/",methods=['GET','POST'])
def index():
    if "name" in session and "email" in session:
        return redirect(url_for("logged_in"))
    return render_template("home.html")

@app.route("/register",methods=['GET','POST'])
def register():
    message = ''
    if "name" in session and "email" in session:
        return redirect(url_for("logged_in"))
    if request.method == 'POST':
        user = request.form.get("fullname")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user_found = records.find_one({"name":user})
        email_found = records.find_one({"email":email})
        if user_found:
            message = 'User already exists'
            return render_template('index.html',message=message)
        elif email_found:
            message = 'Email already exists'
            return render_template('index.html',message=message)
        elif password1 != password2:
            message = 'Passwords does not match'
            return render_template('index.html',message=message)
        else:
            hashed = bcrypt.hashpw(password2.encode('utf-8'),bcrypt.gensalt())
            user_input ={'name':user,'email':email,'password':hashed}
            records.insert_one(user_input)
            
            user_data = records.find_one({"email":email})
            new_email = user_data['email']

            return render_template('logged_in.html',email=new_email)
    return render_template('index.html')

@app.route("/login",methods=['GET','POST'])

def login():
    message = 'Please login to your account'
    if "email" in session:
        return redirect(url_for("logged_in"))
    
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        email_found = records.find_one({"email":email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']
            if bcrypt.checkpw(password.encode('utf-8'),passwordcheck):
                session["name"]  = email_found['name']
                session['email'] = email_val
                return redirect(url_for('logged_in'))
            else:
                message = 'Wrong password'
                return render_template('login.html',message=message,email=email)
        else:
            message = 'Email not found'
            return render_template('login.html',message=message)
    return render_template('login.html',message=message)

@app.route("/logged_in")

def logged_in():
    if "email" in session and "name" in session:
        email = session['email']
        user = session['name']
        return render_template('logged_in.html',email=email,user=user)
    else:
        return redirect(url_for('login'))
    
@app.route("/logout")
def logout():
    if "email" in session:
        print(session["email"])
        session.pop("email",None)
        session.pop("name",None)
        return render_template('signout.html')
    else:
        return render_template('home.html')
    

if __name__ == "__main__":
  app.run(debug=True)
