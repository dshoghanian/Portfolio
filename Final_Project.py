# 12.1 Course Project: Spring 2023

# In this lab, you are tasked with programming using functions named for the various techniques taught week by week in the course.

# You will start with basic code that will create the groundwork for later weeks and will end by showing the real power of your skills. For each week we will have a function. All of the functions will return a value that will be used later in different parts of the project.

# There will be a description of the purpose of each function, and its docstring should also give you arguments and return values.

# Note due to federal educational grants, we are required to specify which part of this project corresponds to a week's material in ICS 31. As such, we took this opportunity to functions week_x() where each x is the week in the course.

# Please use this as an opportunity to appreciate how important good function names are.

# Good work so far this quarter, and good luck with this project.

# The overall goal of this project will be to accurately predict if a pole-vaulter can clear a bar, allowing the Olympic commission to pre-screen applicants.

# Week 1: Get basic information.

# The first step in finding good applicants for an Olympic team is asking people for information. 

# Write a function week_1() that asks for a pole vaulter's height and maximum speed. 

# Call input to receive the values with the following prompts:
# "Please enter the pole vaulter's height: \n" 
# "Please enter the pole vaulter's maximum running speed: \n" 

# return the values in the order: height and max_speed 

# TLDR: call input to get height and speed; return height and max_speed 

# Week 2: Convert to international format.

# Unfortunately, the equations used to screen people are based on physics which uses SI or System International units. Since we collect or data using imperial units we need a function to convert from imperial to SI. 

# Write a function week_2(height, maximum_speed) that converts the numbers given by the week_1 function to their SI counterparts.

# Using the following formulas, convert the height, velocity, and speed given: 
# Inches -> meters: | 1 inch == 0.0254m | height * 0.0254 == standard_height 
# mph -> mps: | 1 mph == (1609.344 m / 3600 seconds) == 0.44704 mps | maximum_speed * 0.44704 == standard_maximum_speed 

# return the standardized values of the height and maximum speed given in week 2's function parameters 

# TLDR: get height and maximum_speed as parameters; convert them to SI units; return the SI converted standard_height and standard_maximum_speed

# Week 3: Organize your data.

# For the purposes of displaying applicant information, sometimes it will be necessary to give statistics using mixed unit types. To help with building applicant data for later reports, we need a way of consolidating imperial and SI units into easy-to-access data. 

# Write a function week_3(i_height, s_height, i_speed, s_speed): that returns a list, dictionary, and named tuple all representing your vaulter. 

# List: put the parameters into a list of lists containing your heights and speeds in sublists, [[i_height, s_height], [i_speed, s_speed]] 
# Dictionary: create a dictionary where every key is the name of the variable, and every value is its numerical value, {i_height: 72, … 
# Named_tuple. Using the named tuple Vaulter, build a vaulter named tuple using the parameters Vaulter(i_height, s_height… 

# return the three data structures vaulter_list, vaulter_dict, vaulter_namedtuple

# TLDR: use function parameters i_height, s_height, i_speed and s_speed to build and return vaulter_list, vaulter_dict, vaulter_namedtuple 

# Week 4: Estimate jump height.

# In this program were are screening for pole vault jump height. To help screen people we need to estimate their maximum jump height before we test them in person.

# Write a function that receives a vaulter's information, estimates their maximum jump height and returns the estimated jump height

# You will receive one of the outputs of week_3() as the variable vaulter, However, you will not know which structured type it is so you need to use branching logic to determine its type. 

# Using vaulter you need to calculate and return the vaulter's estimated jump height. 
# to calculate jump height use the equation (1/2) * (vaulter's s_speed)^2 / g + vaulter's s_height 
# g is the gravitational constant 9.8 m/s^2 

# TLDR: find vaulter's type; get the s_height and s_speed; calculate jump_height; return jump_height 

# Week 5 Build a list of scores.

# Now we need to collect the statistics of our prospective pole vaulters. To do this we need to receive information from every prospective pole vaulter and build it into a single data structure.

# Write a function that receives an integer named applicants as a function parameter. 
# Then call week_1() for each applicant and store the return value of week_1() into a list of scores. 
# return the scores. 

# TLDR: get # of applicants with function parameter; call week_1() for every applicant and save into scores list; return scores list 

# Week 6 build a list of vaulter structured types.

# Now that we are able to build all of the stats of a vaulter from their initial scores, we need a way to automate score generation. The simplest way to do this will be to call previously created functions on our list of vaulters.

# Write a function week_6(scores) that receives a list of scores in the format of the week_5() function. 
# Then use week_2() to convert to SI units. 
# Use week_3() for each score to create the vaulter lists. and append the vaulter_list, vaulter_dict, and vaulter_namedtuple to a list of vaulters. 
# return the list of valuters. 

# TLDR: get a list of scores as a function parameter; for each score use weeks 2 and 3 to build a vaulter list; return the vaulter list

# Week 7 Filter a list of vaulters.

# Now that we are able to build a list of vaulter data types, we need to filter out the vaulters who do not meet our team's criteria. 

# Write a function week_7(vaulters, cutoff) that receives a list of vaulters of unknown type, and integer cutoff. 

# For each vaulter, use week_4() to calculate their jump_height. 
# If their jump_height is at least equal to the cutoff add them to the list of valid_applicants. 
# Return the list of valid_applicants. 

# TLDR: Get a list of vaulters and a cutoff integer as function parameters; filter out vaulters based on jump_height with week_4(); return list of vaulters 

# Week 8 Build a list of vaulter reports.

# The Olympic committee is very busy reviewing applicants for all of the events, so now we will build a report for them to view easily. 

# Write a function week_8(vaulters) that receives a list of vaulter dictionaries. 

# Build a list of strings named report using imperial units and jump height. 
# Each line of the report should be structured as follows: 
# "Applicant's height {'i_height'}, Applicant's vaulting speed: {'i_speed'}, Applicant's estimated jump_height: {jump_height}"

# Return the report 

# TLDR: Get a list of vaulter; for each vaulter add a string with their imperial statistics and jump_height to a report list; return the report list.

# Week 9 build vaulter reports based on an imported text file.

# The Olympic committee, in order to maintain privacy requirements, needs us to make the program compatible with text files. 

# Write a function week_9(applicant_file, cutoff) that has a file name applicant_file and a float cutoff as arguments. 
# applicant_file is a text file where each line is a pair of imperial scores, i_height, i_speed\n". 
# Build a list of scores like the format of week_5() 
# Filter the vaulters based on the cutoff, like in week_7() 
# Build a report in the format of week_8() using the filtered vaulters 
# Return the report

# Important: to make sure the report matches with the test case when reusing week_8 function, you need to convert *both* i_height and i_speed into floats!

# TLDR: read text file in the format "i_height, i_speed\n" and return a report list from week_9() 

# Week 10 List sorted by jump_heights.

# Now finally we need to get an idea of how our candidates will perform.

# Write a function week_10(report) that has a report list as a function parameter. 
# return a sorted list of jump heights from the report in descending order 

# Note: you should be able to do this in one line with a list comprehension. It's also good practice for the final. 

# Assuming you have made it this far, congratulations, you made a script that could be useful in the real world for helping filter applicants for a job.


from collections import namedtuple

Vaulter = namedtuple('Vaulter', 'height max_speed')

def week_1():
    """
    Prompts a user for a pole vaulter's height and maximum_speed

    Arguments:
    None

    Return values:
    height -- an integer containing the height of the pole vaulter in inches
    maximum_speed -- a float containing the maximum running speed with a pole of the pole vaulter
    """
    height = int(input("Please enter the pole vaulter's height: \n"))
    max_speed = float(input("Please enter the pole vaulter's maximum running speed: \n"))
    return height, max_speed


    return Vaulter(height, max_speed)
    
    
def week_2(height, maximum_speed):
    """
    Receives height (in inches) and maximum_speed (in mph).  Converts to SI units using the formulas given
    in the written instructions.  Returns the converted
    values.

    Arguments:
    height -- an int containing a pole vaulter's height in inches
    maximum_speed -- a float containing a pole vaulter's maximum speed in miles per hour or mph

    Return values:
    standard_height -- a float containing the converted height of the pole vaulter in meters or m
    standard_maximum_speed -- a float containing the converted maximum running speed with a pole of the pole vaulter in
                              meters per second or mps or m/s
    """
    standard_height = float(height) * 0.0254
    standard_maximum_speed = maximum_speed * 0.44704

    return standard_height, standard_maximum_speed
    

from collections import namedtuple

def week_3(i_height, s_height, i_speed, s_speed):
    """
    Using the input values given, build and return a list, dictionary, and named tuple all representing your vaulter.

    Arguments
    i_height -- the height in imperial units
    s_height -- the height in standard units
    i_speed -- the speed in imperial units
    s_speed -- the speed in standard units

    Return Values:
    vaulter_list -- A list of lists containing two floats each e.g. [[1.0, 0.0254], [1.0, 0.44704]]
    vaulter_dict -- S dictionary where keys are the parameter names, and values the values e.g. {'i_height': 1.0,
    vaulter_namedtuple --  A Vaulter named tuple using the function parameters e.g. Vaulter(1.0, 2.45...

    return the three data structures vaulter_list, vaulter_dict, vaulter_namedtuple
    """
    i_height = int(i_height)
    i_speed = float(i_speed)

    vaulter_list = [[i_height, s_height], [i_speed, s_speed]]

    vaulter_dict = {'i_height': i_height, 's_height': s_height, 'i_speed': i_speed, 's_speed': s_speed}

    Vaulter = namedtuple('Vaulter', ['i_height', 's_height', 'i_speed', 's_speed'])
    vaulter_namedtuple = Vaulter(i_height, s_height, i_speed, s_speed)

    return vaulter_list, vaulter_dict, vaulter_namedtuple
    
    
def week_4(vaulter):
    """
    Receives a vaulter's information and returns their estimated jump height

    Arguments:
    vaulter -- a list, dictionary, or namedtuple that contains a pole vaulter's information

    Return values:
    jump_height -- a float containing the approximate jump height in meters
    """
    if isinstance(vaulter, list):
        s_speed = vaulter[1][1]
        s_height = vaulter[0][1]
    elif isinstance(vaulter, dict):
        s_speed = vaulter['s_speed']
        s_height = vaulter['s_height']
    else:
        s_speed = vaulter.s_speed
        s_height = vaulter.s_height
    jump_height = 0.5 * (s_speed**2) / 9.8 + s_height
    return jump_height


def week_5(applicants):
    """
    Given a number of applicants, prompt the user once for each applicant and add the i_height and i_speed as a
    2 value list to a scores list

    Arguments:
        applicants -- an int representing the number of applicants

    Return Values:
        scores -- a list of lists in the format [[i_height_1, i_speed_1],
                                                 [i_height_2, i_speed_2],
                                                 ...,
                                                 [i_height_n, i_speed_n]]
    """
    scores = []
    for _ in range(applicants):
        height, max_speed = week_1()
        scores.append([height, max_speed])
    return scores


def week_6(scores):
    """
    Builds a list of vaulter structured types given
    a list of i_height and i_speeds in the format [[i_height_1, i_speed_1], [i_heieght_2, i_speed_2], ... ]

    Arguments:
        scores -- list of i_height and i_speeds in the format [[i_height_1, i_speed_1], [i_heieght_2, i_speed_2], ... ]

    Return Value:
        vaulters -- list of vaulters in format [[vaulter1_list, vaulter1_dict, vaulter1_namedtuple], [vaulter2_list ...]
    """
    vaulters = []
    for score in scores:
        i_height, i_speed = score
        s_height, s_speed = week_2(*score)
        vaulter_list, vaulter_dict, vaulter_namedtuple = week_3(i_height, s_height, i_speed, s_speed)
        vaulters.append([vaulter_list, vaulter_dict, vaulter_namedtuple])
    return vaulters


def week_7(vaulters, cutoff):
    """
    Given a list of vaulters (the vaulters may be any data type),
    calculates the jump heights and removes the vaulters who don't make the cutoff.

    Arguments:
        vaulters -- a list of vaulters, potentially of any data type
        cutoff -- the minimum estimated jump_height needed for a vaulter to make the team

    Return Values:
        team_members -- a list of vaulter dictionaries who beat the jump_height cutoff
    """
    valid_applicants = []
    for vaulter in vaulters:
        if isinstance(vaulter, list):
            vaulter_dict = {
                "i_height": vaulter[0][0],
                "s_height": vaulter[0][1],
                "i_speed": vaulter[1][0],
                "s_speed": vaulter[1][1]
            }
        elif isinstance(vaulter, dict):
            vaulter_dict = vaulter
        elif isinstance(vaulter, Vaulter): 
            vaulter_dict = vaulter._asdict()

        jump_height = week_4(vaulter_dict)
        if jump_height >= cutoff:
            valid_applicants.append(vaulter)
    return valid_applicants


def week_8(vaulters):
    """
    Given a list of vaulter dictionaries, build a list of strings that reports their
    i_height, i_speed, and jump_height in the following format:
    "Applicant's height {}, Applicant's vaulting speed: {}, Applicant's estimated jump_height: {}"

    Remember to use the IMPERIAL units and NOT the STANDARD units.

    Arguments:
        vaulters -- a list of dictionaries representing vaulters

    Return values:
        report -- a list of strings in the format:
                       "Applicant's height {}, applicant's vaulting speed: {}, applicant's estimated jump_height: {}"

    """
    report = []
    for vaulter in vaulters:
        if isinstance(vaulter, dict):
            vaulter_dict = vaulter
        elif isinstance(vaulter, Vaulter):
            vaulter_dict = vaulter._asdict()

        jump_height = week_4(vaulter_dict) 

        report_line = f"Applicant's height {vaulter_dict['i_height']}, Applicant's vaulting speed: {vaulter_dict['i_speed']}, Applicant's estimated jump_height: {jump_height}"
        report.append(report_line)
    return report
    

def week_9(applicant_file, cutoff):
    """
 Creates a report list using a text file.

    Arguments:
        vaulter_file -- a file with each line in the format "i_height, i_speed\n"
        cutoff -- the minimum estimated jump_height needed for a vaulter to make the team

    Return values:
        file_report -- a list of strings in the format:
                       "Applicant's height {}, applicant's vaulting speed: {}, applicant's estimated jump_height: {}"
    """
    vaulters = []
    with open(applicant_file, 'r') as file:
        for line in file:
            i_height, i_speed = map(float, line.strip().split(","))
            s_height, s_speed = week_2(i_height, i_speed)
            vaulter = {
                'i_height': i_height,
                'i_speed': i_speed,
                's_height': s_height,
                's_speed': s_speed
            }
            vaulters.append(vaulter)
            
    valid_vaulters = week_7(vaulters, cutoff)

    report = week_8(valid_vaulters)
    
    return report
    

def week_10(report):
    """
    Given a report, sort it by the jump_height

    Arguments:
        report -- a list of strings reporting candidate statistics

    Return values:
        sorted_report -- a sorted list of strings representing each candidate's jump height (a one line comprehension is fine)
    """
    return [str(height) for height in sorted([float(candidate.split(":")[-1]) for candidate in report], reverse=True)]


if __name__ == "__main__":
    # Here is a a suite of print statements to help you test your code
    # I are the two recommended examples for basic testing: 
    #     height 1, and speed 10; a patholigical example to test edge cases
    #     height 72, speed 23; a realistic example of an olympic athelete
    
    ti_height, ti_speed = week_1()
    print("Test week 1 ti_height:", ti_height)
    print("Test week 1 ti_speed:", ti_speed)
    print()

    ts_height, ts_speed = week_2(ti_height, ti_speed)
    print("Test week 2 ts_height:", ts_height)
    print("Test week 2 ts_speed:", ts_speed)
    print()

    tv_list, tv_dict, tv_namedtuple = week_3(ti_height, ts_height, ti_speed, ts_speed)
    print("Test week 3 tv_list:", tv_list)
    print("Test week 3 tv_dict:", tv_dict)
    print("Test week 3 tv_namedtuple:", tv_namedtuple)
    print()

    l_j_height = week_4(tv_list)
    d_j_height = week_4(tv_dict)
    n_j_height = week_4(tv_namedtuple)
    print("Test week 4 l_j_height:", l_j_height) 
    print("Test week 4 tv_dict:", tv_dict)
    print("Test week 4 tv_namedtuple:", tv_namedtuple)
    print()

    applicant_num = int(input("Please enter the number of applicants you would like to test: \n"))
    app_list = week_5(applicant_num)
    for i, app in enumerate(app_list):
        print(f"Testing week 5 applicant {i}: {app}")
    print()

    sc_list = week_6(app_list)
    for j, appl in enumerate(sc_list):
        print(f"testing week 6 number {j}: \n\tlist: {appl[0]}\n\tdict: {appl[1]}\n\tamedtuple: {appl[2]}")
    print()

    cutoff_test = int(input("Please enter a value to test cutoff for week 7: \n"))
    test_team_members = week_7([sc[1] for sc in sc_list], cutoff_test)
    print("Test week 7:", test_team_members)
    print()

    test_r = week_8(test_team_members)
    for k, mem in enumerate(test_r):
        print(f"Test week 8 member {k}: {mem}\n")
    print()

    test_f = week_9("vaulter_test_file.txt", cutoff_test)
    print("Testing week 9:")
    for f in test_f:
        print('\t', f)
    print()

    test_s = week_10(test_f)
    print("Test week 10:", test_s)