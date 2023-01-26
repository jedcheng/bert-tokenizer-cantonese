from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('vocab-bart-base-cantonese.txt')
tokenizer.push_to_hub('jed351/gpt2-tiny-zh-hk')
