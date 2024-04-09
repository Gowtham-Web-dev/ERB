#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import  cgi, cgitb,pymysql
cgitb.enable()
form=cgi.FieldStorage()
con1=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur1=con1.cursor()
Q="select * from vendor where Status='new'"
cur1.execute(Q)
rec1=cur1.fetchall()
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
thead{
        background-color: #a6f793f3;
        color: #000;
        font-family:  "Mulish", sans-serif;
    }
    tbody{
        background-color: rgb(177, 237, 230);
        border:#caeef1 2px solid;
        font-family:  "Mulish", sans-serif;
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
    top: 3px;
    right: 3px;
    cursor: pointer;
    color: #555;
    font-size: 16px;
    z-index: 3;

}
.card {
  width: max-content;
  background-color: #fff;
  overflow: hidden;
}

.card-img {
  width: 100%;
  height: auto;
}

.card-content {
  padding: 10px 10px 10px 40px;
}

.card-title {
}

.card-text {
  font-size: 1rem;
  color: #666;
  margin-bottom: 15px;
}

.btn {
  display: inline-block;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #0056b3;
}
.custom-list {
  list-style: none;
  padding: 0;
}

.custom-list li {
  padding: 2px 2px;
  border-bottom: 1px solid #ddd;
  position: relative; /* Required for positioning the image */
}

.custom-list li:last-child {
  border-bottom: none;
}

.custom-list li:hover {
  background-color: #f0f0f0;
}

.custom-list li::before {
  content: "";
  background-image: url('./dbmedia/list.png'); /* URL of your image */
  background-size: contain; /* Adjust image size as needed */
  background-repeat: no-repeat;
  width: 20px; /* Adjust image width */
  height: 20px; /* Adjust image height */
  display: inline-block;
  position: absolute;
  left: -30px; /* Adjust image position */
  top: 50%;
  transform: translateY(-50%);
  margin-right: 10px; /* Adjust spacing between image and text */
}
.btn {
  display: inline-block;
  font-size: 10px;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s, color 0.3s, border-color 0.3s;
}

.btn-primary {
  color: #fff;
  background-color: #007bff;
  border: 2px solid #007bff;
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}

.btn-primary:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.5);
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
                <a data-toggle="dropdown"  id="op"><span class="fa fa-user" ></span> Employee<span class="caret" style="margin-top: 10px;"></span></a>
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
                <a data-toggle="dropdown" id="op" style="background-color: #23395f; color: white; margin-left: -10px; margin-right: -8px; border-left:3px solid orange;"><i class="fa fa-users-line" style="color: #CFEEFF;"></i> Vendor<span class="caret" style="margin-top: 10px;"></span></a>
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
                </div><!--End-->    
""")
print("""
            <div id="Secount_continer_box">
 <div class="centered-form-container" id="popupForm" style="background-color: #fff; display:none; border-radius:10px;box-shadow: rgba(67, 71, 85, 0.27) 0px 0px 0.25em, rgba(90, 125, 188, 0.05) 0px 0.25em 1em; padding:20px">
                        <div class="close-button" onclick="toggleFormVisibility()">X</div>
                        <div class="card">
  <div class="card-content">
    <p class="card-title h1" style="color: #C04000; font-weight: 600; font-size: 24px; text-transform: uppercase; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);">Vendor Detail</p>

    <ul class="custom-list">
  <li id="name"></li>
  <li id="email"></li>
  <li id="pno"></li>
  <li id="organozation"></li>
  <li id="address"></li>
  <li id="city"></li>
  <li id="state"></li>
  <li id="pincode"></li>
  <li id="serivice"></li>
</ul>
  </div>
        <form method="post" enctype="multipart/form-data">
           <input type="hidden" name="id" id="id">
            <input type="submit" value="Aprrove" name="Approve" class="btn btn-primary form-control">
        </div>
    </form>
</div>
               <div class="row">
                <div class="col-sm-2 d-none d-lg-block d-xl-block"></div>
                <div class="col-sm-10">
                <h3 style="font-family: verdana;font-weight: bold;font-size: 20px;color: rgb(0, 208, 255);">New Vendor Details  </h3>
                    <table class="table">
                    <thead>
                        <tr>
                            <th style="display:none">Vendor ID</th>
                            <th>Name</th>
                            <th>Service Type</th>
                            <th>Organization</th>
                            <th>Address</th>
                            <th>Action</th>
                        </tr>
                    </thead> 
                    <tbody style="background-color:#fff">""")
for J in rec1:
    print("""
                        <tr>
                                
                                <td style="display:none"><input type ="number" name="vid" style="border:none;width:40px" readonly value="%s"></td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td><button class="btn btn-primary" onclick="openPopup('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')">view</button></td>
                                
                            </tr>""" % (J[0], J[1], J[9], J[4], J[6],J[0],J[1],J[2],J[3],J[4],J[5],J[6],J[7],J[8],J[9]))
print("""
                    </tbody>   
                    </table>
                </div>
               </div>          

            </div>

        </div>


    </div>

    <script>
    //------------------------------------------------Sayary------------------------------------//

            //----------------------------Time set event----------------------/
            var s=new Date()
            document.getElementById('time').innerHTML= +""+s.toLocaleString()
            //______________________________End______________________________//
        function openPopup(id,name,email,pno,organization,Address,city,state,pincode,service) {
        console.log(id)
        
        document.getElementById('id').value= id;
        document.getElementById('name').innerText = name;
        document.getElementById('email').innerText= email;
        document.getElementById('pno').innerText= pno;
        document.getElementById('organozation').innerText= organization;
        document.getElementById('address').innerText= Address;
        document.getElementById('city').innerText= city;
        document.getElementById('state').innerText = state;
        document.getElementById('pincode').innerText= pincode;
        document.getElementById('serivice').innerText= service;
        
        
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
updatestatus=form.getvalue('Approve')
if updatestatus !=None:
    VID=int(form.getvalue('id'))
    con = pymysql.connect(host="localhost", user="root", password="", database="erp")
    cur= con.cursor()
    Q="update vendor set Status='Approved' where VID ='%s'"%VID
    cur.execute(Q)
    con.commit()
    print("""<script>alert("Vendor Status Update)</script>""")

