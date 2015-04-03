import matplotlib.pyplot as plt


tissue = [50237.9 , 63793.1 , 68321.8 , 70121.7 , 70895.9 , 71220.8 , 71331.1 , 71357.5 , 71157.8 , 71032.7 , 70886.4 , 70674.4 , 70376.3 , 70131.2 , 69905.6 , 69663.7 , 69260.5 , 69012.4 , 68746.7 , 68353.3 , 68067.2 , 67802.1 , 67496.9 , 67100.7 , 66793.8 , 66483.9 , 66072.3 , 65757.9 , 65480.7 , 65155.1 , 64732.6 , 64409 , 64123.8 , 63660.5 , 63333.8 , 63042.9 , 62713.7 , 62272.7 , 61942.1 , 61644.4 , 61307 , 60836.4 ,60538.2 , 60196.8 , 59763.9 , 59411.9 , 59109.8 , 58762.3 , 58328.9 , 57983.6 , 57636.6 , 57204.2 , 56851.9 , 56542.8 , 56179.9 , 55750.8 , 55392.6 , 55081.9 , 54608 , 54251 , 53934.6 , 53576.7 , 53137.1 , 52776.9 , 52458 , 52094.2 , 51622.4 , 51303.9 , 50936.3 , 50513.1 , 50134.8 , 49814.2 , 49440.8 , 49022.3 , 48651.2 , 48278.6 , 47863.7 , 47486.8 , 47162.1 , 46772.4 , 46361.4 , 45981 , 45655 , 45195.2 , 44813.8 , 44484.5 , 44099.6 , 43683.7 , 43299.8 , 42966.7 , 42578.5 , 42125.2 , 41795.2 , 41401 , 41009.6 , 40603 , 40271 , 39872.1 , 39487.5 , 39092.2 , 38694.1 , 38316.1 , 37913.6 , 37576.9 , 37157.8 , 36788.4 , 36379.8 , 36040.9 , 35611 , 35203 , 34859.6 , 34447.7 , 34077.2 , 33663.9 , 33317.9 , 32899.9 , 32482.7 , 32139 , 31718.1 , 31373.3 , 30937.5 , 30590.7 , 30170.7 , 29822.5 , 29408.3 , 28995.2 , 28645.5 , 28227.1 , 27875.9 , 27441.8 , 27088.5 , 26672.2 , 26316.4 , 25907.3 , 25497.6 , 25135.2 , 24726.5 , 24344.2 , 23937 , 23570 , 23163.5 , 22759.9 , 22396.6 , 21987.4 , 21621.8 , 21192.9 , 20823.4 , 20417.7 , 20045.2 , 19649 , 19254.7 , 18879.4 , 18479.5 , 18101.2 , 17676.8 , 17294.7 , 16898.3 , 16512.6 , 16127.6 , 15740.8 , 15346 , 14958.6 , 14541.1 , 14154.2 , 13758.8 , 13371 , 12986 , 12598.2 , 12200 , 11810.8 , 11403.4 , 11015.4 , 10616 , 10226.7 , 9840.79 , 9454.64 , 9064.04 , 8659.48 , 8267 , 7880.1 , 7487.86 , 7084.77 , 6692.22 , 6304.89 , 5910.46 , 5511.95 , 5116.92 , 4730.43 , 4332.3 , 3942.13 , 3544.01 , 3153.7 , 2756.91 , 2365.92 ,1971.56 , 1577.2 , 1183.13 , 788.663 , 394.353 , 0.0610799]
bone = [9985.91 , 17001.3 , 22063.1 , 25790.3 , 28581.1 , 30701.4 , 32322.4 , 33574.1 , 34546.5 , 35302.9 , 35890.2 , 36343.1 , 36690.3 , 36952.3 , 37143.1 , 37280.2 , 37368.1 , 37419.7 , 37434 , 37427.7 , 37390.3 , 37340 , 37265.2 , 37184.4 , 37087.5 , 36969.5 , 36858.1 , 36723.7 , 36599 ,36446.8 , 36307.2 , 36146.9 , 35997.4 , 35829.2 , 35653.8 , 35499.2 , 35317.4 , 35146.3 , 34961.2 , 34793 , 34600.6 , 34402.1 , 34232.3 , 34031.4 , 33856.2 , 33645 , 33470.7 , 33261.3 , 33081.4 , 32875.1 , 32663.2 , 32484.5 , 32268.7 , 32086 , 31863.5 , 31680.2 , 31461.3 , 31272.8 , 31059.5 , 30840.2 , 30651.9 , 30431.1 , 30235.2 , 30014.2 , 29823.3 , 29601.3 , 29379.6 , 29190 , 28963.6 , 28772.1 , 28539.5 , 28346.6 , 28121.4 , 27927.3 , 27703.2 , 27479 , 27284.6 , 27056.8 , 26860.6 , 26625.8 , 26428.9 , 26201 , 26002.1 , 25778.3 , 25552 , 25351.2 , 25125.5 , 24914.5 , 24688.4 , 24484.7 , 24259.2 , 24034.2 , 23832.9 , 23604.2 , 23402.1 , 23163.2 , 22959.9 , 22731.1 , 22526.6 , 22302.4 , 22077.7 , 21872.7 , 21645 , 21438.1 , 21198.8 , 20991.1 , 20764.3 , 20555 , 20332.7 , 20108.8 , 19895.9 , 19672.8 , 19446.1 , 19222.4 , 19007.2 , 18785 , 18564.4 , 18351.6 , 18126 , 17911.9 , 17673.2 , 17457.1 , 17233.4 , 17015.8 , 16797.9 , 16580.7 , 16361.7 , 16139 , 15919.7 , 15682.4 , 15463.4 , 15240.5 , 15021.3 , 14802.9 , 14583.6 , 14359.2 , 14139.2 , 13904.2 , 13684 , 13459.6 , 13239.4 , 13020.7 , 12800.1 , 12574.1 , 12353.2 , 12120.8 , 11900 , 11673.7 , 11452.8 , 11233.4 , 11013.9 , 10792.6 , 10564.3 , 10342.2 , 10115 , 9893.04 , 9664.62 , 9442.56 , 9222.26 , 8999.82 , 8769.27 , 8546.26 , 8325.5 , 8102.51 , 7871.67 , 7648.41 , 7427.76 , 7203.73 , 6974.34 , 6750.16 , 6529.28 , 6304.56 , 6076.12 , 5851.41 , 5629.84 , 5408.03 , 5181.79 , 4956.38 , 4729.83 , 4507.61 , 4279.89 , 4057.29 , 3829.57 , 3606.56 , 3379.02 , 3155.66 , 2928.51 , 2706.5 , 2480.15 , 2255.41 , 2029.94 , 1804.27 , 1578.57 , 1353.8 , 1128.1 , 902.399 , 677.028 , 451.253 , 225.643 , 0.0349594 ]



bone1 = [2036.88 , 3223.87 , 3964.55 , 4448.59 , 4774.59 , 4997.97 , 5151.67 , 5256.33 , 5325.63 , 5368.67 , 5391.69 , 5399.43 , 5395.15 , 5381.38 , 5359.81 , 5331.98 , 5299 , 5261.73 , 5220.94 , 5177.1 , 5130.66 , 5081.96 , 5031.48 , 4979.24 , 4925.59 , 4870.78 , 4814.74 , 4757.79 , 4699.78 , 4641.26 , 4581.93 , 4522.01 , 4461.5 , 4400.48 , 4338.98 , 4277.01 , 4214.79 , 4152.04 , 4088.93 , 4025.53 , 3962.18 , 3898.3 , 3834.08 , 3769.81 , 3705.26 , 3640.43 , 3575.5 , 3510.47 , 3445.16 , 3379.72 , 3314.1 , 3248.34 , 3182.46 , 3116.42 , 3050.27 , 2984.06 , 2917.8 , 2851.21 , 2784.58 , 2718 , 2651.21 , 2584.32 , 2517.49 , 2450.48 , 2383.35 , 2316.14 , 2248.95 , 2181.54 , 2114.17 , 2046.54 , 1979.16 , 1911.53 , 1843.84 , 1776.16 , 1708.37 , 1640.52 , 1572.61 , 1504.68 , 1436.69 , 1368.66 , 1300.54 , 1232.48 , 1164.28 , 1096.07 , 1027.75 , 959.525 , 891.197 , 822.825 , 754.411 , 685.971 , 617.528 , 549.004 , 480.476 , 411.915 , 343.326 , 274.712 , 206.07 , 137.403 , 68.7147]
tissue1 = [69335.2 , 68199.9 , 67464.6 , 66959.4 , 66598.5 , 66330 , 66125.7 , 65965.8 , 65839 , 65736.1 , 65652 , 65582 , 65522.9 , 65473.1 , 65430 , 65393.5 , 65361.2 , 65333.3 , 65308.4 , 65286.6 , 65267.4 , 65249.5 , 65234.2 , 65219.8 , 65207.2 , 65195.5 , 65185 , 65175.4 , 65166.7 , 65158.5 , 65151 , 65144 , 65137.8 , 65131.7 , 65126.2 , 65120.9 , 65116.1 , 65111.4 , 65107.1 , 65103 , 65099.2 , 65095.6 , 65092.2 , 65089.1 , 65086 , 65083.1 , 65080.2 , 65077.6 , 65075.1 , 65072.6 , 65070.3 , 65068.1 , 65065.9 , 65063.9 , 65061.8 , 65060 , 65058.2 , 65056.5 , 65054.8 , 65053.3 , 65051.6 , 65050.3 , 65048.8 , 65047.4 , 65045.9 , 65044.5 , 65043.2 , 65042 , 65040.8 , 65039.6 , 65038.4 , 65037.4 , 65036.3 , 65035.3 , 65034.3 , 65033.4 , 65032.4 , 65031.3 , 65030.3 , 65029.5 , 65028.6 , 65027.8 , 65026.9 , 65026.1 , 65025.2 , 65024.5 , 65023.8 , 65023.1 , 65022.3 , 65021.7 , 65021 , 65020.2 , 65019.6 , 65018.9 , 65018.3 , 65017.6 , 65017 , 65016.4 , 65015.8 ]


print len(bone1), len(tissue1)

# --- plot 1 ---------
'''
n = range(200)
i=0
temp = 0.005
while i < 200:
	n[i] = temp
	temp += 0.005
	i = i+1

plt.plot(n, tissue)
plt.plot(n, bone)
'''
# -------- plot 2 ----------

n1 = range(99)
i=0
temp = 0.01
while i < 0.989:
	n1[i] = temp
	temp += 0.01
	i = i+1


plt.plot(n1, tissue1)
plt.plot(n1, bone1)


plt.ylabel(' bone opacity varying; tissueOpacity = 0.03; step size = 0.01 ')

plt.show()