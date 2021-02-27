class Student:
    def __init__(self,name,last_name,student_id):
        self.name = name # Name of the student
        self.last_name = last_name # Last name of the student
        self.__student_id = student_id # Private student id
        self.given_answers = None # Given answers of the student
        self.type_of_exambook = None # Type of exam book of the student
        self.department_choices = None # Department choices of the student
        self.point = None # Point of the student
    def set_the_optionals(self,given_answers,type_of_exambook,department_choices):
        self.given_answers = given_answers
        self.type_of_exambook = type_of_exambook
        self.department_choices = department_choices
    def calculate_the_point(self):
        file = open("key.txt","r") # Opening the key file
        exam_a, exam_b = file.read().splitlines() # Assigning the A and B type of exam book
        if self.type_of_exambook == "A":
                keys = exam_a # Making the key A if the student's exam book type is A
        elif self.type_of_exambook == "B": # Making the key B if the student's exam book type is B
                keys = exam_b

        true_answers = 0
        wrong_answers = 0
        blank_answers = 0
        for i in range(len(self.given_answers)): #Looping through the student's given answers
                    answer = self.given_answers[i] # One of the answers changing at every step of the loop
                    try: key = keys[i] # One of the keys changing at every step of the loop
                    except: print("The exambook type was not valid for the student with id " + str(self.get_student_id()))
                    if answer == key:
                        true_answers += 1
                    elif answer == "*":
                        blank_answers += 1
                    elif answer != key:
                        wrong_answers += 1
        net = true_answers - (wrong_answers / 4) # Calculating the net of the student by the given answers
        point = net * 15
        return (point, net, true_answers, blank_answers, wrong_answers) # Returning



    def get_student_id(self):
        """This function is to access the student id when it is required, since it is a private attribute"""
        return self.__student_id
    def __str__(self):
        return self.name + " " + self.last_name



class University:
    def __init__(self,uni_id,department,capacity):
        self.uni_id = uni_id # Id of the university
        self.department = department # University-Department Name
        self.capacity = capacity # Capacity of the department
        self.students = [] # Students who are placed into the department
        self.ceil_point = 0
        self.floor_point = 0
    def add_student(self,student):
        """This function is used to add students into the university's students list attribute"""
        self.students.append(student)
        self.capacity -= 1






# This create_a_student_dict function creates a student database from the existing text file on the path at every calling
# and by opening these files we use these to create student objects in order to add the dictionary. And the keys of the
# dictionary are the number of the students.
def create_a_student_dict():
    student_dict = {}  # Creating a new student dictionary
    file = open("student.txt", "r", encoding="utf-8")  # Opening the file
    for line in file.readlines():  # Reading the data from the file
        if len(line.split()) == 4:  # Checking if the student has 2 names or not.
            line = line.split()  # Splitting the line to parse the data
            name = line[1] + " " + line[2]  # The student has 2 names
            student_id = line[0]  # The student id
            surname = line[3]  # Last name of the student
        elif len(line.split()) == 3:  # If the student has only one name
            student_id, name, surname = line.split()  # Parsing the line
        # if the length of line is not 3 or 4, the student won't be taken into consideration.
        if student_id not in student_dict.keys() and student_id.isdigit() and len(student_id) == 6:
            # Adding the student
            # to the dictionary.
            student_dict[student_id] = Student(name,surname,student_id) # Creating a student object and adding it by
            # the student's id as a key.
    file.close()
    file = open("answers.txt","r")  # Opening the file to get the other data of the same student.
    for line in file.readlines():
        try:
            student_id, type_of_exambook, given_answers, choice1, choice2 = line.split() # Parsing the data in the file.
            if student_id in student_dict.keys():
                student_dict[student_id].set_the_optionals(given_answers.strip(),type_of_exambook.strip(),[choice1.strip(),choice2.strip()])
            # Setting the indicated parameters to the same students that already exist in the dictionary values.
        except:
            print("There are some occurred problems about some of the student's data.")
    return student_dict # Returning this dictionary to use when it is needed

def create_a_university_dict():
    university_dict = {} # Creating a new university dictionary
    file = open("university.txt","r",encoding="utf-8") # Reading the university.txt file
    for line in file.readlines():
        enum,department,capacity = line.split(",") # Parsing the line in order to create university object
        # by passing these parameters into the university object.
        if enum not in university_dict.keys():
            university_dict[enum] = University(enum,department,int(capacity)) # Adding the universities
            # to the dictionary by using their number codes as keys.
    file.close()
    return university_dict

def sorting_by_point(student):
    """This function is being used when there is needed some kind of sorting, to be used as the key parameter of
    the sorted function. It returns the student's point of the exam."""
    return student.calculate_the_point()[0]




def show_student_name(student_id):
    student_database = create_a_student_dict()  # Calling the function that creates a student dictionary.
    # It will try if the input student_id parameter is proper to the condition of being a student id number.
    try:
        print("The student you're looking for is " + student_database[student_id].__str__())
    except:
        print("There isn't any valid student with this number. Please try again by choosing the same option again." + "\n"
                                                                                                              "ID must include 6 digits")
def remove_the_not_attendants_from_the_database(student_database):
    """This function is used to remove the students that who didn't attend to the exam and thus they don't have results."""
    new_database = {}
    for student_id in student_database.keys():
        if student_database[student_id].given_answers != None:
            new_database[student_id] = student_database[student_id]
    return new_database


def placing_the_students():
    student_database = create_a_student_dict()  # Calling the function that creates a student dictionary
    student_database = remove_the_not_attendants_from_the_database(student_database) # Removing the students who are not
    # attended to the exam.
    university_database = create_a_university_dict()  # Calling the function that creates a university dictionary
    student_list = sorted(student_database.values(), reverse=True, key=sorting_by_point)  # Sorting the students by
    # their points in a list.
    for student in student_list:
        student.point = student.calculate_the_point()[0]  # Adding the student's point as the object's attribute value.
        if university_database[student.department_choices[0]].capacity != 0:
            # Checking if the student's choice department has the capacity and the student's point is higher than the
            # department's base point. If it is, the student is being added to this department's student list attribute.
            university_database[student.department_choices[0]].add_student(student)
            university_database[student.department_choices[0]].floor_point = student.point
            if university_database[student.department_choices[0]].ceil_point == 0:
                university_database[student.department_choices[0]].ceil_point = student.point
            elif student.point > university_database[student.department_choices[0]].ceil_point:
                university_database[student.department_choices[0]].ceil_point = student.point

        elif university_database[student.department_choices[1]].capacity != 0:
            # If the student can't be placed at their first choice, The function will try to place the student at
            # their second choice. If it is implemented, then again the student will be added to the university class
            # objects student list attribute.
            university_database[student.department_choices[1]].add_student(student)
            university_database[student.department_choices[1]].floor_point = student.point
            if university_database[student.department_choices[1]].ceil_point == 0:
                university_database[student.department_choices[1]].ceil_point = student.point
            elif student.point > university_database[student.department_choices[1]].ceil_point:
                university_database[student.department_choices[1]].ceil_point = student.point
    return university_database

def show_the_max_base_point_university():
    university_database = placing_the_students() # Creating a university dictionary
    university_list = sorted(university_database.values(), key= lambda university: university.floor_point,reverse=True)
    # this variable sorts the base points to assign the highest of the points.

    # this variable is used to store the universities those have the maximum points in a list.
    print("ID  " + " DEPARTMENT  ".center(80) + "   FLOOR POINT  ".center(15) + "  CEIL POINT ".center(15))
    for university in university_list:
        print(university.uni_id.center(3) + " | " + university.department.center(80) + " | " + str(university.floor_point).rjust(10) + " | " + str(university.ceil_point).rjust(10) + " | ")



def write_the_results():
    student_database = create_a_student_dict() # Creating a student dictionary
    university_database = create_a_university_dict() # Creating a university dictionary
    file = open("results.txt","w",encoding="utf-8") # Creating a results.txt file to write
    file.write("student_id,name,l_name,type,true,wrong,blank,net,point,choice1,choice2\n")
    for student in student_database.values():
        try:
            point, net, true_answers, blank_answers, wrong_answers = student.calculate_the_point() # Calculating the student's
        # exam results.
            file.write("{}, {} ,{} ,{} ,{} ,{} ,{} ,{} ,{} ,{} ,{}\n".format(student.get_student_id(),student.name,student.last_name,
                                                    student.type_of_exambook,true_answers,wrong_answers,blank_answers,
                                                    net,point,university_database[student.department_choices[0]].department,
                                                    university_database[student.department_choices[1]].department))
        except:
            print("Student with " + student.get_student_id() + " ID has no related data with the exam results.")
    file.close()



def list_the_students():
    student_database = create_a_student_dict() # Creating the student dictionary
    student_database = remove_the_not_attendants_from_the_database(student_database) # Removing the students who are not
    # attended to the exam.
    students_list = [(student.get_student_id(),student.name,student.last_name,student.calculate_the_point()[0]) for student in student_database.values()]
    # List comprehension above is to get the student's needed details for the table.
    def reaching_the_point(x):
        """This function is to be used in the key parameter of the sorted function. To sort by the point"""
        return x[3]
    student_list = sorted(students_list,key=reaching_the_point,reverse=True) # Sorting the student_list by their points
    print("STUDENT ID".center(11) +" |"+ "NAME".center(22) + " |" + " LAST NAME".center(22) + "|" + "SCORE".center(10))
    print("-"*70)
    for student in student_list:
        student_id, name, last_name, score = student
        print(student_id.center(10) + "  |  " + name.center(20) + " | "
             +  last_name.center(20) + " | " + str(score).center(10))
        print("-"*70)


def list_the_placed_students():
    university_database = placing_the_students() # Calling the placing function
    for university in university_database.values():
        print("_"*(len(university.department)+5))
        print("# " + "|" + university.department + " "+ str(len(university.students)) + "|")
        if len(university.students) == 0:
            print("_" * (len(university.department) + 5))
            print("\tThere isn't any student in this department.")
        else:
            for i in range(len(university.students)):
                student = university.students[i]
                print("_" * (len(university.department) + 5))
                print(str(i + 1) + " | " + student.name.center(20) + " " + student.last_name.center(10) + " | " + str(
                        student.calculate_the_point()[0]).center(20))


def show_the_unplaced_students():
    student_database = create_a_student_dict() # Creating a student dictionary
    student_database = remove_the_not_attendants_from_the_database(student_database) # Removing the students who are not
    # attended to the exam.
    university_database = create_a_university_dict() # Creating a university dictionary
    student_list = sorted(student_database.values(), reverse=True, key=sorting_by_point) # Sorting the students by their
    # points.
    unplaced_students = [] # A list for the unplaced students.
    everyone_placed = True # A boolean to check if the everyone is placed or not.
    for student in student_list:
        # Code below is to check if the student can be placed one of their choices. Else, student will be appended to
        # the unplaced students list.
        student_point = student.calculate_the_point()[0]
        if university_database[student.department_choices[0]].capacity != 0 and student_point > float(
                university_database[student.department_choices[0]].base_point):
            university_database[student.department_choices[0]].add_student(student)
        elif university_database[student.department_choices[1]].capacity != 0 and student_point > float(
                university_database[student.department_choices[1]].base_point):
            university_database[student.department_choices[1]].add_student(student)
        else:
            unplaced_students.append(student)
            everyone_placed = False
    print("These students can't be placed anywhere.")
    print("STUDENT ID   " +  "STUDENT NAME-SURNAME    ".rjust(40) + "SCORE".rjust(20))
    for student in unplaced_students:
        print(student.get_student_id() + "       |  " + student.name.ljust(20) + " " + student.last_name.ljust(20) + "  |   " + str(student.calculate_the_point()[0]).rjust(20))
    if everyone_placed:
        print("There isn't any student who is not placed in a department.")

def list_all_the_departments():
    department_names = []
    department_dict = {} # Creating a department list to add the department names
    #  Creating a university dict to get the data
    university_database = placing_the_students()
    for university in university_database.values():
        name = university.department.split() # To parse the name of the university-department pair
        for word in name:
            if "University" in word or "Institute" in word:
                # When the word is something like "University" or "Institute"
                index = name.index(word) # Getting the index of that word and assigning
                only_department = name[index+1:] # Slicing the name by the index of that word.
                only_department = " ".join(only_department) # Converting the list to string again.
                if only_department not in department_names: # To prevent the repetitive department names.
                    department_names.append(only_department)
                if only_department not in department_dict.keys():
                    department_dict[only_department] = len(university.students)
                else:
                    department_dict[only_department] += len(university.students)

                # Appending the name of the department to the list.
                break

    print("DEPARTMENT NAME".center(100) + "AMOUNT OF STUDENTS".center(20))
    for department_name in department_dict.keys():
        print(department_name.center(100) + " " + str(department_dict[department_name]).center(20)) # Printing the department names through the for loop.


# Code from here is to used to make the code menu-like.
print("Welcome to the Student Dashboard"+"\n"+"Please choose an option to process\n"
      "1. Display a student's name-surname\n"+"2. Show the university with the maximum base point\n"+
      "3. Create the results.txt file which contains all the details about the students\n"+
      "4. List the students by their scores\n"+"5. List the placed students by their universities\n"+
      "6. List the students who couldn't be placed\n"+"7. List all the departments")
option = input("Insert your option here:..")
print("\n" * 2)
while option != "-1":
    if option == "1":
        number = (input("Please enter the student id to look for:"))
        print("o+"*30)
        show_student_name(number)
        print("o+"*30+"\n")
    elif option == "2":
        print("o+"*50)
        show_the_max_base_point_university()
        print("o+"*50+"\n")
    elif option == "3":
        try:
            print("o+"*30)
            write_the_results()
            print("The file 'results.txt' has been created in your project's path.")
            print("o+"*30+"\n")
        except:
            print("\nThere is a problem occurred while writing the results.txt file. So the file won't being written\n")
    elif option == "4":
        print("o+"*40)
        list_the_students()
        print("o+"*40+"\n")
    elif option == "5":
        print("o+"*40)
        list_the_placed_students()
        print("o+"*40+"\n")
    elif option == "6":
        print("o+"*50)
        show_the_unplaced_students()
        print("o+"*50+"\n")
    elif option == "7":
        print("o+"*50)
        list_all_the_departments()
        print("o+" * 50 + "\n")
    else:
        print("You've inserted an invalid option. Please insert again below.")

    print("Please choose an option to process again. Or exit the menu by typing '-1' \n" +
          "1. Display a student's name-surname\n"+"2. Show the university with the maximum base point\n"+
      "3. Create the results.txt file which contains all the details about the students\n"+
      "4. List the students by their scores\n"+"5. List the placed students by their universities\n"+
      "6. List the students who couldn't be placed\n"+"7. List all the departments")
    option = input("Insert here..:")
    print()


    # YUSUF EREN KAYA 
