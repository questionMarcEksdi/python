# from pprint import pprint

class Student:

    def __init__(self, id_num, surname, firstname, occupation, gender, country_code, area_code, contact_num):
        self.__id_num = id_num
        self.__surname = surname
        self.__firstname = firstname
        self.__occupation = occupation

        if gender == 'm':
            self.__gender = 'male'
        elif gender == 'f':
            self.__gender = 'female'

        self.__country_code = country_code
        self.__area_code = area_code
        self.__contact_num = contact_num

    @property
    def Id_number(self):
        return self.__id_num

    @Id_number.setter
    def Id_number(self, num):
        self.__id_num = num

    @property
    def Surname(self):
        return self.__surname

    @Surname.setter
    def Surname(self, sname):
        self.__surname = sname

    @property
    def Firstname(self):
        return self.__firstname

    @Firstname.setter
    def Firstname(self, fname):
        self.__firstname = fname

    @property
    def Occupation(self):
        return self.__occupation

    @Occupation.setter
    def Occupation(self, job):
        self.__occupation = job

    @property
    def Gender(self):
        return self.__gender

    @Gender.setter
    def Gender(self, sex):
        self.__gender = sex

    @property
    def Country_code(self):
        return self.__country_code

    @Country_code.setter
    def Country_code(self, cntry_code):
        self.__country_code = cntry_code

    @property
    def Area_code(self):
        return self.__area_code

    @Area_code.setter
    def Area_code(self, area_code):
        self.__area_code = area_code

    @property
    def Contact_number(self):
        return self.__contact_num

    @Contact_number.setter
    def Contact_number(self, contact_num):
        self.__contact_num = contact_num

    def __repr__(self):
        return repr((self.Id_number, self.Surname, self.Firstname, self.Occupation, self.Contact_number))

    def __str__(self):
        pronoun = ''

        if self.__gender == 'male':
            pronoun = 'His'
        elif self.__gender == 'female':
            pronoun = 'Her'

        return f"Here's info about {self.Id_number}:\n\
{self.Surname} {self.Firstname} is a {self.Occupation}. {pronoun} number is {self.Contact_number}\n\n"


class Phonebook:

    def __init__(self):
        self.__contacts = []
        self.__asean_countries = self.aseanCountries()

    @property
    def get_contact_list(self):
        return self.__contacts

    def add(self, contact):
        self.get_contact_list.append(contact)

    def find(self, student_id):
        return any(student.Id_number == student_id for student in self.get_contact_list)

    def edit(self, option: int, index: int, val=''):
        if option == 1:
            self.__contacts[index].Id_number = val

        elif option == 2:
            self.__contacts[index].Surname = val

        elif option == 3:
            self.__contacts[index].Gender = val

        elif option == 4:
            self.__contacts[index].Occupation = val

        elif option == 5:
            self.__contacts[index].Country_code = val

        elif option == 3:
            self.__contacts[index].Area_code = val

        elif option == 7:
            self.__contacts[index].Contact_number = val

    # #################=================================================###############

    def aseanCountries(self):
        if self:
            return {'Malaysia': [],
                    'Indonesia': [],
                    'Philippines': [],
                    'Singapore': [],
                    'Thailand': []}

    @property
    def countryDict(self):
        return self.__asean_countries

    @property
    def getAll(self):
        data = [str(student_info) for student_info in sorted(self.get_contact_list,
                                                             key=lambda student: student.Surname)]
        d = ''

        for person in data:
            d += str(person)

        return f"Here are students from Philippines, Thailand, Indonesia, Singapore and Malaysia {d}"

    def get_countryName(self, c_code):
        if self:
            return {'60': 'Malaysia',
                    '62': 'Indonesia',
                    '63': 'Philippines',
                    '65': 'Singapore',
                    '66': 'Thailand'}.get(c_code)

    def add_toDict(self):
        asean = self.countryDict

        for student in self.get_contact_list:
            country = self.get_countryName(student.Country_code) #obtaining the country name using students country code
            asean.get(country).append(student) # add student to country

    def display_fromCountry(self, country_name, country_list=None):

        """
        a function that will return all the students from a certain country
        :param country_name
        :param country_list:
        :return:
        """

        country = [c for c in country_name.split(" ")]

        # before: country = Country1 Country2 Country3 ... Country(N)

        num_ofNames = len(country)

        if num_ofNames > 1:

            country.insert(-1, " and ")

            names_ofCountry = country[:-2]
            a = ", ".join(names_ofCountry)
            b = "".join(country[num_ofNames - 1:])

            # After:
            # result (if only 2): name = Country1 and Country3
            # result (if many): name = Country1, Country2, Country3, ..., and Country(N)
            name = a + b

        else:
            name = country_name

        data = ''
        if country_list is not None:
            list_ofPerson = [str(student_info) for student_info
                             in sorted(country_list, key=lambda student: student.Surname)]

            for person in list_ofPerson:
                data += str(person)
        else:
            pass

        if self:
            return f'Here are students from {name}\n{data}'

    def get_aseanCountry(self, country):

        return {'Malaysia': self.countryDict.get('Malaysia'),
                'Indonesia': self.countryDict.get('Indonesia'),
                'Philippines': self.countryDict.get('Philippines'),
                'Singapore': self.countryDict.get('Singapore'),
                'Thailand': self.countryDict.get('Thailand')
                }.get(country)


class Application:

    def __init__(self):
        self.contact = Phonebook()

    def create_contact(self):
        while True:
            
            id_number = input("Enter student number: ")
            surname = input("Enter surname: ")
            firstname = input("Enter firstname: ")
            occupation = input("Enter occupation: ")
            gender = input("Enter gender: [M for male, F for female] ").lower()
            country_code = input("Enter country code: ")
            area_code = input("Enter area code: ")
            contact_number = input("Enter contact number: ")

            student = Student(id_number, surname, firstname, occupation, gender,
                              country_code, area_code, contact_number)

            self.contact.add(student)

            create_another = input("Do you want to create another account?: [Y/N] ").lower()

            if create_another == 'y':
                continue
            elif create_another == 'n':
                print("Contacts successfully created")
                self.contact.add_toDict()  # adding contacts to dictionary of asean countries
                break

    def edit_contact(self):

        while True:

            id_number = input("Enter student number: PRESS 0 TO EXIT ")

            if id_number == '0':
                break

            exists = self.contact.find(id_number)

            if exists:
                print("found it!!!!!")
                student_index = ''

                for contactPerson in self.contact.get_contact_list:
                    if contactPerson.Id_number == id_number:
                        student = str(contactPerson)
                        print(student)

                        student_index = self.contact.get_contact_list.index(contactPerson)

                while True:

                    print("""Which of the following do you wish to change?
                        [1] Student Number [4] Occupation [7] Phone Number
                        [2] Surname [5] Country code [8] None - back to menu
                        [3] Gender [6] Area code""")

                    choice = int(input(">>>> "))

                    if choice == 1:

                        new_id = input("Enter new id: ")
                        self.contact.edit(option=choice, index=student_index, val=new_id)
                        print('student id successfully modified')
                         
                    elif choice == 2:

                        new_surname = input("Enter new surname: ")
                        self.contact.edit(option=choice, index=student_index, val=new_surname)
                        print('surname successfully modified')
                        
                    elif choice == 3:

                        new_gender = input("Enter new gender: ")
                        self.contact.edit(option=choice, index=student_index, val=new_gender)
                        print('gender successfully modified')
                         
                    elif choice == 4:

                        new_job = input("Enter new occupation: ")
                        self.contact.edit(option=choice, index=student_index, val=new_job)
                        print('occupation successfully modified')
                         
                    elif choice == 5:

                        new_country_code = input("Enter new country code: ")
                        self.contact.edit(option=choice, index=student_index, val=new_country_code)
                        print('country code successfully modified')
                        
                    elif choice == 6:

                        new_area_code = input("Enter new area code: ")
                        self.contact.edit(option=choice, index=student_index, val=new_area_code)
                        print('area code successfully modified')
                        
                    elif choice == 7:

                        new_number = input("Enter new phone number: ")
                        self.contact.edit(option=choice, index=student_index, val=new_number)
                        print('contact number successfully modified')
                         
                    elif choice == 8:
                        updated_info = self.contact.get_contact_list[student_index]
                        print("updated info of", updated_info)
                        break

            else:
                print("student not found")
                continue

    def menu(self, choice: int):
        if self:
            return {1: 'Philippines',
                    2: 'Thailand',
                    3: 'Singapore',
                    4: 'Indonesia',
                    5: 'Malaysia',
                    6: 'All',
                    0: 'No more'
                    }.get(choice)

    def search_contact(self):

        print('From which country?:')
        print('[1]Philippines [2]Thailand [3]Singapore [4]Indonesia [5]Malaysia [6]all [0]NO more ')

        country = []
        country_name = ''

        for n in range(1, 7):
            choice = int(input(f'Enter choice {n}: '))

            selected = self.menu(choice)

            if selected != 'No more':
                if selected == 'All':
                    print(self.contact.getAll)
                else:

                    selected_country = self.contact.get_aseanCountry(selected)
                    country.extend(selected_country)
                    country_name += f'{selected} '

            elif selected == 'No more':
                display_selected = self.contact.display_fromCountry(country_name=country_name.rstrip(),
                                                                    country_list=country)
                print(display_selected)
                break

        return self

    def main(self):

        while True:

            print("""[1] Store to ASEAN Phonebook
[2] Edit entry in ASEAN phonebook
[3] Search in ASEAN phonebook by country""")

            choice = int(input(">>> "))

            if choice == 1:
                self.create_contact()

            elif choice == 2:
                self.edit_contact()

            elif choice == 3:
                self.search_contact()

            else:
                break


app = Application()
app.main()
