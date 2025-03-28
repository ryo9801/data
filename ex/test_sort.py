def sort_json(empty_dic,data):
  sorted_data_by_key = sorted([key for key in list(data.keys())])
  sorted_data_by_value = [data[name] for name in sorted_data_by_key]
  for i in range(len(sorted_data_by_key)):
    empty_dic[sorted_data_by_key[i]] = sorted_data_by_value[i]
  newdata = empty_dic
  return newdata