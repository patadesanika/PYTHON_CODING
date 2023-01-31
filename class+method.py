class student1:
    school='zp'
    @classmethod
    def classm(cls):
        return cls.school
s1=student1
print(s1.classm())