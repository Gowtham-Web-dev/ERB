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
for i in rec:
    profile = "./dbmedia/" + i[16]
    role=i[10]
if role=='Manager':
    con3=pymysql.connect(host="localhost",user="root",password="",database="erp")
    cur3=con3.cursor()
    ###Approved Client########
    Q="""select * from client where status='new'  and project_interset='yes'"""
    cur3.execute(Q)
    rec2=cur3.fetchall()
    ####Un Approved Client######
    Q="""select * from client where status='new'  and project_interset='no'"""
    cur3.execute(Q)
    rec3=cur3.fetchall()
    ###Client
    Q="""select * from client where status !='new' """
    cur3.execute(Q)
    rec4=cur3.fetchall()

if role=='Executive':
    con3=pymysql.connect(host="localhost",user="root",password="",database="erp")
    cur3=con3.cursor()
    ###Approved Client########
    Q="""select * from client where status='new' and EID='%s' and project_interset='yes'"""%(ID)
    print("""
    <style>
    #a1{
    display: none;
    }</style>""")
    cur3.execute(Q)
    rec2=cur3.fetchall()
    ####Un Approved Client######
    Q="""select * from client where status='new' and EID='%s' and project_interset='no'"""%(ID)
    cur3.execute(Q)
    rec3=cur3.fetchall()
    ###Client
    Q="""select * from client where status !='new' And EID='%s' """%(ID)
    cur3.execute(Q)
    rec4=cur3.fetchall()

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marketing</title>
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
#LOGOUT{
    color: red;
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
        
        border:#caeef1 2px solid;
        font-family:  "Mulish", sans-serif;
        background-color: #fff;
    }
    table{
        box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
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


print("""
<div class="container-fluid d-none d-lg-block d-xl-block text-right" id="TOP"><i><img src="%s" alt=""  width="30px" height="30px"></i><span class="text xm-text">Welcome :%s</span></div>

    <div class="container-fluid" id="main">
        <div id="Sidebar_cover">
    <div id="Sidebar_cover2">
        <!--SideBar Start-->
        """ % (profile, i[1]))
print("""
                <!--SideBar Start-->
                <div id="Sidebar" class="d-flex flex-column  offcanvas-md offcanvas-start " >
                   <div>
                    <h2 style="color: #ff8f00;"> TECHVOLT  <span style="color: #23395f;">SOFTWARE</span></h2>
                    <hr id="hr">
                    <h3 class="Profile">Personal</h3>
                      <li><a href="./Marketingprofil.py?id=%s" id="a" id="op"><span class="fa fa-user-circle" ></span> Profile </a></li>
                      <li><div class="dropdown">
                        <a data-toggle="dropdown"  id="op" ><span class="fa fa-bell"></span>Leave<span class="caret" style="margin-top: 10px;"></span></a>
                        <ul class="dropdown-menu">
                             <li><a href="./markent_leaveform.py?id=%s" target="_self">New <span class="fa  fa-plus"></span></a></li>
                            <li><a href="./marketingexisingleave.py?id=%s" target="_self"> Existing </a></li>
                        </ul>
                    </div>
                    </li>
                    <li><a href="./marketingsalarytable.py?id=%s" target="_self" id="a"><span class=" fa fa-money-bill-1-wave"></span>Salary</a></li>
                    <li><div class="dropdown">
                        <a data-toggle="dropdown"  id="op"  ><span class="fa fa-bell" ></span>Announcement<span class="caret" style="margin-top: 10px;"></span></a>
                        <ul class="dropdown-menu">
                             <li><a href="./marketingannounment.py?id=%s" target="_self">New <span class="fa  fa-plus"></span></a></li>
                            <li><a href="./maketingannounment2.py?id=%s" target="_self"> Existing </a></li>
                        </ul>
                    </div>
                    </li>
                    <h3 class="Role">Role</h3>
                        <li><div class="dropdown">
                            <a data-toggle="dropdown"  id="op"  style="background-color: #23395f; color: white; margin-left: -10px; margin-right: -8px; border-left:3px solid orange;"><span class="fa fa-user" style="color: #CFEEFF;"></span> Client<span class="caret" style="margin-top: 10px;"></span></a>
                            <ul class="dropdown-menu">
                                 <li><a href="./MarketinnewClient.py?id=%s" target="_self">New <span class="fa  fa-user-plus"></span></a></li>
                                <li><a href="./Marketingexistinclient.py?id=%s" target="_self"> Existing </a></li>
                            </ul>
                        </div>
                        </li>
                         
                        <li><div class="dropdown">
                            <a data-toggle="dropdown" id="op"><i class="fa fa-file-invoice"></i>Invoice<span class="caret" style="margin-top: 10px;"></span></a>
                            <ul class="dropdown-menu">
                                 <li><a href="./Marketininvoic.py?id=%s">New <span></span></a></li>
                                <li><a href="./marketingexistinginvoice.py?id=%s"> Existing </a></li>
                            </ul>
                        </div>
                        </li>
            <li><a href="./maketingclienthistory.py?id=%s" id="a"> <i class="fa fa-clock-rotate-left"></i>Client History </a></li>
             
            <hr id="hr" class="d-md-none">
            <li><a href="index.py" id="LOGOUT_SM" class="d-md-none"> <i class="glyphicon glyphicon-log-out log_icons "></i class="glyphicon glyphicon logout"> Logout</a></li>
                                  
                  </div>
                </div><!-- Sidebar End-->
            </div>
           
        </div>
        """%(ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID))
print("""
        <div class="flex-fill" id="first_content_box">
            <div class=" d-md-none  text-white " id="bars">
                <a href="#" class="text-white" data-bs-toggle="offcanvas" data-bs-target="#Sidebar">
                    <i class="fa-solid fa-bars"></i>
                </a>
            </div>
            <div class="container-fluid d-none d-lg-block d-xl-block " id="Dashbord_Head" ><!--Time-->
                <i class="text-info" style="margin: 220px;">Marketig Dash Bord</i>
                <div id="Logout_TIME">
                <li id="time"></li>
                <li><a href="index.py" id="LOGOUT"> <i class="glyphicon glyphicon-off log_icons"></i class="glyphicon glyphicon logout"> Logout</a></li>
                </div>
                </div><!--End-->
                
            <div id="Secount_continer_box">
                      <div class="row">
                        <div class="col-md-2"></div>
                            <div class="col-md-10">
                             <h3 style="font-family: verdana;font-weight: bold;font-size: 20px;color: rgb(0, 208, 255);">Aprroved Client</h3>
                                <table class="table">
                                    <thead><tr>
                                        
                                        <td>CID</td>
                            
                                        <td>Name</td>
                                        <td>Email</td>
                                        <td>Phone Number</td>
                                        <td>Organization</td>
                                        <td>project</td>
                                        <th>Budget</th>
                                        <th id='a1'>ADD BY</th>
                                        <td>Action</td>
                                    </tr></thead>
                                    <tbody>""")
for a in rec2:
    print("""
                                        <tr>
                                            <form method="post" enctype="multipart/form-data">
                                                <td><input type="number" value="%s" name="cid" style="border: none;width:40px" readonly></td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td id='a1'>%s</td>
                                                <td><input type="submit" value="invoice" name="invoice" class="btn btn-primary"></td>
                                            </form>
                                        </tr>
                                        """%(a[0],a[1],a[2],a[3],a[4],a[11],a[13],a[19]))
print("""
                                    </tbody>
                                  </table>
                                   <h3 style="font-family: verdana;font-weight: bold;font-size: 20px;color: rgb(0, 208, 255);">Un Approved Client's</h3>
                                <table class="table">
                                    <thead><tr>
                                        
                                        <td>CID</td>
                            
                                        <td>Name</td>
                                        <td>Email</td>
                                        <td>Phone Number</td>
                                        <td>Organization</td>
                                        <td>project</td>
                                        <td>Budget</td>
                                        <td>Reason</td>
                                       <th id='a1'>ADD BY</th>
                                        <td>Action</td>
                                    </tr></thead>
                                    <tbody>""")
for a1 in rec3:
    print("""<tr><form method="post" enctype="multipart/form-data">
                    <td><input type="number" value="%s" name="cid" style="border: none; width:40px" readonly></td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td style="font-size:14px">%s</td>
                                                <td id='a1'>%s</td>
                                                <td><input type="submit" value="invoice" name="invoice" class="btn btn-primary"></td>
                                                </tr>
                                                </form>
"""%(a1[0],a1[1],a1[2],a1[3],a1[4],a1[11],a1[13],a1[16],a1[19]))


print("""
                                  </table>
                                   <h3 style="font-family: verdana;font-weight: bold;font-size: 20px;color: rgb(0, 208, 255);">Invoived Client's</h3>
                                    <table class="table">
                                    <thead><tr>
                                        
                                        <td>CID</td>
                                        <td>Name</td>
                                        <td>Email</td>
                                        <td>Phone Number</td>
                                        <td>Organization</td>
                                        <td>project</td>
                                        <td>Issue Date</td>
                                        <td>Status</td>
                                        <th id='a1'>ADD BY</th>
                                    </tr></thead>
                                    <tbody>""")
for b in rec4:
    print("""
                                        <tr>
                                            
                                                <td><input type="number" value="%s" name="cid" style="border: none; width:40px" readonly></td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td>%s</td>
                                                <td id='a1'>%s</td>
                                                
                                            
                                        </tr>
                                        """%(b[0],b[1],b[2],b[3],b[4],b[11],b[17],b[14],b[19]))

print("""
                  </tbody>
                                </table>          
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
          
        </script>
</body>
</html>""")
invoice=form.getvalue('invoice')
if invoice !=None:
    cid=form.getvalue('cid')
    print("""<script>
              location.href="marketing_invoic.py?ID=%s&cid=%s"
            </script>
            """ % (ID,cid))