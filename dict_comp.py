# dictionary comprehensive
# square ={1:2,2:4,3:9}

square={num:num**2 for num in range(1,11)}
print(square)

square1={f"Square of {num} is ":num**2 for num in range(1,11)}
for k,v in square1.items():
    print(f"{k} : {v}")

string="Ankita"
# for i in string:
#     print(i)
word_count={char:string.count(char) for char in string}
print(word_count)
