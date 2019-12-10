import os, json
import pandas as pd
import matplotlib.pyplot as plt


def twoFreqItem(allTypes):
    ret = list()
    for i in range(len(allTypes)):
        for j in range(i + 1, len(allTypes)):
            t = "{0},{1}".format(allTypes[i], allTypes[j])
            ret.append(t)
    return ret

def threeFreqItem(allTypes):
    ret = list()
    for i in range(len(allTypes)):
        for j in range(i + 1, len(allTypes)):
            for k in range(j + 1, len(allTypes)):
                t = "{0},{1},{2}".format(allTypes[i], allTypes[j], allTypes[k])
                ret.append(t)
    return ret


def visualize(base):
    oneTypeCount = dict()
    twoTypes = dict()
    threeTypes = dict()
    for file in os.listdir(base):
        try:
            df = pd.read_json(base + '/' + file, typ='series', dtype=object)
            for column in df['columns']:
                allTypes = []
                for type in column['data_types']:
                    if type['type'] not in oneTypeCount:
                        oneTypeCount.setdefault(type['type'], 0)
                    oneTypeCount[type['type']] += 1
                    allTypes.append(type['type'])

                allTypes.sort()
                if len(allTypes) >= 2:
                    twoFreq = twoFreqItem(allTypes)
                    for pair in twoFreq:
                        if pair not in twoTypes:
                            twoTypes.setdefault(pair, 0)
                        twoTypes[pair] += 1
                if len(allTypes) >= 3:
                    threeFreq = threeFreqItem(allTypes)
                    for tup in threeFreq:
                        if tup not in threeTypes:
                            threeTypes.setdefault(tup, 0)
                        threeTypes[tup] += 1
        except:
            pass

    # print(oneTypeCount)
    # x1 = oneTypeCount.keys()
    # y1 = oneTypeCount.values()
    # plt.bar(x1, y1, width=0.3)
    # plt.title("Count per type")
    # plt.savefig("onetype.png")
    #
    print(twoTypes)
    x2 = twoTypes.keys()
    y2 = twoTypes.values()
    plt.bar(x2, y2)
    plt.xticks(rotation=270)
    plt.title("Count per two types")
    plt.savefig("twotype.png")
    #plt.show()

    # print(threeTypes)
    # x3 = threeTypes.keys()
    # y3 = threeTypes.values()
    # plt.bar(x3, y3)
    # plt.xticks(rotation=270)
    # plt.title("Count per three types")
    # plt.savefig("threetype.png")
    # plt.show()



if __name__ == '__main__':
    base = "../T1data"
    visualize(base)
