import torch
from torch.utils.data import DataLoader


class LM_Dataset(torch.utils.data.Dataset):
    def __init__(self, fname, vocab_fname, max_length):
        with open(fname, 'r') as f:
            self.text = f.read().lower()

        self.word_to_id, self.id_to_word = self.make_mapping(vocab_fname)

        self.tokenized = [['[BOS]'] + seq.split(' ')+['[EOS]'] for seq in self.text.split('\n')]

        self.encoded = [self.encode(seq) for seq in self.tokenized]

        self.X = [torch.tensor(seq[:-1]) for seq in self.encoded]

        self.y = [torch.tensor(seq[1:]) for seq in self.encoded]

        self.max_length = max_length


    def make_mapping(self, vocab_fname):
        with open(vocab_fname, 'r') as f:
            vocab = set(f.read().replace('\n', ''))

        special_tokens = {
            '[PAD]': 0,
            '[BOS]': len(vocab)+1,
            '[EOS]': len(vocab)+2
        }

        word_to_id = {}
        id_to_word = {}

        ## Build word_to_id and id_to_word
        ## Ids for words should start with 1 because [PAD] is 0. 

        return word_to_id, id_to_word

    def encode(self, seq):
        """Encodes sequence of words with IDs
        """
        pass

    def decode(self, seq):
        """Decodes sequence of IDs to words
        """
        pass


    def __getitem__(self, idx):

        x = self.X[idx]
        y = self.y[idx]

        ## Left pad
        padded_x = torch.full((1,self.max_length), self.word_to_id['[PAD]'], dtype=torch.float).flatten()
        padded_x[-x.size(0):] = x

        padded_y = torch.full((1,self.max_length), self.word_to_id['[PAD]']).flatten()
        padded_y[-x.size(0):] = y

        return padded_x,padded_y


    def __len__(self):
        return len(self.X)

def debug():
    ## Use this function to understand how dataloader works
    pass

if __name__ == "__main__":
    debug()