#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import  cgi, cgitb, pymysql,smtplib
import random
import string
cgitb.enable()
form=cgi.FieldStorage()
con=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur=con.cursor()
#######
q1="""select * from employee1 where status='%s'"""%('new')
cur.execute(q1)
rec1=cur.fetchall()
q2="""select * from employee1 where status='%s'"""%('approved')
cur.execute(q2)
rec2=cur.fetchall()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;400;500&display=swap" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="https://fontawesome.com/icons/person?f=classic&s=solid">

  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Audiowide">
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Mulish:ital,wght@0,200..1000;1,200..1000&display=swap" rel="stylesheet">
  <!--Font family-->
  <style>

   .Role,.Profile{ /* model style*/
        font-weight: bolder;
        color: #0a7ae4;
        font-size: 13px;
        font-family: "Mulish", sans-serif;

    }
    thead{
        background-color: #a6f793f3;
        color: #000;
        font-family:  "Mulish", sans-serif;
    }
    tbody{
        background-color: #fff;
        border:#caeef1 2px solid;
        font-family:  "Mulish", sans-serif;
    }
    table{
        box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
    }
    #main{
        display: flex;
        padding: 0;
    }
    #Sidebar_cover{
        position: fixed;
         top: -10px;
         z-index: 1;

        }
    #Sidebar_cover2{
        background-color:#fff; 
        height: max-content;
    }
    #LOGOUT_SM{
        font-weight: bold; color: red;
    }
    #first_content_box{
        background-color:#F3F5F9; height: 100vh;
    }
    #Secount_continer_box{
        padding: 40px;
         background-color:#F3F5F9;
    }
    #bars{
        padding: 10px;
         background-color:black;
    }
    .profil img{
        margin: 20px 20px 0px 100px;
        border: rgb(231, 95, 4) 5px solid;
    }    

    .detial   h3{
        font-family: Arial, Helvetica, sans-serif;
        font-weight: bold;
        margin-top: -5px;
        text-align: center;
       color: rgb(12, 7, 3);
        text-decoration: none;
    }
    p{ 
        color: black;
        font-weight: bold;
        text-align: center;
    }
    .profil{
        background-color:#7ee5f2d3;
        border-radius: 10px 10px 0px 0px;
        margin-bottom: 5px;
        height: 120px;
    }

    .detial{
        margin-top: 55px;
    }
    /* Salay Calculation table Style*/
        #a{
        text-decoration: none; 
        color: #111111;
         font-weight: bold;
         padding: 5px;
         font-family: "Mulish", sans-serif;
         font-size: 14px;
    }
    #a:hover{
        background-color:#CFEEFF;
        border-radius: 7px;
        color: #23395f;


    }
    a{
    display: flex;

}
.mynav{
    color: rgba(14, 230, 230, 0.74);
}

.mynav li a {
    color: #0e0d0d;
    text-decoration: none;
    width: 100%;
    display: block;
    border-radius: 5px;
    padding: 30px 5px;
}
#Sidebar{
    width: 215px; padding: 15px ;
     background-color: rgb(239, 241, 241);  
    height: 100vh;

}
.mynav li a i{
    width: 30px;
    padding: 10px;

}
#time{
    font-weight: bold;
    word-spacing: 2px;
    color:#27B376;
}
#op{
    background-color: none;
    padding: 5px;
    padding-top: 5px;
    color: #0c0c0c;
    font-weight: bold;
    font-family: "Mulish", sans-serif;
    font-size: 14px;
    margin-top: 5px;

}
#op:hover{
    background-color:#CFEEFF;
    border-radius: 7px;
    color: #0a7ae4;



}


li{
    list-style: none;
    font-size: larger; 
}
#hr{
    background-color: rgb(12, 12, 12);
    height: 2px;
}

.fa{
    margin: 0px 10px 0px 5px;
}
h2{
        font-family:'Audiowide',sans-serif;
    }
#TOP{
    padding: 10px;
    background-color:#23395f;
    border-bottom: 1px solid #4ea2cb;
    color: white;
    font-weight: bold;
}
#TOP img{
    border-radius: 50%;
    margin: 2px;
    border: 2px solid orange;
}
#TOP i{
    margin: 2px;
}
#Logout_TIME{
    display: flex;
    float: right;
}
#Logout_TIME #LOGOUT{
    color: #000;
     font-family:"Mulish", sans-serif;; 
     margin-left: 20px;
     font-size: 14px;
     font-weight: bold;


}
#LOGOUT:hover{
    text-decoration: none;

}
#time{
    font-size: 14px;
    font-weight: bold;
    color: #0ec5d2;
}
#Dashbord_Head{
    padding: 10px;
     background-color: white;
}
li .fa{
    color: #23395f;
}
.log_icons{

    color: rgba(231, 25, 25, 0.979);

   font-weight: bolder;
    margin-top: 2px;
    margin-right: 2px;
}
body, html {
    margin: 0;
    padding: 0;
    height: 100%;
    
}

.blur-background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5); /* Adjust the transparency here */
    backdrop-filter: blur(8px); /* Adjust the blur intensity here */
    z-index: 1;
}

.centered-form-container {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 2;
}
.close-button {
    position: absolute;
    top: 10px;
    right: 10px;
    cursor: pointer;
    color: #555;
    font-size: 24px;
    z-index: 3;
}


.heading {
  font-family: 'Mulish', sans-serif;
  font-size: 28px;
  font-weight: bold;
  color: #007bff; /* Primary color */
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2); /* Adding shadow for depth */
}

  </style>
</head>
<body>
    <div class="container-fluid "><!--log image and Name-->
        <div class="row">

        <div class="col-sm-5 d-md-none "><img src="./dbmedia/download.png" alt=""  width="100%"></div>
        <div class="col-sm-4"></div>
        <div class="col-sm-3"></div> 
    </div>
</div>
<div class="container-fluid d-none d-lg-block d-xl-block text-right" id="TOP"><i></i><span class="text xm-text">Welcome :ADMIN</span></div>

    <div class="container-fluid" id="main">
        <div id="Sidebar_cover">
    <div id="Sidebar_cover2">
        <!--SideBar Start-->
        <div id="Sidebar" class="d-flex flex-column  offcanvas-md offcanvas-start " >
           <div>
            <h2 style="color: #ff8f00;"> TECHVOLT  <span style="color: #23395f;">SOFTWARE</span></h2>
            <hr id="hr">
            <h3 class="Profile">Admin</h3>

            <li><div class="dropdown">
                <a data-toggle="dropdown"  id="op"  style="background-color: #23395f; color: white; margin-left: -10px; margin-right: -8px; border-left:3px solid orange;" ><span class="fa fa-user" class="fa fa-user"style="color: #CFEEFF;" ></span> Employee<span class="caret" style="margin-top: 10px;"></span></a>
                <ul class="dropdown-menu">
                     <li><a href="./AD_newemp.py">New <span class="fa  fa-user-plus"></span></a></li>
                    <li><a href="./AD_existingemp.py"> Existing </a></li>
                </ul>
            </div>
            </li>
            <li><div class="dropdown">
                <a data-toggle="dropdown"  id="op" ><i class="fa fa-person-walking-arrow-right"></i></span>Leave<span class="caret" style="margin-top: 10px;"></span></a>
                <ul class="dropdown-menu">
                     <li><a href="./AD_leaverequest.py" target="_self"> New <span class=""></span></a></li>
                    <li><a href="./AD_leaverequestappro.py" target="_self"> Existing </a></li>
                </ul>
            </div>
            </li>
            <li ><a href="AD_client.py" id="a"> <i class="fa fa-users"></i>client</a></li>
            <li><div class="dropdown">
                <a data-toggle="dropdown" id="op"><i class="fa fa-users-line"></i> Vendor<span class="caret" style="margin-top: 10px;"></span></a>
                <ul class="dropdown-menu">
                     <li><a href="./AD_venter.py">New<span class="fa  fa-plus"></span></a></li>
                    <li><a href="./AD_existingventer.py">Existing</a></li>
                </ul>
            </div></li>

            <li><a href="./AD_expenses.py" id="a"><i class="fa fa-money-bill"></i> Expenses</a></li>
            <li><a href="./AD_Income.py" id="a" ><i class="fa fa-sack-dollar"></i> Income</a></li>
            
    <li><div class="dropdown">
        <a data-toggle="dropdown"  id="op"><span class="fa fa-bell"></span>Announcement<span class="caret" style="margin-top: 10px;"></span></a>
        <ul class="dropdown-menu">
             <li><a href="./AD_Announcementform.py" target="_self">New <span class="fa  fa-plus"></span></a></li>
            <li><a href="./AD_Announcementstatus.py" target="_self">  Existing </a></li>
        </ul>
    </div>
    </li>
    <hr id="hr" class="d-md-none">
    <li><a href="index.py" id="LOGOUT_SM" class="d-md-none"> <i class="glyphicon glyphicon-log-out log_icons "></i class="glyphicon glyphicon logout"> Logout</a></li>

          </div>
        </div><!-- Sidebar End-->
    </div>
        </div>
        <div class="flex-fill" id="first_content_box">
            <div class=" d-md-none  text-white " id="bars">
                <a href="#" class="text-white" data-bs-toggle="offcanvas" data-bs-target="#Sidebar">
                    <i class="fa-solid fa-bars"></i>
                </a>
            </div>
            <div class="container-fluid d-none d-lg-block d-xl-block " id="Dashbord_Head" ><!--Time-->
                <i class="text-info" style="margin: 220px;">Admin Dash Bord</i>
                <div id="Logout_TIME">
                <li id="time"></li>
                <li><a href="index.py" id="LOGOUT"> <i class="glyphicon glyphicon-off log_icons"></i class="glyphicon glyphicon logout"> Logout</a></li>
                </div>
                </div><!--End-->    """)

print("""
            <div id="Secount_continer_box">
            

            <div class="centered-form-container" id="popupForm" style="background-color: #fff; display:none; border-radius:10px;box-shadow: rgba(67, 71, 85, 0.27) 0px 0px 0.25em, rgba(90, 125, 188, 0.05) 0px 0.25em 1em; padding:20px">
                        <div class="close-button" onclick="toggleFormVisibility()">X</div>
                        
                        <form method="post" enctype="multipart/form-data">
        <h3 class="text-primary heading">Employee Approve Form</h3>
            <div class="form-group">
            
                <label for="name">Name:</label>
                <input type="text" class="form-control" id="name" name="name" readonly>
            </div>
            <div class="form-group">
                <input type="email" class="form-control" id="email" name="email" readonly style="display:none">
            </div>
            <div class="form-group">
                <label for="department">Department:</label>
                <input type="text" class="form-control" id="department" name="department" readonly>
            </div>
            <div class="form-group">
                <label for="role">Role:</label>
                <input type="text" class="form-control" id="role" name="role" readonly>
            </div>
            <div class="form-group">
                <label for="join"> Date Of Join:</label>
                <input type="text" class="form-control" id="join" name="join" readonly>
            </div>
            <div class="form-group">
                <label for="salary">Salary:</label>
                <input type="number" class="form-control" id="salary" name="salary" readonly>
            </div>
            <div class="form-group" style="display:none">
                <label for="experience">Qualification:</label>
                <input type="text" class="form-control" id="Qualifiaction" name="Qualifiaction" readonly>
            </div>
            <div class="form-group" style="display:none">
                <label for="experience">Gender:</label>
                <input type="text" class="form-control" id="gender" name="gender" readonly>
            </div>
            <div class="form-group" style="display:none">
                <label for="city">City:</label>
                <input type="text" class="form-control" id="city" name="city" readonly>
            </div>
            <div class="form-group" style="display:none">
                <label for="state">State:</label>
                <input type="text" class="form-control" id="state" name="state" readonly>
            </div>
            <div class="form-group">
                <input type="hidden" class="form-control" id="eid" name="eid" readonly>
            </div>
            
            <div class="form-group">
                <label for="branch">Branch:</label>
                <input type="text" class="form-control" id="branch" name="branch" readonly>
            </div>
            <br>
            <div class="form-group">
            <input type="submit" value="Aprrove" name="Approve" class="btn btn-primary form-control">
        </div>
    </form>
</div>
                <div class="container-fluid" id="Employees_table"> <!--Employee Table-->
                    <div class="row">
                    <div class="col-md-2"></div>
                    <div class="col-md-10">
                    <h3 style="font-family: verdana;font-weight: bold;font-size: 20px;color: rgb(0, 208, 255);">New Employee Details</h3>
                    <table class="table">
    <thead style="font-size: x-small;">
        <th>ID No</th>
        <th>Name</th>
        <th>Department</th>
        <th>Designation</th>
        <th>Email</th>
        <th>Phone Number</th>
        <th>Action</th>
    </thead>
    <tbody>
""")


for j in rec1:

    print("""

                        <tr>
                        <td><input type="number" required name="IDS" value="%s" readonly style="border:none;width:35px"></td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td><input type="text" name="email" value="%s" readonly style="border:none;width:210px"></td>
            <td>%s</td>
            <td><button class="btn btn-primary" onclick="openPopup('%s', '%s','%s', '%s', '%s', '%s', '%s','%s','%s','%s','%s','%s')">view</button></td>
        </tr>
    """% (j[0], j[1], j[8], j[10], j[2], j[3], j[0],j[1], j[8], j[10], j[9], j[11], j[15],j[13],j[14],j[6],j[5],j[2]))
print("""
                         
                        </tbody>
                    

                    </table>
                    <h3 style="font-family: verdana;font-weight: bold;font-size: 20px;color: rgb(0, 208, 255);">Existing Employee Details</h3>
                    <table class="table" >
                        <thead style="font-size: x-small;">
                            <th>ID No</th>
                            <th>Name</th>
                            <th>Department</th>
                            <th>Designation</th>
                            <th>email</th>
                            <th>Phone Number</th>
                            <th> View More</th>
                        </thead>
                         
""")
print("""<tbody>""")
for j in rec2:

    print("""
                       
                        <tr>
                        <form   method="post" enctype="multipart/form-data">
                            <td><input type="text"required name="ID" value="%s" readonly style="border:none;width:35px"></td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td><input type="submit" name="view" value="&#128065" style="font-size:30px;background:none;border:none;color:blue"></td>
                         </form>  
                         </tr> 
                       
                       """%(j[0],j[1],j[8],j[10],j[2],j[3]))
print("""</tbody>
                </div>
                    </div>
                 </div><!--End--> 

            </div>

        </div>


    </div>

    <script>
    //------------------------------------------------Sayary------------------------------------//

            //----------------------------Time set event----------------------/
            var s=new Date()
            document.getElementById('time').innerHTML= +""+s.toLocaleString()
            //______________________________End______________________________//
            function openPopup(ID,name, department, role,Barch,salary, join, city, state, Qualifiaction, gender,email) {
        document.getElementById('name').value = name;
        document.getElementById('department').value = department;
        document.getElementById('role').value = role;
        document.getElementById('join').value = join;
        document.getElementById('salary').value = salary;
        document.getElementById('Qualifiaction').value = Qualifiaction;
        document.getElementById('city').value = city;
        document.getElementById('state').value = state;
        document.getElementById('gender').value = gender;
        document.getElementById('eid').value = ID;
        document.getElementById('branch').value = Barch;
        document.getElementById('email').value = email;
        
        document.getElementById('popupForm').style.display = 'block';
    }
    document.addEventListener('DOMContentLoaded', function() {
    var popupForm = document.getElementById('popupForm');
    var blurBackground = document.getElementById('blurBackground');
    
    // Function to toggle the visibility of the form and blur background
    function toggleFormVisibility() {
        popupForm.style.display = (popupForm.style.display === 'none') ? 'block' : 'none';
        blurBackground.style.display = (blurBackground.style.display === 'none') ? 'block' : 'none';
    }

    // Toggle form visibility when clicking the background
    blurBackground.addEventListener('click', toggleFormVisibility);

    // Call the toggle function to hide the form initially
    toggleFormVisibility();
});
function toggleFormVisibility(){
document.getElementById('popupForm').style.display="none";
}

        </script>
</body>
</html>""")
### aprove
Approve=form.getvalue('Approve')
if Approve !=None:
  EID=form.getvalue("eid")
  email=form.getvalue('email')
  print(EID)
  con4 = pymysql.connect(host="localhost", user="root", password="", database="erp")
  cur4 = con4.cursor()
  I = """select MAX(EID) from employee1 where status='approved' """
  cur4.execute(I)
  rec4 = cur4.fetchone()
  if rec4[0] != None:
      n = rec4[0]
  else:
      n = 0
  z = ""
  if n <= 9:
      z = "000"
  elif n == 10 or n <= 99:
      z = "00"
  elif n > 99 or n <= 999:
      z = "0"
  userID = "user24"+z + str(n + 1)
  password1 = random.randint(100000,999999)
###Update the userid and password
  con2 = pymysql.connect(host="localhost", user="root", password="", database="erp")
  cur2 = con2.cursor()
  up= """update employee1 set status='approved',password='%s',username='%s' where EID='%s'"""%(password1,userID,EID)
  cur2.execute(up)
  con2.commit()
  form_Add = "gowthamyouth2001@gmail.com"
  password = "bekchburtacmufex"
  to_addres = email
  subject = "Your login password"
  body = f"Eid:{EID}\npassword:\n{password1}\n username:\n{userID}"
  message = "subject:{}\n\n{}".format(subject, body)
  server = smtplib.SMTP("smtp.gmail.com:587")
  server.ehlo()
  server.starttls()
  server.login(form_Add, password)
  server.sendmail(form_Add, to_addres, message)
  server.quit()
  print("""<script>alert("Employee Approved")</script>""")

view=form.getvalue("view")
if view !=None:
     Id=form.getvalue("ID")
     print("""<script>
           location.href="AD_card.py?ID=%s"
         </script>
         """ %Id)
