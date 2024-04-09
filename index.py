#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        .logo{
            float: left;
            
           }
           h1{
            text-align: center;
           }
           .col-sm-6{
            text-align: center;
           }
           .dropdown-submenu {
  position: relative;
}

.dropdown-submenu .dropdown-menu {
  top: 0;
  right: 100%;
  margin-top: -1px;
}
h1
{
    color: brown;
    letter-spacing: 2px;
}
#admin{ 
 display: none;      
}
#Memplye{
    display: none;
}
.admin,.memplye
{
   
 border:white 1px solid;
 margin: 20px;
 background-color: #fff;
 box-shadow: rgba(122, 128, 112, 0.35) 0px 5px 15px;
 border-radius: 7px;
}
.form-group{
    margin: 40px;
}
.img{
    width: 40vw;
}
.main{
    background-image: url("./dbmedia/kevin-bhagat-zNRITe8NPqY-unsplash.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    margin-top: -20px;
}
input{
    border-style:none none solid none ;
    border-bottom-color:black ;
    width: 100%;
    font-weight: bolder;
    letter-spacing: 2px;
}
footer{
    border-top: 2px solid red;
    background-color: black;
    color: #fff;
}
p{
    text-align: center;
}
#fogetpassword{
    display: none;
}

               </style>
</head>
<body>
    <header>
        <div class="container-fluid">
            <div class="row" style="background-color: white;">
              <div class="col-sm-3"></div>
              <div class="col-sm-3"><img src="./dbmedia/download.png" alt="" class="img"></div>
              <div class="col-sm-3"></div>
            </div>
        </div>
    </header>
    <nav class="navbar" style="background-color:#00873E; border-bottom: 3px solid rgb(7, 158, 100);">
        <div class="container-fluid">
            <div class="nav navbar-nav navbar-right" style="margin: 10px 20px 0px 0px;">
                <div class="dropdown">
                    <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown"><span class="glyphicon glyphicon-log-in" style="margin-right: 5px;"></span>Login
                    <span class="caret"></span></button>
                    <ul class="dropdown-menu">
                      <li><a tabindex="-1" href="#" onclick="admin()"> Admin</a></li>
                      <li><a tabindex="-1" href="#" onclick="meploye()">Employee</a></li>
                    </ul>
                  </div>
         </div>
             
        </div>
    </nav>
    <main>
        <div class="container-fluid main"> <!--Conten load in this part-->
            <div class="row">
                <div class="col-sm-4">
                </div>
                <div class="col-sm-4">
                    <div id="admin">
                        <form action="./Admin.py" method="post" enctype="multipart/form-data" name="adminlogin" style="position: relative;" onsubmit=" return adminvalidation()">
                            <span id="remove" onclick="remove()" class=" glyphicon glyphicon-remove" style="position: absolute; top: 0px; right: 0px; margin-top: -18px; margin-right: 2px; background-color: brown; color: white; padding: 5px;"></span>
                            <h2 style="text-align: center;"> <span style="color:#DC143C;">  Admin</span> Login</h2>
                            <div class="form-group">
                                
                                <input type="text" name="userid" placeholder="userid" required  id="userid">
                            </div>
                            <div class="form-group">
                               
                                <input type="password" name="Password" placeholder="password'" required  id="pwd">
                            </div>
                            <div class="form-group">
                                <input type="submit" style="margin-right: 70px;" value="Login" class="btn btn-primary form-control value="Login">
                                
                               </ul>
                            </div>
                        </form>
                    </div>
                    <div id="Memplye">
                        <form method="post" enctype="multipart/form-data" name="empform" style="position: relative;">
                            <span id="remove" onclick="remove1()" class=" glyphicon glyphicon-remove" style="position: absolute; top: 0px; right: 0px; margin-top: -18px; margin-right: 2px; background-color: brown; color: white; padding: 5px;"></span>
                            <h2 style="text-align: center;"> <span style="color:#DC143C;"> Employee </span> Login </h2>
                            <div class="form-group">
                                
                                <input type="text" name="username" id="User id" placeholder="User id" required >
                            </div>
                            <div class="form-group">
                                
                                <input type="password" name="password" id="pwd" placeholder="password'" required>
                            </div>
                            <div class="form-group">
                                <a onclick="forgetpasswod()" style="color: blue;">Forget Password ? </a>
                            </div>
                            <div class="form-group">
                                
                                <input type="submit" style="margin-right: 70px;" name="login" class="btn btn-primary form-control" value="Login"id='login' >
                               
                               
                            </div>
                        </form>
                        <form method="post" enctype="multipart/form-data" id="fogetpassword">
                            
                                <div class="form-group">
                                
                                    <input type="email" name="Email" id="pwd" placeholder="Enter Email Id" required>
                                    <br><br>
                                    <input type="submit" style="margin-right: 70px;" name="submit" class="btn btn-primary form-control" value="submit" onclick="FOR()">
                               
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
                <div class="col-sm-4" style="height:500px;"></div>
            </div>
        </div>
    </main>
<div class="container-fluid footer">
    <div class="row" style="background-color:#98FB98;">
        <div class="col-sm-6">
            <p style="color:#0B6623;text-align: center; margin: 10px;">
                <span style="font-size: large; ">Vision</span> <br>
    Our vision is to develop constantly and grow into a
    major IT service provider. Thereby becoming a
    leading performer in providing quality web and
    software development solutions in the competitive
    global marketplace. We consistently usher our
    Customers towards success. We have the ability to
    accelerate and swiftly share the great work or
    products of your organization or business. We
    believe that these qualities will be the key to
    reaching our goal.</p>
</div>
<div class="col-sm-6">
 <p style="color:0B6623;text-align:center; margin: 10px;"><span style="font-size: large ;">Mission</span> <br>
            Techvolt Software Pvt.Ltd delivers its solutions
            through an empowered team of professionals.
            where all the me
            mbers are encouraged to innovate.
            explore, and take responsibility for their own growth
            both technically and professionally. Techvolt
            Software Pvt.Ltd, has an open work environment
            and culture that encourages personal and group
            achievement with a clear foCus on delivering
            customer satisfaction.</p>
        </div>
    </div>
</div>
<footer class="container-fluid">
    <div class="row">
    <div class="col-sm-4"></div>
    <div class="col-sm-4" >
        <P> <b>TECHVOLT SOFTWARE PVT.LTD</b></P>
        <P>Coimbatore,Tamil Nadu,India</P>
        <p>www.techvoltcoimbatore.com</p>
        <p>+91 84289839</p>
     </div>
    <div class="col-sm-4"><b></b></div>
    </div>
    <hr>
    <p style="text-align: center;">copyright <span class="glyphicon glyphicon-copyright-mark"></span> TECHVOLT SOFTWARE PVT.LID All rights resserved</p>
</footer>
<script>
    function adminvalidation(){
         let userid=document.forms["adminlogin"]["userid"];
         let pwd=document.forms["adminlogin"]["pwd"];
         if(userid.value=="Gowtham@"&&pwd.value=="1234@"){
            return true;
         }
         else{
            alert("Password Or UserId is Wrong");
            document.getElementById("userid").style.border="solid red";
            document.getElementById("pwd").style.border="solid red";
            return false;
         }
    }
    function forgetpasswod(){
        document.getElementById("fogetpassword").style.display='block';
        document.getElementById('login').style.display="none";
    }
    function  FOR(){
    document.getElementById("fogetpassword").style.display='none';
        document.getElementById('login').style.display="block";
    }
    
    function admin(){
        document.getElementById("admin").style.display="block";
        document.getElementById("admin").className="admin";
        document.getElementById("Memplye").style.display="none";
    }
    function remove() {
        document.getElementById("admin").style.display="none";  
    }
    function meploye(){
        document.getElementById("Memplye").style.display="block"
        document.getElementById("Memplye").className="memplye";
        document.getElementById("admin").style.display="none";
    }
    function remove1() {
        document.getElementById("Memplye").style.display="none";  
    }
    </script>
</body>
</html>

""")
import  cgi,cgitb,pymysql,smtplib
cgitb.enable()
con=pymysql.connect(host="localhost",password="",user="root",database="erp")
cur=con.cursor()
form=cgi.FieldStorage()
psubmit=form.getvalue("login")
if psubmit !=None:
    puser=form.getvalue("username")
    ppwd=form.getvalue("password")
    q="select EID,Department from employee1 where username='%s' and password='%s'"%(puser,ppwd)
    cur.execute(q)
    rec=cur.fetchall()
    if len(rec) !=0 :
        for i in rec:
            department=i[1]
            print(department)
            if department =='HR':
                print("""<script>
      location.href="HRmain.py?id=%s"
    </script>
    """%i[0])
            elif department=='Technical':
                print("""<script>
              location.href="Tech.py?id=%s"
            </script>"""%i[0])
            elif department=='Marketing':
                print("""<script>
              location.href="Marketingprofil.py?id=%s"
            </script>"""%i[0])
            elif department=='Finances':
                print("""<script>
              location.href="FainancesProfile.py?id=%s"
            </script>"""%i[0])
    else:
        print("""
        <script>
       alert("No user found")
         </script>
            """)
fsubmit=form.getvalue('submit')
if fsubmit !=None:
    if len(form) != 0:
     pemail=form.getvalue('Email')
     q1 = """select name,username,password,email from employee1 where email='%s'""" % (pemail)
     cur.execute(q1)
     rec1 = cur.fetchall()
    if  rec1:
        for j in rec1:
            name=j[0]
            username=j[1]
            password1=j[2]
            email=j[3]
        form_Add = "gowthamyouth2001@gmail.com"
        password = "bekchburtacmufex"
        to_addres = email
        subject = "Your login password"
        body = f"Eid:{name}\npassword:\n{password1}\n username:\n{username}"
        message = "subject:{}\n\n{}".format(subject, body)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(form_Add, password)
        server.sendmail(form_Add, to_addres, message)
        server.quit()
        print("""<script>alert("Your Loing Details Send Register E-mail")</script>""")
