#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import  cgi, cgitb,pymysql
cgitb.enable()
form=cgi.FieldStorage()
ID=form.getvalue("id")
con1=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur1=con1.cursor()
q="""select * from employee1 where EID='%s'"""%ID
cur1.execute(q)
rec=cur1.fetchall()
###Auto updatetion#####
from datetime import date
c_m=date.today()
DAY=int(c_m.strftime('%d'))
if DAY==25:
    con3= pymysql.connect(host="localhost", user="root", password="", database="erp")
    cur3= con3.cursor()
    #######
    q2= """ update employee1 set salary_satatus='%s' where  status = 'approved'"""%'NOTcalculate'
    cur3.execute(q2)
    con3.commit()
# ########
########################### sala calculatom table befor
con2=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur2=con2.cursor()
q1="""select * from employee1 where salary_satatus='NOTcalculate' and status !=('new')"""
cur2.execute(q1)
rec1=cur2.fetchall()
####salar tabel#######
con3=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur3=con3.cursor()
Q="""select * from salaty_table"""
cur3.execute(Q)
rec2=cur3.fetchall()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hr</title>
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
  #searchInput{
    padding: 20px;
     border-radius: 20px 0px 0px 20px;
}
#Search_Button{
    width: 70px; height: 25px;color: white;
     border-radius:0px 20px 20px 0px;
     padding: 20px; 
    margin-top: 2px;
}
#Search_icon{
    position: relative; bottom: 10px; font-size: x-large;

}
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
    th{
        padding: 5px;
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
        background-color: #111111;
        color: white;
    }
    tbody{
        background-color: white;
        font-weight: bold;
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
#salary_cal{
    display: none;
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
for i in rec:
    profile="./dbmedia/"+ i[16]

print("""
<div class="container-fluid d-none d-lg-block d-xl-block text-right" id="TOP"><i><img src="%s" alt=""  width="30px" height="30px"></i><span class="text xm-text">Welcome :%s</span></div>

    <div class="container-fluid" id="main">
        <div id="Sidebar_cover">
    <div id="Sidebar_cover2">
        <!--SideBar Start-->
        """%(profile,i[1]))
print("""
        <div id="Sidebar" class="d-flex flex-column  offcanvas-md offcanvas-start " >
           <div>
            <h2 style="color: #ff8f00;"> TECHVOLT  <span style="color: #23395f;">SOFTWARE</span></h2>
            <hr id="hr">
            <h3 class="Profile">Personal</h3>
            <li><a href="./Hr copy.py?id=%s" id="a"><span class="fa fa-user-circle" ></span> Profile </a></li>
              <li><div class="dropdown">
                <a data-toggle="dropdown"  id="op"><span class="fa fa-bell "></span>Leave<span class="caret" style="margin-top: 10px;"></span></a>
                <ul class="dropdown-menu">
                     <li><a href="./HR_leaveform.py?id=%s" target="_self">New <span class="fa  fa-plus"></span></a></li>
                    <li><a href="./HR_existingleave.py?id=%s" target="_self"> Existing </a></li>
                </ul>
            </div>
            </li>
            <li><a href="./HR_salarytable.py?id=%s" target="_self" id="a"><span class=" fa fa-money-bill-1-wave"></span>Salary</a></li>
            <li><div class="dropdown">
                <a data-toggle="dropdown"  id="op"><span class="fa fa-bell"></span>Announcement<span class="caret" style="margin-top: 10px;"></span></a>
                <ul class="dropdown-menu">
                     <li><a href="./HR_Announcement.py?id=%s" target="_self">New <span class="fa  fa-plus"></span></a></li>
                    <li><a href="./HR_Announcement2.py?id=%s" target="_self"> Existing </a></li>
                </ul>
            </div>
            </li>
            <h3 class="Role">Role</h3>
                <li><div class="dropdown">
                    <a data-toggle="dropdown"  id="op"><span class="fa fa-user " ></span> Employee<span class="caret" style="margin-top: 10px;"></span></a>
                    <ul class="dropdown-menu">
                         <li><a href="./HR_newemp.py?id=%s" target="_self">New <span class="fa  fa-user-plus"></span></a></li>
                        <li><a href="./HR_existingemp.py?id=%s" target="_self"> Existing </a></li>
                    </ul>
                </div>
                </li>
                 
    <li><div class="dropdown">
        <a data-toggle="dropdown"  id="op"><i class="fa fa-person-walking-arrow-right"></i></span>Leave<span class="caret" style="margin-top: 10px;"></span></a>
        <ul class="dropdown-menu">
             <li><a href="./HR_leaverequest.py?id=%s" target="_self"> New <span class=""></span></a></li>
            <li><a href="./HR_leaverequestappro.py?id=%s" target="_self"> Existing </a></li>
        </ul>
    </div>
    </li>
    <li><a href="./HR_salarycalculation.py?id=%s" id="a" style="background-color: #23395f; color: white; margin-left: -10px; margin-right: -8px; border-left:3px solid orange;"> <i class="fa fa-calculator" style="color: #CFEEFF;"></i> Salary Calculation </a></li>
    <li><div class="dropdown">
        <a data-toggle="dropdown"  id="op"><span class="fa fa-bell"></span>Announcement<span class="caret" style="margin-top: 10px;"></span></a>
        <ul class="dropdown-menu">
             <li><a href="./HR_Announcementform.py?id=%s" target="_self">New <span class="fa  fa-plus"></span></a></li>
            <li><a href="./HR_Announcementstatus.py?id=%s" target="_self">  Existing </a></li>
        </ul>
    </div>
    </li>
    <hr id="hr" class="d-md-none">
    <li><a href="index.html" id="LOGOUT_SM" class="d-md-none"> <i class="glyphicon glyphicon-log-out log_icons "></i class="glyphicon glyphicon logout"> Logout</a></li>
                """%(ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID))
print("""
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
                <i class="text-info" style="margin: 220px;">HR Dash Bord</i>
                <div id="Logout_TIME">
                <li id="time"></li>
                <li><a href="index.py" id="LOGOUT"> <i class="glyphicon glyphicon-off log_icons"></i class="glyphicon glyphicon logout"> Logout</a></li>
                </div>
                </div><!--End-->
                
            <div id="Secount_continer_box" >
                <div class="row"><!--search-->
                           <div class="col-sm-3"></div>
                           <div class="col-sm-8" style="display: flex;"> 
                               <div class="form-group" style="margin-top: 2px; width: 100%;">
                                   <div class="input-group">

                                   <input type="search" name="search"  placeholder="Search to Department " class="form-control" id="searchInput">
                               </div>
                               </div>
                               <button type="button" name="search" onclick="filterTable()"  class="btn btn-primary" id="Search_Button"><i class="fa fa-search" id="Search_icon" ></i></button>
                           </div>
                           <div class="col-sm-2"></div>
                        </div><!--Search bar end-->
                        """)
print("""
                <div class="container-fluid" style=" padding-top: 20px;" id="Salary_calcualtin_Tables_Befor"> <!--Salacaluclatin table-->
                   <div class="row">
                    <div class="col-md-2"></div>
                    <div class="col-md-10">
        
                        <table class="table" id="dataTable">
                            <thead>
                                <tr>
                                <th>ID</th>
                                <th>Name</th>
                                <th>Department</th>
                                <th>Role</th>
                                <th>salary</th>
                                <th>Action</th>
                            </tr>
                            </thead>
                            <tbody>
                        
                        """)
for j in rec1:
 print("""      
 <form method="post" enctype="multipart/form-data">
 <tr>
                                <td><input type="number" readonly name="EID" value="%s" style="border:none; width:35px"></td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td><input type="submit" class="btn btn-warning"  name="calculate" onclick="salaryCal_open()" value="calculate"></td>
                            </tbody>
                            </tr>
       </form>"""%(j[0],j[1],j[8],j[10],j[11]))
print("""
                        </table>
                    </div>
                       </div>
                    </div><!--End-->
                    
                <div class="container-fluid" id="Salary_calcualtin_Tables_after" style="margin-top: 10px;">
                    <div class="row">
                        <div class="col-md-2"></div>
                        <div class="col-md-10"d-none d-lg-block d-xl-block >
                        <h3 style="font-family: verdana;font-weight: bold;font-size: 20px;color: rgb(0, 208, 255);">Calculated Salary Details </h3>
                    <table class="table">
                        <thead>
                            <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Month</th>
                            <th>Department</th>
                            <th>Role</th>
                            <th>Working Days</th>
                            <th>Leave</th>
                            <th>present Day</th>
                            <th>Day payable</th>
                            <th>salary payable</th>
                            <th>Status</th>
                        </tr>
                        </thead>
                        """)
for y in rec2:
    print("""<tbody>
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
                            <td>%s</td>
                            </tr></tbody>
                            """%(y[0],y[1],y[4],y[2],y[3],y[12],y[13],y[7],y[8],y[10],y[11]))
print("""
                        
                    </table>
                    </div>
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
            const searchInput = document.getElementById('searchInput');
    const dataTable = document.getElementById('dataTable');
    const rows = dataTable.getElementsByTagName('tr');

    searchInput.addEventListener('input', function() {
        const searchValue = this.value.toLowerCase();
        for (let i = 1; i < rows.length; i++) { // Start from 1 to skip the header row
            const department = rows[i].getElementsByTagName('td')[2].innerText.toLowerCase();
            if (department.includes(searchValue)) {
                rows[i].style.display = '';
            } else {
                rows[i].style.display = 'none';
            }
        }
    });

          
        </script>
</body>
</html>""")
calculate=form.getvalue("calculate")
if calculate !=None:
    EID = form.getvalue("EID")
    if DAY==25:
        print("""<script>
                     alert("Salary Calculation Form Open Tomorrow")
                   </script>
                   """)
    else:
        print("""<script>
              location.href="Salary_calculationform.py?ID=%s&id=%s"
            </script>
            """ % (ID, EID))

