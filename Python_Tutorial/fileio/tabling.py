def fun(n):
    table =""
    for i in range(1,11):
        table+= f"{n}X{i} ={n*i}\n"
        with open(f"tables/table_{n}","w") as d:
                    d.write(table)
             
for i in range(2,6):
    fun(i)