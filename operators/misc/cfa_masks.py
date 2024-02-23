"""A file containing all the CFA masks and related functions.
"""

import numpy as np

from .spectral_responses.get_spectral_responses import get_filter_response


def get_rgbp_bands(file_name: str) -> tuple:
    """Returns the positions of the red, green, blue and panchromatic bands in a specific filter set.

    Args:
        file_name (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        tuple: Tuple indicating the position of the RGBW filters.
    """
    if file_name == 'dirac':
        return 'red', 'green', 'blue', 'pan'

    elif file_name == 'WV34bands_Spectral_Responses.npz':
        return 2, 1, 0, 4


def get_bayer_GRBG_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Bayer GRBG CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Bayer GRBG mask.
    """
    band_r, band_g, band_b, _ = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), green_filter)

    cfa_mask[::2, 1::2] = red_filter
    cfa_mask[1::2, ::2] = blue_filter

    return cfa_mask


def get_bayer_RGGB_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Bayer RGGB CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Bayer RGGB mask.
    """
    band_r, band_g, band_b, _ = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), green_filter)

    cfa_mask[::2, ::2] = red_filter
    cfa_mask[1::2, 1::2] = blue_filter

    return cfa_mask


def get_quad_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Quad-Bayer CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Quad-Bayer mask.
    """
    band_r, band_g, band_b, _ = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), green_filter)

    cfa_mask[::4, 2::4] = red_filter
    cfa_mask[::4, 3::4] = red_filter
    cfa_mask[1::4, 2::4] = red_filter
    cfa_mask[1::4, 3::4] = red_filter

    cfa_mask[2::4, ::4] = blue_filter
    cfa_mask[2::4, 1::4] = blue_filter
    cfa_mask[3::4, ::4] = blue_filter
    cfa_mask[3::4, 1::4] = blue_filter

    return cfa_mask


def get_sparse_3_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Sparse3 CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Sparse3 mask.
    """
    band_r, band_g, band_b, band_p = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)
    pan_filter = get_filter_response(spectral_stencil, responses_file, band_p)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), pan_filter)

    cfa_mask[::8, ::8] = red_filter

    cfa_mask[::8, 4::8] = green_filter
    cfa_mask[4::8, ::8] = green_filter

    cfa_mask[4::8, 4::8] = blue_filter

    return cfa_mask


def get_kodak_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Kodak CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Kodak mask.
    """
    band_r, band_g, band_b, band_p = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)
    pan_filter = get_filter_response(spectral_stencil, responses_file, band_p)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), pan_filter)

    cfa_mask[3::4, 2::4] = red_filter
    cfa_mask[2::4, 3::4] = red_filter

    cfa_mask[3::4, ::4] = green_filter
    cfa_mask[2::4, 1::4] = green_filter
    cfa_mask[1::4, 2::4] = green_filter
    cfa_mask[::4, 3::4] = green_filter

    cfa_mask[1::4, ::4] = blue_filter
    cfa_mask[::4, 1::4] = blue_filter

    return cfa_mask


def get_sony_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Sony CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Sony mask.
    """
    band_r, band_g, band_b, band_p = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)
    pan_filter = get_filter_response(spectral_stencil, responses_file, band_p)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), pan_filter)

    cfa_mask[2::4, 3::4] = red_filter
    cfa_mask[::4, 1::4] = red_filter

    cfa_mask[3::4, ::4] = green_filter
    cfa_mask[2::4, 1::4] = green_filter
    cfa_mask[1::4, 2::4] = green_filter
    cfa_mask[::4, 3::4] = green_filter

    cfa_mask[3::4, 2::4] = blue_filter
    cfa_mask[1::4, ::4] = blue_filter

    return cfa_mask


def get_chakrabarti_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Chakrabarti CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Chakrabarti mask.
    """
    band_r, band_g, band_b, band_p = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)
    pan_filter = get_filter_response(spectral_stencil, responses_file, band_p)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), pan_filter)

    cfa_mask[2::6, 3::6] = red_filter
    cfa_mask[2::6, 2::6] = green_filter
    cfa_mask[3::6, 3::6] = green_filter
    cfa_mask[3::6, 2::6] = blue_filter

    return cfa_mask


def get_honda_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Honda CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Honda mask.
    """
    band_r, band_g, band_b, band_p = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)
    pan_filter = get_filter_response(spectral_stencil, responses_file, band_p)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), pan_filter)

    cfa_mask[1::4, 3::4] = red_filter

    cfa_mask[1::4, 1::4] = green_filter
    cfa_mask[3::4, 3::4] = green_filter

    cfa_mask[3::4, 1::4] = blue_filter

    return cfa_mask


def get_kaizu_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Kaizu CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Kaizu mask.
    """
    band_r, band_g, band_b, band_p = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)
    pan_filter = get_filter_response(spectral_stencil, responses_file, band_p)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), pan_filter)

    cfa_mask[::6, 0::6] = red_filter
    cfa_mask[1::6, 1::6] = red_filter
    cfa_mask[4::6, 2::6] = red_filter
    cfa_mask[5::6, 3::6] = red_filter
    cfa_mask[2::6, 4::6] = red_filter
    cfa_mask[3::6, 5::6] = red_filter

    cfa_mask[::6, 2::6] = green_filter
    cfa_mask[1::6, 3::6] = green_filter
    cfa_mask[2::6, ::6] = green_filter
    cfa_mask[3::6, 1::6] = green_filter
    cfa_mask[4::6, 4::6] = green_filter
    cfa_mask[5::6, 5::6] = green_filter

    cfa_mask[4::6, ::6] = blue_filter
    cfa_mask[5::6, 1::6] = blue_filter
    cfa_mask[2::6, 2::6] = blue_filter
    cfa_mask[3::6, 3::6] = blue_filter
    cfa_mask[::6, 4::6] = blue_filter
    cfa_mask[1::6, 5::6] = blue_filter

    return cfa_mask


def get_yamagami_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Yamagami CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Yamagami mask.
    """
    band_r, band_g, band_b, band_p = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)
    pan_filter = get_filter_response(spectral_stencil, responses_file, band_p)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), pan_filter)

    cfa_mask[::4, 2::4] = red_filter
    cfa_mask[2::4, ::4] = red_filter

    cfa_mask[1::4, 1::4] = green_filter
    cfa_mask[1::4, 3::4] = green_filter
    cfa_mask[3::4, 1::4] = green_filter
    cfa_mask[3::4, 3::4] = green_filter

    cfa_mask[::4, ::4] = blue_filter
    cfa_mask[2::4, 2::4] = blue_filter

    return cfa_mask


def get_gindele_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Gindele CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Gindele mask.
    """
    band_r, band_g, band_b, band_p = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)
    pan_filter = get_filter_response(spectral_stencil, responses_file, band_p)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), green_filter)

    cfa_mask[::2, 1::2] = red_filter
    cfa_mask[1::2, ::2] = blue_filter
    cfa_mask[1::2, 1::2] = pan_filter

    return cfa_mask


def get_hamilton_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Hamilton CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Hamilton mask.
    """
    band_r, band_g, band_b, band_p = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)
    pan_filter = get_filter_response(spectral_stencil, responses_file, band_p)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), pan_filter)

    cfa_mask[::8, ::8] = red_filter
    cfa_mask[1::8, 1::8] = red_filter
    cfa_mask[2::8, 2::8] = red_filter
    cfa_mask[3::8, 3::8] = red_filter
    cfa_mask[2::8, ::8] = red_filter
    cfa_mask[3::8, 1::8] = red_filter
    cfa_mask[::8, 2::8] = red_filter
    cfa_mask[1::8, 3::8] = red_filter

    cfa_mask[::8, 4::8] = green_filter
    cfa_mask[::8, 6::8] = green_filter
    cfa_mask[1::8, 5::8] = green_filter
    cfa_mask[1::8, 7::8] = green_filter
    cfa_mask[2::8, 4::8] = green_filter
    cfa_mask[2::8, 6::8] = green_filter
    cfa_mask[3::8, 5::8] = green_filter
    cfa_mask[3::8, 7::8] = green_filter

    cfa_mask[4::8, ::8] = green_filter
    cfa_mask[6::8, ::8] = green_filter
    cfa_mask[5::8, 1::8] = green_filter
    cfa_mask[7::8, 1::8] = green_filter
    cfa_mask[4::8, 2::8] = green_filter
    cfa_mask[6::8, 2::8] = green_filter
    cfa_mask[5::8, 3::8] = green_filter
    cfa_mask[7::8, 3::8] = green_filter

    cfa_mask[4::8, 4::8] = blue_filter
    cfa_mask[5::8, 5::8] = blue_filter
    cfa_mask[6::8, 6::8] = blue_filter
    cfa_mask[7::8, 7::8] = blue_filter
    cfa_mask[6::8, 4::8] = blue_filter
    cfa_mask[7::8, 5::8] = blue_filter
    cfa_mask[4::8, 6::8] = blue_filter
    cfa_mask[5::8, 7::8] = blue_filter

    return cfa_mask


def get_luo_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Luo CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Luo mask.
    """
    band_r, band_g, band_b, band_p = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)
    pan_filter = get_filter_response(spectral_stencil, responses_file, band_p)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), pan_filter)

    cfa_mask[1::4, ::4] = red_filter
    cfa_mask[1::4, 2::4] = red_filter

    cfa_mask[::4, 1::4] = green_filter
    cfa_mask[2::4, 1::4] = green_filter

    cfa_mask[1::4, 1::4] = blue_filter

    return cfa_mask


def get_wang_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Wang CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Wang mask.
    """
    band_r, band_g, band_b, band_p = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)
    pan_filter = get_filter_response(spectral_stencil, responses_file, band_p)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), pan_filter)

    cfa_mask[2::5, ::5] = red_filter
    cfa_mask[::5, 1::5] = red_filter
    cfa_mask[1::5, 3::5] = red_filter
    cfa_mask[3::5, 2::5] = red_filter
    cfa_mask[4::5, 4::5] = red_filter

    cfa_mask[3::5, ::5] = green_filter
    cfa_mask[1::5, 1::5] = green_filter
    cfa_mask[4::5, 2::5] = green_filter
    cfa_mask[2::5, 3::5] = green_filter
    cfa_mask[::5, 4::5] = green_filter

    cfa_mask[4::5, ::5] = blue_filter
    cfa_mask[2::5, 1::5] = blue_filter
    cfa_mask[::5, 2::5] = blue_filter
    cfa_mask[3::5, 3::5] = blue_filter
    cfa_mask[1::5, 4::5] = blue_filter

    return cfa_mask


def get_yamanaka_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Yamanaka CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Yamanaka mask.
    """
    band_r, band_g, band_b, _ = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), green_filter)

    cfa_mask[::2, 1::4] = red_filter
    cfa_mask[1::2, 3::4] = red_filter

    cfa_mask[1::2, 1::4] = blue_filter
    cfa_mask[::2, 3::4] = blue_filter

    return cfa_mask


def get_lukak_mask(input_shape: tuple, spectral_stencil: np.ndarray, responses_file: str) -> np.ndarray:
    """Gives the Lukak CFA mask using the specified filters.

    Args:
        input_shape (tuple): The shape of the input. Will also be the shape of the mask.
        spectral_stencil (np.ndarray): Wavelength values in nanometers at which the input is sampled.
        responses_file (str): The name of the file in which the filters are. If 'dirac' then abstract dirac filters are used.

    Returns:
        np.ndarray: The Lukak mask.
    """
    band_r, band_g, band_b, _ = get_rgbp_bands(responses_file)

    red_filter = get_filter_response(spectral_stencil, responses_file, band_r)
    green_filter = get_filter_response(spectral_stencil, responses_file, band_g)
    blue_filter = get_filter_response(spectral_stencil, responses_file, band_b)

    cfa_mask = np.kron(np.ones((input_shape[0], input_shape[1], 1)), green_filter)

    cfa_mask[::4, 1::2] = red_filter
    cfa_mask[2::4, ::2] = red_filter

    cfa_mask[1::4, 1::2] = blue_filter
    cfa_mask[3::4, ::2] = blue_filter

    return cfa_mask
