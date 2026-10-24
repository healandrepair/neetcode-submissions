class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dictionary = dict()
        for i in s1:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1


        counter = len(s1)
        j = 0
        for i in range(len(s2)):
            print(counter)
            print(dictionary)
            if (abs(i - j + 1) > len(s1)):
                jVal = s2[j]
                if (jVal in dictionary):
                    dictionary[jVal] += 1
                    if dictionary[jVal] > 0:
                        counter += 1
                    
                j+= 1
            iVal = s2[i]
            if (iVal in dictionary):        
                dictionary[iVal] -= 1
                if dictionary[iVal] >= 0:
                    counter -= 1
            if counter == 0:
                print(f"i:{i} j:{j}")

                print(f"i:{s2[i:j+1]}")
                return True

        return False
            
