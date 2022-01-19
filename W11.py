st_list = []
id_list = []
def add (item,score):   
    pos = id_list.index(item[0])
    st_list[pos].append(str(score))
with open('profile.txt','r') as pro:
  data = pro.read().splitlines()
  for line in data:
    item = line.split()
    st_list.append(item)
    id_list.append(item[0])
  with open('midterm.txt','r') as mid:
    data = mid.read().splitlines()
    for line in data:
      item = line.split()
      score = (item[1])
      add(item,score)
    with open('final.txt','r') as fin: 
      data = fin.read().splitlines()
      for line in data:
        item = line.split()
        score = (item[1])
        add(item,score)
      for line in st_list:
          score = (float(line[5])+float(line[6]))
          add(line,score)
          if score >= 80 and score <= 100 :
            add(line,"A")
          elif score >= 70 and score <= 79 :
            add(line,"B")
          elif score >= 60 and score <= 69 :
            add(line,"C")
          elif score >= 50 and score <= 59 :
            add(line,"D")
          elif score < 50 :
            add(line,"F")     
      with open('gradereport.txt','w') as summ:
        for line in st_list:
          summ.write("%-9s%-12s%-20s%-6s%0.2f  Grade %s\n"%(line[0],line[1],line[2],line[3],float(line[7]),line[8],))