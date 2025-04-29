import json
with open("info.json") as f:
    employee_data=json.load(f)
def sort_json(empty_dic,data):
  sorted_data_by_id = sorted([data[id]["id"] for id in list(data.keys())])
  for key in list(data.keys()):
    #sorted_name = 
  #newdata = empty_dic
  #return sorted_data
#print(sort_json({},employee_data))