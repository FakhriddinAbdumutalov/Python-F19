import threading
from collections import Counter

def count_words(lines, counter):
    local_counter = Counter()
    for line in lines:
        for word in line.strip().split():
            local_counter[word.lower()] += 1
    counter.update(local_counter)

def threaded_word_count(file_path, num_threads=4):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    chunk_size = len(lines) // num_threads
    counters = [Counter() for _ in range(num_threads)]
    threads = []

    for i in range(num_threads):
        start = i * chunk_size
        # Last thread takes remaining lines
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        t = threading.Thread(target=count_words, args=(lines[start:end], counters[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_counter = Counter()
    for c in counters:
        total_counter += c

    return total_counter

if __name__ == "__main__":
    file_path = "your_large_file.txt"  # Replace with your file path
    counts = threaded_word_count(file_path, num_threads=4)

    for word, count in counts.most_common(10):
        print(f"{word}: {count}")