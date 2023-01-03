import sqlite3
con=sqlite3.connect('bbsdb2.db')
cur=con.cursor()
cur.execute('create table operator(oid int PRIMARY KEY , oname varchar(30) NOT NULL, phone varchar(10) NOT NULL, email varchar(50), address varchar(100))')
cur.execute('create table pass_booking(book_ref int PRIMARY KEY, pname varchar(30) NOT NULL, gender char(1), age int, phone varchar(10) NOT NULL, seats int, travel_on varchar(12) NOT NULL, booked_on varchar(12))')
cur.execute('create table buses(bid varchar(5) PRIMARY KEY, oid int NOT NULL rid int ,bus_type varchar(15), capacity int, fare int ) ')
cur.execute('create table route(rid int, staid int , sta_name varchar(20))')
cur.execute('create table run(bid int NOT NULL FOREIGN KEY refrences buses(bid), seat_available int , run_date varchar(20) NOT NULL)')

#cur.execute('insert into operator(oid,oname,phone,email,address) values(2001,"Kamla Travels","9876543210","kamlatravels@gmail.com","Soni Colony, Guna, Madhya Pradesh")')
#cur.execute('insert into operator(oid,oname,phone,email,address) values (2002,"Ambica Travels","9998887779","ambicatravels@gmail.com","Lalghati, Bhopal, Madhya Pradesh") ')
#cur.execute('insert into operator(oid,oname,phone,email,address) values ( 2003,"Rayeen travels","9695847345","rayeentravels@gmail.com","Sadar nagar, Bhopal, Madhya Pradesh") ')
#cur.execute('insert into operator(oid,oname,phone,email,address) values (2004,"Krishna Travels","8698479646","krishnatravels@gmail.com","Silicon City, Indore, Madhya Pradesh") ')
#cur.execute('insert into operator(oid,oname,phone,email,address) values (2005,"Srinath Travels","8765892485","srinathtravels@gmail.com","Deen Dayal Nagar, Gawalior, Madhya Pradesh") ')
#con=sqlite3.connect('SQLite_Retrieving_data.db')
#cur=con.cursor()
#res=cur.execute('alter table pass_booking add  bid varchar(5);')
#cur.execute('drop table buses')
#cur.execute('delete from pass_booking;')
#cur.execute('update pass_booking set boarding_point="Sada" where phone="987654321"')



con.commit()
cur.close()
con.close()
