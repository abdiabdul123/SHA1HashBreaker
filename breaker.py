import time
import hashlib
import sys


def hasher(str):
   # original_Hash = input("Enter the hash: ")
    num = 0
    # password_list = open('10-million-password-list-top-1000000.txt').readlines()
    password_list = open('10-million-password-list-top-1000000.txt').read()  # opening the file that is saved into the folder so that we can start comparing each hashed password to given one.

    # for password in password_list:
    for password in password_list.split('\n'):  # splitting the file by name, therefore making password each line on the txt to test compared to our inputted hash
        """""
         print(password, num) // testing to make sure my num+=1 would work
        num+=1
        """""
        hashedPassword = hashlib.sha1(password.encode()).hexdigest()  # this is where our password is turned into an encoded version of the string, then turned into bytes by the hexidigest call, which is then hashed ans saved into the hashed password object
        start = time.time()
        if hashedPassword == str:  # where we make sure our hashed password is equal to the given hashed password, we also are counting how many tries it takes before it fails, or succeeds.
            num += 1
            end = time.time()
            seconds = end-start
            print("password is:",password,"number of tries took were: ", num, 'time taken: ', seconds,"seconds'")
            quit()
        elif hashedPassword != str:
            num += 1
            print("Current number of tries: ", num)

    print("Inserted password isn't apart of the list")


def salt_hash(str,str2):
    saltHash = str
    hashOrig= str2

    num = 0
    password_list = open('10-million-password-list-top-1000000.txt').read()  # opening the file that is saved into the folder so that we can start comparing each hashed password to given one.

    for password in password_list.split('\n'):  # splitting the file by name, therefore making password each line on the txt to test compared to our inputted hash

        combination = str + password # here we combine the salt with the first password in the list
        hashed_password = hashlib.sha1(combination.encode()).hexdigest() #here we hash that value

        start_time = time.time()
        if hashed_password == hashOrig:  # where we make sure our hashed password is equal to the given hashed password, we also are counting how many tries it takes before it fails, or succeeds.
            num += 1
            end_time = time.time()
            seconds = end_time - start_time
            print("password is:", password, "number of tries took were: ", num, 'time taken: ', seconds,"seconds'")
            quit()

        elif hashed_password != hashOrig:

            num += 1
            print("Current number of tries: ", num)

    print("Inserted hash and salt aren't apart of the list")


#run's the above program depending on how many arguements are taken(declaring if it's a salt hash or a normal hash)
if (len(sys.argv)<=1 or len(sys.argv)>3): #checks if one or 2(for salt hash) are passed.
    print("not enough arguements")

elif (len(sys.argv) == 2): #(tried changing the 2 to 1, don't get why it won't work unless it's a 2, assuming it's non-zero based, so when it says 2 it means less than 2(meaning 1)if length of arguements is 2, then only 1 arguement was passed so we are assuming it's just the non-salt hash, so we run it through the first normal SHA1 hash breaker.
    hash1 = sys.argv[1] #sets the first element in the arg array to hash1, then proceeds to run that arguement into the hasher function
    hasher(hash1)

elif (len(sys.argv) == 3): #(3 equals 2, so i think when it says length is 3, it means there are only 2 arguements) length of arguements is 3, so we have two arguements passed
    salt_term = sys.argv[1] #set the first element as the salt term
    original_hash = sys.argv[2]#set the second element as the whole full hash.
    hashed_salt_term = hasher(salt_term) #we first hash the salted term
    salt_hash(hashed_salt_term,original_hash)#we now run the hashed salted term, and compare it when concatended with the hashed password list to see if it matches the original hash. If it does, that password in the list is the password, and we broke the SHA1.



#salt_hash('f0744d60dd500c92c0d37c16174cc58d3c4bdd8e','ece4bb07f2580ed8b39aa52b7f7f918e43033ea1')
#hasher('801cdea58224c921c21fd2b183ff28ffa910ce31')
