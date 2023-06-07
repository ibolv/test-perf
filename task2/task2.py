import sys

def getData(data):
    f = open(data, 'r')
    dataFile = f.read().split('\n')
    dataArr = []
    for item in dataFile:
        dataArr.append(item.split(' '))
    f.close
    for item in range(len(dataArr)):
        dataArr[item] = [float(x) for x in dataArr[item]]
    return dataArr


def inCircle():
    circleData = getData(sys.argv[1])
    pointsData = getData(sys.argv[2])
    result = ''
    for points in pointsData:
        equation = (points[0] - circleData[0][0])**2 + (points[1] - circleData[0][1])**2
        if equation == circleData[1][0] * circleData[1][0]:
            result = result + '0 '
        if equation < circleData[1][0] * circleData[1][0]:
            result = result + '1 '
        if equation > circleData[1][0] * circleData[1][0]:
            result = result + '2 '

    print(result[:-1])


inCircle()