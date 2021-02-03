# naam sahi karlena iss file ka
#  name email phone_no specialization location password appointment
fakeDoctorsKaBioData = [("Dr. Ashok Rajgopal","Dr. Naresh Trehan","Prof. Dr. Suresh H. Advani","Dr. Ashok Seth","Dr. Sandeep Vaishya","Dr IPS Oberoi","Prof. Dr. Mohamed Rela","Dr Randhir Sud","Dr. Arvinder Singh Soin","Dr. R.C.M Kaza","Dr Harit Chaturvedi","Dr. Ajay Kaul","Dr. Kapil Kumar","Dr Aditya Gupta","Dr Devi Prasad Shetty","Dr. V. P. Singh","Dr Sandeep Attawar","Dr. Sumana Manohar","Dr. Ashok Vaid","Dr. Pradeep Sharma"),('ashokraj@gmail.com','trehannaresh@yahoo.in','advani1232@gmail.com','sethashok@gmail.com','sandeepp897@gmail.com','oberoiameeri@gmail.com','relamohd@live.in','randhirsud1276@hotmail.com','arvindsing45@gmail.com','kaza420@gmail.com','chaturvediharnit12@gmail.com','ajay7kaul8@gmail.com','kapilkumar@hotmail.com','adiguptu1201@yahoo.in','shettyprasad@gmail.com','vpsingh34@gmail.com','sandeep34lmao@live.in','sumana01munana@gmail.com','ashokvaid@gmail.com','pradeepsharma.01@gmail.com'),(3477302818,8331300318,6229702617,9047300542,8099201418,6306582135,5245565495,7329986346,7738649485,7105693129,5406633723,6456022686,9936262722,6622662208,8304651662,5261174285,9466204636,8820565072,5236879086,8279031741),("Cardiologist","Paediatrician","ENT specialist","Psychiatrists","Dentist","Paediatrician","Orthopaedic surgeon","Psychiatrists","ENT specialist","Dentist","Gynaecologist","Radiologist","Cardiologist","Neurologist","Gynaecologist","Audiologist","Radiologist","Cardiologist","Orthopaedic surgeon","Neurologist"),('Noida, Uttar pradesh','Rohini, Delhi','gurgaon, haryana','Shimla, Himachal Pradesh','Lucknow, Uttar Pradesh','Pune, Maharashtra','Jaipur, Rajasthan','Kullu, Himachal','Ghaziabad, Uttar Pradesh','Indore, Madhya Pradesh','Bhopal, Madhya Pradesh','Gwalior, Madhya Pradesh','Panchkula, Haryana','Sonipat, Haryana','Chandigarh, Haryana','Greater Mumbai, Maharashtra','Meerut, Uttar Pradesh','Agra, Uttar Pradesh','Indore, Madhya Pradesh','Manali, Himachal Pradesh'),("MKF2sh","nF1B37","wLP6IY","66kwQ2","hFr1bX","yx_E5iwa","_!5ZhX{G","1G?iI)v<","{GyBg$7d","sdSb4]D","'HQ:t8u`","xNW9+8y","2pm+>Xm)","N6WiytSI","bek7jDxj","nL2Qr9E7","cYWEr7ZL","C6iv1GtF","qxnqLS4u","SsyST2bo")]
l1 = []

count = 0
for i in range(20):
    l1.append([])
    for j in range(len(fakeDoctorsKaBioData)):
        l1[i].append(fakeDoctorsKaBioData[j][i])
    l1[i] = tuple(l1[i])
    count +=1
# print(count)
# print(l1)