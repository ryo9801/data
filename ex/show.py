def show_list(data_dic):
  show = {"item":[key for key in list(data_dic.keys())],
          "plice":[data_dic[key]["plice"] for key in list(data_dic.keys())],
          "stock":[data_dic[key]["stock"] for key in list(data_dic.keys())],
          "id":[data_dic[key]["id"] for key in list(data_dic.keys())]}
  return show