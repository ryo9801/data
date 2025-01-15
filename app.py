from dataclasses import dataclass,asdict
import json
import streamlit as st
import os
import time
import pandas as pd
# チェックしたいディレクトリとファイル名
folder_path = '/Users/宮井/Desktop/program/vscode/test'  # フォルダのパス
file_name = 'items.json'       # 調べたいファイル名
# ファイルが存在するか確認
if file_name in os.listdir(folder_path):
    with open("items.json") as f:
      items=json.load(f)

else:
    with open("items.json", "w", encoding="utf-8") as json_file:
      json.dump({},json_file)
      pass  # 何も書き込まずにファイルを閉じる
with open("items.json") as f:
      items=json.load(f)

def create_dict(): 
  dic = {}
  return dic

@dataclass
class info:
  plice : int
  stock : int
  id :str

page = st.sidebar.selectbox("ページを選んでください", ["ホーム", "add", "del", "plice" , "stock"]) 
 
if page == "ホーム":
  st.title("ホームページです")
  data ={"item":[key for key in list(items.keys())],
         "plice":[items[key]["plice"] for key in list(items.keys())],
         "stock":[items[key]["stock"] for key in list(items.keys())],
         "id":[items[key]["id"] for key in list(items.keys())]}
  st.write(pd.DataFrame(data))

elif page == "add":
  st.title("データを追加します")
  placeholder = st.empty()
  item = create_dict()
  name = st.text_input("name",value="")
  plice = st.number_input("plice ",value=0)
  stock = st.number_input("stock",value=0)
  id = st.text_input("id",value="")
  button = st.button("追加")
  if button:
    a = info(plice,stock,id)
    item[name] = asdict(a)
    new_items = dict(items,**item) 
    with open("items.json","w") as f:
        json.dump(new_items,f)
    placeholder.write("追加しました")
    time.sleep(0.5)
    placeholder.write("")

elif page == "del":
  st.title("データを消去します")
  placeholder = st.empty()
  name = st.selectbox("商品選択",[key for key in list(items.keys())])
  button = st.button('消去')
  for key in list(items.keys()):
    if key == name and button:
      del items[name]
      placeholder.write("消去しました")
      time.sleep(0.5)
      placeholder.write("")
    with open("items.json","w") as f:
      json.dump(items,f)
     
elif page == "plice":
    st.title("値段を変えます")
    placeholder = st.empty()
    name = st.selectbox("商品選択",[key for key in list(items.keys())])
    plice = st.number_input("change_plice",value=0)
    button = st.button('変更')
    if plice and name and button:
      items[name]["plice"] = items[name]["plice"] + plice
      with open("items.json","w") as f:
        json.dump(items,f)
      placeholder.write("変更完了")
      time.sleep(0.5)
      placeholder.write("")

elif page == "stock":
    st.title("在庫管理します")
    placeholder = st.empty()
    name = st.selectbox("商品選択",[key for key in list(items.keys())])
    stock = st.number_input("change_stock",value=0)
    button = st.button("変更")
    if stock and name and button:
      items[name]["stock"] = items[name]["stock"] + stock
      with open("items.json","w") as f:
        json.dump(items,f)
      placeholder.write("変更完了")
      time.sleep(0.5)
      placeholder.write("")