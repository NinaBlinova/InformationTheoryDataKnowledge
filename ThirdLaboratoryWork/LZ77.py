class LZ77Compressor:
    def __init__(self, window_size=20):
        self.window_size = window_size

    def compress(self, data):
        i = 0
        compressed_data = []
        while i < len(data):
            match = self.find_longest_match(data, i)
            if match:
                (best_offset, best_length) = match
                # Проверяем, не выходит ли i + best_length за пределы строки
                if i + best_length < len(data):
                    next_char = data[i + best_length]
                else:
                    next_char = ''  # Если за пределами, устанавливаем пустой символ
                compressed_data.append((best_offset, best_length, next_char))
                i += best_length + 1
            else:
                compressed_data.append((0, 0, data[i]))
                i += 1
        return compressed_data

    def find_longest_match(self, data, current_position):
        search_start = max(0, current_position - self.window_size)
        longest_match = (0, 0)  # Длина сравнения

        for j in range(search_start, current_position):
            length = 0
            while (length < self.window_size and
                   current_position + length < len(data) and
                   data[j + length] == data[current_position + length]):
                length += 1

            if length > longest_match[1]:
                longest_match = (current_position - j, length)

        return longest_match if longest_match[1] > 0 else None


class LZ77Decompressor:
    @staticmethod
    def decompress(compressed_data):
        decompressed_data = []
        for offset, length, char in compressed_data:
            if offset == 0 and length == 0:
                decompressed_data.append(char)
            else:
                start = len(decompressed_data) - offset
                for i in range(length):
                    decompressed_data.append(decompressed_data[start + i])
                decompressed_data.append(char)
        return ''.join(decompressed_data)


class LZ77Factory:
    @staticmethod
    def create_compressor(window_size=20):
        return LZ77Compressor(window_size)

    @staticmethod
    def create_decompressor():
        return LZ77Decompressor()
