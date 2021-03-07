#Becky Matthews-Pease
#IST 652: Scripting for Data Analysis
#Lab 01


import pandas as pd

nbaData = pd.read_csv('C:\\Users\\becky\\Desktop\\nba-attendance-1989.txt', sep='\t+', header=None, engine='python')

for index, row in nbaData.iterrows():
    print('The attendance at {} was {:,d} and the ticket price was ${:.2f}'.format(row[0], row[1], row[2]))




#Output = The attendance at Atlanta was 13,993 and the ticket price was $20.06
#The attendance at Boston was 14,916 and the ticket price was $22.54
#The attendance at Charlotte was 23,901 and the ticket price was $17.00
#The attendance at Chicago was 18,404 and the ticket price was $21.98
#The attendance at Cleveland was 16,969 and the ticket price was $19.63
#The attendance at Dallas was 16,868 and the ticket price was $17.05
#The attendance at Denver was 12,668 and the ticket price was $17.40
#The attendance at Detroit was 21,454 and the ticket price was $24.42
#The attendance at Golden_State was 15,025 and the ticket price was $17.04
#The attendance at Houston was 15,846 and the ticket price was $17.56
#The attendance at Indiana was 12,885 and the ticket price was $13.77
#The attendance at LA_Clippers was 11,869 and the ticket price was $21.95
#The attendance at LA_Lakers was 17,378 and the ticket price was $29.18
#The attendance at Miami was 15,008 and the ticket price was $17.60
#The attendance at Milwaukee was 16,088 and the ticket price was $14.08
#The attendance at Minnesota was 26,160 and the ticket price was $10.92
#The attendance at New_Jersey was 12,160 and the ticket price was $13.31
#The attendance at New_York was 17,815 and the ticket price was $22.70
#The attendance at Orlando was 15,606 and the ticket price was $20.47
#The attendance at Philadelphia was 14,017 and the ticket price was $19.04
#The attendance at Phoenix was 14,114 and the ticket price was $16.59
#The attendance at Portland was 12,884 and the ticket price was $22.19
#The attendance at Sacramento was 17,014 and the ticket price was $16.96
#The attendance at San_Antonio was 14,722 and the ticket price was $16.79
#The attendance at Seattle was 12,244 and the ticket price was $18.11
#The attendance at Utah was 12,616 and the ticket price was $18.41
#The attendance at Washington was 11,565 and the ticket price was $14.55