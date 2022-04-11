import csv
from functools import reduce

csvf = open("911_Calls_for_Service_(Last_30_Days).csv")
reader = csv.DictReader(csvf)

filtered_lst = list(filter(lambda row: row["zip_code"] != "" and row["neighborhood"] != "" and row["totalresponsetime"] != "" and row["dispatchtime"] != "" and row["totaltime"] != "", reader))

tot_response_time = reduce(lambda t1, t2: t1 + float(t2["totalresponsetime"]), filtered_lst, 0)
avg_tot_response_time = tot_response_time / len(filtered_lst)
print(f"Average total response time: {avg_tot_response_time}")

tot_dispatch_time = reduce(lambda t1, t2: t1 + float(t2["dispatchtime"]), filtered_lst, 0)
avg_dispatch_time = tot_dispatch_time / len(filtered_lst)
print(f"Average dispatch time: {avg_dispatch_time}")

tot_time = reduce(lambda t1, t2: t1 + float(t2["totaltime"]), filtered_lst, 0)
avg_tot_time = tot_time / len(filtered_lst)
print(f"Average total time: {avg_tot_time}")

neighborhood_lst = []
for i in filtered_lst:
    if i["neighborhood"] not in neighborhood_lst:
        neighborhood_lst += i["neighborhood"]

neighborhood_lst = neighborhood_lst.sort()

for i in neighborhood_lst:
    print(f"{i}:")
    