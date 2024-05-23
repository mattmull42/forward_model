import numpy as np
import matplotlib.pyplot as plt

from cfa_operator import cfa_operator


def main():
    x = np.empty((10, 15, 3))

    CFAS = sorted(['bayer_GRBG', 'quad_bayer', 'gindele', 'chakrabarti', 'hamilton', 'honda', 'kaizu', 'kodak', 'sony', 'sparse_3', 'wang', 'yamagami', 'yamanaka', 'bayer_RGGB', 'lukac', 'xtrans', 'luo', 'binning', 'honda2', 'random'])

    for cfa in CFAS:
        op = cfa_operator(cfa, x.shape)

        plt.imshow(op.pattern)
        plt.title(f'{cfa}, {op.pattern.shape}')
        plt.show()


if __name__ == '__main__':
    main()
