#input deklarasi database

kelas = ["ali", "budi", "caca", "dinda", "elo", "dzikra", "aurel", "angie"]

print("========================================")

#proses

for i in range (0,len(kelas)):
#output yang berulang 
    print ("nama mahasiswa ke", i+1, "adalah =", kelas[i])

print("========================================")

#output
print(kelas[3])
print(kelas[1])
print(len(kelas))

# #program matrik 3 x 3 

matriksA=[[1,2,3], 
          [4,5,6],
          [7,8,9]]

#output

print(matriksA)

# format matrik ke 2

for x in range (0, len(matriksA)):
    print()
    for y in range(0,len(matriksA[0])):
        print(matriksA[x][y], end="  ")
    print()

print("===============================")

#proses penjumlahan matrik 1 dan matrik 2 

for x in range (0,len(matriksA)):
   #print()
   for y in range(0, len(matriksA[0])):
   #print(HasilJumlah[x][y], end=" ")

    print()


print("===============================")      
#menambah data base
kelas.append("ade")
kelas.append("maria")
kelas.insert(2,"kaka")
kelas.remove("caca")

for i in range (0,len(kelas)):
#output yang berulang 
    print ("nama mahasiswa ke", i+1, "adalah =", kelas[i])

