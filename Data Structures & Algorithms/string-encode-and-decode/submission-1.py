class Solution:

    def encode(self, strs: List[str]) -> str:
        #length based encoding
        strings = ""
        for i in strs:
            strings+=str(len(i))+ "#" + i
        return strings 


    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j]!='#':
                j+=1
            
            length = int(s[i:j])

            word_start_index = j+1
            word_end = j+1+length

            word=s[word_start_index:word_end]
            res.append(word)

            i=word_end

        return res 

        
                

        
        
