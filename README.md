# SHA1HashBreaker
Assignment 2 Blockchain
CSC 4980 / 6980 Blockchain & Applications
Abdullahi Abdi


SHA1 Hash Breaker

Purpose

This code has two distinct functions, the breaker and saltHash function. Each of these functions break SHA1 hashes, with the breaker.py program it takes in one arguement( a SHA1Hash) and compares it with the hash of each of our given 10-million-password-list.txt file to see if that hash matches one of the hatches in the list to find the password. The saltHash function is a salt-hash meaning that som random string was concatened to the password before it was hashed, therefore changing the hash so that it doesn't match any of the hashes in our .txt file. My fix was first adding the salt string to each of the passwords in the list, then hashing them and seeing if it matches the full hash1 we were given, if we find a match we then know the password added to the salt was the password to the hash we were given.

Imported Libraries

I imported the time and hashlib libraries for this program. The hashlib library was imported so that I could use the hashlib.sha1 function which would make my inputs a SHA1 function, which I would then compare to my inputted arguement to teest if I broke the hash or not.
Additionally, the time library was used so that I could measure time difference between the start and end of the execution time. Was needed to calculate the run time taken when attempting to break the hash.
Lastly, I used the sys library. The reason for it's implementation is beacuse I needed it to take the input the user gave me, and make it be used as an arguement for my functions to work.

How to run the program?

1. Save the  breaker.py, and the 10-million-password-list.txt file all in the same folder on your system.
2. Open terminal(or cmd for window systems), cd your way into the location of the  files.
3. (Assumption made: current Python model is installed ont your stem)To run the program type 'python [breaker.py],and after it put a space and input the the one(or two for the salt hash, for the salt hash seperate the two hashes with a space) SHA1 hash functions you want to break. ie: python breaker.py b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 or saltHash.py f0744d60dd500c92c0d37c16174cc58d3c4bdd8e ece4bb07f2580ed8b39aa52b7f7f918e43033ea1.

Questions:

a) (20 points) testing program hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
b) (25 points) medium hacker hash: 801cdea58224c921c21fd2b183ff28ffa910ce31
c) (30 points) leet hacker hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
Hint: The salt term here is: f0744d60dd500c92c0d37c16174cc58d3c4bdd8e this is concatenated
before hashing with another word to produce the salted hash.

Solution to the questions:

A.Hash:b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 the  password is: letmein, took 15 tries, and the runtime taken was 1.2 seconds.
B. Hash:801cdea58224c921c21fd2b183ff28ffa910ce31 password is vjhtrhsvdctcegth, took 999968 tries, and the runtime taken was 9.5367431640625e-07
C.(Salt Hash)Salt Hash: f0744d60dd500c92c0d37c16174cc58d3c4bdd8e, full hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 password is slayer, took 217 tries, and the runtime taken was 1.9 seconds .
