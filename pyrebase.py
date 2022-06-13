import pyrebase
from distance import distance


config = {
    apiKey: "AIzaSyDRNRy2kWJEf6ZyQ57Q_TP6N0iloIjBUK8",
  authDomain: "p-rasp.firebaseapp.com",
  databaseURL: "https://p-rasp-default-rtdb.firebaseio.com",
  projectId: "p-rasp",
  storageBucket: "p-rasp.appspot.com",
  messagingSenderId: "235208075939",
  appId: "1:235208075939:web:0641ffba5e71a35c1ced16"
    

};


firebase = pyrebase.initialize_app(config)



storage = firebase.storage()
database = firebase.database()
a = distance()
print (a)
database.child("DB object name")
data = {"key1": a}
database.set(data)
