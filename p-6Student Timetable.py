timetable = [
    ("Python", "Monday", 9, 11, "R101"),
    ("Mathematics", "Monday", 10, 12, "R102"),
    ("Physics", "Tuesday", 9, 11, "R103"),
    ("English", "Wednesday", 11, 12, "R101")
]
unavailable_rooms = [
    ("R101", "Monday", 9, 10),
    ("R103", "Tuesday", 10, 12)
]

conflicts = []

for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):
        c1 = timetable[i]
        c2 = timetable[j]

        if c1[1] == c2[1]:
            if c1[2] < c2[3] and c2[2] < c1[3]:
                conflicts.append(
                    "Time conflict: " + c1[0] + " and " + c2[0]
                )

for course in timetable:
    for room in unavailable_rooms:
        if course[4] == room[0] and course[1] == room[1]:
            if course[2] < room[3] and room[2] < course[3]:
                conflicts.append(
                    "Room conflict: " + course[0] +
                    " uses unavailable room " + course[4]
                )

print("========== STUDENT TIMETABLE ==========")

for course in timetable:
    print(course[0], "-", course[1],
          "Time:", str(course[2]) + ":00 to",
          str(course[3]) + ":00",
          "Room:", course[4])

print("\n========== CONFLICT REPORT ==========")

if conflicts:
    for conflict in conflicts:
        print(conflict)

    print("\nTimetable Status: INVALID")
else:
    print("No conflicts detected.")
    print("Timetable Status: VALID")

print("\n========== PROPOSED COURSE VALIDATION ==========")

proposed_course = (
    input("Enter course name: "),
    input("Enter day: "),
    int(input("Enter start time (hour): ")),
    int(input("Enter end time (hour): ")),
    input("Enter room: ")
)

proposed_conflicts = []
if proposed_course[2] >= proposed_course[3]:
    proposed_conflicts.append("Invalid time period.")
for course in timetable:
    if proposed_course[1] == course[1]:
        if (proposed_course[2] < course[3] and
                course[2] < proposed_course[3]):
            proposed_conflicts.append(
                "Time overlaps with " + course[0]
            )
for room in unavailable_rooms:
    if (proposed_course[4] == room[0] and
            proposed_course[1] == room[1]):
        if (proposed_course[2] < room[3] and
                room[2] < proposed_course[3]):
            proposed_conflicts.append(
                "Room " + proposed_course[4] +
                " is unavailable during this period."
            )
if proposed_conflicts:
    print("Proposed timetable is INVALID.")
    for conflict in proposed_conflicts:
        print(conflict)
else:
    print("Proposed timetable is VALID.")
