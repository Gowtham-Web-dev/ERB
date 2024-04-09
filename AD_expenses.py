#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import  cgi, cgitb,pymysql
import datetime
import  calendar
c_m=datetime.datetime.now().month
month=calendar.month_name[c_m]
cgitb.enable()
form=cgi.FieldStorage()
con=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur=con.cursor()
q="select*from salay_expenses"
cur.execute(q)
##Exisying incomr
rec=cur.fetchall()
q1="select sum(AMOUNT)from salay_expenses"
cur.execute(q1)
rec1=cur.fetchall()
##present month
q2="select sum(AMOUNT)from salay_expenses where Month ='%s'"%(month)
cur.execute(q2)
rec2=cur.fetchall()
if  rec2[0][0] ==None:
    rec2=0
else:
    rec2=rec2[0][0]
Q="select*from vendor_expences"
cur.execute(Q)
Rec=cur.fetchall()
Q1="select sum(Payment)from vendor_expences"
cur.execute(Q1)
Rec1=cur.fetchall()
##present month
Q2="select sum(Payment)from vendor_expences where Month ='%s'"%(month)
cur.execute(Q2)
Rec2=cur.fetchall()
if  Rec2[0][0] ==None:
    Rec2=0
else:
    Rec2=Rec2[0][0]

######
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
    #show-more {
            display: none; /* Initially hide the show more button */
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
thead{
        background-color: #a6f793f3;
        color: #000;
        font-family:  "Mulish", sans-serif;
    }
    tbody{
        background-color: #fff;
        
        font-family:  "Mulish", sans-serif;
    }
    table{
        
       
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
#closes,#mores,#vmore,#closev{
display:none;
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
                <a data-toggle="dropdown" id="op"><i class="fa fa-users-line"></i> Vendor<span class="caret" style="margin-top: 10px;"></span></a>
                <ul class="dropdown-menu">
                     <li><a href="./AD_venter.py">New<span class="fa  fa-plus"></span></a></li>
                    <li><a href="./AD_existingventer.py">Existing</a></li>
                </ul>
            </div></li>

            <li><a href="./AD_expenses.py" id="a" style="background-color: #23395f; color: white; margin-left: -10px; margin-right: -8px; border-left:3px solid orange;"><i class="fa fa-money-bill" style="color: #CFEEFF;"></i> Expenses</a></li>
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
            <div class="row"> 
    <div class="col-md-2"></div>
    <div class="col-md-2">
        <div style="width:20rem; background-color: #CCCCFF; border-radius: 8px; color: #800080;"> 
            <h6 style="text-align: center; padding: 3px;">Total Salary Expenses</h6>
            <i style="font-size: large; padding: 5px;">
                <i class="fa fa-money-bill" style="background-color: #fff; padding: 10px; border-radius: 80px; color: #23395f;margin:0px 0px 10px 0px"></i>
                <i>%s</i>
            </i>
        </div> 
    </div>
    <div class="col-md-2">
        <div style="width: 20rem; background-color: #CCCCFF; border-radius: 8px; color: #800080;"> 
            <h6 style="text-align: center; padding: 3px;">Monthly Salary Expenses</h6>
            <i style="font-size: large; padding: 5px;">
                <i class="fa fa-money-bill" style="background-color: #fff; padding: 10px; border-radius: 80px; color: #23395f;margin:0px 0px 10px 0px"></i>
                <i>%s</i>
            </i>
        </div>
    </div>
    <div class="col-md-2">
        <div style="width: 20rem; background-color: #CCCCFF; border-radius: 8px; color: #800080;"> 
            <h6 style="text-align: center; padding: 3px;">Total Vendor Expenses</h6>
            <i style="font-size: large; padding: 5px;">
                <i class="fa fa-money-bill" style="background-color: #fff; padding: 10px; border-radius: 80px; color: #23395f;margin:0px 0px 10px 0px"></i>
                <i>%s</i>
            </i>
        </div> 
    </div>
    <div class="col-md-2">
        <div style="width:20rem; background-color: #CCCCFF; border-radius: 8px; color: #800080;"> 
            <h6 style="text-align: center; padding: 3px;">Monthly Vendor Expenses </h6>
            <i style="font-size: large; padding: 5px;">
                <i class="fa fa-money-bill" style="background-color: #fff; padding: 10px; border-radius: 80px; color: #23395f;margin:0px 0px 10px 0px"></i>
                <i>%s</i>
            </i>
        </div> 
    </div>
</div>

               <div class="row">
               <div class="col-md-2"></div>
               <div class="col-md-10">
               <h3 style="font-family: verdana;font-weight: bold;font-size: 20px;color: rgb(0, 208, 255);">Salary Expenses Detail's</h3>
               <table class="table" id="lows">
               <thead>
               <tr>
               <th>Year</th>
               <th>Month</th>
               <th>Issue Date</th>
               <th>Employee ID</th>
               <th>Name</th>
               <th>Department</th>
               <th>Role</th>
               <th>Bank</th>
               <th>Ac/no</th>
               <th>Payment</th>
               </tr>
               </thead>
               
            """%(rec1[0][0],rec2,Rec1[0][0],Rec2))
for index, row in enumerate(rec):
    display_style = "" if index < 3 else "style='display:none;'"
    print("""
    <tbody>
    <tr %s>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    </tr>
    </tbody>
    """ % (display_style, row[11], row[10], row[12], row[1], row[2], row[3], row[4], row[7], row[8], row[5]))
print("""
</table>
<table class="table" id="mores">
               <thead>
               <tr>
               <th>Year</th>
               <th>Month</th>
               <th>Issue Date</th>
               <th>Employee ID</th>
               <th>Name</th>
               <th>Department</th>
               <th>Role</th>
               <th>Bank</th>
               <th>Ac/no</th>
               <th>Payment</th>
               </tr>
               </thead>
    <tbody>""")
for i in rec:
    print("""
    <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    </tr>
"""%(i[11],i[10],i[12],i[1],i[2],i[3],i[4],i[7],i[8],i[5]))
print("""    
</tbody>
</table>
               <button class="btn btn-info" onclick="shows()" id="shows">Show More</button>
               <button class="btn btn-info" onclick="closes()" id="closes">Close</button>
               </div>
               </div>
               <div class="row">
               <div class="col-md-2"></div>
               <div class="col-md-10">
              <h3 style="font-family: verdana;font-weight: bold;font-size: 20px;color: rgb(0, 208, 255);">Vendor Expenses Details</h3>
               <table class="table" id="vlow">
               <thead>
               <tr>
               <th>Year</th>
               <th>Month</th>
               <th>Issue date</th>
               <th>Organization</th>
               <th>Name</th>
                <th>Type Service</th>
                <th>Service Date</th>
               <th>Payment Method</th>
                <th>Bill</th>
               <th>UPI ID</th>
               <th>Payment</th>
               </tr>
               </thead>
               <tbody style="background-color:#fff">
        """)
for index, row in enumerate(Rec):
    display_style = "" if index < 3 else "style='display:none;'"
    bill="./dbmedia/"+row[6]
    print("""
    <tr %s>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td><a href="%s" download > Bill</a></td>
    <td>%s</td>
    <td>%s</td>
    </tr>
"""%(display_style,row[11],row[12],row[7],row[3],row[2],row[4],row[5],row[9],bill,row[10],row[8]))
print("""</tbody>
               </table>
               
               <table class="table" id="vmore">
               <thead>
               <tr>
               <th>Year</th>
               <th>Month</th>
               <th>Issue date</th>
               <th>Organization</th>
               <th>Name</th>
                <th>Type Service</th>
                <th>Service Date</th>
               <th>Payment Method</th>
                <th>Bill</th>
               <th>UPI ID</th>
               <th>Payment</th>
               </tr>
               </thead>
               <tbody style="background-color:#fff">
        """)
for i in Rec:
    bill="./dbmedia/"+i[6]
    print("""
    <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td><a href="%s" download > Bill</a></td>
    <td>%s</td>
    <td>%s</td>
    </tr>
"""%(i[11],i[12],i[7],i[3],i[2],i[4],i[5],i[9],bill,i[10],i[8]))
print("""
              </tbody>
               </table>
               <button class="btn btn-info" onclick="showv()" id="showv">Show More</button>
               <button class="btn btn-info" onclick="closev()" id="closev">Close</button>
               </div>
               </div>


                        </div><!--End-->


            </div>

        </div>


    </div>

    
</body>
<script>
    
    //------------------------------------------------Sayary------------------------------------//

            //----------------------------Time set event----------------------/
            var s=new Date()
            document.getElementById('time').innerHTML= +""+s.toLocaleString()
            //______________________________End______________________________//
            function shows(){
            document.getElementById('mores').style.display="inline";
            document.getElementById('closes').style.display="block";
            document.getElementById('lows').style.display="none";
            document.getElementById('shows').style.display="none";
            }
            function closes()
{

           document.getElementById('mores').style.display="none";
            document.getElementById('closes').style.display="none";
            document.getElementById('lows').style.display="block";
            document.getElementById('shows').style.display="block";
}
function showv(){
            document.getElementById('vmore').style.display="inline";
            document.getElementById('closev').style.display="block";
            document.getElementById('vlow').style.display="none";
            document.getElementById('showv').style.display="none";
            }
function closev()
{

           document.getElementById('vmore').style.display="none";
            document.getElementById('closev').style.display="none";
            document.getElementById('vlow').style.display="block";
            document.getElementById('showv').style.display="block";
}
    
        </script>
</html>""")