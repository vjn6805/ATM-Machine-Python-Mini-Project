#File for storing name and pin of the user for authentication
import pickle

#data for authentication
info={
    "user1": {"pin": 0000, "balance": 1000.0},
    "user2": {"pin": 5678, "balance": 1500.0},
    "veer" : {"pin":1234,"balance":3000}
    # Add more users as needed
}


file1=open("namepin.bat","ab")
pickle.dump(info,file1)

file1.close()
