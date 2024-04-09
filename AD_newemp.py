#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import  cgi, cgitb, pymysql
cgitb.enable()
form=cgi.FieldStorage()
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
    #form{
    border: 2px solid white;
     background-color: white;
      border-radius: 2px;
     box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
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
#Head_form {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  border-bottom: 2px solid #007bff;
  padding-bottom: 5px;
  margin-bottom: 20px;
  text-transform: uppercase;
  letter-spacing: 2px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
   font-size: 24px;
  font-weight: bold;
  color: #007bff; /* Blue color */
  border-bottom: 2px solid #007bff; /* Blue border bottom */
  padding-bottom: 10px;
  margin-bottom: 20px;
}


  </style>
</head>
<body>
    <div class="container-fluid "><!--log image and Name-->
        <div class="row">
        
        <div class="col-sm-5 d-md-none "><img src="./media/download.png" alt=""  width="100%"></div>
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
                <a data-toggle="dropdown"  id="op" style="background-color: #23395f; color: white; margin-left: -10px; margin-right: -8px; border-left:3px solid orange;"><span class="fa fa-user"style="color: #CFEEFF;" ></span> Employee<span class="caret" style="margin-top: 10px;"></span></a>
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
                </div><!--End-->    
                
            <div id="Secount_continer_box">
                <div class="row" id="newemp"> <!--Add Employee Form Table-->          
                    <div class="col-sm-5"></div>
     <div class="col-sm-3" id="form" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 8px;">  
         <form   method="post" enctype="multipart/form-data">
             <legend id="Head_form">Employee Details</legend>
                  
             <div class="form-group">
                 <div class="input-group">
                <div class="input-group-addon" ><span class="fa fa-user"></span></div>
                     <input type="text" placeholder="Name" required name="name" class="form-control">
                 </div>
                 </div>
             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-envelope"></i></div>     
                     <input type="email" placeholder=" E-mail " required name="email" class="form-control">
             </div>
                 </div>
             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-phone"></i></div>     
                     <input type="tel" placeholder="Phone Number" required name="phno" pattern="[986][0-9]{9}"title="please Enter correct formet" class="form-control" id="PNO" onchange="pno()">
                 </div>
                 </div>
             <div class="form-group">
                 <label for="DOB">DOB</label>
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-calendar-days"></i></div>     
                 <input type="date" placeholder="Enter the DOB" required name="DOB" class="form-control">
                 </div>
             </div>
             <div class="form-group">
                 <label for="gender">Gender</label><br>
                 <input type="radio"  required name="gender"  value="male">Male
                 <input type="radio"  required name="gender"  value="female">Female
             </div>

             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-graduation-cap"></i></div>     
                 <select required name="Qualification" class="form-control">
                     <optgroup label="Ug">
                         <option selected disabled>Qualification</option>
                         <option value="BSC">BSC</option>
                         <option value="BCA">BCA</option>
                         <option value="B.COM">B.COM</option>
                         <option value="BBA">BBA</option>
                         <option value="BA">BA</option>
                         <option value="BE">BE</option>
                         <option value="B.TECH">B.TECH</option>
                     </optgroup>
                     <optgroup label="Pg">
                         <option value="MSC">MSC</option>
                         <option value="MCA">MCA</option>
                         <option value="M.COM">M.COM</option>
                         <option value="MBA">MBA</option>
                         <option value="ME">ME</option>
                         <option value="M.TECH">M.TECH</option>
                     </optgroup>
                     </select>
                 </div>
                 </div>
             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-briefcase"></i></div>     
                 
                 <select required name="Experiance" class="form-control">
                     <option selected disabled>Experience</option>
                         <option value="Fresher">Fresher</option>
                         <option value="1">1</option>
                         <option value="2">2</option>
                         <option value="3">3</option>
                         <option value="above3year">above 3 year</option>
                </select>
                 </div>
             </div>       
             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-diagram-project"></i></div>   
                 <select required name="Department" class="form-control">
                         <option selected disabled>Department</option>
                         <option value="Marketing">Marketing</option>
                         <option value="Technical">Technical</option>
                         <option value="Finances">Finances</option>
                         <option value="HR">HR</option>
                </select>
                 </div>
             </div>
             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-code-branch"></i></i></div>     
                 <select required name="branch" class="form-control">
                 <option selected disabled>Branch</option>
                 <option value="Erode">Erode</option>
                 <option value="Chennai">Chennai</option>
                 <option value="karur">Coimbatore</option>
                 <option value="mathurai">Karur</option>
                </select>
                </div>
             </div>
             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon"><i class="fa fa-circle-user"></i></div>
                 <select required name="role" class="form-control">
                     <option selected disabled>Role</option>
                 <option value="Executive">Marketing Executive</option>
                 <option value="Accountent">Accountent</option>
                 <option value="Manager">Manager</option>
                 <option value="JavaDeveloper">Java Developer</option>
                 <option value="PythonDeveloper">Python Developer</option>
                 <option value="PHPDeveloper">PHP Developer Developer</option>
                 <option value="Hr">Hr</option>
                </select>
                </div>
             </div>
             <div class="form-group">
                 <label for="Dateofjoin">Date Of Join</label>
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-calendar-week"></i></div> 
                 <input type="date" placeholder="Date of Join" required name="Dateofjoin" class="form-control">
                 </div>
             </div>

             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-money-bill-1-wave"></i></div> 
                 <input type="number" placeholder="Salary" required name="salary" class="form-control">
                 </div>
             </div>      
             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-bank"></i></div> 
                 <input type="text" placeholder="Bank" required name="bank" class="form-control">
                 </div>
             </div>
             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-bank"></i></div> 
                 <input type="text" placeholder="IFSC Code" required name="IFSC_CODE" class="form-control">
                 </div>
             </div>   
             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-bank"></i></div> 
                 <input type="text" placeholder="Ac/NO" required name="ACNO" class="form-control">
                 </div>
             </div>
             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-map-location-dot"></i></div> 
                 <input type="txext" placeholder="Address line1" required name="addres" class="form-control">
                 </div>
             </div>
             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon"><i class="fa fa-map-location-dot"></i></div> 
                 <input type="text" placeholder="Address line2" required name="addres1" class="form-control">
                 </div>
             </div>
             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-city"></i></div>
                 <select required name="city" class="form-control">
                     <option selected disabled>City</option>
                     <option value="Delhi">Delhi</option>
                     <option value="Mumbai">Mumbai</option>
                     <option value="Kolkata">Kolkata</option>
                     <option value="Surat">Surat</option>
                     <option value="Bangalore">Bangalore</option>
                     <option value="Chennai">Chennai</option>
                     <option value="Pune">Pune</option>
                     <option value="Indore">Indore</option>
                     <option value="Hyderabad">Hyderabad</option>
                     <option value="Kanpur">Kanpur</option>
                     <option value="Ahmedabad">Ahmedabad</option>
                     <option value="Chandigarh">Chandigarh</option>
                     <option value="Jaipur">Jaipur</option>
                     <option value="Lucknow">Lucknow</option>
                     <option value="Nagpur">Nagpur</option>
                     <option value="Mysore">Mysore</option>
                     <option value="Bhopal">Bhopal</option>
                     <option value="Visakhapatnam">Visakhapatnam</option>
                     <option value="Vijaywada">Vijaywada</option>
                     <option value="Varanasi">Varanasi</option>
                     <option value="Vadodara">Vadodara</option>
                </select>
                </div>
                </div>
             <div class="form-group">
                 <div class="input-group">
                     <div class="input-group-addon" ><i class="fa fa-map-location-dot"></i></div> 
                 <select required name="state" class="form-control">
                     <option selected disabled>State</option>
                     <option value="tamil nadu">Tamil Nadu</option>
                     <option value="Chhattisgarh">Chhattisgarh</option>
                     <option value="Assam">Assam</option>
                     <option value="Bihar">Bihar</option>
                     <option value="Arunachal Pradesh">Arunachal Pradesh</option>
                     <option value="Andhra Pradesh"> Andhra Pradesh</option>
                     <option value="Jharkhand">Jharkhand</option>
                     <option value="Himachal Pradesh">Himachal Pradesh</option>
                     <option value="Haryana">Haryana</option>
                     <option value="Gujarat">Gujarat</option>
                     <option value="Goa">Goa</option>
                     <option value="Madhya Pradesh">Madhya Pradesh</option>
                     <option value="Kerala">Kerala</option>
                     <option value="Karnataka">Karnataka</option>
                     <option value=" Sikkim"> Sikkim</option>
                     <option value="Rajasthan">Rajasthan</option>
                     <option value="Punjab">Punjab</option>
                     <option value="Odisha">Odisha</option>
                     <option value="Nagaland">Nagaland</option>
                     <option value="Mizoram">Mizoram</option>
                     <option value="Meghalaya">Meghalaya</option>
                     <option value="Manipur">Manipur</option>
                     <option value="Maharashtra">Maharashtra</option>
                     <option value=" Uttar Pradesh"> Uttar Pradesh</option>
                     <option value="Tripura">Tripura</option>
                     <option value="Telangana">Telangana</option>
                 </select>
                 </div>
             </div>
             <div class="form-group">
                 <div class="form-group">
                     <div class="input-group">
                         <div class="input-group-addon" ><i class="fa fa-thumbtack"></i></div> 
                 <input type="number" name="pincode" placeholder="Pin code" required class="form-control" id="">
             </div>
             </div>
             </div>
       
             <div class="form-group">
                 <input type="submit" value="Register" name="regiseter" class="btn btn-primary form-control >
             </div>
         </form>
     </div>
     <div class="col-sm-4"></div>                            
             
         
     </div><!--End-->         
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
          
        </script>
</body>
</html>""")
regiseter=form.getvalue('regiseter')

if regiseter != None:
    name=form.getvalue('name')
    email=form.getvalue('email')
    pno=form.getvalue('phno')
    dob=form.getvalue('DOB')
    gender = form.getvalue('gender')
    Qualification = form.getvalue('Qualification')
    Experiance = form.getvalue('Experiance')
    Department = form.getvalue('Department')
    branch = form.getvalue('branch')
    role = form.getvalue('role')
    Dateofjoin = form.getvalue('Dateofjoin')
    salary = form.getvalue('salary')
    addres = form.getvalue('addres')
    addres1 = form.getvalue('addres1')
    city = form.getvalue('city')
    state = form.getvalue('state')
    pincode= form.getvalue('pincode')
    Address=addres+addres1
    BANK = form.getvalue('bank')
    AC_no = form.getvalue('ACNO')
    IFSC_CODE=form.getvalue('IFSC_CODE')
    con=pymysql.connect(host="localhost",user="root",password="",database="erp")
    cur=con.cursor()
    q = """insert into employee1(name,email,phoneNo,dob,gender,qulification,Experience,Department,Branch,role,salary,address,city,state,Dateofjoin,pincode,status,salary_satatus,Bank,ACno,profile,IFSC_Code) values
         ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (name, email, pno, dob, gender, Qualification, Experiance, Department, branch, role, salary, Address, city, state,Dateofjoin, pincode, 'new', 'NOTcalculate', BANK, AC_no, 'images.jpg',IFSC_CODE)
    cur.execute(q)
    con.commit()
    print("""<script>alert("Employee Add Successfuly")</script>""")
