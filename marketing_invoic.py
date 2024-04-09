#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("content-type:text/html \r\n\r\n")
import  cgi, cgitb,pymysql,smtplib
cgitb.enable()
form=cgi.FieldStorage()
ID=form.getvalue("ID")
cid=form.getvalue('cid')
con1=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur1=con1.cursor()
q="""select * from employee1 where EID='%s'"""%ID
cur1.execute(q)
rec=cur1.fetchall()
####client tabel#######
con3=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur3=con3.cursor()
Q="""select * from client where CID='%s'"""%cid
cur3.execute(Q)
rec2=cur3.fetchall()
for j in rec2:
    Tax=j[13]*.14
    Toate=Tax+j[13]
####invoicen
con4=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur4=con4.cursor()
I="""select MAX(CID) from client where status='invoiced'"""
cur4.execute(I)
rec4=cur4.fetchone()
if rec4[0]!=None:
    n=rec4[0]
else:
    n=0
z=""
if n<=9:
    z="000"
elif n==10 or n<=99:
    z="00"
elif n>99 or n<=999:
    z="0"
invoice_no=z+str(n+1)
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
    #yes,#byes{
        display: none; /* this for client input form yes no button */
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
        
    }
    .profil{
        background-color:#7ee5f2d3;
        border-radius: 10px 10px 0px 0px;
        margin-bottom: 5px;
        height: 120px;
    }
    li{
    color: #23395f;
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
#Secount_continer_box hr{
    background-color: #000;
    height: 2px;
}
#Secount_continer_box p{
    margin-top: 20px;
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
#LOGOUT{
    color: red;
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
#form{
    border: 2px solid white; 
    background-color: white; 
    border-radius: 2px; 
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px; 
}
input{
    border: none;
    background-color: #fff;
}
table input{
    width: 90px;
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
    profile = "./dbmedia/" + i[16]

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
        """ % (ID, ID, ID, ID, ID, ID, ID, ID, ID, ID, ID))
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
                      
                <div class="row" id="tas">           
                    <div class="col-sm-3"></div>
                    <div class="col-md-6" style="background-color: #fff; border:2px solid">
                        <form method="post" enctype="multipart/form-data">
                        <div class="row">
                            <div class="col-md-6" style="color: #23395f;">
                                <h3>TECHVOLT<sub>SOFTWARE</sub></h3>
                                <li>Coimbatore</li>
                                <li> +91 8428983975</li>
                            </div>
                            <div class="col-md-6">
                                <h1 style="margin-top: 70PX; margin-left: 40PX;color: orange;">INVOICE</h1>
                            </div>
                        </div>
                        <hr>
                        <div class="row">
                            <div class="col-md-6">
                                <li><input type="text" name="Organization" value="%s" readonly></li>
                                <li><input type="text" name="address" value="%s" readonly></li>
                                <li><input type="text" name="city" value="%s" readonly></li>
                                <li><input type="text" name="picode" value="%s" readonly></li>
                            </div>
                            <div class="col-md-6">
                                <li>invoice no</li>
                                <li><input type="text" name="incoiveno" value="%s"readonly></li>
                                <li>Duedate</li>
                                <li><input type="date" name="Duedate" required></li>
                                <li>Issue Date</li>
                                <li><input type="date" name="Issue_date" required></li>
                            </div>
                        </div>
                        <hr>
                        <div class="row">
                            <div class="col-sm-12">
                                <table class="table">
                                    <thead><tr>
                                        <th>Project</th>
                                        <th>Delivery date</th>
                                        <th>Cost</th>
                                        <th>Tax</th>
                                        <th>Total</th>
                                    </tr></thead>
                                    <tbody>
                                        <tr>
                                            <td><input type="text" name="prject" value="%s" readonly style="width:140px"></td>
                                            <td><input type="date" name="Delevary_date" value="%s" required ></td>
                                            <td><input type="number" name="cost" style="border: 2px solid;" value="%s"  id="cost" onchange="tax()"></td>
                                            <td><input type="number" name="Tax" id="taxs" value="%s" required></td>
                                            <td><input type="number" name="total" id="total" value="%s" required></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <p> contact  </p>
                                <li> <input type="text" name="phno" value=" +91 9384904893" readonly></li>
                                <li> <input type="text" name="mail" value="gowthamsakthivel@gmail.com"  readonly style="width:300px"></li>
                            </div>
                            <div class="col-md-6"></div>
                        </div>
                        <hr>
                        <div class="row">
                            <div class="col-md-6">
                                <B>NOTE:</B>
                                <li>Mention invoice Number  while making payment</li>
                                <li>This invoice will be valid for 15 days only</li>
                            </div>
                            <div class="col-md-6">
                                <li>Bank Details</li>
                                <li><input type="text" value="Indian overseas Bank" name="bank" readonly></li>
                                <li>Ac/NO:<input type="text" name="acno" value="13242567635" readonly></li>
                                <li>AC/Name:<input type="text" name="acname" value="TECHVOLT.pvt" readonly></li>
                            </div>
                        </div>
                        <hr>
                        <div class="row">
                            <div class="col-md-3 form-group">
                            </div>
                           <div class="col-md-6 form-group">
                            <input type="submit" value="send" name="send" class="form-control btn btn-primary">
                           </div> 
                            <div class="col-md-3 form-group">
                            </div> 
                        </div>
                   </form>
                 </div>
     <div class="col-sm-3"></div>                            
             
         </div>
                        </div><!--End-->"""%(j[4],j[7],j[8],j[10],invoice_no,j[11],j[12],j[13],Tax,Toate))
print("""                        
               
            </div>
            
        </div>

        
    </div>
   
    <script>
    //------------------------------------------------Sayary------------------------------------//
    function tax(){
           var cost=document.getElementById('cost');
           console.log(cost.value)
           taxs=cost.value*0.14
           var net_cost=Number(cost.value)+Number(taxs)
           console.log(net_cost)
           document.getElementById('taxs').value=taxs
           document.getElementById('total').value=net_cost
           }
            //----------------------------Time set event----------------------/
            var s=new Date()
            document.getElementById('time').innerHTML= +""+s.toLocaleString()
            //______________________________End______________________________//
        
        </script>
</body>
</html>
""")
send=form.getvalue('send')


import os
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from fpdf import FPDF  # Import FPDF library for PDF generation

# Define the directory path where you want to save the PDF files
dbmedia_directory = "invoice/invo"

# Check if the directory exists, if not create it
if not os.path.exists(dbmedia_directory):
    os.makedirs(dbmedia_directory)

# Assuming `send`, `form`, `j`, `cid`, `ID`, and other variables are defined somewhere in your code.

if send is not None:
    Organization = form.getvalue('Organization')
    address = form.getvalue('address')
    city = form.getvalue('city')
    picode = form.getvalue('picode')
    Issue_date = form.getvalue('Issue_date')
    Duedate = form.getvalue('Duedate')
    incoiveno = form.getvalue('incoiveno')
    prject = form.getvalue('prject')
    Delevary_date = form.getvalue('Delevary_date')
    cost = form.getvalue('cost')
    Tax = form.getvalue('Tax')
    total = form.getvalue('total')
    name = j[1]
    phno = j[3]
    email = j[2]
    binesstype = j[5]
    contact_email = i[2]
    contact_number = i[3]

    # Inserting data into the invoice table
    con = pymysql.connect(host="localhost", user="root", password="", database="erp")
    cur = con.cursor()
    IN = """INSERT INTO `invoice`(CID,name,Phone_no,email,organizationname,businesstype,project,issue_date,Due_date, invoice_no, Amount, deleviry_date,Status,Payment_Satus,project_status,EID,EMPname) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cur.execute(IN, (cid, name, phno, email, Organization, binesstype, prject, Issue_date, Duedate, incoiveno, total,Delevary_date, 'Invoiced', 'Notpaid', 'NOT_Assigned', ID,i[1]))
    con.commit()

    # Create PDF file
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    # Write data to PDF
    pdf.cell(200, 10, txt="Invoice", ln=True, align="C")
    pdf.cell(200, 10, txt="TECHVOLT SOFTWARE", ln=True, align="L")
    pdf.cell(200, 10, txt="Coimbatore", ln=True, align="L")
    pdf.cell(200, 10, txt="+91 8428983975", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Invoice NO: {incoiveno}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Organization: {Organization}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Issue Date: {Issue_date}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Due Date: {Duedate}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Delivery date: {Delevary_date}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Project: {prject}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Cost: {cost}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Tax: {Tax}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Total: {total}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Contact: {contact_email}, {contact_number}", ln=True, align="L")
    pdf.cell(200, 10, txt="NOTE: Mention invoice Number while making payment. This invoice will be valid for 15 days only", ln=True, align="L")
    pdf.cell(200, 10, txt="Bank Details", ln=True, align="L")
    pdf.cell(200, 10, txt="Indian overseas Bank", ln=True, align="L")
    pdf.cell(200, 10, txt="Ac/NO: 13242567635", ln=True, align="L")
    pdf.cell(200, 10, txt="AC/Name: TECHVOLT.pvt", ln=True, align="L")
    pdf_output = os.path.join(dbmedia_directory, f"invoice_{incoiveno}.pdf")
    pdf.output(pdf_output)

    # Email Sending
    form_Add = "gowthamyouth2001@gmail.com"
    password = "bekchburtacmufex"
    to_addres = email
    subject = "TECHVOLT SOFTWARE(Invoice)"
    body = f"TECHVOLT SOFTWARE\nCoimbatore\n+91 8428983975\nInvoice NO: {incoiveno}\nIssue date: {Issue_date}, Due date: {Duedate}"

    # Email Sending with attachment
    msg = MIMEMultipart()
    msg['From'] = form_Add
    msg['To'] = to_addres
    msg['Subject'] = subject

    # Attach the PDF file
    with open(pdf_output, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(pdf_output)}",
    )

    msg.attach(part)

    # Connect to SMTP server and send email
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(form_Add, password)
    server.sendmail(form_Add, to_addres, msg.as_string())
    server.quit()

    # Update file name in the database
    update_filename_query = """UPDATE `invoice` SET `invoice_file` = %s WHERE `invoice_no` = %s"""
    cur.execute(update_filename_query, (os.path.basename(pdf_output), incoiveno))
    con.commit()

    # Update Status
    update_status_query = """UPDATE `client` SET `status`='invoiced', IssueDate='%s' WHERE `CID`='%s'""" % (Issue_date, cid)
    cur.execute(update_status_query)
    con.commit()
    print("""<script>alert("Invoice sent")</script>""")
    print("""<script>
                 location.href="MarketinnewClient.py?id=%s"
               </script>
                """ % ID)
