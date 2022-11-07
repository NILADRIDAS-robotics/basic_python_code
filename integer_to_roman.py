class py_solution:
  def convert_roman(self,num):
      val=[1,4,5,9,10,40,50,90,100]
      sym=["I","IV","V","IX","X","XL","L","XC"]
    
      roman_num=''
    
      i=0
    
      while num > 0:
        for _ in range(num//val[i]):
            roman_num+=sym[i]
            num -=val[i]
        i+=1
        return roman_num

print(py_solution().convert_roman(5))