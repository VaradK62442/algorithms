from trie import Trie


class LZWCompression:
    def __init__(self, alphabet: list[str]):
        self.alphabet = alphabet
        
        self.k = self._get_num_bits()


    def _get_num_bits(self):
        k = 0
        while 2 ** k < len(self.alphabet):
            k += 1
        return k
    
    def _initialise_dictionary(self) -> Trie:
        dictionary = Trie()
        for i, char in enumerate(self.alphabet):
            dictionary.insert(char, str(i))

        self.dict = dictionary.getSize()
        
        return dictionary

    def _int_to_codeword(self, codeword: str, k: int) -> str:
        return str(bin(int(codeword)))[2:].zfill(k)
    
    def _longest_string_in_dictionary(self, text: str, i: int) -> str:
        s = text[i]
        j = i + 1
        while j < len(text):
            if self.dictionary.search(s + text[j]) is not None: s += text[j]
            else: break
            j += 1
        return s
    
    
    def compress(self, text: str) -> str:
        res = ''
        k = self.k
        i = 0

        self.dictionary = self._initialise_dictionary()
        
        while i < len(text):
            # identify longest string s, starting at position i of text
            # that is in the dictionary
            s = self._longest_string_in_dictionary(text, i)

            # output the codeword for s
            codeword = self.dictionary.search(s)
            res += self._int_to_codeword(codeword, k)

            # move to next position in text
            i += len(s)

            # add s + c to the dictionary
            if self.dictionary.getSize() == 2 ** k: k += 1
            if i < len(text): 
                self.dictionary.insert(s + text[i], str(self.dictionary.getSize()))

        return res


    def decompress(self, text: str) -> str:
        res = ''
        k = self.k
        i = self.k

        self.dictionary = self._initialise_dictionary()
        
        # read first codeword
        s = self.dictionary.look_up(text[:k])
        res += s

        while i < len(text):
            if self.dictionary.getSize() == 2 ** k: k += 1
            old_s = s

            x = text[i:i+k]
            s = self.dictionary.look_up(x)

            # handle special case
            if s is False: s = old_s + old_s[0]

            new_s = old_s + s[0]
            self.dictionary.insert(new_s, str(self.dictionary.getSize()))

            res += s
            i += k

        return res