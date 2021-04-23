import csv
import statistics
with open('SOCR-HeightWeight.csv',newline = '')as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0) 
new_info = []
for i in range(len(file_data)):
    num = file_data[i][2]
    new_info.append(float(num))
new_info.sort()
#print(new_info)
n = len(new_info)
print(n)
total = 0
for x in new_info:
    total += x
mean = total/n
print("The mean is: "+str(mean))
if n%2 == 0:
    median1 = float(new_info[n//2])
    median2 = float(new_info[n//2-1])
    print("median1: "+ str(median1))
    print("median2: "+ str(median2))
    median = (median1+median2)/2
else:
    median = new_info[n//2]
print("The median is: "+str(median))
mode = statistics.mode(n)
print(mode)