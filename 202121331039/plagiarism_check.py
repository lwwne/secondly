import sys

def calc_similarity(original_file, plagiarized_file):
    with open(original_file, 'r', encoding='utf-8') as f1, open(plagiarized_file, 'r', encoding='utf-8') as f2:
        original_text = f1.read()
        plagiarized_text = f2.read()

    # 去除标点符号和空白字符
    original_text = ''.join(e for e in original_text if e.isalnum())
    plagiarized_text = ''.join(e for e in plagiarized_text if e.isalnum())

    # 计算重复率
    if len(original_text) == 0 or len(plagiarized_text) == 0:
        similarity = 0.0
    else:
        same_count = 0  # 相同字数计数
        for c in plagiarized_text:
            if c in original_text:
                same_count += 1
        similarity = same_count / len(original_text) * 100

    return similarity

if __name__ == '__main__':
    # 获取命令行参数
    original_file = sys.argv[1]
    plagiarized_file = sys.argv[2]
    output_file = sys.argv[3]

    # 计算重复率
    similarity = calc_similarity(original_file, plagiarized_file)

    # 写入答案文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('%.2f' % similarity)
        f.write('\n')  # 添加换行符

    print('重复率已写入文件：', output_file)
