import itertools

subjects = ["Math", "AI", "OS"]
teachers = {"Math": "T1", "AI": "T2", "OS": "T3"}
rooms = ["R1", "R2"]
times = ["Mon9", "Mon10", "Tue9", "Tue10"]

def is_valid(assign):
    used_time_teacher = {}
    used_time_room = {}
    for subj, (t, r, time) in assign.items():
        if (t, time) in used_time_teacher or (r, time) in used_time_room:
            return False
        used_time_teacher[(t, time)] = True
        used_time_room[(r, time)] = True
    return True

def backtrack(assign):
    if len(assign) == len(subjects):
        return assign
    subj = subjects[len(assign)]
    for room, time in itertools.product(rooms, times):
        new_assign = assign.copy()
        new_assign[subj] = (teachers[subj], room, time)
        if is_valid(new_assign):
            result = backtrack(new_assign)
            if result: return result
    return None

solution = backtrack({})
print("Timetable:", solution)
