from LZ77 import LZ77Factory


def main():
    data = "жили были два хороших друга Биба и Боба"

    # LZ77
    lz77_compressor = LZ77Factory.create_compressor()
    lz77_compressed = lz77_compressor.compress(data)
    print("LZ77 сжатые данные:", lz77_compressed)

    lz77_decompressor = LZ77Factory.create_decompressor()
    lz77_decompressed = lz77_decompressor.decompress(lz77_compressed)
    print("LZ77 декодированные данные:", lz77_decompressed)

    compressed_sequence = [
        (0, 0, 'б'), (0, 0, 'и'), (2, 1, 'а'), (4, 1, 'о'), (4, 2, 'с'),
        (0, 0, 'т'), (9, 1, 'ч'), (0, 0, 'н'), (0, 0, 'ы'), (0, 0, 'й'),
        (12, 5, 'б'), (20, 3, 'с'), (16, 6, '')
    ]

    result = lz77_decompressor.decompress(compressed_sequence)
    print("Декодированная строка:", result)


if __name__ == "__main__":
    main()
