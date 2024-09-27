"""
1. ** Data Smoothing **: Apply a moving average to smooth the data.
2. ** Hadamard transformation **: Compress the smoothed data.
3. ** Delta Encoding **: Store differences between successive Hadamard coefficients.
4. ** Quantization **: Reduce the precision of the coefficients.
5. ** Entropy Encoding **: Use Huffman coding or similar techniques for further compression.
"""

# 1. Data Smoothing

import numpy as np
import pandas as pd
from scipy.linalg import hadamard
from scipy.ndimage import uniform_filter1d

df = pd.read_csv('nolableAccDataLabeled_Tag5_Cow733_2021-03-05.csv', header=None)

timestamp = df[0]

x_data = df[1]
y_data = df[2]
z_data = df[3]


# Function to smooth data using a moving average
def smooth_data(data, window_size):
    return uniform_filter1d(data, size=window_size)


# Define parameters
window_size = 10

# Smooth the data
smoothed_x = smooth_data(x_data, window_size)
smoothed_y = smooth_data(y_data, window_size)
smoothed_z = smooth_data(z_data, window_size)


# 2. Hadamard Transformation


# Function to apply Hadamard transformation
def apply_hadamard(data, num_coefficients):
    # Ensure the data length is a power of 2 for Hadamard transformation
    length = 2 ** int(np.ceil(np.log2(len(data))))
    padded_data = np.pad(data, (0, length - len(data)), 'constant')
    hadamard_matrix = hadamard(length)
    transformed_data = hadamard_matrix @ padded_data
    return transformed_data[:num_coefficients]


# Define number of coefficients to keep
num_coefficients = 16  # Adjusted to fit the target size

# Apply Hadamard transformation to each axis
hadamard_x = apply_hadamard(smoothed_x, num_coefficients)
hadamard_y = apply_hadamard(smoothed_y, num_coefficients)
hadamard_z = apply_hadamard(smoothed_z, num_coefficients)


# 3. Delta Encoding
# Function to apply delta encoding
def delta_encode(data):
    return np.diff(data, prepend=0)


# Apply delta encoding
delta_x = delta_encode(hadamard_x)
delta_y = delta_encode(hadamard_y)
delta_z = delta_encode(hadamard_z)


# 4. Quantization
# Function to quantize data
def quantize(data, num_bits):
    quantized_data = np.round(data * (2 ** (num_bits - 1))).astype(int)
    return quantized_data


# Define number of bits for quantization
num_bits = 4  # Reduced to fit the target size

# Apply quantization
quantized_x = quantize(delta_x, num_bits)
quantized_y = quantize(delta_y, num_bits)
quantized_z = quantize(delta_z, num_bits)

# 5. Entropy Encoding (Huffman Coding)

import heapq
from collections import defaultdict


# Function to build Huffman tree and generate codes
def huffman_encoding(data):
    frequency = defaultdict(int)
    for value in data:
        frequency[value] += 1

    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    huffman_code = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    return {symbol: code for symbol, code in huffman_code}


# Apply Huffman encoding
def encode_data(data, huffman_code):
    return "".join(huffman_code[value] for value in data)


# Generate Huffman codes for quantized data
huffman_code_x = huffman_encoding(quantized_x)
huffman_code_y = huffman_encoding(quantized_y)
huffman_code_z = huffman_encoding(quantized_z)

# Encode data using Huffman codes
encoded_x = encode_data(quantized_x, huffman_code_x)
encoded_y = encode_data(quantized_y, huffman_code_y)
encoded_z = encode_data(quantized_z, huffman_code_z)

# Calculate the total size of the encoded data
total_size_bits = len(encoded_x) + len(encoded_y) + len(encoded_z)
total_size_bytes = total_size_bits / 8

print(f"Total data size: {total_size_bytes} bytes")
