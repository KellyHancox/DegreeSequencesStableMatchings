
    "The purpose of this project is for you to find the degree sequence of a given graph and then use this to determine properties of the graph.  In addition, you will find the in-degree and out-degree of a specified vertex in a directed graph and use this to determine properties of the digraph.  Lastly, you will implement the Havel-Hakimi algorithm on a given sequence of integers. The ONLY IMPORT ALLOWED is  \"copy\" and you are ONLY allowed to use the copy.deepcopy() method from this package.  All of your code should be 'from scracth."
    
    "You are to write a function \"deg_seq(graph)\" that takes in a graph as its input, and then returns the degree sequence of the graph as a list."

    def deg_seq(graph):
        degree = []

        #searches through vertices in graph
        for vertex in graph:
    
            #Adds how many incoming lines are in the graph to the degrees list
            degree.append(len(graph[vertex]))
        #Returns the degrees in descending order
        return sorted(degree, reverse=True)
   
 
    "Write a function \"euler(graph)\" that takes in a connected graph as its input, and then determines if it is Eulerian or not."

    def euler(graph):
        degree_list = deg_seq(graph)
        odd_num_count = 0

        #loops through degrees list and looks for any odd degrees
        for element in degree_list:

            #if an odd degree, then add to the odd number count
            if element % 2 == 1:
                odd_num_count = odd_num_count + 1
        #Only Euler if there are no odd numbers
        if odd_num_count == 0:
            return True
        return False

    "Write a function \"in_out(digraph, vert)\" that takes in a directed graph and a vertex as its input, and then returns the in-degree and out-degree of that vertex in the directed graph in the form of a list with rst entry as the in-degree and second entry as the out-degree."

    def in_out(digraph, vert):
        in_out_degrees = []
        count_in = 0
        count_out = 0
        for vertex in digraph:
            #Counts the number of vertices going out
            if vertex == vert:
                count_out = len(digraph[vertex])
            
            #counts how many vertices are coming into the graph by looking for that node in other lists
            if vert in digraph[vertex]:
                count_in = count_in + 1

        in_out_degrees.append(count_in)
        in_out_degrees.append(count_out)
        return in_out_degrees

    "Write a function \"dir_euler(digraph)\" that takes in a connected, directed graph as its input, and then determines whether or not a directed Eulerian circuit exists."

    def dir_euler(digraph):
        #loops through vertices
        for vertex in digraph:

            #If at any point, the number of incoming lines does not equal the number of out lines
            #this is false
            if in_out(digraph, vertex)[0] != in_out(digraph, vertex)[1]:
                return False
        #If it passes every vertex and doesn't return false, then it will return true
        return True"

    "Write a function \"hav_hak(lst)\" that takes in a list of non-increasing integers as its input, and then determines whether or not this is the degree sequence of a graph."

    def hav_hak(lst):
        zero_count = 0
        other = 0
        
        #loops through every number
        for number in lst:
        
            #if there is a number less than 0, it will be false
            if  number < 0:
                return False

            #if there is a 0, then count them and if everything is 0, then it is true
            elif number == 0
                zero_count = zero_count + 1
                if zero_count == len(lst):
                    return True
        #Otherwise: save the first number and take it off the list
        first_number = lst[0]
        lst.pop(0)

        #then for the number in that range between 0 and the first number, subtract one
        for num in range (0,first_number):
            lst[num] = lst[num]-1

        #return the list in a descending order and recurse
        lst = sorted(lst, reverse = True)
        return hav_hak(lst)

