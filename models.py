from collections import namedtuple

Person=namedtuple("Person", ["email", "first_name", "last_name", "age"])

data={
    1: Person("johndoe@gmail.com", "John", "Doe", 35),
    2: Person("janedoe@gmail.com", "Jane", "Doe", 30),
    3: Person("johnsmith@gmail.com", "John", "Smith", 23),
    4: Person("jasonross@gmail.com", "Jason", "Ross", 40),
}