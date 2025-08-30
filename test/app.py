import json
import streamlit as st
import os
import time
import pandas as pd
from ex import data_c 
from dataclasses import asdict
# チェックしたいディレクトリとファイル名
folder_path = '/Users/宮井/Desktop/program/vscode/test/jsons'  # フォルダのパス
files =  [f for f in os.listdir(folder_path)]
new_files = []
for i in range(len(files)):
  if f"{files[i].split('.')[0]}.json" in files:
    new_files.append(files[i].split('.')[0]) 
def create_dict(): 
  dic = {}
  return dic

page = st.sidebar.selectbox("ページを選んでください", ["Home", "Add", "Del", "create"]) 

if page == "Home":
  st.title("ホームページです")
  radio = st.radio("選択",new_files, horizontal=True)
  with open(f"jsons/{radio}.json") as f:
    data = json.load(f)
  st.write(pd.DataFrame(data) if data.keys() else "データがありません")

elif page == "Add":
  st.title("データを追加します")
  placeholder = st.empty()
  radio = st.radio("選択",new_files, horizontal=True)
  n = int(radio.split("_")[1])
  item = create_dict()
  name = st.text_input("name")
  info = [0 for i in range(n)]
  for i in range(n):
    info[i] = st.text_input(f"{i+1}")
  button = st.button("追加")
  if button:
    with open(f"jsons/{radio}.json") as f:
      data = json.load(f)
    print(info)
    a = data_c.info_2(info[0],info[1])
    item[name] = asdict(a)
    new_items = dict(data,**item)  
    with open(f"jsons/{radio}.json","w") as f:
      json.dump(new_items,f,indent=1)
    placeholder.write("追加しました")
    time.sleep(0.5)
    placeholder.write("")

elif page == "Del":
  st.title("データを消去します")
  placeholder = st.empty()  
  radio = st.radio("選択",new_files, horizontal=True)
  with open(f"{radio}.json") as f:
    name_list = [key for key in list(f.keys())]
  name = st.selectbox("選択",name_list)
  button = st.button('消去')
  if button:
    del radio[name]
    placeholder.write("消去しました")
    time.sleep(0.5)
    placeholder.write("")
    with open(f"jsons/{radio}.json","w") as f:
      json.dump(radio,f,indent=1)
elif page =="create":
  placeholder = st.empty()
  st.title("ファイルを作成")
  file_name = st.text_input("ファイル名")
  data = st.number_input("",value = 0)
  button = st.button("作成")
  if button:
    placeholder.write("作成完了")
    time.sleep(0.5)
    placeholder.write("")
    with open(f"jsons/{file_name}_{data}.json", "w") as f:
      json.dump({},f)