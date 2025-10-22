questions = [["Who is the prime minester of the India ?","Rahul Gandhi", "Narender Modi", "Shahrukh Khan","Amit Shah",2],
             ["Who is Shahrukh Khan ?", "Footballer", "Political Leader", "Actor", "Pilot", 3],
             ["Where is the tallest Building of the world ?", "Mumbai", "Delhi", "America", "Dubai", 4],
             ["What is the Capital of the France ?", "Paris", "Berlin", "New York", "Delhi", 1],
             ["Which Occean is the largest ?", "Atlantic", "Arctic", "Pacific", "India", 3],
             ["Which Planet Known as the Red Planet ?", "Mars", "Venus", "Jupiter", "Neptune",1],
             ["Which is the largest mammal ?", "Shark", "Lion", "Octopus", "Blue Whale", 4],
             ["Which River is know as longest River in the world ?", "Ganga", "Nile", "Amazon","Narmada", 2],
             ["What is National Bird of the India ?", "Sparrow", "Parrot", "Peacock", "Koyal", 3],
             ["What is Square root of 64 ?", "12", "28", "9", "8", 4]
             ]

prizes = [100,200,300,400,500,1000,1500,2500,3000,5000]
i = 0
for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

# Check whether the answer is correct or not
    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d\n"))
    if(question[5] == a):
        print("Correct Answer")
    else:
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time!")
        break 
    print(f"You won {prizes[i]}")
    i +=1    
