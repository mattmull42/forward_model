"""The file describing the CFA operator.
"""

import numpy as np
from scipy.sparse import csr_array

from .abstract_operator import abstract_operator
from .misc.cfa_masks import *


class cfa_operator(abstract_operator):
    def __init__(self, cfa: str, input_shape: tuple, spectral_stencil: np.ndarray, filters: str, name: str = None) -> None:
        """Creates an instane of the cfa_operator class.

        Args:
            cfa (str): The name of the CFA to be used.
            input_shape (tuple): The shape of the object the operator takes in input.
            spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
            filters (str): The name of the filters to use for the operation.
            name (str, optional): A simple nametag for the operator. Defaults to None.
        """

        self.cfa = cfa
        self.name = 'CFA' if name is None else name

        if self.cfa == 'bayer_VRBV':
            self.cfa_mask = get_bayer_mask(input_shape, spectral_stencil, filters)
        
        elif self.cfa == 'bayer_RVVB':
            self.cfa_mask = get_bayer_bis_mask(input_shape, spectral_stencil, filters)

        elif self.cfa == 'quad_bayer':
            self.cfa_mask = get_quad_mask(input_shape, spectral_stencil, filters)

        elif self.cfa == 'sparse_3':
            self.cfa_mask = get_sparse_3_mask(input_shape, spectral_stencil, filters)

        elif self.cfa == 'kodak':
            self.cfa_mask = get_kodak_mask(input_shape, spectral_stencil, filters)

        elif self.cfa == 'sony':
            self.cfa_mask = get_sony_mask(input_shape, spectral_stencil, filters)

        super().__init__(input_shape, input_shape[:-1], self.name)


    def direct(self, x: np.ndarray) -> np.ndarray:
        """A method method performing the computation of the operator.

        Args:
            x (np.ndarray): The input array. Must be of shape self.input_shape.

        Returns:
            np.ndarray: The output array. Must be of shape self.output_shape.
        """

        return np.sum(x * self.cfa_mask, axis=2)


    def adjoint(self, y: np.ndarray) -> np.ndarray:
        """A method performing the computation of the adjoint of the operator.

        Args:
            y (np.ndarray): The input array. Must be of shape self.output_shape.

        Returns:
            np.ndarray: The output array. Must be of shape self.input_shape.
        """

        return self.cfa_mask * y[..., np.newaxis]


    @property
    def matrix(self) -> csr_array:
        """A method giving the sparse matrix representation of the operator.

        Returns:
            csr_array: The sparse matrix representing the operator.
        """

        N_k = self.input_shape[2]
        N_ij = self.input_shape[0] * self.input_shape[1]
        N_ijk = self.input_shape[0] * self.input_shape[1] * N_k

        cfa_i = np.repeat(np.arange(N_ij), N_k)
        cfa_j = np.arange(N_ijk)

        cfa_data = self.cfa_mask[cfa_i // self.input_shape[1], cfa_i % self.input_shape[1], cfa_j % N_k]

        return csr_array((cfa_data, (cfa_i, cfa_j)), shape=(N_ij, N_ijk))