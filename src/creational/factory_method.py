class Interviewr:
    def ask_question(self):
        pass

class Developer(Interviewr):
    def ask_question(self):
        print("Ask a question about Development")

class Accountant(Interviewr):
    def ask_question(self):
        print("Ask a question about Accounting")
    
class HiringManager:
    def make_interviewer(self):
        pass

    def take_interview(self):
        interviewer = self.make_interviewer()
        interviewer.ask_question()

class DevelopmentManager(HiringManager):
    def make_interviewer(self):
        return Developer()
    
class AccountingManager(HiringManager):
    def make_interviewer(self):
        return Accountant()
    
if __name__ == "__main__":
    dev_manager = DevelopmentManager()
    dev_manager.take_interview()

    accounting_manager = AccountingManager()
    accounting_manager.take_interview()