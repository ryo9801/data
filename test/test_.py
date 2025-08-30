import os
folder_path = '/Users/宮井/Desktop/program/vscode/test'  # フォルダのパス
files =  [f for f in os.listdir(folder_path)]
print(files)
for i in range(len(files)):
  if f"{files[i].split('.')[0]}.json" in files:
    print(files[i].split('.')[0])