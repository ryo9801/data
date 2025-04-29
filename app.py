from dataclasses import dataclass,asdict
import json
import streamlit as st
import os
import time
import pandas as pd
from ex import show
# チェックしたいディレクトリとファイル名
folder_path = '/Users/mling/Desktop/test2/data-main'  # フォルダのパス
file_name = 'info.json'  # 調べたいファイル名
def create_dict(): 
  dic = {}
  return dic

@dataclass
class employee:
  id : int
  attendance : bool
# ファイルが存在するか確認  
if file_name in os.listdir(folder_path):
  with open("info.json") as f:
    employee_data=json.load(f)
else:
  with open("info.json", "w", encoding="utf-8") as f:
    json.dump({},f)
  with open("info.json") as f:
    employee_data=json.load(f)

page = st.sidebar.selectbox("ページを選んでください", ["Home", "Add", "Del"]) 
if page == "Home":
  st.title("社員情報一覧表です")
  st.write(pd.DataFrame(show.show_list(employee_data)) if list(employee_data.keys()) else "データがありません")
elif page == "Add":
  st.title("社員情報を追加します")
  placeholder = st.empty()
  info = create_dict()
  name = st.text_input("name")
  number = st.text_input("id ",value=0)
  attendance = ""
  button = st.button("追加")
  if button:
    a = employee(number,attendance)
    info[name] = asdict(a)
    new_items = dict(employee_data,**info)  
    with open("info.json","w") as f:
      json.dump(new_items,f,indent=1)
    placeholder.write("追加しました")
    time.sleep(0.5)
    placeholder.write("")
elif page == "Del":
  st.title("データを消去します")
  placeholder = st.empty()
  name = st.selectbox("商品選択",[key for key in list(employee_data.keys())])
  button = st.button('消去')
  if button:
    del employee_data[name]
    placeholder.write("消去しました")
    time.sleep(0.5)
    placeholder.write("")
    with open("info.json","w") as f:
      json.dump(employee_data,f,indent=1)