Important Notes

This code snippet developed in Python will crack the hash data 100%, but I don't know if your life is long enough. :D 
I did a little experiment. If you give the hash value of the word "can", it takes 76 seconds to find the word.
If you try a word with 5 characters and only letters, you will probably wait for hours.
Note that this snippet is not an optimized hash cracker. This code is just a simple example.
This code makes hashes by placing all ascii values side by side. It then checks whether it is the same as the hash value given by the user.
It creates all the possibilities that can occur with 1 character and checks the hash values. 
If the values do not match, it creates all possible 2-character possibilities and again checks whether the hash values match. The system works this way.
