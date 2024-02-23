# This is a sample Python script.

def read_edgelist(filename):
    """
    从edgelist文件中读取图数据，返回节点数、边数和边列表。
    """
    edges = []
    nodes = set()
    with open(filename, 'r') as file:
        for line in file:
            source, target = line.strip().split()
            edges.append((int(source), int(target)))
            nodes.add(int(source))
            nodes.add(int(target))
    num_nodes = max(nodes) + 1
    num_edges = len(edges)
    return num_nodes, num_edges, edges

def write_csr(filename, num_nodes, num_edges, edges):
    """
    将图数据以CSR格式写入文件。
    """
    row_ptr = [0] * (num_nodes + 1)
    col_ind = []
    for edge in edges:
        row_ptr[edge[0] + 1] += 1
        col_ind.append(edge[1])
    for i in range(num_nodes):
        row_ptr[i + 1] += row_ptr[i]

    with open(filename, 'w') as file:
        # 写入节点数和边数
        file.write(f"{num_nodes} {num_edges}\n")
        # 写入row_ptr数组
        file.write(' '.join(map(str, row_ptr)) + '\n')
        # 写入col_ind数组
        file.write(' '.join(map(str, col_ind)) + '\n')

# 读取edgelist文件
filename = 'wang/wang_reordered.txt'
num_nodes, num_edges, edges = read_edgelist(filename)

# 将图数据以CSR格式写入文件
write_csr('wang/wang_csr.txt', num_nodes, num_edges, edges)


