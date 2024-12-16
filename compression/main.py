from lzwCompression import LZWCompression

import time


def main():
    text = "primes produce patterns proving properties"

    alphabet = sorted(list(set(text)))
    lzw = LZWCompression(alphabet)

    compression_start = time.time()
    compressed = lzw.compress(text)
    compression_end = time.time()

    decompression_start = time.time()
    decompressed = lzw.decompress(compressed)
    decompression_end = time.time()

    print(f"Original: {text}\n")
    print(f"Compressed: {compressed}")
    print(f"\tCompression time: {compression_end - compression_start:.6f}s")
    print(f"Decompressed: {decompressed}")
    print(f"\tDecompression time: {decompression_end - decompression_start:.6f}s")

    print(f"\nOriginal == Decompressed: {text == decompressed}")


if __name__ == '__main__':
    main()