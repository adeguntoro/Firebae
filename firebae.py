import pyrebase 
##pyrebase bisa di download di https://github.com/thisbejim/Pyrebase.
##untuk mendapatkan config file atau kode bisa didapatkan pada opsi Web di Firebase
##jangan lupa untuk menginstal beberapa requriment yang diperlukan.
##pastikan baca README yang ada atau require text.

import pyrebase
##config = {
##  "apiKey"			: "AIzaSyCrO3u9ZcydR6EvecSIgtCZP7jCQX_Bdm0",
##  "authDomain"		: "python-296c0.firebaseapp.com", 
##  "databaseURL"		: "https://python-296c0.firebaseio.com",
##  "storageBucket"	: "python-296c0.appspot.com",
##  "serviceAccount"	: "path/to/serviceAccountCredentials.json"
##}
config = {
  "apiKey"		: "AIzaSyAEGZaEPnJkb0Kte4BROjWSm8KpmpVUc18",
  "authDomain"		: "skripsi1-caef6.firebaseapp.com", 
  "databaseURL"		: "https://skripsi1-caef6.firebaseio.com",
  "storageBucket"	: "skripsi1-caef6.appspot.com"
}
firebase 	= pyrebase.initialize_app(config)
##auth		= firebase.auth()
db = firebase.database()

##mengupdate database
##db.child("Sensor1").update({"Persentasi": "200", "Level": "1020"})

##menghapus data
##db.child("users").child("Morty").remove()
##db.child("Sensor1").remove()


##mengupload data di tabel yang sudah di tentukan
data = {"Persentase": "90", "Level": "1020"}
db.child("Sensor1").set(data)

##mengupload data dengan unique id / sembarang nama
#data = {"Persentasi": "90", "Level": "1020"}
#db.child("Sensor1").push(data)

##menampilkan data
#a = db.child("Sensor1").get()
#print(a.val())
