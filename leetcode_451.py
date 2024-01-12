class Solution:
    def frequencySort(self, s: str) -> str:
        st = ""
        lst = []
        for i in s:
            if not i in st:
                st+=i
                lst.append(i*s.count(i))
        lst = sorted(lst, key = lambda x: len(x), reverse=True)
        
        return "".join(lst)