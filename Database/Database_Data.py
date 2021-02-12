# Doctors Table Data
from werkzeug.security import generate_password_hash
import logging
Doctor_Details = [
    (
        "Dr. Ashok Rajgopal", "Dr. Naresh Trehan", "Prof. Dr. Suresh H. Advani", "Dr. Ashok Seth",
        "Dr. Sandeep Vaishya", "Dr IPS Oberoi", "Prof. Dr. Mohamed Rela", "Dr Randhir Sud", "Dr. Arvinder Singh Soin",
        "Dr. R.C.M Kaza", "Dr Harit Chaturvedi", "Dr. Ajay Kaul", "Dr. Kapil Kumar", "Dr Aditya Gupta",
        "Dr Devi Prasad Shetty", "Dr. V. P. Singh", "Dr Sandeep Attawar", "Dr. Sumana Manohar", "Dr. Ashok Vaid",
        "Dr. Pradeep Sharma"
    ),
    (
        'ashokraj@gmail.com', 'trehannaresh@yahoo.in', 'advani1232@gmail.com', 'sethashok@gmail.com',
        'sandeepp897@gmail.com', 'oberoiameeri@gmail.com', 'relamohd@live.in', 'randhirsud1276@hotmail.com',
        'arvindsing45@gmail.com', 'kaza420@gmail.com', 'chaturvediharnit12@gmail.com', 'ajay7kaul8@gmail.com',
        'kapilkumar@hotmail.com', 'adiguptu1201@yahoo.in', 'shettyprasad@gmail.com', 'vpsingh34@gmail.com',
        'sandeep34lmao@live.in', 'sumana01munana@gmail.com', 'ashokvaid@gmail.com', 'pradeepsharma.01@gmail.com'
    ),
    (
        3477302818, 8331300318, 6229702617, 9047300542, 8099201418, 6306582135, 5245565495, 7329986346, 7738649485,
        7105693129, 5406633723, 6456022686, 9936262722, 6622662208, 8304651662, 5261174285, 9466204636, 8820565072,
        5236879086, 8279031741
    ),
    (
        "Cardiologist", "Paediatrician", "ENT specialist", "Psychiatrists", "Dentist", "Paediatrician",
        "Orthopaedic surgeon", "Psychiatrists", "ENT specialist", "Dentist", "Gynaecologist", "Radiologist",
        "Cardiologist",
        "Neurologist", "Gynaecologist", "Audiologist", "Radiologist", "Cardiologist", "Orthopaedic surgeon",
        "Neurologist"
    ),
    (
        'Noida Uttar pradesh', 'Rohini, Delhi', 'gurgaon haryana', 'Shimla Himachal Pradesh', 'Lucknow Uttar Pradesh',
        'Pune Maharashtra', 'Jaipur Rajasthan', 'Kullu Himachal Pradesh', 'Ghaziabad Uttar Pradesh',
        'Indore Madhya Pradesh', 'Bhopal Madhya Pradesh', 'Gwalior Madhya Pradesh', 'Panchkula Haryana',
        'Sonipat Haryana', 'Chandigarh Haryana', 'Greater Mumbai Maharashtra', 'Meerut Uttar Pradesh',
        'Agra Uttar Pradesh', 'Indore Madhya Pradesh', 'Manali Himachal Pradesh'
    ),
    (
        "MKF2sh", "nF1B37", "wLP6IY", "66kwQ2", "hFr1bX", "yxE5iwa", "5ZhXG", "1GiIv", "GyBg7d", "sdSb4D", "'HQt8u`",
        "xNW98y", "2pmXm", "N6WiytSI", "bek7jDxj", "nL2Qr9E7", "cYWEr7ZL", "C6iv1GtF", "qxnqLS4u", "SsyST2bo"
    ),
    (
        2008, 2016, 1998, 2017, 1997, 1998, 2008, 2016, 2018, 2005, 1995, 1998, 2007, 2017, 2019, 2014, 2013, 2008, 2006, 2008
    )

]
Doctors_Data = []

count = 0
for i in range(20):
    Doctors_Data.append([])
    for j in range(len(Doctor_Details)):
        Doctors_Data[i].append(Doctor_Details[j][i])
    Doctors_Data[i].append("{}")
    Doctors_Data[i].append(i + 1)
    Doctors_Data[i][5] = generate_password_hash(Doctors_Data[i][5])
    Doctors_Data[i] = tuple(Doctors_Data[i])
    count += 1
print(Doctors_Data)
# Patients Table Data
Patients_Details = [
    (
        1, 2, 3
    ),
    (
        "Yash", "SHR08OPXD", "MofoAkshat"
    ),
    (
        'ysh@123.com', 'Shr@epic.com', 'Aks@epic.com'
    ),
    (
        1234567891, 3454389841, 6584271395
    ),
    (
        'nothing', 'Hyper Tension', 'Covid Survivor'
    ),
    (
        'Delhi', 'Omicron Noida', 'Delta Noida'
    ),
    (
        '22/06/2003', '08/04/2004 ', '04/08/2001'
    ),
    (
        1, 2, 3
    ),
    (
        "HelloYash", 'testcase1 ', 'testcase2'
    ),
    (
        "{}", "{}", "{}"
    )]

Patients_Data = []
for i in range(3):
    Patients_Data.append([])
    for j in range(len(Patients_Details)):
        Patients_Data[i].append(Patients_Details[j][i])
    Patients_Data[i][8] = generate_password_hash(Patients_Data[i][5])
    Patients_Data[i] = tuple(Patients_Data[i])
    count += 1
print(Patients_Data)
# Chemists Table Data
Chemists_Details = [
    (
        "Ram Gopal", "Gabbar", "Jayant"
    ),
    (
        "ramgopal@123.com", "gabbarakshay@321.com", "jayant@456.com"
    ),
    (
        9876543210, 8976543210, 9384758393
    ),
    (
        4.7, 4.3, 3.9
    ),
    (
        "Borawali East", "Alpha 1", "Gurugram"
    ),
    (
        1, 2, 3
    ),
    (
        "RamG123", "Insaaf", "SaasModeOn"
    )
]
Chemists_Data = []
for i in range(3):
    Chemists_Data.append([])
    for j in range(len(Chemists_Details)):
        Chemists_Data[i].append(Chemists_Details[j][i])
    Chemists_Data[i][6] = generate_password_hash(Chemists_Data[i][6])
    Chemists_Data[i] = tuple(Chemists_Data[i])
    count += 1
print(Chemists_Data)

# Profiles Table data

Profiles_Data = []
for i in range(3):
    Profiles_Data.append((Chemists_Data[i][1], 'Chemist'))
for i in range(3):
    Profiles_Data.append((Patients_Data[i][2], 'Patient'))
for i in range(20):
    Profiles_Data.append((Doctors_Data[i][1], 'Doctor'))

# print(Profiles_Data)

# Generating Hash Password

#
# new_password_for_Doctors = []
# for i in range(20):
#     new_password_for_Doctors.append(generate_password_hash(Doctors_Data[i][5]))
# # for i in range(20):
# #     Temp_List = list(Doctors_Data[i])
# #     print(Temp_List[5])
# #     print(type(Doctors_Data[i][5]))
# # print(new_password_for_Doctors)
#
# for i in range(20):
#     Temp_list = list(Doctors_Data[i])
#     Temp_list[5] = generate_password_hash(Temp_list[5])
#     Doctors_Data[i] = tuple(Temp_list)
# print(Doctors_Data)
data = logging.getLogger("Data Updated")

data.debug("Data Updated Successfully")