import os
import numpy as np

# 問題データを読み込む関数
def load_XOR(prob_name: str) -> (np.ndarray, np.ndarray):
    data_file = os.path.join(os.path.dirname(__file__), prob_name + ".txt")
    index = 0
    input_size = None
    output_size = None
    input_data = []
    output_data = []
    
    with open(data_file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            elif index == 0:
                input_size = int(line)
            elif index == 1:
                output_size = int(line)
            else:
                data = list(map(float, line.split(" ")))
                assert len(data) == input_size + output_size
                input_data.append(data[:input_size])
                output_data.append(data[input_size:])
            index += 1

        input_data = np.vstack(input_data) # 入力データを行列に変換: (N, input_size)
        output_data = np.vstack(output_data) # 出力データを行列に変換: (N, output_size)

    return (input_data, output_data)