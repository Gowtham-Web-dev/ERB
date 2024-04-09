#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import  cgi, cgitb, pymysql
cgitb.enable()
form=cgi.FieldStorage()
ID=form.getvalue("id")
con1=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur1=con1.cursor()
q="""select * from employee1 where EID='%s'"""%ID
cur1.execute(q)
rec=cur1.fetchall()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HR</title>
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
    .s{
    width: 350px;
    background-color: white; 
    height: max-content; 
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
    .profil img{
    border-radius: 50%
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
#newpwd{
    display: none;

}
#newprofile{
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
</div>
""")
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
              <li><a href="./Hr copy.py?id=%s" id="a"style="background-color: #23395f; color: white; margin-left: -10px; margin-right: -8px; border-left:3px solid orange;"><span class="fa fa-user-circle" style="color: #CFEEFF;" ></span> Profile </a></li>
              <li><div class="dropdown">
                <a data-toggle="dropdown"  id="op"><span class="fa fa-bell "></span>Leave<span class="caret" style="margin-top: 10px;"></span></a>
                <ul class="dropdown-menu">
                     <li><a href="./HR_leaveform.py?id=%s" target="_self">New <span class="fa  fa-plus"></span></a></li>
                    <li><a href="./HR_existingleave.py?id=%s" target="_self"> Existing </a></li>
                </ul>
            </div>
            </li>
            <li><a href="./HR_salarytablepy?id=%s" target="_self" id="a"><span class=" fa fa-money-bill-1-wave"></span>Salary</a></li>
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
    <li><a href="./HR_salarycalculation.py?id=%s" id="a"> <i class="fa fa-calculator"></i></i> Salary Calculation </a></li>
    <li><div class="dropdown">
        <a data-toggle="dropdown"  id="op"><span class="fa fa-bell"></span>Announcement<span class="caret" style="margin-top: 10px;"></span></a>
        <ul class="dropdown-menu">
             <li><a href="./HR_Announcementform.py?id=%s" target="_self">New <span class="fa  fa-plus"></span></a></li>
            <li><a href="./HR_Announcementstatus.py?id=%s" target="_self">  Existing </a></li>
        </ul>
    </div>
    </li>
    <hr id="hr" class="d-md-none">
    <li><a href="index.py" id="LOGOUT_SM" class="d-md-none"> <i class="glyphicon glyphicon-log-out log_icons "></i class="glyphicon glyphicon logout"> Logout</a></li>
                          
          </div>
        </div><!-- Sidebar End-->
    </div>
        </div>
        """%(ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID))
print(""""
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
                """)

print("""
            <div id="Secount_continer_box">
                <div class="container-fluid"> 
                    <div class="row">
                        <div class="col-md-4"></div>
                        <div class="col-md-2">
                        <div class="s">
                            <div class="main">
                                <div class="profil" ><img src='%s' alt="image" height="150px" width="150px"></div>
                                 <div class="detial">
                                    <h3>%s</h3>
                                    <p>%s</p>
                                    <table align="center">
                                  <tr> <th> Department:</th><th> %s</th></tr>
    
                                </table>
                                 </div> """%(profile,i[1],i[10],i[8]))
print("""
                            
                            </div>
                                <div class="d-flex justify-content-around p-3">
                                    <button onclick="changepwd()" class="btn btn-info">change Password</button>
                                    <button onclick="Updateprfile()" class="btn btn-info">Update Profile</button>
                                </div>
                                <form method="post" enctype="multipart/form-data" id="newpwd">
                                    <div class="form-group">
                                        <label>New password</label>
                                        <input type="text" required name="password" class="form-control" placeholder="Enter password">
                                        <br>
                                        <input type="submit" name="update" class="btn btn-info" style="margin: 0px 0px 20px;text-align: right;" >
                                    </div>
                                </form>
                                <form method="post" enctype="multipart/form-data" id="newprofile">
                                    <div class="form-group">
                                        <label>Update Profile:</label>
                                        <input type="file" name="photo" class="form-control" placeholder="Enter password">
                                        <br>
                                        <input type="submit" name="updateprofile" class="btn btn-info" style="margin: 0px 0px 20px;text-align: right;" >
                                    </div>
                                </div>
                                
                                </div>
                                </div>
                            </div>      
                        </div><!--End-->
                        
               
            </div>
            """)
print("""
            
        </div>

        
    </div>
   
    <script>
    //------------------------------------------------Sayary------------------------------------//
    
            //----------------------------Time set event----------------------/
            var s=new Date()
            document.getElementById('time').innerHTML= +""+s.toLocaleString()
            //______________________________End______________________________//
            function Updateprfile(){
                document.getElementById('newprofile').style.display="block";
                document.getElementById('newpwd').style.display="none";
            }
            function changepwd(){
                document.getElementById('newprofile').style.display="none";
                document.getElementById('newpwd').style.display="block"; 
            }
          
        </script>
</body>
</html>""")

import os

Submit=form.getvalue("update")
if Submit!=None:
    passwod=form.getvalue('password')
    con = pymysql.connect(host="localhost", user="root", password="", database="erp")
    cur = con.cursor()
    q1 = """update employee1 set password='%s' where EID='%s'"""%(passwod,ID)
    cur.execute(q1)
    con.commit()
    print("""<script>alert("password is Updated")</script>""")
prfileUpdate=form.getvalue("updateprofile")
if prfileUpdate !=None:
    print(prfileUpdate)
    profile1 = form['photo']
    if profile1.filename:
        fns = os.path.basename(profile1.filename)
        open("dbmedia/" + fns, "wb").write(profile1.file.read())
        con2 = pymysql.connect(host="localhost", user="root", password="", database="erp")
        cur2 = con2.cursor()
        q2= "update employee1 set profile='%s' where EID='%s'" % (fns, ID)
        cur2.execute(q2)
        con2.commit()
        print("""<script>
                alert(" Profile  updated")
                </script>""")
            # if profile.filename:
        #     fns=os.path.basename(profile.filename)
        #     open("dbmedia/"+fns,"wb").write(profile.file.read())
        #     q="update emp1 set image='%s' where id='%s'"%(fns,9)
        #     cur.execute(q)
        #     con.commit()
        #     print("""<script>
        #     alert("updated")
        #     </script>""")