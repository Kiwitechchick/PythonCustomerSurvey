# Customer Questionnaire
# Change and adjust
# Choices

choices = " 1) Strongly Disagree\n 2) Somewhat Disagree\n 3) Neither Agree or Disagree\n 4) Somewhat agree\n 5) Strongly Agree\n"
print(choices)


# Open and readlines of Questions.txt file. The path is located in C drive but you can change the path accordingly

with open('C:\Assignment\Questions.txt') as f:
    questions = f.readlines()

print(questions)


# writelines onto Answers.txt file. 

fa = open('C:\Assignment\Answers.txt', 'a') 

for index in range(len(questions)):
        answer=input(questions[index]+choices)
        fa.writelines(answer+'\n') 

fa.close()
# Read and total answer
q1=["Q1",0,0,0,0,0]
q2=["Q2",0,0,0,0,0]
q3=["Q3",0,0,0,0,0]
q4=["Q4",0,0,0,0,0]
q5=["Q5",0,0,0,0,0]
i=0


# Open file to calculate survey score.

with open('C:\Assignment\Answers.txt') as f:
   for answer in f:
        i+=1
        if i > 5 :
            i = 1
        if i == 1 :
            q1[int(answer)]+=1
        elif i == 2:
            q2[int(answer)]+=1
        elif i == 3:
            q3[int(answer)]+=1
        elif i == 4:
            q4[int(answer)]+=1
        elif i == 5:
            q5[int(answer)]+=1



# In[9]:

print(" 1) Strongly Disagree 2) Somewhat Disagree 3) Neither Agree or Disagree 4) Somewhat agree 5) Strongly Agree\n")

print(q1[0],q1[1],q1[2],q1[3],q1[4],q1[5]) 
print(q2[0],q2[1],q2[2],q2[3],q2[4],q2[5]) 
print(q3[0],q3[1],q3[2],q3[3],q3[4],q3[5]) 
print(q4[0],q4[1],q4[2],q4[3],q4[4],q4[5]) 
print(q5[0],q5[1],q5[2],q5[3],q5[4],q5[5]) 





