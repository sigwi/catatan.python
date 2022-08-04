import pandas as pd

bacagaji = pd.read_csv(
"D:\LATIHAN PANDAS SUMBER DATA\DOB_Job_Application_Filings_Raw.csv")
print(bacagaji.shape) #untuk mengetahui berapa jumlah kolom dan baris
# print(bacagaji.head())
# print(bacagaji.tail())
# print(bacagaji.columns)
# print(bacagaji.isnull()) #apakah ada data kosong, biasanya tidak terlihat karena tampak sebagian dari atas dan bawah
# print(bacagaji.isnull().sum()) #jumlah data kosong per kolom
# print(bacagaji.isnull().values.any()) #apakah ada yang hilang? (true/false)
# print(bacagaji.isnull().sum().sum()) #jumlah data yang kosong? jawaban langsung total

# print(bacagaji[["Applicant's First Name","Applicant's Last Name"]])
# nama = bacagaji[["Applicant's First Name","Applicant's Last Name"]]
# print(nama.isnull().sum())

#mengganti data yg kosong dengan nama sesuai keinginan kita
# nama["Applicant's First Name"].fillna(value="Anonymous",inplace=True) #kalau kyk gini yg dirubah copy nya
bacagaji["Applicant's First Name"].fillna(value="Anonim",inplace=True) #ini baru sumbernya

#mengecek apakah masih ada yg kosong
# print(nama.isnull().sum()) #cek copy
print(bacagaji["Applicant's First Name"].isnull().sum()) #cek sumber

#bikin kolom baru, ambil dari source yg kita pilih
a=bacagaji["Applicant's First Name"]
b=bacagaji["Applicant's Last Name"]
df=pd.DataFrame(list(zip(a,b)), columns=['Nama Depan','Nama Belakang']) #bikin kolom baru dan menambah nama kolom/headers
print(df)