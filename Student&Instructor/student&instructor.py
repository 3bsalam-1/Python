def write_stu():
    with open('studentpy.txt', 'a') as file:
        c = 'y'
        while c == 'y':
            name = input('Enter The Student Name : ')
            id_num = input('Enter The Student ID : ')
            age = input('Enter The Student Age : ')
            Academic_Year = input('Enter The Student Academic Year : ')
            phone_Number = input('Enter The Student Phone Number : ')
            Gender = input('Enter The Student Gender : ')
            Recedent = input('Enter The Student Recedent : ')
            file.write(
                name + '\t' + id_num + '\t' + age + '\t' + Academic_Year + '\t' + phone_Number + '\t' + Gender + '\t' + Recedent + '\n')
            print('----------------------------------------------------------------------------- ')
            c = input('Do You Want To Enter Another Record ( y / n ) ? : ')
            print('----------------------------------------------------------------------------- ')
        print('File Saved Successfully')
        print('----------------------------------------------------------------------------- ')


def search_stu():
    name = input('Enter The Name Of The Student To Search For : ')
    with open('studentpy.txt', 'r') as file:
        flag = False
        for line in file:
            fields = line.split('\t')
            if fields[0] == name:
                flag = True
                print('Name\t ID\tAge\tAcademic Year\tphone Number\tGender\t  Recedent')
                print('----------------------------------------------------------------------------- ')
                print(line, end='')
                print('----------------------------------------------------------------------------- ')
        if not flag:
            print('Student Not Found')
            print('----------------------------------------------------------------------------- ')


def read_stu():
    with open('studentpy.txt', 'r') as file:
        print('Name\tID\tAge\tYear\tphone Number\tGender\tRecedent')
        print('----------------------------------------------------------------------------- ')
        for line in file:
            print(line, end='')
        print('\n')


def delete_stu():
    import os
    file = open('studentpy.txt', 'r')
    tempfile = open('tempstudentpy.txt', 'w')
    name = input('Enter The Name Of The Student To Delete : ')
    flag = False
    for line in file:
        st = line.split('\t')
        if st[0] == name:
            flag = True
        else:
            tempfile.write(line)
    file.close()
    tempfile.close()
    os.remove('studentpy.txt')
    os.rename('tempstudentpy.txt', 'studentpy.txt')

    if not flag:
        print('Student Not Found')
        print('----------------------------------------------------------------------------- ')
    else:
        print('Student Deleted Successfully')
        print('----------------------------------------------------------------------------- ')


def update_stu():
    import os
    file = open('studentpy.txt', 'r')
    tempfile = open('tempstudentpy.txt', 'w')
    name = input('Enter The Name Of The Student To Update : ')
    flag = False
    for line in file:
        st = line.split('\t')

        if st[0] == name:
            flag = True
            age = input('Enter The New Age for The Student : ')
            academic_year = input('Enter The New Academic Year for The Student : ')
            recedent = input('Enter The New Recedent for The Student : ')
            line = st[0] + '\t' + st[1] + '\t' + age + '\t' + academic_year + '\t' + st[4] + '\t' + st[
                5] + '\t' + recedent + '\n'
        tempfile.write(line)

    file.close()
    tempfile.close()
    os.remove('studentpy.txt')
    os.rename('tempstudentpy.txt', 'studentpy.txt')

    if not flag:
        print('Student Not Found')
        print('----------------------------------------------------------------------------- ')
    else:
        print('Student Deleted Successfully')
        print('----------------------------------------------------------------------------- ')


def write_inst():
    with open('instructor.txt', 'a') as file:
        c = 'y'
        while c == 'y':
            name = input('Enter instructor name : ')
            inst_id = input('Enter instructor id : ')
            age = input('Enter instructor age : ')
            course = input('Enter instructor course : ')
            department = input('Enter instructor department : ')
            file.write(name + '\t' + inst_id + '\t' + age + '\t' + course + '\t' + department + '\n')
            c = input('Do you want to enter records again ( y / n ) ? ')
        print('File saved successfully')


def read_inst():
    with open('instructor.txt', 'r') as file:
        print('Name\tID\tAge\tCourse\tDepartment')
        print('-------------------------------------')
        for line in file:
            print(line, end='')


def search_inst():
    c = input(' 1- ID \n 2- Name\nchoose the way that you want to search :')
    if c == '1':
        inst_id = input('Enter Id of the instructor to search for : ')
        with open('instructor.txt', 'r') as file:
            found = False
            for line in file:
                fields = line.split('\t')
                if fields[1] == inst_id:
                    found = True
                    print('Name\tID\tAge\tCourse\tDepartment')
                    print('-------------------------------------')
                    print(line)
            if not found:
                print('instructor not found')
                return

    elif c == '2':
        name = input('Enter Name of the instructor to search for : ')
        with open('instructor.txt', 'r') as file:
            found = False
            for line in file:
                fields = line.split('\t')
                if fields[0] == name:
                    found = True
                    print('Name\tID\tAge\tCourse\tDepartment')
                    print('-------------------------------------')
                    print(line)
            if not found:
                print('instructor not found')
                return


def delete_inst():
    import os
    inst_id = input('Enter Id of the instructor to Delete : ')
    file = open('instructor.txt', 'r')
    temp = open('temp.txt', 'w')
    found = False
    for line in file:
        fields = line.split('\t')
        if fields[1] == inst_id:
            found = True
        else:
            temp.write(line)
    file.close()
    temp.close()
    os.remove('instructor.txt')
    os.rename('temp.txt', 'instructor.txt')
    if not found:
        print('instructor not found')
    else:
        print('instructor deleted successfully')


def update_inst():
    import os
    inst_id = input('Enter Id of the instructor you want to update : ')
    file = open('instructor.txt', 'r')
    temp = open('temp.txt', 'w')
    found = False
    for line in file:
        st = line.split('\t')
        if st[1] == inst_id:
            found = True
            name = input('Enter New instructor name : ')
            inst_id = input('Enter New instructor id : ')
            age = input('Enter New instructor age : ')
            course = input('Enter New instructor course : ')
            department = input('Enter New instructor department : ')
            line = name + '\t' + inst_id + '\t' + age + '\t' + course + '\t' + department + '\n'
        temp.write(line)
    file.close()
    temp.close()
    os.remove('instructor.txt')
    os.rename('temp.txt', 'instructor.txt')
    if found:
        print('instructor successfully updated')
    else:
        print('instructor not found')


def main():
    print('1: instructor')
    print('2: Student')
    h = input('Your choice: ')
    if h == '1':
        c = 'y'
        while c == 'y':
            print('1: To add new instructor ')
            print('2: To read all instructors ')
            print('3: To search for a instructor ')
            print('4: To delete a instructor ')
            print('5: To update instructor record ')
            c = input('Your choice: ')
            if c == '1':
                write_inst()
            elif c == '2':
                read_inst()
            elif c == '3':
                search_inst()
            elif c == '4':
                delete_inst()
            elif c == '5':
                update_inst()
            c = input('Perform another operation ( y / n ) : ')
    elif h == '2':
        c = 'y'
        while c == 'y':
            print('1: To add new student ')
            print('2: To read all students ')
            print('3: To search for a student ')
            print('4: To delete a student ')
            print('5: To update student record ')
            c = input('Your choice: ')
            if c == '1':
                write_stu()
            elif c == '2':
                read_stu()
            elif c == '3':
                search_stu()
            elif c == '4':
                delete_stu()
            elif c == '5':
                update_stu()
            c = input('Perform another operation ( y / n ) : ')


main()
