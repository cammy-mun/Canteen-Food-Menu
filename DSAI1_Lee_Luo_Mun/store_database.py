d={}
try:
    with open("C:/Users/User/Desktop/mini_project_done_program/DSAI1_Lee_Luo_Mun/DSAI1_Lee_Luo_Mun/operating_timetextfile.txt") as f1:
        for line in f1:
            (key1,key2,val1,val2,val3)=line.strip().split(",")
            d[(key1,key2)]= (int(val1),int(val2),int(val3))
except FileNotFoundError:
    print("Data containing store info cannot be found")
    sys.exit(1)





