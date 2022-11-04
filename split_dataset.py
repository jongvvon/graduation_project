
import os
import numpy as np
from tqdm import tqdm

# train_data_path = "./dataset/train_input_img"

"""
전처리가 완료된 이미지가 포함된 디렉토리를 매개변수로 받아 train_size를 기준으로
train set과 validation set로 분할한 .txt 파일을 반환합니다.
"""

def split_dataset(train_data_path, train_size=0.85, random_state=1004):
    data_list = os.listdir(train_data_path)
    data_len = len(data_list)
    
    train_len = int(data_len * train_size)
    validation_len = data_len - train_len

    np.random.seed(random_state)
    shuffled = np.random.permutation(data_len)


    train_txt_path = "./dataset/train.txt"
    validation_txt_path = "./dataset/validation.txt"

    f = open(train_txt_path, 'w')
    print("\n >>> Currently spliting training set.")
    for idx in tqdm(shuffled[:train_len]):
        img_id = data_list[idx].split("_")[2]
        img_input = data_list[idx]
        label_img = data_list[idx][:6] + "label" + data_list[idx][11:]
        
        train_line = "%s, %s, %s \n" % (img_id, img_input, label_img)
        f.write(train_line)
    f.close()

    f = open(validation_txt_path, 'w')
    print("\n >>> Currently spliting validation set.")
    for idx in tqdm(shuffled[train_len:]):
        img_id = data_list[idx].split("_")[2]
        img_input = data_list[idx]
        label_img = data_list[idx][:6] + "label" + data_list[idx][11:]
        
        train_line = "%s, %s, %s \n" % (img_id, img_input, label_img)
        f.write(train_line)
    f.close()

    print("\n Completely split all dataset.")

split_dataset(train_data_path)