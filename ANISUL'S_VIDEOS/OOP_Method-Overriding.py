class student:
    def __init__(self):
        print("I am a student")

class teacher(student):
    def __init__(self):
        super().__init__()
        print("I am a teacher")

t=teacher()
