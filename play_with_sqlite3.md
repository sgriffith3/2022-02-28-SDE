# Learning SQLite3 demo

1. Apt install sqlite3

    `sudo apt install sqlite3`
    
2. Create a new database.

    `sqlite3 practice.db`
    
3. Show what tables exist in the database already (right now there are none).

    `>` `.tables`
    
0. Create a table


    `>` `CREATE TABLE COMPANY (NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50), SALARY REAL);`
    
    > NOTE: This is slightly different than the lab, because we removed the need of the ID - sqlite3 actually automatically generates a numeric primary key for each entry.
    
0. Get tables again. 

    `>` `.tables`
    
0. See there is nothing in that table.

    `>` `SELECT * FROM company;`
    
    > blank

0. Add some data.

    `>` `INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) VALUES ('Paul', 32, 'California', 200000.00);`
    
0. Check on that data.

0. See there is nothing in that table.

    `>` `SELECT * FROM company;`
    
0. Here are two tips to make the output easier to read. Do these.

    `>` `.mode columns`
    
    `>` `.headers on`
    
    `>` `SELECT * FROM company;`
    
    > See prettier output

0. Add another value to our table.

    `>` `INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) VALUES ('Allen', 25, 'Texas', 15000.00);`

    `>` `SELECT * FROM company`
    
    > See two lines of output


0. Update Paul's salary.

    `>` `UPDATE COMPANY set SALARY = 25000.00 where name = 'Paul';`
    
    `>` `SELECT * FROM company`
    
0. Let's pretend Allen got fired.

    `>` `DELETE from COMPANY where name = 'Allen';`
    
    `>` `SELECT * FROM company`
    

You just did CRUD!

|CRUD| SQL Action|
|---|---|
|Create| INSERT INTO|
|Read | SELECT FROM|
|Update | UPDATE|
|Delete | DELETE|
