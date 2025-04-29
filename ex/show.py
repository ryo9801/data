def show_list(data_dic):
  show = {"employee":[key for key in list(data_dic.keys())],
          "id":[data_dic[key]["id"] for key in list(data_dic.keys())],
          "attendance":[data_dic[key]["attendance"] for key in list(data_dic.keys())]}
  return show