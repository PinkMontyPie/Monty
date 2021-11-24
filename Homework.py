part_pos,full_pos,fulltime_list,parttime_list,sum_fulltime,sum_parttime = [],[],[],[],[],[]
def getdata():
    with open("profile.txt","r") as profile :
        data = profile.read().splitlines()
        for line in data :
            item = line.split()
            if item[3] == "F":
                summary = int(item[4]) + (int(item[5])*0.1)
                fulltime_list.append(item)
                sum_fulltime.append(summary)
                full_pos.append(item[0])
                pos = full_pos.index(item[0])
                fulltime_list[pos].append(float(summary))
            elif item[3] == "P":   
                summary = int(item[4]) + (int(item[5])*0.1)
                parttime_list.append(item)
                sum_parttime.append(summary)
                part_pos.append(item[0])
                pos = part_pos.index(item[0])
                parttime_list[pos].append(float(summary))
def writedata2file():
    with open("parttime.txt","w") as parttime , open("fulltime.txt","w") as fulltime :
        parttime.write("%42s\n"%("SHOW INCOME EMPLOYEE PARTTIME"))
        parttime.write("  %-10s%-15s%-10s%-10s%-10s\n"%("NAME","SURNAME","SALARY","SALE","INCOME"))
        parttime.write("  %-10s%-15s%-10s%-10s%-10s\n"%("="*4,"="*7,"="*6,"="*4,"="*6))
        for i in parttime_list:
            parttime.write("  %-10s%-15s%-10s%-10s%-10.0f\n"%(i[1],i[2],i[4],i[5],i[6]))
        parttime.write("="*55)
        parttime.write("\nTotal Income  =  %0.0f"%(sum(sum_parttime)))
        fulltime.write("%42s\n"%("SHOW INCOME EMPLOYEE FULLTIME"))
        fulltime.write("  %-10s%-15s%-10s%-10s%-10s\n"%("NAME","SURNAME","SALARY","SALE","INCOME"))
        fulltime.write("  %-10s%-15s%-10s%-10s%-10s\n"%("="*4,"="*7,"="*6,"="*4,"="*6))
        for i in fulltime_list:
            fulltime.write("  %-10s%-15s%-10s%-10s%-10.0f\n"%(i[1],i[2],i[4],i[5],i[6]))
        fulltime.write("="*55)
        fulltime.write("\nTotal Income  =  %0.0f"%(sum(sum_fulltime)))
getdata()
writedata2file()