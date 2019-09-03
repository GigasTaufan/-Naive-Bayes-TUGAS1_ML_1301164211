import csv

class naive:
    def __init__(self):
        self.dataTrain = []
        self.dataTest = []

        self.terima = 0
        self.tolak = 0
        self.prob_income = []
        # untuk AGE
        self.probAgeYoung = []
        self.youngIya = 0
        self.youngTdk = 0
        self.probAgeAdult = []
        self.adultIya = 0
        self.adultTdk = 0
        self.probAgeOld = []
        self.oldIya = 0
        self.oldTdk = 0
        # untuk WORKCLASS
        self.probWCPriv = []
        self.privIya = 0
        self.privTdk = 0
        self.probWCGov = []
        self.govIya = 0
        self.govTdk = 0
        self.probWCSelf = []
        self.selfIya = 0
        self.selfTdk = 0
        # untuk EDUCATION
        self.probEduBc = []
        self.bachelorIya = 0
        self.bachelorTdk = 0
        self.probEduHs = []
        self.highScIya = 0
        self.highScTdk = 0
        self.probEduCol = []
        self.collIya = 0
        self.collTdk = 0
        # untuk MARITAL-STATUS
        self.probMarMarried = []
        self.marriedIya = 0
        self.marriedTdk = 0
        self.probMarNever = []
        self.neverIya = 0
        self.neverTdk = 0
        self.probMarDiv = []
        self.divorceIya = 0
        self.divorceTdk = 0
        # untuk OCCUPATION
        self.probOccCraft= []
        self.craftIya = 0
        self.craftTdk = 0
        self.probOccExec = []
        self.execIya = 0
        self.execTdk = 0
        self.probOccProf = []
        self.profIya = 0
        self.profTdk = 0
        # untuk RELATIONSHIP
        self.probRelHusband = []
        self.husbandIya = 0
        self.husbandTdk = 0
        self.probRelNot = []
        self.notfamilyIya = 0
        self.notfamilyTdk = 0
        self.probRelOwnChild = []
        self.ownchildIya = 0
        self.ownchildTdk = 0
        # untuk HOURS-PER-WEEK
        self.probHPWLow = []
        self.lowIya = 0
        self.lowTdk = 0
        self.probHPWNormal = []
        self.normalIya = 0
        self.normalTdk = 0
        self.probHPWMany = []
        self.manyIya = 0
        self.manyTdk = 0

        self.jum = 0

    # OPEN TRAINSET
    def openTrainset(self):
        with open('TrainsetTugas1ML.csv') as csvfile:
            next(csvfile)
            spamreader = csv.reader(csvfile)
            for row_train in spamreader:
                self.dataTrain.append(row_train)
        csvfile.close()

    # INCOME
    def probabilitasIncome(self):
        for data in self.dataTrain:
            if data[8] ==">50K":
                self.terima+=1
            if data[8] == "<=50K":
                self.tolak+=1
            self.jum+=1

        self.prob_income.append(self.terima/self.jum)
        self.prob_income.append(self.tolak/self.jum)

    # AGE
    def probabilitasAge(self):
        for data in self.dataTrain:
            if data[1] == "young" and data[8] == ">50K":
                self.youngIya+=1
            if data[1] == "young" and data[8] == "<=50K":
                self.youngTdk+=1
            if data[1] == "adult" and data[8] == ">50K":
                self.adultIya+=1
            if data[1] == "adult" and data[8] == "<=50K":
                self.adultTdk+=1
            if data[1] == "old" and data[8] == ">50K":
                self.oldIya+=1
            if data[1] == "old" and data[8] == "<=50K":
                self.oldTdk+=1

        self.probAgeYoung.append(self.youngIya / self.terima)
        self.probAgeYoung.append(self.youngTdk / self.tolak)
        self.probAgeAdult.append(self.adultIya / self.terima)
        self.probAgeAdult.append(self.adultTdk / self.tolak)
        self.probAgeOld.append(self.oldIya / self.terima)
        self.probAgeOld.append(self.oldTdk / self.tolak)

    # WORDKCLASS
    def probabilitasWorkclass(self):
        for data in self.dataTrain:
            if data[2] == "Private" and data[8] == ">50K":
                self.privIya+=1
            if data[2] == "Private" and data[8] == "<=50K":
                self.privTdk+=1
            if data[2] == "Local-gov" and data[8] == ">50K":
                self.govIya+=1
            if data[2] == "Local-gov" and data[8] == "<=50K":
                self.govTdk+=1
            if data[2] == "Self-emp-not-inc" and data[8] == ">50K":
                self.selfIya+=1
            if data[2] == "Self-emp-not-inc" and data[8] == "<=50K":
                self.selfTdk+=1

        self.probWCPriv.append(self.privIya / self.terima)
        self.probWCPriv.append(self.privTdk / self.tolak)
        self.probWCGov.append(self.govIya / self.terima)
        self.probWCGov.append(self.govTdk / self.tolak)
        self.probWCSelf.append(self.selfIya / self.terima)
        self.probWCSelf.append(self.selfTdk / self.tolak)

    # EDUCATION
    def probabilitasEducation(self):
        for data in self.dataTrain:
            if data[3] == "Bachelors" and data[8] == ">50K":
                self.bachelorIya+=1
            if data[3] == "Bachelors" and data[8] == "<=50K":
                self.bachelorTdk+=1
            if data[3] == "HS-grad" and data[8] == ">50K":
                self.highScIya+=1
            if data[3] == "HS-grad" and data[8] == "<=50K":
                self.highScTdk+=1
            if data[3] == "Some-college" and data[8] == ">50K":
                self.collIya+=1
            if data[3] == "Some-college" and data[8] == "<=50K":
                self.collTdk+=1

        self.probEduBc.append(self.bachelorIya / self.terima)
        self.probEduBc.append(self.bachelorTdk / self.tolak)
        self.probEduHs.append(self.highScIya / self.terima)
        self.probEduHs.append(self.highScTdk / self.tolak)
        self.probEduCol.append(self.collIya / self.terima)
        self.probEduCol.append(self.collTdk / self.tolak)

    #  MARITAL
    def probabilitasMaritalStatus(self):
        for data in self.dataTrain:
            if data[4] == "Married-civ-spouse" and data[8] == ">50K":
                self.marriedIya+=1
            if data[4] == "Married-civ-spouse" and data[8] == "<=50K":
                self.marriedTdk+=1
            if data[4] == "Never-married" and data[8] == ">50K":
                self.neverIya+=1
            if data[4] == "Never-married" and data[8] == "<=50K":
                self.neverTdk+=1
            if data[4] == "Divorced" and data[8] == ">50K":
                self.divorceIya+=1
            if data[4] == "Divorced" and data[8] == "<=50K":
                self.divorceTdk+=1

        self.probMarMarried.append(self.marriedIya / self.terima)
        self.probMarMarried.append(self.marriedTdk / self.tolak)
        self.probMarNever.append(self.neverIya / self.terima)
        self.probMarNever.append(self.neverTdk / self.tolak)
        self.probMarDiv.append(self.divorceIya / self.terima)
        self.probMarDiv.append(self.divorceTdk / self.tolak)

    #  OCCUPATION
    def probabilitasOccupation(self):
        for data in self.dataTrain:
            if data[5] == "Craft-repair" and data[8] == ">50K":
                self.craftIya += 1
            if data[5] == "Craft-repair" and data[8] == "<=50K":
                self.craftTdk += 1
            if data[5] == "Exec-managerial" and data[8] == ">50K":
                self.execIya += 1
            if data[5] == "Exec-managerial" and data[8] == "<=50K":
                self.execTdk += 1
            if data[5] == "Prof-specialty" and data[8] == ">50K":
                self.profIya += 1
            if data[5] == "Prof-specialty" and data[8] == "<=50K":
                self.profTdk += 1

        self.probOccCraft.append(self.craftIya / self.terima)
        self.probOccCraft.append(self.craftTdk / self.tolak)
        self.probOccExec.append(self.execIya / self.terima)
        self.probOccExec.append(self.execTdk / self.tolak)
        self.probOccProf.append(self.profIya / self.terima)
        self.probOccProf.append(self.profTdk / self.tolak)

    #  RELATIONSHIP
    def probabilitasRelationship(self):
        for data in self.dataTrain:
            if data[6] == "Husband" and data[8] == ">50K":
                self.husbandIya += 1
            if data[6] == "Husband" and data[8] == "<=50K":
                self.husbandTdk += 1
            if data[6] == "Not-in-family" and data[8] == ">50K":
                self.notfamilyIya += 1
            if data[6] == "Not-in-family" and data[8] == "<=50K":
                self.notfamilyTdk += 1
            if data[6] == "Own-child" and data[8] == ">50K":
                self.ownchildIya += 1
            if data[6] == "Own-child" and data[8] == "<=50K":
                self.ownchildTdk += 1

        self.probRelHusband.append(self.husbandIya / self.terima)
        self.probRelHusband.append(self.husbandTdk / self.tolak)
        self.probRelNot.append(self.notfamilyIya / self.terima)
        self.probRelNot.append(self.notfamilyTdk / self.tolak)
        self.probRelOwnChild.append(self.ownchildIya / self.terima)
        self.probRelOwnChild.append(self.ownchildTdk / self.tolak)

    #  HOURS-PER-WEEK
    def probabilitasHoursPerWeek(self):
        for data in self.dataTrain:
            if data[7] == "low" and data[8] == ">50K":
                self.lowIya += 1
            if data[7] == "low" and data[8] == "<=50K":
                self.lowTdk += 1
            if data[7] == "normal" and data[8] == ">50K":
                self.normalIya += 1
            if data[7] == "normal" and data[8] == "<=50K":
                self.normalTdk += 1
            if data[7] == "many" and data[8] == ">50K":
                self.manyIya += 1
            if data[7] == "many" and data[8] == "<=50K":
                self.manyTdk += 1

        self.probHPWLow.append(self.lowIya / self.terima)
        self.probHPWLow.append(self.lowTdk / self.tolak)
        self.probHPWNormal.append(self.normalIya / self.terima)
        self.probHPWNormal.append(self.normalTdk / self.tolak)
        self.probHPWMany.append(self.manyIya / self.terima)
        self.probHPWMany.append(self.manyTdk / self.tolak)

    # OPEN TESTSET
    def openTestset(self):
        with open('TestsetTugas1ML.csv') as csvfile:
            next(csvfile)
            spamreader = csv.reader(csvfile)
            for row_test in spamreader:
                self.dataTest.append(row_test)
        csvfile.close()

    # perbandingan untuk menentukan income terhadap data Test
    def perbandingan(self):
        for data2 in self.dataTest:
            self.hasilYa = 1
            self.hasilTdk = 1
            for i in range(1,len(data2)):
                if i == 1:
                    if data2[i] == "young":
                        self.hasilYa *= self.probAgeYoung[0]
                        self.hasilTdk *= self.probAgeYoung[1]
                    elif data2[i] == "adult":
                        self.hasilYa *= self.probAgeAdult[0]
                        self.hasilTdk *= self.probAgeAdult[1]
                    elif data2[i] == "old":
                        self.hasilYa *= self.probAgeOld[0]
                        self.hasilTdk *= self.probAgeOld[1]
                if i == 2:
                    if data2[i] == "Private" :
                        self.hasilYa *= self.probWCPriv[0]
                        self.hasilTdk *= self.probWCPriv[1]
                    elif data2[i] == "Local-gov":
                        self.hasilYa *= self.probWCGov[0]
                        self.hasilTdk *= self.probWCGov[1]
                    elif data2[i] == "Self-emp-not-inc":
                        self.hasilYa *= self.probWCSelf[0]
                        self.hasilTdk *= self.probWCSelf[1]
                if i == 3:
                    if data2[i] == "Bachelors":
                        self.hasilYa *= self.probEduBc[0]
                        self.hasilTdk *= self.probEduBc[1]
                    elif data2[i] == "HS-grad":
                        self.hasilYa *= self.probEduHs[0]
                        self.hasilTdk *= self.probEduHs[1]
                    elif data2[i] == "Some-college":
                        self.hasilYa *= self.probEduCol[0]
                        self.hasilTdk *= self.probEduCol[1]
                if i == 4:
                    if data2[i] == "Married-civ-spouse":
                        self.hasilYa *= self.probMarMarried[0]
                        self.hasilTdk *= self.probMarMarried[1]
                    elif data2[i] == "Never-married":
                        self.hasilYa *= self.probMarNever[0]
                        self.hasilTdk *= self.probMarNever[1]
                    elif data2[i] == "Divorced":
                        self.hasilYa *= self.probMarDiv[0]
                        self.hasilTdk *= self.probMarDiv[1]
                if i == 5:
                    if data2[i] == "Craft-repair":
                        self.hasilYa *= self.probOccCraft[0]
                        self.hasilTdk *= self.probOccCraft[1]
                    elif data2[i] == "Exec-managerial":
                        self.hasilYa *= self.probOccExec[0]
                        self.hasilTdk *= self.probOccExec[1]
                    elif data2[i] == "Prof-specialty":
                        self.hasilYa *= self.probOccProf[0]
                        self.hasilTdk *= self.probOccProf[1]
                if i == 6:
                    if data2[i] == "Husband":
                        self.hasilYa *= self.probRelHusband[0]
                        self.hasilTdk *= self.probRelHusband[1]
                    elif data2[i] == "Not-in-family":
                        self.hasilYa *= self.probRelNot[0]
                        self.hasilTdk *= self.probRelNot[1]
                    elif data2[i] == "Own-child":
                        self.hasilYa *= self.probRelOwnChild[0]
                        self.hasilTdk *= self.probRelOwnChild[1]
                if i == 7:
                    if data2[i] == "normal":
                        self.hasilYa *= self.probHPWNormal[0]
                        self.hasilTdk *= self.probHPWNormal[1]
                    elif data2[i] == "low":
                        self.hasilYa *= self.probHPWLow[0]
                        self.hasilTdk *= self.probHPWLow[1]
                    elif data2[i] == "many":
                        self.hasilYa *= self.probHPWMany[0]
                        self.hasilTdk *= self.probHPWMany[1]

            self.hasilYa *= self.prob_income[0]
            self.hasilTdk *= self.prob_income[1]

            if self.hasilYa > self.hasilTdk:
                print(">50K")
                self.writer.writerow(['>50K'])
            else:
                print("<=50K")
                self.writer.writerow(['<=50K'])
        self.output.close()

    # save file
    def savefile(self):
        self.output = open("TebakanTugas1ML.csv", "w")
        self.writer = csv.writer(self.output, lineterminator = '\n')

if __name__ == '__main__':
    coba = naive()
    coba.openTrainset()
    coba.savefile()
    coba.probabilitasIncome()
    coba.probabilitasAge()
    coba.probabilitasWorkclass()
    coba.probabilitasEducation()
    coba.probabilitasMaritalStatus()
    coba.probabilitasOccupation()
    coba.probabilitasRelationship()
    coba.probabilitasHoursPerWeek()
    coba.openTestset()
    coba.perbandingan()