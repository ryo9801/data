from dataclasses import dataclass,asdict
import json
import streamlit as st
import os
import time
import pandas as pd
from ex import test_sort,show,serch
# チェックしたいディレクトリとファイル名
folder_path = '/Users/宮井/Desktop/program/vscode/test'  # フォルダのパス
file_name = 'drink.json'  # 調べたいファイル名
file_name2 = "vegetable.json"
def create_dict(): 
  dic = {}
  return dic

@dataclass
class info:
  plice : int
  stock : int
  id : int
# ファイルが存在するか確認  
if file_name in os.listdir(folder_path):
  with open("drink.json") as f:
    items=json.load(f)
else:
  with open("drink.json", "w", encoding="utf-8") as json_file:
    json.dump({},json_file)
    pass  # 何も書き込まずにファイルを閉じる
with open("drink.json") as f:
  items=json.load(f)

if file_name2 in os.listdir(folder_path):
  with open("vegetable.json") as f:
    items2=json.load(f)
else:
  with open("vegetable.json", "w", encoding="utf-8") as json_file:
    json.dump({},json_file)
    pass  # 何も書き込まずにファイルを閉じる
with open("vegetable.json") as f:
  items2=json.load(f)



page = st.sidebar.selectbox("ページを選んでください", ["Home", "Add", "Del", "Plice" , "Stock","Serch"]) 

if page == "Home":
  st.title("ホームページです")
  radio = st.radio("選択",("drink", "vegetable"), horizontal=True)
  home_data = items if radio == "drink" else items2 if radio == "vegetable" else "error"
  with open(f"{radio}.json","w") as f:
    json.dump(test_sort.sort_json(create_dict(),home_data),f,indent=1)
  with open(f"{radio}.json") as f:
    data=json.load(f)
  st.write(pd.DataFrame(show.show_list(data)) if data.keys() else "データがありません")

elif page == "Add":
  st.title("データを追加します")
  placeholder = st.empty()
  radio = st.radio("選択",("drink", "vegetable"), horizontal=True)
  add_data = items if radio == "drink" else items2 if radio == "vegetable" else "error"
  item = create_dict()
  name = st.text_input("name")
  plice = st.number_input("plice ",value=0)
  stock = st.number_input("stock",value=0)
  id = st.number_input("id",value=0)
  button = st.button("追加")
  if button:
    a = info(plice,stock,id)
    item[name] = asdict(a)
    new_items = dict(add_data,**item)  
    with open(f"{radio}.json","w") as f:
      json.dump(new_items,f,indent=1)
    placeholder.write("追加しました")
    time.sleep(0.5)
    placeholder.write("")

elif page == "Del":
  st.title("データを消去します")
  placeholder = st.empty()
  radio = st.radio("選択",("drink", "vegetable"), horizontal=True)
  del_data = items if radio == "drink" else items2 if radio == "vegetable" else "error"
  name = st.selectbox("商品選択",[key for key in list(del_data.keys())])
  button = st.button('消去')
  if button:
    del del_data[name]
    placeholder.write("消去しました")
    time.sleep(0.5)
    placeholder.write("")
    with open(f"{radio}.json","w") as f:
      json.dump(del_data,f,indent=1)
     
elif page == "Plice":
  st.title("値段を変えます")
  placeholder = st.empty()
  radio = st.radio("選択",("drink", "vegetable"), horizontal=True)
  plice_data = items if radio == "drink" else items2 if radio == "vegetable" else "error"
  name = st.selectbox("商品選択",[key for key in list(plice_data.keys())])
  plice = st.number_input("change_plice",value=0)
  button = st.button('変更')
  if plice and name and button:
    plice_data[name]["plice"] = plice 
    with open(f"{radio}.json","w") as f:
      json.dump(plice_data,f,indent=1)
    placeholder.write("変更完了")
    time.sleep(0.5)
    placeholder.write("")

elif page == "Stock":
  st.title("在庫管理します")
  placeholder = st.empty()
  radio = st.radio("選択",("drink", "vegetable"), horizontal=True)
  stock_data = items if radio == "drink" else items2 if radio == "vegetable" else "error"
  name = st.selectbox("商品選択",[key for key in list(stock_data.keys())])
  stock = st.number_input("change_stock",value=0)
  button = st.button("変更")
  if stock and name and button:
    stock_data[name]["stock"] = stock_data[name]["stock"] + stock
    with open(f"{radio}.json","w") as f:
      json.dump(stock_data,f,indent=1)
    placeholder.write("変更完了")
    time.sleep(0.5)
    placeholder.write("")

elif page == "Serch":
  st.title("検索します")
  radio = st.radio("選択",("drink", "vegetable"), horizontal=True)
  serch_data = items if radio == "drink" else items2 if radio == "vegetable" else "error"
  name = st.selectbox("商品選択",[key for key in list(serch_data.keys())])
  st.write(pd.DataFrame(serch.serch_list(name,serch_data)))