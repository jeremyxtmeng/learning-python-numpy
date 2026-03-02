# lesson 12: Capstone project: name mashup
print("Welcome to the Mashup Game!")
name1 = input("Enter one full name (FIRST LAST): ")
name2 = input("Enter another full name (FIRST LAST): ")

sep1=name1.find(" ")
name1_first=name1[0:sep1]
name1_last=name1[sep1+1:len(name1)]

sep2=name2.find(" ")
name2_first=name2[0:sep2]
name2_last=name2[sep2+1:len(name2)]


n11=name1_first[0:int(sep1/2)]
n12=name1_first[int(sep1/2): sep1]

n21=name2_first[0:int(sep2/2)]
n22=name2_first[int(sep2/2): sep2]

n13=name1_last[0:int(len(name1_last)/2)]
n14=name1_last[int(len(name1_last)/2): len(name1_last)+1]
n23=name2_last[0:int(len(name2_last)/2)]
n24=name2_last[int(len(name2_last)/2): len(name2_last)+1]

print(n21+n12, " ", n23+n14)