#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import  cgi, cgitb, pymysql
cgitb.enable()
form=cgi.FieldStorage()
ID=form.getvalue("id")
ID=form.getvalue("id")
con1=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur1=con1.cursor()
#######
q="""select * from employee1 where EID='%s'"""%ID
cur1.execute(q)
rec=cur1.fetchall()
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
    <link rel="stylesheet" href="./style.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="https://fontawesome.com/icons/person?f=classic&s=solid">

  <style>
    h3{
        font-weight: bolder;
        color: #009d63;
        text-decoration: underline;
        
    }
    h2{
        font-family:'Bungee Spice';
    }
    #Sidebar h2{
        font-family:"Audiowide", sans-serif;
    }
    #Sidebar{
        border-right:2px rgb(82, 88, 85) solid ;
       
    }
    li{
        margin-top: 30px;
    } 
   .Role,.Profile{ /* model style*/
        font-weight: bolder;
        color: #009d63;
        text-decoration: underline;
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
  </style>
</head>
<body>
    <div class="container-fluid "><!--log image and Name-->
        <div class="row">
        
        <div class="col-sm-5 d-md-none "><img src="./download.png" alt=""  width="100%"></div>
        <div class="col-sm-4"></div>
        <div class="col-sm-3"></div> 
    </div>
</div>
    <div class="container-fluid" style="display: flex;padding: 0;">
    <div style="background-color:#ffff ; height: max-content">
        <!--SideBar Start-->
        <div id="Sidebar" class="d-flex flex-column  offcanvas-md offcanvas-start " style="width: 215px; padding: 15px ; height: max-content; background-color: rgb(239, 241, 241);  height: 100vh;">
            <div>
             <h2 style="color: rgb(243, 29, 14);"> TECHVOLT  <span style="color: rgb(28, 88, 4);">SOFTWARE</span></h2>
             <hr id="hr">
             <h3 
             class="Profile">Personal</h3>
               <li id="op" data-toggle="modal" data-target="#myModel"><span class="fa fa-user-circle" ></span> Profile </li>
               <li><div class="dropdown">
                 <a data-toggle="dropdown" style="color: rgb(14, 13, 13); text-decoration: none; " id="op"><span class="fa fa-bell "></span>Leave<span class="caret" style="margin-top: 10px;"></span></a>
                 <ul class="dropdown-menu">
                      <li><a href="./leaveform.html" target="_self">New <span class="fa  fa-plus"></span></a></li>
                     <li><a href="./existingleave.html" target="_self"> Existing </a></li>
                 </ul>
             </div>
             </li>
             <li><a href="./salarytable.html" target="_self"><span class=" fa fa-money-bill-1-wave"></span>Salary</a></li>
             <li><div class="dropdown">
                 <a data-toggle="dropdown" style="color: rgb(14, 13, 13); text-decoration: none; " id="op"><span class="fa fa-bell"></span>Announcement<span class="caret" style="margin-top: 10px;"></span></a>
                 <ul class="dropdown-menu">
                      <li><a href="./Announcement.html" target="_self">New <span class="fa  fa-plus"></span></a></li>
                     <li><a href="./Announcement2.html" target="_self"> Existing </a></li>
                 </ul>
             </div>
             </li>
             <h3 class="Role">Role</h3>
             <li><div class="dropdown">
                <a data-toggle="dropdown" style="color:rgb(14, 13, 13); text-decoration: none;" id="op"><i class="fa fa-diagram-project"></i> Project<span class="caret" style="margin-top: 10px;"></span></a>
                <ul class="dropdown-menu">
                     <li><a href="./newproject.html" target="_self">New</a></li>
                    <li><a href="./existingproject.html" target="_self"> Existing </a></li>
                   
                </ul>

            </div>
            </li>
     <hr id="hr">
     <li><a href="index.html" style="font-weight: bold; color: red;"> <i class="glyphicon glyphicon-log-out log_icons "></i class="glyphicon glyphicon logout"> Logout</a></li>
                           
           </div>
         </div><!-- Sidebar End-->
    </div>
        <div class="flex-fill" style="background-color: #c1efde; height: 100vh;">
            <div class=" d-md-none  text-white " style="padding: 10px; background-color:black;">
                <a href="#" class="text-white" data-bs-toggle="offcanvas" data-bs-target="#Sidebar">
                    <i class="fa-solid fa-bars"></i>
                </a>
            </div>
            <div class="container-fluid"><!--Time-->
                <li id="time"></li>
                </div><!--End-->
                <hr id="hr">
            <div style="padding: 40px; background-color: #c1efde;">
                
                <div class="container-fluid"> <!-- model in profile-->
                    <div class="modal fade" id="myModel">
                        <div class="modal-dialog" style="width: 350px; background-color: white; height: max-content;"  >
                            <div class="main">
                                <div class="profil"  ><img src="./do.webp" alt="image" height="150px" width="150px" style="border-radius: 50%"></div>
                                 <div class="detial">
                                    <h3>Gowtham</h3>
                                    <p>Marketing Executive</p>
                                    <table align="center">
                                  <tr> <th> Department:</th><th> Marketig</th></tr>
    
                                </table>
                                 </div>   
                            
                            </div>
                                <div class="modal-footer" style="position: relative;">
                                    <button type="button" class="btn btn-primary"   onclick="forpwd()"  style="position: absolute; left: 10px; color: blue;  background-color: #fff;">Change Pasword</button>
                                    <button type="button" class="btn btn-primary" data-dismiss="modal" style="width: 150px;">close</button>
                                </div>
                                </div>
                            </div>      
                        </div><!--End-->
                        <div class="container-fluid" id="Existin_Leaves" style="background-color: rgba(241, 243, 241, 0.342); box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;">
                            <!--Existing leave table-->
                            <div class="row"><!--search-->
                                <div class="col-sm-4"></div>
                                <div class="col-sm-4" style="display: flex;"> 
                                    <div class="form-group" style="margin-top: 2px;">
                                        <div class="input-group">
                                            <div class="input-group-addon" style="background-color: white;"><i class="fa fa-search"></i></div>
                                            <input type="search" name="search"  placeholder="Search for month" class="form-control" id="searchInput">
                                        </div>
                                    </div>
                                    <button type="button" name="search" onclick="filterTable()" style="width: 70px; height: 30px;color: white;margin-top: 4px; background-color:#009d63;">Search</button>
                                </div>
                                <div class="col-sm-4"></div>
                            </div><!--Search bar end-->
                        
                            <table class="table">
                                <thead style="background-color: #111111;">
                                    <tr>
                                        <th>Month</th>
                                        <th>Year</th>
                                        <th>Start Date</th>
                                        <th>End Date</th>
                                        <th>Reason</th>
                                        <th>Total Leave days</th>
                                        <th>Status</th>
                                    </tr>
                                </thead>
                                <tbody style="background-color: #f0eded;">
                                    <tr>
                                        <td>Jan</td>
                                        <th>2024</th>
                                        <td>20/1/2024</td>
                                        <td>24/1/2024</td>
                                        <td>Medical leave</td>
                                        <td>2</td>
                                        <td>UnderProcess</td>
                                    </tr>
                                    <tr>
                                        <td>Jan</td>
                                        <th>2023</th>
                                        <td>2/1/2024</td>
                                        <td>4/1/2024</td>
                                        <td>Personal leave</td>
                                        <td>2</td>
                                        <td>Approved</td>
                                    </tr>
                                </tbody>
                                <tfoot style="background-color: #ffff; ">
                                    <tr>
                                        <th>Total Leave</th>
                                        <td></td>
                                        <td></td>
                                        <td></td>
                                        <td></td>
                                        <td>4</td>
                                        <td></td>
                                    </tr>
                                </tfoot>
                            </table>
                        </div><!--End-->
                        --End-->           
             
            </div>
            
        </div>

        
    </div>
    <script>
    //------------------------------------------------Sayary------------------------------------//
       
           //document.getElementById("present").value= Number(present);
        
        
            //----------------------------Time set event----------------------/
            var s=new Date()
            document.getElementById('time').innerHTML= +""+s.toLocaleString()
            //______________________________End______________________________//
           
             function closes(){//leave form close
                document.getElementById('Leave_request_forms').style.display="none";
             }
             function datecalculate(){///leave calculation
                let start_date=document.getElementById("startdate").value
                let end_date=document.getElementById("enddate").value
                let s_d=new Date(start_date)
                let e_d=new Date(end_date)
                var time_difference=e_d.getTime()-s_d.getTime()
                if(time_difference>0){
                var time_difference=time_difference/(1000*60*60*24)
                document.getElementById("totalleave").value=time_difference
                }
                else{
                    alert("Choose correct date")
                }
             }
             function empty(){/// total leave empty
                let totalleave=document.getElementById("totalleave").value
                if(totalleave==''){
                    document.getElementById("totalleave").style.border="red 2px solid";
                    document.getElementById("totalleave").style.boxShadow="0px 0px 5px red inset";1
                    alert("Total Leave Field is empty")
                    return false
                }
                else{
                    return true
                }
             }
         //__________________________________End__________________________________________//
         function filterTable() {
        var searchValue = document.getElementById("searchInput").value.trim().toLowerCase();
        var rows = document.querySelectorAll("#Existin_Leaves tbody tr");

        rows.forEach(function(row) {
            var month = row.cells[0].textContent.toLowerCase();
            if (month.includes(searchValue)) {
                row.style.display = ""; // Show the row
            } else {
                row.style.display = "none"; // Hide the row
            }
        });
    }
        </script>
</body>
</html>""")