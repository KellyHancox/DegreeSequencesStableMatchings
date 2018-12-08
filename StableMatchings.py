#Gale-Shapley Algorithm
"The purpose of this project is for you to write codes that implement the Gale-Shapley Algorithm. In addition, you will determine whether or not a specific pair is unstable, given preference lists and a current matching. The ONLY IMPORT ALLOWED is  \"copy\" and you are ONLY allowed to use the copy.deepcopy() method from this package.  All of your code should be 'from scracth'"

    "In the cell below, you are to write a function called \"matched(dic)\" that takes in a dictionary and returns the boolean value False if any key is exactly '[]', and returns True otherwise."

def matched(dic):\n",
#loops through dictionary
for key in dic:
    #returns false when [] is found as a value\n",
    if dic[key] == []:
    return False\n",
return True"


"After compiling the above cell, you should be able to compile the following cell and obtain the desired outputs: True False"

    
"In the cell below, you are to write a function \"find_match(dic, fam)\" that takes in a dictionary and value 'fam', and returns the key for which fam is the value. If 'fam' is NOT the value of any key, then the method should return []."

def find_match(dic, fam):
    #loops through the dictionary\n",
    for key in dic:
        if dic[key] == fam:
           #returns key when the intended value is found\n",
           return key
    return []

    
    "In the cell below, you are to write a function \"switch(pref, dog, fam, cur_dog)\" that takes in a preference list 'pref' (in which 'fam' is a key), along with three objects 'dog', 'fam', and 'cur_dog'. This method should return the boolean value True if 'fam' prefers (based on the preference list 'pref') 'dog' over 'cur_dog', and return False otherwise."

    def switch(pref, dog, fam, cur_dog):
        #Looks through every key in the list
        for key in pref:
            #If the key is the fam, then it will check the placements of the dog
            if key == fam:
                #creates a counter to find where the dog is in the list
                count = 0\
                #Loops through values for the key
                for doggo in pref[fam]:
                    #when it finds a value, it saves the count to variables\n",
                    if doggo == dog:
                        dog_number = count
                    if doggo == cur_dog:
                        cur_dog_number = count

                    count = count + 1
        #compares the variables
        if dog_number < cur_dog_number:
            #returns true if 'fam' prefers dog over cur_dog
            return True
        #returns false if 'fam' prefers cur_dog over dog
        return False

    "In the cell below, you are to write a function \"stable(pref1, pref2)\" that takes in two preference lists (say one for dogs and the other for families), and returns a stable matching (in the form of a dictionary)."

    def stable(pref1, pref2):
        final_matchings = {}
        dog = []

        #adds the second preference list to \"dog\"
        for pup in pref2:
            dog.append(pup)
            
        #instantiates the dictionary with []
        for key, value in pref1.items():
            final_matchings[key] = []

        #Makes sure that no key has [] as a value
        while not matched(final_matchings):

            #keys are a, b, c then x, y, z
            for key,value in pref1.items():
                numTries = 0
                
                while final_matchings.get(key)==[]:
                    #values are x, y, z
                    if value[numTries] in dog:

                        #gives us the current key in final matching
                        final_matchings[key] = value[numTries]

                        #removes the dog from the list
                        dog.remove(value[numTries])

                    else:
                        cur_fam = find_match(final_matchings, value[numTries])
     
                        #If the value prefers the testing key instead of it's current key
                        if switch(pref2, key, value[numTries], cur_fam):

                            #Replaces current key with blank and gives value to testing key
                            final_matchings[cur_fam] = []
                            final_matchings[key] = value[numTries]
                
                        #If the value is taken and you have to try it again
                        else:
                            numTries = numTries + 1

        return final_matchings


    "You are to write a function \"unstable_pair(pref1, pref2, stabl, pair)\" that takes in two preference lists, a current matching (in the form of a dictionary), and a pair in the form of a list (you may assume that the first entry of the pair is a key in pref1 and stabl, and the second entry of the pair is a key in pref2 . This method should return the boolean value True if this pair is an unstable pair for the given matching 'stabl', and return False otherwise. (You may assume that the objects in pair are not actually paired up in the matching stabl)"

        def unstable_pair(pref1, pref2, stabl, pair):
              curr_key = find_match(stabl, pair[1])
              curr_val = stabl[pair[0]]
              #Checks if the current pair wants their current values over the pair that's being tested\n",
              if switch(pref1, pair[1], pair[0], curr_val) and switch(pref2, pair[0], pair[1], curr_key):
                    return True
              return False

   
