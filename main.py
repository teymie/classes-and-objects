class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
        print('My name is', name , ',i am' , age , 'years old', ',my tracks are' , tracks ,'and my score is' , score)
    def change_name(self , name):
        self.name = str(name)
        print("My name is",name)

    def change_age(self , age):
        self.age = int(age)
        print("I am",age , "years old")

    def add_track(self, track):
        self.track = self.tracks.append(track)
        print("My tracks are", self.tracks) 

    def get_score(self):
        
        return (self.score)


        

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
Bob

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print(f"My score is {Bob.get_score()}")
