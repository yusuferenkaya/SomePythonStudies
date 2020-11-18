 #Getting an iterable's unique elements without using list methods such as count or append etc.
 
 def get_unique_elements(the_list):
    for i in range(len(the_list)):
        checking = the_list[i]
        the_list[i] = ""
        if checking not in the_list:
            print(checking)
        the_list[i] = checking
 
