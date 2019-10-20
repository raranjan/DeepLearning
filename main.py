import numpy as np

def compute_error(b, m, points):
    pass


def step_gradient(b_current, m_current, points, learning_rate):
    pass


def gradient_descent_runner(points, initial_b, initial_m, num_iterations, learning_rate):
    b = initial_b
    m = initial_m

    for i in range(num_iterations):
        b, m = step_gradient(b, m, np.array(points), learning_rate)

    return [b, m]


def run():
    points = np.genfromtxt('data/data.csv', delimiter=',')
    
    #hyperparameters
    learning_rate=0.0001

    #y = mx + b (slope formula)
    initial_b = 0
    initial_m = 0

    num_iterations = 1000

    [b, m] = gradient_descent_runner(points, initial_b, initial_m, num_iterations, learning_rate)


if __name__ == "__main__":
    run()
