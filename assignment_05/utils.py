import math

def f(x, y, w1, w2):
    return math.sin(math.sqrt((w1*x)**2 + (w2*y)**2 + (w1*w2*x*y)**2))

def analytical_grad_wrt_w1(x, y, w1, w2):
    m = math.sqrt((w1*x)**2 + (w2*y)**2 + (w1 * w2 * x * y)**2)
    return w1 * math.cos(m)/m * (x**2 + (w2 * x * y)**2)

def analytical_grad_wrt_w2(x, y, w1, w2):
    m = math.sqrt((w1*x)**2 + (w2*y)**2 + (w1 * w2 * x * y)**2)
    return w2 * math.cos(m)/m * (y**2 + (w1 * x * y)**2)