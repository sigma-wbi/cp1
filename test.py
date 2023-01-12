import pandas as pd
allData= pd.DataFrame({'pcname':['홍콩반점창업■안양■수익3000만＼오토운영＼실매장＼무료상담', '《잠실 분당 미소야》→[수익 1000만] 초보 안정성 여성 창업 부업 투자', '★일산지역★투썸플레이스★특급 가성비매장★초보창업★사회초년생창업 추천★']})
pclist = ['홍콩반점','미소야','투썸플레이스']

for elem in pclist:
    datafilter = allData['pcname'].str.contains(elem)
    pc = allData[datafilter]
    pcindex = pc.index
    allData.drop(pcindex, axis=0, inplace=True)
    pc['pcname']= elem
    allData = pd.concat([allData,pc])

print(allData)