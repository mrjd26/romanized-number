


class Solution:
    def intoRoman(self, num: int) -> str:
      romanized = ""
      hundreds = {
          000: "",
          100: "C",
          200: "CC",
          300: "CCC",
          400: "CD",
          500: "D",
          600: "DC",
          700: "DCC",
          800: "DCCC",
          900: "CM"
          }
      tens = {
           00: "",
           10: "X",
           20: "XX",
           30: "XXX",
           40: "XL",
           50: "L",
           60: "LX",
           70: "LXX",
           80: "LXXX",
           90: "XC"
      }
      ones = {
           0: "",
           1: "I",
           2: "II",
           3: "III",
           4: "IV",
           5: "V",
           6: "VI",
           7: "VII",
           8: "VIII",
           9: "IX"
           }

      #make digits into array
      def get_pos_nums(num):
        pos_nums = []
        while num != 0:
          pos_nums.append(num % 10)
          num = num // 10
        return pos_nums

      num_array = get_pos_nums(num)

      #check if thousands digit
      if len(num_array) == 4:
        i = 0
        while i < num_array[3]:
            romanized += "M"
            i+=1

      #handle hundreds digit
      if len(num_array) >= 3:
          romanized += hundreds.get(num_array[2] * 100)
      #tens digit
      if len(num_array) >= 2:    
          romanized += tens.get(num_array[1] * 10)
      #ones
      romanized += ones.get(num_array[0])
      
      print(romanized)

while True:
    num = input("enter a number:")
    num = int(num)
    s = Solution()
    s.intoRoman(num)
