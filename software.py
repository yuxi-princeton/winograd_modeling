import numpy as np
from base import BaseModel

class Software(BaseModel):
    def __init__(self, input):
        self.A3 = np.array([[1., 1., 1., 0.],
                            [0., 1.,-1.,-1.]])
        self.A3 = self.A3.T
        self.B3 = np.array([[1., 0.,-1., 0.],
                            [0., 1., 1., 0.],
                            [0.,-1., 1., 0.],
                            [0., 1., 0.,-1.]])
        self.B3 = self.B3.T
        self.G3 = np.array([[  1.,   0.,   0.],
                            [1/2., 1/2., 1/2.],
                            [1/2.,-1/2., 1/2.],
                            [  0.,   0.,   1.]])
        self.A2 = np.array([])
        self.B2 = np.array([])
        self.G2 = np.array([])
    def trans():
        pass

    def ele_mul():
        pass

    def inverse_trans():
        pass


if __name__=='__main__':