def process_csr_format_file(filename):
    """
    对存储在 csr.txt 文件中的 CSR 格式数据进行处理，要求在 col_ind 中，比前一个数大的数都保存为其相对于前一个数据的偏移量。
    """
    stop_point = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
        num_nodes = int(lines[0].strip().split()[0])
        num_edges = int(lines[0].strip().split()[1])
        row_ptr = list(map(int, lines[1].split()))
        col_ind = list(map(int, lines[2].split()))

        processed_row_ptr = []
        processed_col_ind = []
        processed_row_ptr.append(0)
        for i in range(len(row_ptr) - 2):
            if row_ptr[i+1] - row_ptr[i] > 1 :
                processed_row_ptr.append(row_ptr[i+1])
                stop_point += 1

        print(processed_row_ptr[stop_point])

        '''
        t = row_ptr[-1]
        for i in range(len(row_ptr) - 2, -1, -1):
            # print(i)
            if t == row_ptr[i]:
                # del lists[i]
                row_ptr.remove(row_ptr[i])
            else:
                t = row_ptr[i]
        '''

        # 遍历列表，进行预处理
        for i in range(processed_row_ptr[stop_point]):
            if i == 0:
                processed_col_ind.append(col_ind[i])
            else:
                if col_ind[i] > col_ind[i - 1]:
                    processed_col_ind.append(col_ind[i] - col_ind[i - 1])
                else:
                    processed_col_ind.append(col_ind[i])
                    #processed_col_ind.append(-1)

    '''
    binary_row = []
    binary_col = []
    for i in processed_row_ptr:
        temp = '{:016b}'.format(i)
        binary_row.append(temp)
    for j in processed_col_ind:
        current = '{:016b}'.format(j)
        binary_col.append(current)
    with open('wikilens/wikilens_dcsr_row_b.txt', 'w') as f:
        f.write(",".join(map(str, binary_row)))
    with open('wikilens/wikilens_dcsr_col_b.txt', 'w') as f:
        f.write(",".join(map(str, binary_col)))
    '''
    # 将更新后的 D-CSR 格式数据写入文件
    with open('trip/trip_dcsr.txt', 'w') as f:

        f.write(f"num_nodes={num_nodes}\n")
        f.write(f"num_edges={num_edges}\n")
        f.write("row_ptr=")

        f.write(" ".join(map(str, processed_row_ptr)))
        f.write("\n")

        f.write("col_ind=")

        f.write(" ".join(map(str, processed_col_ind)))
        f.write("\n")


# 处理 CSR 格式文件
filename = 'trip/trip_csr.txt'
process_csr_format_file(filename)

