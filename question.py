class question:

    def __init__(self,data,opt1,opt2,opt3,opt4,canswer):
        self.data = data
        self.opt1 = opt1
        self.opt2 = opt2
        self.opt3 = opt3
        self.opt4 = opt4
        self.canswer = canswer

    def __str__(self):
        return f"{self.data} \n A.{self.opt1 }\nB.{self.opt2} \nC.{self.opt3} \nD.{self.opt4}"