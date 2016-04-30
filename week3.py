"""
GP Calculator
"""

Courses = {
    "software" : 1,
    "hardware" : 1,
    "music" : 2,
    "philosophy" : 3
}

Grades = {
    "A" : 5, "B" : 4, "C" : 3, "D" : 2, "E" : 1, "F" : 0
}

Results = {
    "software" : "",
    "hardware" : "",
    "music" : "",
    "philosophy" : ""
}

Name1 = raw_input ("FIRST NAME:")
Name2 = raw_input ("LAST NAME:")

print Name1, Name2

Results["software"] = raw_input ("What is your score in software\n")
Results["hardware"] = raw_input ("What is your score in hardware\n")
Results["music"] = raw_input ("What is your score in music\n")
Results["philosophy"] = raw_input ("What is your score in philosophy\n")

print Results


C1 = Courses["software"] * Grades[Results["software"]]
C2 = Courses["hardware"] * Grades[Results["hardware"]]
C3 = Courses["music"] * Grades[Results["music"]]
C4 = Courses["philosophy"] * Grades[Results["philosophy"]]

GP = ((C1 + C2 + C3 + C4)/sum(Courses.values()))

Full = Name1 + Name2, "This is your GP", GP




print Full