import pandas as pd
import numpy as np


# 肥料銘柄数
num_fert = len(sehi_data)

# N, P, K
num_cont = 3 

# numpy配列への代入
F_ij = np.zeros([int(num_fert), int(num_cont)])
C_i = np.zeros([int(num_fert)])
b_i = np.zeros([int(num_cont)])

# F_ijへの代入
for i in range(int(num_fert)):
    C_i[i] = sehi_data.iat[i,4]
    for j in range(int(num_cont)):
        F_ij[i,j] = sehi_data.iat[i,j+1]

#print(sehi_data)
#print(num_fert)
#print(sehi_data.iat[1,1])
#print(F_ij)
#print(C_i)



field_data = pd.read_csv("field.csv")
for i in range(int(num_cont) ):
    b_i[i] = field_data.iat[i,1]
area = field_data.columns
area_val = area[1]
field_data.head()
#print(field_data)
#print(b_i)
#print(area)


# MC粒子数
particle = input("粒子数を指定してください(整数値、1000以上推奨）")
particle = int(particle)
sehi_data = pd.read_csv("sehi.csv")
sehi_data.head()

for i in range(int(num_cont) ):
    b_i[i] = float(area_val) * b_i[i]

# Solver : Monte-Carlo method
# range:
x_ranges = np.zeros([int(num_fert),2])
for i in range(int(num_fert)):
    # Minimum (kg)
    x_ranges[i,0] = 0.0
    # Maximum (kg) Nを全てi番目の肥料で賄った場合の数量
    v_tr = np.zeros([int(num_cont)])
    for j in range(int(num_cont)):
        if F_ij[i,j]==0:
            v_tr[j] = 0.0
        else:
            v_tr[j] = float(field_data.iat[j,1])*float(area_val)/float(F_ij[i,j])
    x_ranges[i,1] = np.max(v_tr)
    print("探索範囲：肥料 "+str(sehi_data.iat[i,0])+str(x_ranges[i,0])+" ~ "+str(x_ranges[i,1])+" kg")
# trial value をばらまく

for i in range(particle):
    # 試行値生成
    x_i_tr = np.random.rand(int(num_fert) )

    for j in range(int(num_fert) ):
        x_i_tr[j] = x_ranges[j,1]*x_i_tr[j]
    if i ==0:
        # もし最初ならx_i[:]に保存
        x_i = x_i_tr
        cost = np.dot(C_i, x_i)

        # 目標施肥量からの差をdifに計算
        dif=0.0
        Fx = np.zeros([int(num_cont)])
        for k in range(int(num_cont) ):
            for l in range(int(num_fert) ):
                Fx[k] = Fx[k] + F_ij[l,k]* x_i_tr[l]

        for k in range(int(num_cont) ):
            dif = dif + abs( b_i[k] - Fx[k] )
    else:
        # 目標施肥量からの差をdifに計算
        dif_tr=0.0
        Fx = np.zeros([int(num_cont)])
        for k in range(int(num_cont) ):
            for l in range(int(num_fert) ):
                Fx[k] =Fx[k] +  F_ij[l,k]* x_i_tr[l]
        
        for k in range(int(num_cont) ):
            dif_tr = dif_tr + abs( b_i[k] - Fx[k] )
        
        cost_tr = np.dot(C_i, x_i_tr)
        # もし誤差が少なければx_i[]候補
        if dif_tr < dif:
            # もし2回目以降ならコストを比較し、より少なければx_i[]候補
            if cost_tr < cost:
                x_i = x_i_tr
                cost = cost_tr
                dif = dif_tr
            
    print(" ")
    print("Trial : "+str(i)+"/ 金額 = "+str( int(cost))+"円" )
    print("購入量(kg) "+str(x_i_tr) )

    Fx = np.zeros([int(num_cont)])
    for k in range(int(num_cont) ):
        for l in range(int(num_fert) ):
            Fx[k] =Fx[k] + F_ij[l,k]* x_i[l]
    print("成分投入量(kg) "+str(Fx))
    fval = np.zeros(3)
    fval[0] = float(Fx[0])/float(area_val)
    fval[1] = float(Fx[1])/float(area_val)
    fval[2] = float(Fx[2])/float(area_val)

    print("10aあたり目標成分投入量(kg) "+str(b_i/float(area_val)) )
    print("10aあたり予測成分投入量(kg) "+str(fval))
    print("er : "+str(dif))

f = open("result.csv",'w')
f.write("解析結果,\n")
for i in range(int(num_fert) ):
    f.write(str(sehi_data.iat[i,0])+", "+str(x_i[i])+" kg\n")
f.write("\n")
f.write("10aあたり目標成分投入量(kg), "+str(b_i/float(area_val))+"\n" )
f.write("10aあたり予測成分投入量(kg), "+str(fval)+"\n")
f.write("er, "+str(dif)+"\n")
f.write("粒子数,"+str(particle)+"\n" )
f.close()


result = pd.read_csv("result.csv")
print(result)