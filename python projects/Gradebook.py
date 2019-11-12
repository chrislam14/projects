class Assignment:
    def __init__(self, description, score, total): #constructor
        self._des = description
        self._score = score
        self._total = total
    def getDescription(self)->str: #returns the description
        return self._des
    def getScore(self)->float: #returns the score
        return self._score
    def getTotal(self)->float: #returns the total
        return self._total
    def changeScore(self, score:float): #changes the score
        self._score = score
    def __repr__(self): #string representation
        return "Assignment with Description: " + self._des + " and Score: " + str(self._score) +" out of " + str(self._total)
        
class CategoryAssignment(Assignment):
    def __init__(self, description, category, score, total):
        super().__init__(description, score, total) #constructor for parent class
        self._category = category 
    def getCategory(self)->str: #returns the category
        return self._category
    
    def __repr__(self): #string representation
        return "Category Assignment with Description: " + self._des + " Category: " + self._category + " and Score: " + str(self._score) +" out of " + str(self._total)

class Student:
    def __init__(self, studentID): #constructor
        self._SID = studentID
        self._alist = []
        self._anlist = []
    def getAList(self)->list: #returns a list
        return self._alist 
    def getId(self)->int: #returns ID
        return self._SID
    def getScore(self, assignmentName:str)->float: #gets score
        for a in self._alist:
            if assignmentName == a.getDescription():
                return a.getScore()
    def addAssignment(self, score:Assignment): #adds an assignment to the list
        self._alist.append(score)
        self._anlist.append(score.getDescription())
    def changeScore(self, assignmentName:str, score:float): #changes the score
        for a in self._alist:
            if assignmentName == a.getDescription():
                a.changeScore(score)
    def removeScore(self, assignmentName:str):
        for a in self._alist:
            if assignmentName == a.getDescription():
                self._alist.remove(a)
                self._anlist.remove(a.getDescription())
    def __repr__(self): #string representation
        return "Student with ID: " + str(self._SID) + " and Assignment list: \n" + str(self._anlist)

class Gradebook:
    def __init__(self): #constructor
        self._gB = {}
    def addStudent(self, student:Student): #adds a student to the gradebook dictionary
        self._gB[str(student.getId())] = student
    def dropStudent(self, SID:int): #removes a student from the gradebook
        self._gB.pop(str(SID), None)
    def search(self, SID:int)->Student: #returns the student with the ID
        if str(SID) in self._gB:
            return self._gB[str(SID)]
    def addAssignment(self, SID:int, score:Assignment): #adds score to a student with given ID
        self._gB[str(SID)].addAssignment(score)

class TotalPointsGradebook(Gradebook):
    def __init__(self):
        super().__init__()
        self._classPerc = 0
    def writeGradebookRecord(self, SID:int, fileName:str):
        outfile = open(fileName, 'w')
        totalS = 0
        totalT = 0
        totalP = 0
        if str(SID) not in self._gB:
            outfile.write("Student Not Found")
        else:
            outfile.write(str(SID)+'\n') 
            for a in self.search(SID).getAList():
                outfile.write(a.getDescription()+ '\n' + str(a.getScore()) + '/' + str(a.getTotal())+ "\n")
                totalS += a.getScore()
                totalT += a.getTotal()
            totalP = (totalS/totalT)*100 
            outfile.write("Total: "+str(totalS)+"/"+str(totalT)+"\n")
            outfile.write("Percentage: "+str(totalP))
        outfile.close()
    def classAverage(self)->float:
        classPerc = 0
        for s in self._gB:
            totalS = 0
            totalT = 0
            totalP = 0
            for a in self._gB[s].getAList():
                totalS += a.getScore()
                totalT += a.getTotal()
            totalP += totalS/totalT
            classPerc += totalP
        self._classPerc = classPerc/len(self._gB)
        return self._classPerc*100

class CategoryGradebook(Gradebook):
    def __init__(self):
        super().__init__()
        self._weightedtotal = 0
        self._weighted = {}
        self._classPerc = 0
    def addCategory(self, description:str, weight:float):
        self._weighted[description] = weight
    def isBalanced(self)->bool:
        self._weightedtotal = 0
        for c in self._weighted:
            self._weightedtotal += self._weighted[c]
        return (self._weightedtotal == 100)
    def writeGradebookRecord(self, SID:int, fileName:str):
        outfile = open(fileName, 'w')
        totals = {}
        finalPerc = 0
        if str(SID) not in self._gB:
            outfile.write("Student Not Found")
        else:
            outfile.write(str(SID)+'\n') 
            for a in self.search(SID).getAList():
                outfile.write(a.getCategory()+ ": " + a.getDescription()+ '\n' + str(a.getScore()) + '/' + str(a.getTotal())+ "\n")
                if a.getCategory() not in totals:
                    totals[a.getCategory()] = [0,0,0]
                
                totals[a.getCategory()][0] += a.getScore()
                totals[a.getCategory()][1] += a.getTotal()
            for a in self._weighted:
                outfile.write(a + ": " + str((totals[a][0]/totals[a][1]))+'\n')    
                totals[a][2] = (totals[a][0]/totals[a][1])*(self._weighted[a])
                finalPerc += totals[a][2]
            outfile.write("Percentage: "+str(finalPerc))
        outfile.close()
        
    def classAverage(self)->float:
        classPerc = 0
        for s in self._gB:
            sPerc = 0
            totals = {}
            for a in self._gB[s].getAList():
                if a.getCategory() not in totals:
                    totals[a.getCategory()] = [0,0,0]               
                totals[a.getCategory()][0] += a.getScore()
                totals[a.getCategory()][1] += a.getTotal()
            for a in self._weighted:
                sPerc += (totals[a][0]/totals[a][1])*(self._weighted[a])
            classPerc += sPerc
        self._classPerc = (classPerc/len(self._gB))
        return self._classPerc
    