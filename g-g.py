import webbrowser
import os
import requests
import json
import time
#2.오늘 3.내일 추가
#지역 검색기능
#다른 지역도 검색 가능하도록
#속도개선(불러오는게 느린게 아닌듯, 처리가 느린듯)

def list_show(li_st,name,nex):
    li_st.sort()

    os.system(f"mode con cols=80 lines={len(li_st)*2+5}")

    input_ = input(("\n\n"+"\n\n".join([" | ".join(i[1:]) for i in li_st]) if li_st else f"\n{name}이 없습니다.") +(f"\n\n{nex}을 보려면 아무 키나 입력하시오.(s = 웹 페이지 열기,d = 다른 날짜 입력) " if name != "일반석" else "\n\n날짜 입력으로 돌아갑니다. (s = 웹사이트 이동, e = 종료)"))
    return input_
def open_url():
    date_two = time.strftime("%Y%m%d",time.localtime(time.mktime(time.strptime(date,"%Y%m%d"))+86400*2))                     
    url = f"https://domair.interpark.com/dom/main.do?trip=OW&dep={depp}&arr={arrr}&dep2=GMP&arr2=KWJ&depdate={date}&retdate={date_two}&adt=1&chd=0&inf=0&mbn=tourair&mln=airdome_search1#anchor-list"
    webbrowser.open(url)
    
months = {"1":31,"2":28,"3":31,"4":30,"5":31,"6":30,"7":31,"8":31,"9":30,"10":31,"11":30,"12":31}
names = {"KWJ":"광주", "GMP":"김포"}
depp = "KWJ"
arrr = "GMP"
while True:
    os.system("mode con cols=60 lines=10")
    
    while True:
        try:
            os.system('cls')
            date = int(input(f"{names[depp]} --> {names[arrr]}\n날짜를 입력하세요. ( 1 = 출발<->도착 변경) \nex) 317(3월17일), 1211(12월11일)\n\n\n=>  " ))
            str_date = str(date)
            if not date:
                print("입력되지 않았습니다.")
                time.sleep(0.2)
            if date == 1:
                depp,arrr = arrr,depp
                
            elif len(str_date) == 3:
                
                if int(str_date[1:]) <= months[str_date[0]]:
                    date = "2021"+"0"+ str_date
                    break
                    
                else:
                    print("일자가 유효하지 않습니다.")
                    time.sleep(0.2)
                
            elif len(str_date) == 4:
                
                month = str_date[0:2]
                if month in months:
                    if int(str_date[2:]) <= months[month]:
                        date = "2021"+ str_date
                        break
                    else:
                        print("일자가 유효하지 않습니다.")
                        time.sleep(0.2)
                        
                    
                else:
                    print("월자가 유효하지 않습니다.")
                    time.sleep(0.2)
            else:
                print("유효한 날짜가 아닙니다.")
                time.sleep(0.2)
        except ValueError:
            print("숫자만 입력하세요")
            time.sleep(0.2)
    ports = ['KE','OZ','7C','LJ','ZE','TW','BX']
    special = []
    sale = []
    general = []
    
    for air in ports:
        
        r = requests.get(f'https://domair.interpark.com/api/booking/airJourney.do?format=json&dep={depp}&arr={arrr}&depDate={date}&adt=1&chd=0&inf=0&tripDivi=0&airlineCode={air}&siteCode=')

        js = json.loads(r.text)
        if js['replyAvailFare'] == None:
            pass
        else:
            for i in js['replyAvailFare']['availFareSet']:
                seg = i['segFare']
                det = seg['classDetail']
                air_name = seg['carDesc']
                dep_time = f'{seg["depTime"][:-2]}시 {seg["depTime"][-2:]}분 츨발'
                arr_time = f'{seg["arrTime"][:-2]}시 {seg["arrTime"][-2:]}분 도착'
                fuel = int(seg['fuelChg']) if seg['fuelChg'] != "" else 0
                tax = int(seg['airTax']) if seg['airTax'] != "" else 0
                tasf = int(seg['tasf']) if seg['tasf'] != "" else 0
                fee = fuel + tax + tasf
                for z in det:
                    avail = z['noOfAvailSeat']
                    fare = int(z['fare']) + fee if z['fare'] != "" else fee
                    
                    if z['classNumber'] == "4":
                        
                         special.append([fare,f"{fare} 원",air_name,dep_time,arr_time,f"{avail}좌석 남음"])
                    elif z['classNumber'] == "3":
                         sale.append([fare,f"{fare} 원",air_name,dep_time,arr_time,f"{avail}좌석 남음"])
                    elif z['classNumber'] == "2":
                         general.append([fare,f"{fare} 원",air_name,dep_time,arr_time,f"{avail}좌석 남음"])
                         

    
    
    first = list_show(special,"특가석","할인석")
    if first == "s":
        open_url()
    elif first == "d":
        pass
    else:
        second = list_show(sale,"할인석","일반석")
        
        if second == "s":
            open_url()
        elif second == "d":
            pass
        else:
            third = list_show(general,"일반석",None)
            
            if   third == "s":
                open_url()
                
            elif third == "e":
                exit()
            else:
                pass
                
    

    
    
                     
    

