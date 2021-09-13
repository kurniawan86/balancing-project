readme program:
there are 3 file in this folder.
===============================
open thirth.py and run program
==================================================
at file thith.py there are class classGuttman and some main class code at line (53-60)
explanation of that line:

this line for create object for class classGuttman
obj=classGuttman()

this syntax for grab dataset (cluster) from excel file (data.xlsx) 
obj.getDataset()

this syntax for get value Score for convertion from data (original data)
obj.getArteryScore()

this syntax for multiply score and data
obj.getArteryMuliply()

syntax for calculate sum of each row data multiply
obj.getScalar()

syntax for labeling each data with guttman method
obj.getGuttmanClass()

syntax for export value of label dataset to excel file
obj.writeExcel()

syntax for export value label guttman and all attribute to excel file
obj.writeExcelExixting()

=====================================
at file second.py there is classMultiply:
main output from this class is value of multiply ,value of scalar data, PRTA and labeling Guttman. method which generate value multiply is calMultiply(self) at line 40. and value which calculate scalar value is calScalar. calPRTA and getGuttmanClass are method which calculate value of PRTA and generate label guttman method.