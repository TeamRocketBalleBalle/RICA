import sqlite3
# Creating Connection with Database

conn = sqlite3.connect('Rica_AlphaV0.1.db')
cur = conn.cursor()
# Dropping old Tables
cur.execute("DROP TABLE IF EXISTS Doctors")
cur.execute("DROP TABLE IF EXISTS Patients")
cur.execute("DROP TABLE IF EXISTS Chemists")
cur.execute("DROP TABLE IF EXISTS Profiles")
# Making Table Doctors
cur.execute("""CREATE TABLE Doctors(  
    name TEXT,
    email TEXT,
    Contact_No INTEGER,
    specialization TEXT,
    loc TEXT,
    pass TEXT,
    appointment BLOB,
    UID INTEGER)""")
# Making Patients Tables
cur.execute("""CREATE TABLE Patients(
    reg_no INTEGER,  
    name TEXT,
    email TEXT,   
    Contact_No INTEGER,  
    history BLOB,     
    loc  TEXT,        
    DOB  DATE,        
    UID  INTEGER ,        
    password TEXT,    
    Prescription BLOB)
    """)
# Making Chemists Table
cur.execute("""CREATE TABLE Chemists(
    Name TEXT,
    email TEXT,
    Contact_No INTEGER,
    Rating REAL,
    Location TEXT,
    UID INTEGER,
    password TEXT)
    """)
# Making Profiles Table
cur.execute("""CREATE TABLE Profiles(
    email TEXT,
    UType TEXT)
""")
print("EXECUTED SUCCESSFULLY")
conn.commit()
conn.close()
