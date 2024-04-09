#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import  cgi, cgitb, pymysql
import datetime
import  calendar
c_m=datetime.datetime.now().month
month=calendar.month_name[c_m]
cgitb.enable()
form=cgi.FieldStorage()
ID=form.getvalue("id")
con1=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur1=con1.cursor()
q="""select * from employee1 where EID='%s'"""%ID
cur1.execute(q)
Rec=cur1.fetchall()
###salary
s="""select*from salaty_table where Status='Notpaid' """
cur1.execute(s)
rec=cur1.fetchall()
s1="""select sum(Salary)from salaty_table where Status='Notpaid' """
cur1.execute(s1)
salaryex=cur1.fetchall()
salaryex1=salaryex[0][0]
S1="""select sum(AMOUNT) from salay_expenses """
cur1.execute(S1)
Salar_Expencess=cur1.fetchone()
##vendor
V="""select * from vendor_expences"""
cur1.execute(V)
rec1=cur1.fetchall()
v1="""select sum(Payment)from vendor_expences"""
cur1.execute(v1)
vendor_expencess=cur1.fetchone()
if vendor_expencess[0]==None:
    vendor_expencess1=0;
else:
   vendor_expencess1=vendor_expencess[0]
if  Salar_Expencess[0]==None:
    Salar_Expencess1=0
else:
    Salar_Expencess1=Salar_Expencess[0]
current_Expencess=Salar_Expencess1+vendor_expencess1
###Bank Balanec
I="""select sum(payment_Amount)from income"""
cur1.execute(I)
Income=cur1.fetchone()
E="""select sum(AMOUNT)from salay_expenses """
cur1.execute(E)
Expencess=cur1.fetchone()
Bank_balaenc=Income[0]-current_Expencess
if Bank_balaenc<=1000:
    print("""
    <style>
    #pay{
    display:none;
    color:red;
    }
    </style>""")
##tax
T="select sum(payment_Amount)from income where year='2024'"
cur1.execute(T)
Tax=cur1.fetchone()
if Tax[0]==None:
    Tax1=0
else:
    Tax1=int(Tax[0])
    Tax1=round(Tax1*0.14)
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Finance</title>
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
    .input-group-addon{
        background-color: #c1efde;
        color: #009d63;
    } 
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
    .modal-dialog{
        border-radius: 10px ;
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
        background-color:#12c4dbd3;
        border-radius: 10px 10px 0px 0px;
        margin-bottom: 5px;
        height: 120px;
    }
   #pwd .btn{
        border-radius: 20px;
        font-weight: bold;
        border:solid blue 0.5px;
    }
    .detial{
        margin-top: 55px;
    }
    /* Salay Calculation table Style*/
    #month,#Department{
        padding: 10px;
        border-radius: 20px;
        width: 70%;
        margin-bottom: 20px;
        background-color: rgba(245, 222, 179, 0.452);
    }
    #month:hover,#Department:hover{
        box-shadow: 0px 0px 10px rgb(125, 231, 231);
  
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
    table{
        box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
    }
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
.log_icons{
    
    color: rgba(231, 25, 25, 0.979);
    
   font-weight: bolder;
    margin-top: 2px;
    margin-right: 2px;
}


li{
    list-style: none;
    font-size: larger; 
}
#hr{
    background-color: rgb(12, 12, 12);
    height: 2px;
}
.icons{
    background-color: rgb(231, 224, 224);
    color: rgb(44, 11, 233);
    padding:8px;
    border-radius: 50%;
    margin: -5px 5px 5px 5px;
}
#icons2{
    background-color: rgb(231, 224, 224);
    color: rgb(44, 11, 233);
    padding:8px;
    border-radius: 50%;
    margin: -5px 5px 5px 5px;
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
    top: 5px;
    right: 7px;
    cursor: pointer;
    color: #555;
    font-size: 18px;
    z-index: 3;
}
.payment-heading {
  font-family: 'Mulish', sans-serif;
  font-size: 32px;
  font-weight: bold;
  color: #007bff;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
  margin-top: -10px;
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
</div>""")
for i in Rec:
    profile="./dbmedia/"+ i[16]
print("""
<div class="container-fluid d-none d-lg-block d-xl-block text-right" id="TOP"><i><img src="%s" alt=""  width="30px" height="30px"></i><span class="text xm-text">Welcome :%s</span></div>

    <div class="container-fluid" id="main">
        <div id="Sidebar_cover">
    <div id="Sidebar_cover2">"""%(profile,i[1]))
print("""
        <!--SideBar Start-->
        <div id="Sidebar" class="d-flex flex-column  offcanvas-md offcanvas-start " >
           <div>
            <h2 style="color: #ff8f00;"> TECHVOLT  <span style="color: #23395f;">SOFTWARE</span></h2>
            <hr id="hr">
            <h3 class="Profile">Personal</h3>
            <li><a href="./FainancesProfile.py?id=%s" id="a" ><span class="fa fa-user-circle"></span> Profile </a></li>
              <li><div class="dropdown">
                <a data-toggle="dropdown"  id="op"><span class="fa fa-bell "></span>Leave<span class="caret" style="margin-top: 10px;"></span></a>
                <ul class="dropdown-menu">
                     <li><a href="./FN_leaveform.py?id=%s" target="_self">New <span class="fa  fa-plus"></span></a></li>
                    <li><a href="./FN_existingleave.py?id=%s" target="_self"> Existing </a></li>
                </ul>
            </div>
            </li>
            <li><a href="./FN_salarytable.py?id=%s" target="_self" id="a"><span class=" fa fa-money-bill-1-wave"></span>Salary</a></li>
            <li><div class="dropdown">
                <a data-toggle="dropdown"  id="op" ><span class="fa fa-bell" ></span>Announcement<span class="caret" style="margin-top: 10px;"></span></a>
                <ul class="dropdown-menu">
                     <li><a href="./FN_Announcement.py?id=%s" target="_self">New <span class="fa  fa-plus"></span></a></li>
                    <li><a href="./FN_Announcement2.py?id=%s" target="_self"> Existing </a></li>
                </ul>
            </div>
            </li>
            <h3 class="Role">Role</h3>
            <li><a href="./FN_income.py?id=%s" id="a" ><i class="fa fa-sack-dollar"></i> Income</a></li>
                 
            <li><div class="dropdown">
                <a data-toggle="dropdown"id="op"><i class="fa fa-users"></i> Client<span class="caret" style="margin-top: 10px;"></span></a>
                <ul class="dropdown-menu">
                     <li><a href="./FN_client.py?id=%s">New <span class="fa  fa-plus"></span></a></li>
                    <li><a href="./FN_existingclient.py?id=%s"> Existing </a></li>
                </ul>
            </div>
            </li>
            <li><div class="dropdown">
                <a data-toggle="dropdown" id="op"><i class="fa fa-users-line"></i> Vendor<span class="caret" style="margin-top: 10px;"></span></a>
                <ul class="dropdown-menu">
                     <li><a href="./FN_ventor.py?id=%s">New<span class="fa  fa-user-plus"></span></a></li>
                    <li><a href="./FN_existingventor.py?id=%s">Existing</a></li>
                </ul>
            </div></li>
            
            <li><div class="dropdown">
                <a data-toggle="dropdown"  id="op" style="background-color: #23395f; color: white; margin-left: -10px; margin-right: -8px; border-left:3px solid orange;"><i class="fa fa-money-bill" style="color: #CFEEFF;"></i> Expenses<span class="caret" style="margin-top: 10px;"></span></a>
                <ul class="dropdown-menu">
                     <li><a href="./FN_expencess.py?id=%s">New <span class="fa  fa-plus"></span></a></li>
                    <li><a href="./FN_ExpencessVendor.py?id=%s">Existing <span class>Vendor Expenses</span></a></li>
                    <li><a href="./FN_existingexpencess.py?id=%s" target="_self"> Salary Expenses  </a></li>

                </ul>
            </div>
            </li>   
    <hr id="hr" class="d-md-none">
    <li><a href="index.py" id="LOGOUT_SM" class="d-md-none"> <i class="glyphicon glyphicon-log-out log_icons "></i class="glyphicon glyphicon logout"> Logout</a></li>
                          
          </div>
        </div><!-- Sidebar End-->
    </div>
        </div>"""%(ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID))
print("""
        <div class="flex-fill" id="first_content_box">
            <div class=" d-md-none  text-white " id="bars">
                <a href="#" class="text-white" data-bs-toggle="offcanvas" data-bs-target="#Sidebar">
                    <i class="fa-solid fa-bars"></i>
                </a>
            </div>
            <div class="container-fluid d-none d-lg-block d-xl-block " id="Dashbord_Head" ><!--Time-->
                <i class="text-info" style="margin: 220px;">Finance Dash Bord</i>
                <div id="Logout_TIME">
                <li id="time"></li>
                <li><a href="index.py" id="LOGOUT"> <i class="glyphicon glyphicon-off log_icons"></i class="glyphicon glyphicon logout"> Logout</a></li>
                </div>
                </div><!--End-->""")
print("""
            
            <div id="Secount_continer_box">
            <div class="centered-form-container" id="paymentForm" style="background-color: #fff; border-radius:10px;box-shadow: rgba(67, 71, 85, 0.27) 0px 0px 0.25em, rgba(90, 125, 188, 0.05) 0px 0.25em 1em; padding:30px">
        <div class="close-button" onclick="toggleFormVisibility()">X</div>
            <h2 class="payment-heading">Payment Form</h2>
            <form method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <input type="hidden" name="payment_SID" id="payment_SID" class="form-control" readonly>
                    <input type="hidden" name="payment_EID" id="payment_EID" class="form-control" readonly>
                </div>
                <div class="form-group">
                    <label for="payment_name">Name</label>
                    <input type="text" name="payment_name" id="payment_name" class="form-control" readonly>
                </div>
                <div class="form-group">
                    <label for="payment_salary">Salary</label>
                    <input type="number" name="payment_salary" id="payment_salary" class="form-control" readonly>
                </div>
                <div class="form-group">
                    <label for="payment_bank">Bank</label>
                    <input type="text" name="payment_bank" id="payment_bank" class="form-control" readonly>
                </div>
                <div class="form-group">
                    <label for="payment_acno">AC/NO</label>
                    <input type="text" name="payment_acno" id="payment_acno" class="form-control" readonly>
                </div>
                <div class="form-group">
                    <label for="payment_salary">IFSC Code</label>
                    <input type="text" name="payment_IFSC" id="payment_IFSC" class="form-control" readonly>
                </div>
                <input type="submit" name="confirmPayment" value="Confirm Payment" class="btn btn-success">
            </form>
        </div>
                <div class="row"> 
                    <div class="col-sm-3"></div>
                    <div class="col-sm-3">
                        <div style=" width: 25rem; background-color: #097969; border-radius: 10px; color: #fff;">
                            
                            <h4 style="text-align: center; padding: 5px;">Bank Balance</h4>
                            <i style="font-size:xx-large;padding: 10px;"><i class="fa fa-bank" style="background-color: #23395f; padding: 20px; border-radius: 120px; color: #fff;" ></i><i>%s</i></i>
                            </div> 
                    </div>
                    
                    <div class="col-sm-3">
                        <div style=" width: 25rem; background-color: #00cED1; border-radius: 10px; color: #fff;">
                            
                            <h4 style="text-align: center; padding: 5px;"> Expenses</h4>
                            <i style="font-size:xx-large;padding: 10px;"><i class="fa fa-indian-rupee-sign" style="background-color: #23395f; padding: 20px; border-radius: 120px; color: #fff;" ></i><i>%s</i></i>
                            </div>
                    </div>
                    <div class="col-sm-3">
                        <div style=" width: 25rem; background-color: #ff8f00; border-radius: 10px; color: #fff;">
                            
                            <h4 style="text-align: center; padding: 5px;"> TAX</h4>
                            <i style="font-size:xx-large;padding: 10px;"><i class="fa fa-indian-rupee-sign" style="background-color: #23395f; padding: 20px; border-radius: 120px; color: #fff;" ></i><i>%s</i></i>
                            </div>
                    </div>
                 </div>
                 """%(Bank_balaenc,salaryex1,Tax1))
html_rows = ""

for row in rec:
    html_rows += f"""
                            <tr>
                                <td style="display: none;">{row[14]}</td>
                                <td>{row[0]}</td>
                                <td>{row[1]}</td>
                                <td>{row[2]}</td>
                                <td>{row[3]}</td>
                                <td>{row[6]}</td>
                                <td>{row[4]}</td>
                                <td>{row[10]}</td>
                                <td style="display: none;">{row[15]}</td>
                                <td style="display: none;">{row[16]}</td>
                                <td style="display: none;">{row[17]}</td>
                            
                                <td><button class="btn btn-info" onclick="openPaymentForm('{row[14]}', '{row[0]}','{row[1]}','{row[15]}','{row[16]}','{row[17]}','{row[10]}')">Pay</button></td>
                            </tr>
"""


print("""
                 
                <div class="row">
                    <div class="col-sm-3"></div>
                    <div class="col-md-8">
                    <h3 style="font-family: verdana;font-weight: bold;font-size: 20px;color: rgb(0, 208, 255);">Salary Expenses</h3>
                        <table class="table">
                            
                            <thead>
                        <tr>
                            <th style="display: none;">SID</th>
                            <th>EID</th>
                            <th>Name</th>
                            <th>Department</th>
                            <th>Role</th>
                            <th>Basic Salary</td>
                            <th>Month</th>
                            <th>Salary Payable</th>
                            <th>Action</th>
                        </tr>  
                    </thead>
                    <tbody style="background-color: #fff;">""")

print(f"""
                        {html_rows}
</tbody>
</table>""")
# print("""
#
#                         </table>
#                         <table class="table">
#                             <thead>
#                         <tr>
#
#                             <th>Vendor ID</th>
#                             <th>Name</th>
#                             <th>Organization</th>
#                             <th>AC/NO</th>
#                             <th>Ac/Name</th>
#                             <th>Bank</th>
#                             <th>Pyament</th>
#                             <th>Action</th>
#                         </tr>
#                     </thead>
#                     <tbody style="background-color: #fff;">""")
# for J in rec1:
#     print("""
#                         <tr>
#                             <form method="post" enctype="multipart/form-data">
#                             <td><input type="number"  readonly name="VID" value="%s" style="border: none;width:30px"></td>
#                             <td>%s</td>
#                             <td>%s</td>
#                             <td>%s</td>
#                             <td>%s</td>
#                             <td>%s</td>
#                             <td><input type="number"  name="payment" style="border: none; width:60px" readonly value="%s"></td>
#                             <td><input type="submit" name="vpay" value="Pay" class="btn btn-info"></td>
#                         </form>
#                         </tr>
#                         """%(J[0],J[1],J[4],J[10],J[11],J[12],J[13]))
# print("""
#                     </tbody>
#                         </table>
print("""
                    </div>
                 </div>         
           <!-- Payment Form -->

        
    </div>
   
    <script>
    //------------------------------------------------Sayary------------------------------------//
    
            //----------------------------Time set event----------------------/
            var s=new Date()
            document.getElementById('time').innerHTML= +""+s.toLocaleString()
            //______________________________End______________________________//
          
           function openPaymentForm(SID,EID,name,bank,AC_No,IFSC,salary) {
        // Populate payment form fields
        document.getElementById('payment_SID').value = SID;
        document.getElementById('payment_EID').value = EID;
        document.getElementById('payment_salary').value = salary;
        document.getElementById('payment_name').value = name;
        document.getElementById('payment_bank').value = bank;
        document.getElementById('payment_acno').value = AC_No;
        document.getElementById('payment_IFSC').value = IFSC;
        // Optionally, you can add additional logic here

        // Display payment form
        document.getElementById('paymentForm').style.display = 'block';
    }
    document.addEventListener('DOMContentLoaded', function() {
    var paymentForm = document.getElementById('paymentForm');
    var blurBackground = document.getElementById('blurBackground');
    var closeButton = document.querySelector('.close-button');
    
    // Function to toggle the visibility of the payment form and blur background
    function toggleFormVisibility() {
        paymentForm.style.display = (paymentForm.style.display === 'none') ? 'block' : 'none';
        blurBackground.style.display = (blurBackground.style.display === 'none') ? 'block' : 'none';
    }

    // Toggle payment form visibility when clicking the close button
    closeButton.addEventListener('click', toggleFormVisibility);

    // Call the toggle function to hide the payment form initially
    toggleFormVisibility();
});
        </script>
</body>
</html>""")
spay=form.getvalue('confirmPayment')
vpay=form.getvalue('vpay')
if spay !=None:
    EID=form.getvalue('payment_EID')
    SID=form.getvalue('payment_SID')
    payment_acno=form.getvalue('payment_acno')
    payment_bank=form.getvalue('payment_bank')
    payment_IFSC=form.getvalue('payment_IFSC')
    payment_salary=int(form.getvalue('payment_salary'))
    print(Bank_balaenc)

    if Bank_balaenc<payment_salary:
        print("""<script>alert("Bank Balance is To Low Can't Pay ")</script>""")
    else:

        con = pymysql.connect(host="localhost", user="root", password="", database="erp")
        cur = con.cursor()
        c_m = datetime.datetime.now().month
        month = calendar.month_name[c_m]
        EMP_data="""select * from employee1 where EID='%s'"""%EID
        cur.execute(EMP_data)
        E_rec=cur.fetchall()
        for J in E_rec:
            name=J[1]
            Department=J[8]
            Role=J[10]
        year="2024"
        reason="salary"
        from datetime import date
        todays_date = date.today()
        Payment_method="TO bank Account"
        IN="""INSERT INTO `salay_expenses`(`EID`, `Name`, `Department`, `Role`, `AMOUNT`, `Payment_method`, `Bank`, `AcNO`, `IFCcOde`, `Month`, `Year`,Date) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(EID,name,Department,Role,payment_salary,Payment_method,payment_bank,payment_acno,payment_IFSC,month,year,todays_date)
        cur.execute(IN)
        con.commit()
        from datetime import date
        Issue_date = date.today()
        UP="update salaty_table set Status='Paid',Issue_date='%s' where SID='%s'"%(Issue_date,SID)
        cur.execute(UP)
        con.commit()
        print("""<script>alert("Salary Payment Successfully")</script>""")
######vendor payment
# if vpay !=None:
#     VID=form.getvalue('VID')
#     payment=int(form.getvalue('payment'))
#     if Bank_balaenc < payment:
#         print("""<script>alert("Bank Balance is To Low Can't Pay ")</script>""")
#     else:
#         con = pymysql.connect(host="localhost", user="root", password="", database="erp")
#         cur = con.cursor()
#         c_m = datetime.datetime.now().month
#         month = calendar.month_name[c_m]
#         year = "2024"
#         reason = "Vendor Payment"
#         IN = """INSERT INTO expenses(Year,Month,Resone,Payment,referance) VALUES ('%s','%s','%s','%s','%s')""" % ('2024', month, reason, payment, VID)
#         cur.execute(IN)
#         con.commit()
#         UP = "update vendor set Payment_status='Paid' where VID='%s'" % VID
#         cur.execute(UP)
#         con.commit()
#         print("""<script>alert(" Vendor Payment Successfully")</script>""")
