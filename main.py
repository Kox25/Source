from experta import *

class diagnosis(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action='start')

    # Define the first rule to declare another fact
    @Rule(Fact(action='start'), NOT(Fact(name=W())))  
    def ask_name(self):
        self.declare(Fact(name=input("What's your name? ")))

    # Info 1 (sleep)
    @Rule(Fact(action='start'), NOT(Fact(sleep=W())))
    def ask_sleep(self):
        self.declare(Fact(sleep=input("could you sleep at night ? ")))

    # Info 2 (eating)
    @Rule(Fact(action='start'), NOT(Fact(eating=W())))
    def ask_eating(self):
        self.declare(Fact(eating=input("could you eat well ? ")))

    # Info 3 (hallucination)
    @Rule(Fact(action='start'), NOT(Fact(hallucination=W())))
    def ask_hallucination(self):
        self.declare(Fact(hallucination=input("could you see unreal stuff ? ")))

    # Info 4 (age)
    @Rule(Fact(action='start'), NOT(Fact(age=W())))
    def ask_age(self):
        self.declare(Fact(age=input("How old are you ? ")))

    # Info 5 (gender)
    @Rule(Fact(action='start'), NOT(Fact(gender=W())))
    def ask_gender(self):
        self.declare(Fact(gender=input("are you male or female ? ")))

    # Info 6 (negativity)
    @Rule(Fact(action='start'), NOT(Fact(nigativety=W())))
    def ask_negativity(self):
        self.declare(Fact(nigativety=input("do you have a negative thoughts ? ")))

    # Info 7 (salary)
    @Rule(Fact(action='start'), NOT(Fact(salery=W())))
    def ask_salary(self):
        self.declare(Fact(salery=input("are you student or graduated ? ")))

    # Info 8 (status)
    @Rule(Fact(action='start'), NOT(Fact(status=W())))
    def ask_status(self):
        self.declare(Fact(status=input("are you married or single ? ")))

    # Info 9 (relationship)
    @Rule(Fact(action='start'), NOT(Fact(relationship=W())))
    def ask_relationship(self):
        self.declare(Fact(relationship=input("do you have a relationship ? ")))

    # Info 10 (safety status)
    @Rule(Fact(action='start'), NOT(Fact(safety=W())))
    def ask_safety(self):
        self.declare(Fact(safety=input("what is the degree you think have it of safety ? ")))

    # Define the action based on rules
    @Rule(Fact(action='start'),
          Fact(name=MATCH.name),
          Fact(sleep='no'),
          Fact(eating='no'),
          Fact(hallucination='yes'),
          Fact(age=MATCH.age & (lambda age: age >= 18)),
          Fact(gender=MATCH.gender),
          Fact(nigativety='yes'),
          Fact(salery=MATCH.salery & (lambda salery: salery <= 3000)),
          Fact(status='single'),
          Fact(safety='low'))
    def go_to_doctor_action(self):
        print("bro you have to visit doctor")

    @Rule(Fact(action='start'),
          Fact(name=MATCH.name),
          Fact(sleep='yes'),
          Fact(eating='yes'),
          Fact(hallucination='no'),
          Fact(age=MATCH.age & (lambda age: age >= 18)),
          Fact(gender=MATCH.gender),
          Fact(nigativety='no'),
          Fact(salery=MATCH.salery & (lambda salery: salery >= 3000)),
          Fact(status='married'),
          Fact(safety='high'))
    def relax_action(self):
        print("bro you just need to relax and have fun")




dia = diagnosis()
dia.reset()
dia.run()
