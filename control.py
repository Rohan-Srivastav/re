from flask import *
from flask_sqlalchemy import *
from datetime import timedelta
global us,pas,Email
'''def encrypt(x):
    p="abcdefghijklmnopqrstuvwxyz"
    ni="0123456789"
    x=list(x) 
    p=list(p)
    ni=list(ni)
    for i in x:
        if i in p:
            x.index(i)=x[x.index(i)+2]'''
app = Flask(__name__) 
app.secret_key="danke Toni8"
app.permanent_session_lifetime=timedelta(minutes=10)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)
class users(db.Model):
    num=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(500))
    Email=db.Column(db.String(900))
    passw=db.Column(db.String(400))
    def __init__(self,name,Email,passw):
        self.name=name
        self.Email=Email
        self.passw=passw
@app.route('/loginpage/')
def login():
    if request.method=="POST":
        us=request.form["username"]
        em=request.form["Email"]
        pas=request.form["password"]
        a=users.query.filter_by(name=us).first()
        b=users.query.filter_by(Email=em).first()
        c=users.query.filter_by(passw=pas).first()
        if a and b and c:
            session["us"]=us
            session["em"]=em
            session["pas"]=pas
            return redirect(url_for("jk"))
        else:
            return render_template("loginpage.html")

    return render_template("loginpage.html")
@app.route('/')
def seefirst():
    return render_template("homepage.html")
@app.route('/workez/')
def work():       
    us=request.form["username"]
    em=request.form["Email"]
    pas=request.form["password"]
    a=users.query.filter_by(name=us).first()
    b=users.query.filter_by(Email=em).first()
    c=users.query.filter_by(passw=pas).first()

    if ("us"in session )and a and b and c:
        us=request.form["username"]
        em=request.form["Email"]
        pas=request.form["password"]
        session["us"]=us
        session["em"]=em
        session["pas"]=pas
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> JPBM Student Portal</title>
    <style>
        body {
    font-family: 'Montserrat', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
    display: flex;
}

.header {
    background-color: #000000;
    color: black;
    padding: 10px;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1000;
    border-bottom: 2px solid black;
}

.header .logo {
    height: 50px;
    margin-right: 20px;
}

.sidebar {
    width: 250px;
    position: fixed;
    top: 0;
    left: 0;
    background-color: #2c3e50;
    padding-top: 100px;
    height: 100%;
    color: white;
    overflow-y: auto;
    border-right: 3px solid black;
}

.sidebar a {
    padding: 15px 20px;
    text-decoration: none;
    color: white;
    display: block;
    font-size: 16px;
    border-bottom: 1px solid black;
}

.sidebar a:hover {
    background-color: #34495e;
}

.sidebar a i {
    margin-right: 10px;
}

.main-content {
    margin-left: 260px;
    padding: 20px;
    padding-top: 120px;
    width: calc(100% - 260px);
}

.profile-card {
    display: flex;
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    align-items: center;
    border: 2px solid black;
}

.profile-photo {
    border-radius: 50%;
    width: 150px;
    height: 150px;
    margin-right: 20px;
    border: 2px solid black;
}

.profile-info {
    flex: 1;
}

.profile-info h2 {
    margin-top: 0;
    color: #3b5998;
}

.profile-info p {
    margin: 5px 0;
    color: #555;
}

.edit-btn {
    background-color: #000000;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    border: 1px solid black;
}

.edit-btn:hover {
    background-color: #2c3e50;
}

.section {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    border: 2px solid black;
}

.section h2 {
    margin-top: 0;
    color: #000000;
}
    </style>
</head>
<body>
    <div class="header">
        <img src="https://cdnimages.myclassboard.com/loginpages/jaipuriaschool_assets/Images/Seth_Jaipuria_logo.png" alt="School Logo" class="logo">
        <h1><font color="white"> Jaipuria Personalized Board of Management </font></h1>
        <a href="/logout"><button style="float: right;"> logout<button></a>
    </div>
    <div class="sidebar">
        <a href="/workez/"><i class="fas fa-home"></i> Student Home</a>
       <a href="/workez/"><i class="fas fa-home"></i> Student Home</a>
    </div>
    <div class="main-content">
        <div class="profile-card">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/68/Taj_Mahal%2C_Agra%2C_India.jpg" alt="Student Photo" class="profile-photo">
            <div class="profile-info">
                <h2>Demo Account</h2>
                <p><strong>Name:</strong>'''+str(us) +'''</p>
                <p><strong>Email</strong>'''+str(em)+'''</p>
                <p><strong>Volunteered for</strong>'''+str()+'''</p>
                <button class="edit-btn">Edit Details</button>
            </div>
        </div>
        <div class="section announcements">
            <h2>Announcements</h2>
            <p>No new announcements.</p>
        </div>
    </div>
</body>
</html>'''
    else:
        return redirect(url_for("homepage"))
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)