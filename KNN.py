# coding: utf-8

def calc(x, y):
    sum = 0
    for item in zip(x, y):
        sum += (item[0] - item[1]) * (item[0] - item[1])
    return sum



if __name__ == "__main__":
    # file directory and file name
    dirname = "/Users/zhangjiacheng/Desktop/Knn&Kmeans/knn/"
    test_file_name = "test.txt"
    train_file_name = "train.txt"

    # numerization three classes
    idx = {}
    idx['Iris-setosa'] = 1             # 1 stands for Iris-setosa
    idx['Iris-versicolor'] = 2         # 2 stands for Iris-versicolor
    idx['Iris-virginica'] = 3          # 3 stands for Iris-virginica

    # training
    train_record = []
    with open(dirname + train_file_name, 'r') as train:
        lines = train.readlines()
        for line in lines:
            # column 0 - 3 for attributes, 4 for class
            attributes = [float(x) for x in line.split(",")[0:4]]
            name = line.strip().split(",")[4].strip()
            # list of each case
            attributes.append(idx[name])
            # list of all above lists
            train_record.append(attributes)
        # normalization
        # attr_max = [max([x[i] for x in train_record]) for i in range(4)]
        # attr_min = [min([x[i] for x in train_record]) for i in range(4)]

        # for items in train_record:
        #     for i in range(len(items) - 1):
        #         items[i] = (items[i] - attr_min[i]) / (attr_max[i] - attr_min[i])

    # print attr_max, attr_min
    # print train_record

    # testing
    with open(dirname + test_file_name, 'r') as test:
        for line in test:
            rank = []
            attr = [float(x) for x in line.split(',')[:4]]

            # for i in range(len(attr) - 1):
            #     attr[i] = (attr[i] - attr_min[i]) / (attr_max[i] - attr_min[i])
            # name = idx[line.split(',')[4].strip()]

            for record in train_record:
                # Euclidean Distance
                rank_score = 0
                for i in range(4):
                    rank_score += (attr[i] - record[i]) * (attr[i] - record[i])
                rank.append([rank_score, record[4]])
            # ranking
            rank = sorted(rank, key=lambda score: score[0])
            print rank
            # rank = [(x[4], calc(attr, x[:4])) for x in train_record]
            # rank = sorted(rank, key=lambda x : x[1])
            # print rank