from flask import *
import sqlite3

app = Flask(__name__)  
 
@app.route("/")  
def index():  
    return render_template("index.html") 
 
@app.route("/add")  
def add():  
    return render_template("add.html") 

@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"]  
            product = request.form["product"]
            price = request.form["price"]  
            with sqlite3.connect("product.db") as con:  
                curp = con.cursor()  
                curp.execute("INSERT into Orders (name, email, product, price) values (?,?,?,?)",(name,email,product,price))  
                con.commit()  
                msg = "Order successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the order to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()   

@app.route("/view")  
def view():  
    con = sqlite3.connect("product.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Orders")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)  

@app.route("/delete")  
def delete():  
    return render_template("delete.html")  

@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("product.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from Orders where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record.html",msg = msg) 

@app.route("/update")  
def update():  
    return render_template("update.html")  


@app.route("/updaterecord",methods = ["POST"])  
def updaterecord():  
     
    if request.method == "POST":  
        try:  
            id = request.form["id"] 
            name = request.form["name"]  
            email = request.form["email"]  
            product = request.form["product"]
            price = request.form["price"]  
            with sqlite3.connect("product.db") as con:  
                curp = con.cursor()  
                
                curp.execute("update Orders set name=?,email=?,product=?,price=? where id=?",(id,name,email,product,price)) 
                con.commit()  
                msg = "Order Updated successfully"  
        except:  
            con.rollback()  
            msg = "We can not Update the order to the list"  
        finally:  
            return render_template("success.html",msg = msg) 
            con.close()   
  

 
  
if __name__ == "__main__":  
    app.run(debug = True)