colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green', 'green', 'green']


motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]

sensor_right = 0.7

p_move = 0.8


def show(p):
    for i in range(len(p)):
        print p[i]


def calculate():

    #DO NOT USE IMPORT
    #ENTER CODE BELOW HERE
    #ANY CODE ABOVE WILL CAUSE
    #HOMEWORK TO BE GRADED
    #INCORRECT
  
    sensor_wrong = 1.0 - sensor_right
    p_stay = 1.0 - p_move
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for col in range(len(colors[0]))] for row in range(len(colors))]


    def sense(p, colors, measurement):
        aux = [[0.0 for col in range(len(p[0]))] for row in range(len(p))]

        s = 0.0
        for row in range(len(p)):
            for col in range(len(p[row])):
                hit = (measurement == colors[row][col])
                aux[row][col] = p[row][col] * (hit * sensor_right + (1 - hit) * (sensor_wrong))
                s += aux[row][col]
        for row in range(len(aux)):
            for col in range(len(p[row])):
                aux[row][col] /= s
        return aux


    def move(p, motion):
        aux = [[0.0 for col in range(len(p[0]))] for row in range(len(p))]

        for row in range(len(p)):
            for col in range(len(p[0])):
                aux[row][col] = (p_move * p[(row - motion[0]) % len(p)][(col - motion[1]) % len(p[0])]) + (p_stay * p[row][col])
        return aux

    for i in range(len(measurements)):
        p = move(p, motions[i])
        p = sense(p, colors, measurements[i])

    show(p)

    return p

