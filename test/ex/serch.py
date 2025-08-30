def serch_list(serch_data,dic_data):
  if dic_data:
    keys = list(dic_data.keys())
  else:
   return None
  if serch_data in keys:
    show = {"item":[serch_data],
          "plice":[dic_data[serch_data]["plice"] ],
          "stock":[dic_data[serch_data]["stock"] ],
          "id":[dic_data[serch_data]["id"]]}
  return show