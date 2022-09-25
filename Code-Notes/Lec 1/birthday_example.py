import array as arr 

def birthday_match(students) :
    n = len(students)
    record = arr.Array(n)
    for k in range(n):
        (name1, bday1) = students[k]
        for i in range(k):
            (name2,bday2) = record.get_at(i)
            if bday1 == bday2:
                return name1, bday1
        record.set_at(k, (name1, bday1))
    return None
                
    