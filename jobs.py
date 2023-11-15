def schedule_job(jobs, deadlines, profits, sch_jobs):
    total_profit = 0
    for i in range(len(jobs)):
        j = deadlines[i]
        while (j != 0):
            if (sch_jobs[j] != None):
                j = j-1
            else:
                sch_jobs[j] = jobs[i]
                total_profit = total_profit+profits[i]
                break

    print("Maximum profit Sequence : ", end="")
    for i in range(1, len(sch_jobs)):
        if (sch_jobs[i] != None):
            print(sch_jobs[i], end="")
        if (i < len(sch_jobs)-1 and sch_jobs[i+1] != None):
            print("-->", end="")
    print("\n")
    print("Total profit is : ", total_profit)



n = int(input("Enter Number of Jobs you want to enter : "))
in_jobs = []
in_profits = []
in_deadlines = []
for i in range(n):
    name = str(input("Enter name of job %d : " % (i+1)))
    in_jobs.append(name)
    deadline = int(input("Enter deadline of job %d : " % (i+1)))
    in_deadlines.append(deadline)
    profit = int(input("Enter profit of job %d : " % (i+1)))
    in_profits.append(profit)
    print("\n")

sch = []
for i in range(max(in_deadlines)+1):
    sch.append(None)
for i in range(len(in_jobs)):
    max = i
    for j in range(i+1, len(in_jobs)):
        if (in_profits[j] > in_profits[max]):
            max = j
    (in_deadlines[i], in_deadlines[max]) = (in_deadlines[max], in_deadlines[i])
    (in_profits[i], in_profits[max]) = (in_profits[max], in_profits[i])
    (in_jobs[i], in_jobs[max]) = (in_jobs[max], in_jobs[i])

schedule_job(in_jobs, in_deadlines, in_profits, sch)
