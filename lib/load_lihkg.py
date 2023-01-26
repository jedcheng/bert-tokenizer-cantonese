from os.path import expanduser
from typing import List

def load_lihkg() -> List[str]:
    filename = expanduser('lihkg-1-2850000-processed-dedup.csv')
    sentences = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            sentences.append(line.rstrip('\n'))
    print(f'INFO: Loaded {len(sentences)} sentences.')
    return sentences
