#-----------------
#- This project is emplement of a semple CV program
#----------------
class Experience:
     def __init__(self, comp, jop_title, start_date, end_date):
         self.company = comp
         self.jop_title = jop_title
         self.start_date = start_date
         self.end_date = end_date
     def display_exper(self):
         return f' -Title:{self.jop_title}\n -Company Name:{self.company}\n -Start at:{self.start_date}\n -End at:{self.end_date}'


class Education:
    def __init__(self, deg, instituion, compl_date):
        self.degree = deg
        self.instituion = instituion
        self.copletion_data = compl_date

    def display_education(self):
        return f' -Degree:{self.degree}\n -Institution:{self.instituion}\n -Completion Date:{self.copletion_data}\n'



class Skill:
    def __init__(self, skill, percentage):
        self.skill = skill
        self.prc = percentage
    def dis_skill(self):
        return f' -Skill name:{self.skill} {self.prc}%'

class CV:
    def __init__(self):
      self.experience = []
      self.education = []
      self.skill = []

    def add_exper(self):
        while True:
           cop = input("plaese Enter the name of the Company:")
           jop = input("Enter Jop Title:")
           start = input("Enter the Date of start:")
           end = input("Enter the Date of End:")
           expr = Experience(cop, jop, start, end)

           self.experience.append(expr)
           ans = input("You want to add more experience: Answer with yes or no:")
           if ans == "yes":
                continue
           else:
             break

    def add_edu(self):
        while True:
            deg = input("Enter your Degree:")
            inst = input("Enter Institution Name:")
            compl = input("Enter Completion Date:")
            edu = Education(deg, inst, compl)
            self.education.append(edu)
            ans = input("You want to add more education: Answer with yes or no:")
            if ans == "yes":
                continue
            else:
                break

    def add_skill(self):
        while True:
            sk = input("Enter the Skill Name:")
            prc = input("Enter your Skill Percentage:")
            skl = Skill(sk, prc)
            self.skill.append(skl)
            ans = input("Do you want to add more skill? Answer with yes or no:")
            if ans == "yes":
                continue
            else:
                break

    def cv_dis(self):
        print("*********CV*********")
        print("#Experienc:")
        for exp in self.experience:
         print(exp.display_exper())
        print("#Education:")
        for edu in self.education:
            print(edu.display_education())
        print("#Skills:")
        for sk in self.skill:
            print(sk.dis_skill())







if __name__ == "__main__":
    # ex = Experience("my comp", "Software Eng", 2020, 2023)
    # print(ex.display_exper())
    # ed = Education("prof", "sana`a unvircity", 2024)
    # print(ed.display_education())
    # sk = Skill("DB designer", 80)
    # print(sk.dis_skill())
    c = CV()
    c.add_exper()
    c.add_edu()
    c.add_skill()
    c.cv_dis()

