from konlpy.tag import Okt
from data import data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,jansu,dic_name,menu,zumun,dic_num,menu_list,name_tuple
import os
import konlpy
import zipfile
import pandas as pd
import openpyxl
import csv
import re


for i in range(2):  # 마지막엔 해당 파일을 삭제 해야한다..
    konlpy_path = os.path.dirname(konlpy.__file__)
    java_path = os.path.join(konlpy_path, "java")
    os.chdir(java_path)
    os.getcwd()
        
    jar_file_path = 'open-korean-text-2.1.0.jar'
        
    with zipfile.ZipFile(jar_file_path, 'r') as jar:
        jar.extractall()
            
    with open("C:/Users/djdjd/AppData/Local/Programs/Python/Python312/Lib/site-packages/konlpy/java/org/openkoreantext/processor/util/noun/names.txt", "r", encoding="UTF-8") as f:
        data = f.read()
    
    data += data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + jansu + menu + data11
        
    with open("C:/Users/djdjd/AppData/Local/Programs/Python/Python312/Lib/site-packages/konlpy/java/org/openkoreantext/processor/util/noun/names.txt", 'w', encoding="UTF-8") as f:
        f.write(data)
    data
    
    
okt = Okt()

eat_sum = {"페이없이 먹은 금액" : 0, "페이로 먹은 금액" : 0}
check_gift = {"선물한 커피 갯수" : 0}
except_gift = {}

pay = 0
pay_log = []

dic_doyou = {"두유" : 0}

def menu_fun(m): # main처럼 함수로 만들기.
    global pay 
    money = (m*cup)
    
    change = 0
    change_2 = 0
    
    if (pay > 0) and (ta != "공개") and yes_pay:
        change = pay - money
        if change < 0:
            eat_sum["페이로 먹은 금액"] += money + change
            change_2 = -change
            eat_sum["페이없이 먹은 금액"] += change_2
            while change_2 > 0:
                if dic_name[ta][4] > 0:
                    dic_name[ta][4] -= 100
                    dic_name[ta][1] += 100
                    change_2 -= 100
                elif dic_name[ta][4] == 0:
                    dic_name[ta][0] += 100
                    dic_name[ta][1] += 100
                    change_2 -= 100
            pay = 0
        
        else:
            eat_sum["페이로 먹은 금액"] += money
            pay = pay - money
            
    else :
        eat_sum["페이없이 먹은 금액"] += money
        while money > 0:
            if dic_name[ta][4] > 0:
                dic_name[ta][4] -= 100
                dic_name[ta][1] += 100
                money -= 100
            elif dic_name[ta][4] == 0:
                dic_name[ta][0] += 100
                dic_name[ta][1] += 100
                money -= 100
            
                  


def menu_all(cup = 0):
    if i_menu == "베리고":
        menu_fun(4000)
    elif i_menu == "에스프레소":
        menu_fun(2500)
    elif i_menu == "뜨아":
        menu_fun(2500)
    elif i_menu == "따아":
        menu_fun(2500)
    elif i_menu == "아아":
        menu_fun(2500)
    elif i_menu == "아메리카노":
        menu_fun(2500)
    elif i_menu == "아메":
        menu_fun(2500)
    elif i_menu == "라떼":
        menu_fun(3000)
    elif i_menu == "플렛화이트":
        menu_fun(3000)
    elif i_menu == "따라":
        menu_fun(3000)
    elif i_menu == "아라":
        menu_fun(3000)
    elif i_menu == "카페라떼":
        menu_fun(3000)
    elif i_menu == "카푸치노":
        menu_fun(3000)
    elif i_menu == "바닐라라떼":
        menu_fun(3500)
    elif i_menu == "아바라":
        menu_fun(3500)
    elif i_menu == "카페모카":
        menu_fun(3500)
    elif i_menu == "더치":
        menu_fun(3500)
    elif i_menu == "콜드브루":
        menu_fun(3000)
    elif i_menu == "더치라떼":
        menu_fun(4000)
    elif i_menu == "보리커피":
        menu_fun(2500)
    elif i_menu == "탄산수":
        menu_fun(500)
    elif i_menu == "탄산":
        menu_fun(500)
    elif i_menu == "밀크티":
        menu_fun(3000)
    elif i_menu == "딸기라떼":
        menu_fun(3500)
    elif i_menu == "캐모마일":
        menu_fun(2500)
    elif i_menu == "루이보스":
        menu_fun(2500)
    elif i_menu == "보이차":
        menu_fun(2500)
    elif i_menu == "페퍼민트":
        menu_fun(2500)
    elif i_menu == "레몬그라스":
        menu_fun(2500)
    elif i_menu == "라벤더":
        menu_fun(2500)
    elif i_menu == "차":
        menu_fun(2500)
    elif i_menu == "티":
        menu_fun(2500)
    elif i_menu == "아이스크림":
        menu_fun(2500)
    elif i_menu == "녹차아이스크림":
        menu_fun(2500)
    elif i_menu == "맥주":
        menu_fun(3000)
    elif i_menu == "무알콜":
        menu_fun(3000)
    elif i_menu == "기네스":
        menu_fun(5000)
    elif i_menu == "제주누보":
        menu_fun(3000)
    elif i_menu == "누보":
        menu_fun(3000)
    elif i_menu == "아바":
        menu_fun(3500)
    elif i_menu == "아보바나나":
        menu_fun(3500)
    elif i_menu == "아보카도":
        menu_fun(3500)
    elif i_menu == "아보카토":
        menu_fun(4000)
    elif i_menu == "미숫가루":
        menu_fun(3500)
    elif i_menu == "망고":
        menu_fun(4000)
    elif i_menu == "망스":
        menu_fun(4000)
    elif i_menu == "망바":
        menu_fun(4000)
    elif i_menu == "아포카도":
        menu_fun(4000)
    elif i_menu == "아포카토":
        menu_fun(4000)
    elif i_menu == "아포가토":
        menu_fun(4000)
    elif i_menu == "아인슈페너":
        menu_fun(4000)
    elif i_menu == "포춘쿠키":
        menu_fun(1000)
    elif i_menu == "포츈쿠키":
        menu_fun(1000)
    elif i_menu == "포춘":
        menu_fun(1000)
    elif i_menu == "포츈":
        menu_fun(1000)
    elif i_menu == "민트초코라떼":
        menu_fun(4000)
    elif i_menu == "민트초코":
        menu_fun(4000)
    elif i_menu == "민초라떼":
        menu_fun(4000)
    elif i_menu == "민초라":
        menu_fun(4000)
    elif i_menu == "초코민트라떼":
        menu_fun(4000)
    elif i_menu == "초코민트":
        menu_fun(4000)       
    elif i_menu == "초민라":
        menu_fun(4000)
    elif i_menu == "페퍼민트라떼":
        menu_fun(4000)
    elif i_menu == "페퍼민트":
        menu_fun(4000)
    elif i_menu == "페민라":
        menu_fun(4000)
    elif i_menu == "스피아민트라떼":
        menu_fun(4000)
    elif i_menu == "스피아민트":
        menu_fun(4000)
    elif i_menu == "스민라":
        menu_fun(4000)
    elif i_menu == "애플민트스무디":
        menu_fun(3500)
    elif i_menu == "쌍화탕":
        menu_fun(1700)
    elif i_menu == "쌍화":
        menu_fun(1700)
    elif i_menu == "쌍화차":
        menu_fun(1700)
    elif i_menu == "보약":
        menu_fun(1700)
    elif i_menu == "아사히":
        menu_fun(3000)
    elif i_menu == "아사이":
        menu_fun(3000)
    elif i_menu == "드립":
        menu_fun(4000)
    elif i_menu == "섭":
        menu_fun(4000)
    elif i_menu == "패션후르츠에이드":
        menu_fun(3500)
    elif i_menu == "패션후르츠":
        menu_fun(3500)
    elif i_menu == "레몬에이드":
        menu_fun(3500)
    elif i_menu == "레몬":
        menu_fun(3000)
    elif i_menu == "복바에이드":
        menu_fun(3500)
    elif i_menu == "복숭아에이드":
        menu_fun(3500)
    elif i_menu == "복숭아":
        menu_fun(3500)
    elif i_menu == "복바":
        menu_fun(3500)
    elif i_menu == "복숭아바질에이드":
        menu_fun(3500)
    elif i_menu == "하이볼":
        menu_fun(5000)
    elif i_menu == "브륄레":
        menu_fun(3000)
    elif i_menu == "브릴레":
        menu_fun(3000)
    elif i_menu == "로즈마리라떼":
        menu_fun(4000)
    elif i_menu == "로즈마리":
        menu_fun(4000)
    elif i_menu == "꼼빠냐":
        menu_fun(3500)
    elif i_menu == "비건":
        menu_fun(2000)
    elif i_menu == "튀일":
        menu_fun(2000)
    elif i_menu == "튀일쿠키":
        menu_fun(2000)
    elif i_menu == "트윌":
        menu_fun(2000)
    elif i_menu == "아몬드":
        menu_fun(2000)
    elif i_menu == "수제":
        menu_fun(2000)
    elif i_menu == "트윌쿠키":
        menu_fun(2000)
    elif i_menu == "유자":
        menu_fun(3000)                  # 우유, 오트 체크
    elif i_menu == "모히또":
        menu_fun(5000)
    elif i_menu == "모히토":
        menu_fun(5000)
    elif i_menu == "샹그리아":
        menu_fun(5000)
    elif i_menu == "깔루아밀크":
        menu_fun(5000)
    elif i_menu == "칼루아밀크":
        menu_fun(5000)
    elif i_menu == "잭콜":
        menu_fun(5000)
    elif i_menu == "잭콕":
        menu_fun(5000)
    elif i_menu == "안주":
        menu_fun(2000)
    elif i_menu == "자두":
        menu_fun(3500)
    elif i_menu == "초코라떼":
        menu_fun(3500)
    elif i_menu == "핫초코":
        menu_fun(3500)
    elif i_menu == "비어":
        menu_fun(5000)
    elif i_menu == "와인":
        menu_fun(4000)
    elif i_menu == "뱅쇼":
        menu_fun(3000)
    elif i_menu == "아이스티":
        menu_fun(2500)
    elif i_menu == "밀크티라떼":
        menu_fun(3500)
    elif i_menu == "아샷추":
        menu_fun(3000)
    elif i_menu == "요거트":
        menu_fun(4000)
    elif i_menu == "그릭":
        menu_fun(4000)
    elif i_menu == "딸바":
        menu_fun(4000)
    elif i_menu == "딸기":
        menu_fun(3500)
    elif i_menu == "두유":
        dic_doyou["두유"] += cup
        menu_fun(2000)
        
        
    
    
# 초코 관련 메뉴 추가. 샷추가. 오트추가
    
    
    
if __name__ == "__main__":
    # 메인 문장 시작(텍스트 파일을 읽는다.)
    with open("C:/Users/djdjd/OneDrive/바탕 화면/Python/python_cafe/선물의심.txt", "r", encoding="UTF-8") as f:
        text = f.read().replace("\n", " ")
        pattern_1 = r'(\] \[)'
        text = re.sub(pattern_1,"][",text)
        pattern_1 = r'한테'
        text = re.sub(pattern_1,"에게",text)
        pattern_1 = r'께'
        text = re.sub(pattern_1,"에게",text)
        pattern_1 = r'민트 초코'
        text = re.sub(pattern_1,"민트초코",text)
        pattern_1 = r'꼰빠냐'
        text = re.sub(pattern_1,"꼼빠냐",text)
        pattern_1 = r'꼰파냐'
        text = re.sub(pattern_1,"꼼빠냐",text)
        pattern_1 = r'꼼파냐'
        text = re.sub(pattern_1,"꼼빠냐",text)
        pattern_1 = r'초코 라떼'
        text = re.sub(pattern_1,"초코라떼",text)
        pattern_1  = r'민초 라떼'
        text = re.sub(pattern_1,"민초라떼",text)
        pattern_1  = r'라테'
        text = re.sub(pattern_1," 라떼 ",text)
        pattern_1  = r'돌초 라떼'
        text = re.sub(pattern_1,"민초라떼",text)
        pattern_1  = r'돌초라떼'
        text = re.sub(pattern_1,"민초라떼",text)
        pattern_1  = r'초민 라떼'
        text = re.sub(pattern_1,"민초라떼",text)
        pattern_1  = r'초민라떼'
        text = re.sub(pattern_1,"민초라떼",text)
        pattern_1  = r'초코 민트'
        text = re.sub(pattern_1,"초코민트",text)
        pattern_1  = r'페퍼 민트'
        text = re.sub(pattern_1,"페퍼민트",text)
        pattern_1  = r'민트 라떼'
        text = re.sub(pattern_1,"민트라떼",text)
        pattern_1  = r'스피아 민트'
        text = re.sub(pattern_1,"스피아라떼",text)
        pattern_1  = r'더치 라떼'
        text = re.sub(pattern_1,"더치라떼",text)
        pattern_1  = r'상그리아'
        text = re.sub(pattern_1,"샹그리아",text)
        pattern_1  = r'카페 라떼'
        text = re.sub(pattern_1,"카페라떼",text)
        pattern_1  = r'섭드립'
        text = re.sub(pattern_1,"섭 드립",text)
        pattern_1  = r'딸기바나나'
        text = re.sub(pattern_1,"딸바 ",text)
        pattern_1  = r'딸기'
        text = re.sub(pattern_1,"딸기 ",text)
        pattern_1  = r'바닐라 라떼'
        text = re.sub(pattern_1,"바닐라라떼",text)
        pattern_1  = r'콜드 브루'
        text = re.sub(pattern_1,"콜드브루",text)
        pattern_1  = r'보리 커피'
        text = re.sub(pattern_1,"보리커피",text)
        pattern_1  = r'딸기 라떼'
        text = re.sub(pattern_1,"딸기라떼",text)
        pattern_1  = r'밀크티 라떼'
        text = re.sub(pattern_1,"밀크티라떼",text)
        pattern_1  = r'흑맥주'
        text = re.sub(pattern_1,"기네스",text)
        pattern_1  = r'에일'
        text = re.sub(pattern_1,"기네스",text)
        pattern_1  = r'꿀'
        text = re.sub(pattern_1," 꿀 ",text)
        pattern_1  = r'찰스버그'
        text = re.sub(pattern_1,"기네스",text)
        pattern_1  = r'따바라'
        text = re.sub(pattern_1,"아바라",text)
        pattern_1  = r'페이시작'
        text = re.sub(pattern_1,"페시",text)
        pattern_1  = r'루이 보스'
        text = re.sub(pattern_1,"루이보스",text)
        pattern_1  = r'애플민트 스무디'
        text = re.sub(pattern_1,"애플민트스무디",text)
        pattern_1  = r'레몬 에이드'
        text = re.sub(pattern_1,"레몬에이드",text)
        pattern_1  = r'복바 에이드'
        text = re.sub(pattern_1,"복바에이드",text)
        pattern_1  = r'카푸 치노'
        text = re.sub(pattern_1,"카푸치노",text)
        pattern_1  = r'누보 망고'
        text = re.sub(pattern_1,"누보",text)
        pattern_1  = r'누보망고'
        text = re.sub(pattern_1,"누보",text)
        pattern_1  = r'망고 누보'
        text = re.sub(pattern_1,"누보",text)
        pattern_1  = r'망고누보'
        text = re.sub(pattern_1,"누보",text)
        pattern_1  = r'섭드립'
        text = re.sub(pattern_1," 섭 드립 ",text)
        pattern_1 = r'싸모'
        text = re.sub(pattern_1,"싸모님",text)
        pattern_1 = r'연화'
        text = re.sub(pattern_1,"지우",text)
        pattern_1 = r'사모'
        text = re.sub(pattern_1,"싸모님",text)
        pattern_1 = r'싸모님님'
        text = re.sub(pattern_1,"싸모님",text)
        pattern_1 = r'신영'
        text = re.sub(pattern_1,"싸모님",text)
        pattern_1 = r'중렬'
        text = re.sub(pattern_1,"중열",text)
        pattern_1 = r'김민경'
        text = re.sub(pattern_1,"바태",text)
        pattern_1 = r'민경'
        text = re.sub(pattern_1,"바태",text)
        pattern_1 = r'지원자'
        text = re.sub(pattern_1," ",text)
        pattern_1 = r'하루종일'
        text = re.sub(pattern_1,"",text)
        pattern_1 = r'하루 종일'
        text = re.sub(pattern_1,"",text)
        pattern_1 = r'윤라연'
        text = re.sub(pattern_1,"하루나",text)
        pattern_1 = r'라연'
        text = re.sub(pattern_1,"하루나",text)
        pattern_1 = r'대표님'
        text = re.sub(pattern_1,"목사님",text)
        pattern_1 = r'민수'
        text = re.sub(pattern_1,"목사님",text)
        pattern_1 = r'오쭈'
        text = re.sub(pattern_1,"오주현",text)
        pattern_1 = r'공동체손님'
        text = re.sub(pattern_1,"공개",text)
        pattern_1 = r'이쭈'
        text = re.sub(pattern_1,"이주현",text)
        pattern_1 = r'들에게'
        text = re.sub(pattern_1,"에게",text)
        pattern_1 = r'에게도'
        text = re.sub(pattern_1,"에게",text)
        pattern_1 = r'에게는'
        text = re.sub(pattern_1,"에게",text)
        pattern_1 = r'한 잔'
        text = re.sub(pattern_1,"한잔",text)
        pattern_1 = r'한잔'
        text = re.sub(pattern_1," 한잔",text)
        pattern_1 = r'두 잔'
        text = re.sub(pattern_1,"두잔",text)
        pattern_1 = r'두잔'
        text = re.sub(pattern_1," 두잔",text)
        pattern_1 = r'세 잔'
        text = re.sub(pattern_1,"세잔",text)
        pattern_1 = r'석 잔'
        text = re.sub(pattern_1,"석잔",text)
        pattern_1 = r'세잔'
        text = re.sub(pattern_1," 세잔",text)
        pattern_1 = r'네 잔'
        text = re.sub(pattern_1,"네잔",text)
        pattern_1 = r'네잔'
        text = re.sub(pattern_1," 네잔",text)
        pattern_1 = r'넉 잔'
        text = re.sub(pattern_1,"넉잔",text)
        pattern_1 = r'다섯 잔'
        text = re.sub(pattern_1,"다섯잔",text)
        pattern_1 = r'다섯잔'
        text = re.sub(pattern_1," 다섯잔",text)
        pattern_1 = r'한 캔'
        text = re.sub(pattern_1,"한캔",text)
        pattern_1 = r'두 캔'
        text = re.sub(pattern_1,"두캔",text)
        pattern_1 = r'세 캔'
        text = re.sub(pattern_1,"세캔",text)
        pattern_1 = r'네 캔'
        text = re.sub(pattern_1,"네캔",text)
        pattern_1 = r'다섯 캔'
        text = re.sub(pattern_1,"다섯캔",text)
        pattern_1 = r'한 개'
        text = re.sub(pattern_1,"한개",text)
        pattern_1 = r'두 개'
        text = re.sub(pattern_1,"두개",text)
        pattern_1 = r'세 개'
        text = re.sub(pattern_1,"세개",text)
        pattern_1 = r'네 개'
        text = re.sub(pattern_1,"네개",text)
        pattern_1 = r'다섯 개'
        text = re.sub(pattern_1,"다섯개",text)
        pattern_1 = r'부탁드'
        text = re.sub(pattern_1,"부탁해요",text)
        pattern_1 = r'오트밀'
        text = re.sub(pattern_1,"오트밀 ",text)
        pattern_1 = r'오트'
        text = re.sub(pattern_1,"오트 ",text)
        pattern_1 = r'야'
        text = re.sub(pattern_1,"",text)
        pattern_1 = r'플랫화이트'
        text = re.sub(pattern_1,"플렛화이트",text)
        pattern_1 = r'플렛 화이트'
        text = re.sub(pattern_1,"플렛화이트",text)
        pattern_1 = r'이에'
        text = re.sub(pattern_1,"에",text)
        pattern_1 = r'하나요'
        text = re.sub(pattern_1,"하나",text)
        pattern_1 = r'두개요'
        text = re.sub(pattern_1,"두개",text)
        pattern_1 = r'세개요'
        text = re.sub(pattern_1,"세개",text)
        pattern_1 = r'쩡은'
        text = re.sub(pattern_1,"정은",text)
        pattern_1 = r'이름'
        text = re.sub(pattern_1," 이름 ",text)
        pattern_1 = r'노페이'
        text = re.sub(pattern_1," 노페 ",text)

        
        
        # 아래에 계속 적기.
        text = text.split(" [") # 먼저 텍스트 파일에서 ] [ 이걸 ][로 바꿔줘야 한다 !
        #print(text)
        # 문장 진짜 시작.
        for text_line in text:
            pos_tags = okt.pos(text_line)
            result = [word for word, pos in pos_tags if pos in ["Noun", "Josa", "Number", "Verb"]]
            ta = result[0]
            for _ in range(3):
                result.pop(0)
            #print(ta, result)
        # 일반적으로 선물 주는 경우

            yes_pay = True
        
            # 페이체크
            if (ta == "이지연" and "페시" in result):
                pay_log.append(result[(result.index("페시")+1)])
                temp = result[(result.index("페시")+1)]
                pay += int(temp.replace(",","").replace("원",""))
                
            if ("에게" in result) and ("선물" in result):
            # 갯수 체크(수량 잡기)
                for cup in result:
                    if cup in ["한잔", "두잔", "세잔", "네잔", "다섯잔", "여섯잔", "일곱잔", "하나", "두개", "세개", "네개", "석잔", "넉잔", "다섯개", "여섯개", "일곱개", "한캔", "두캔", "세캔", "네캔", "다섯캔", "여섯캔"]:
                        num1 = dic_num[cup]
                        break
                    elif cup in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50"]:
                        if (result.index(cup) < result.index("선물")) and (result.index(cup) > result.index("에게")): # 선물하는 경우에서, 다른 숫자들이 나오면 안된다..ex) 22기 졸업생
                            num1 = dic_num[cup]
                            break
                    else:
                        num1 = 1
                    
                # 이름 중복 제외
                result = set(result)
                result = list(result)
                
                # 성을 붙인 이름과 안 붙인 이름이 같이 있으면 하나를 지워주는 부분
                count_name = 0
                for n in result:
                    if n in dic_name.keys():
                        count_name = 0
                        key = n
                        pattern = fr'({key})'
                        for text in result:
                            match = re.findall(pattern,text)
                            if key in match:
                                count_name += 1
                            if count_name >= 2:
                                result.pop(result.index(key))
                                count_name = 0
                print(result)
                    
                # 준 사람 & 받은 사람
                count = 0
                check_person = 0
                for rec in result:
                    
                    if rec in dic_name.keys() :
                        count += 1
                        check_person += 1
                        # 받는 사람
                        if dic_name[rec][0] > 0:
                            money = num1 * 3000
                            while money > 0:
                                if dic_name[rec][0] > 0:
                                    dic_name[rec][0] -= 100
                                    dic_name[rec][3] += 100
                                    money -= 100
                                elif dic_name[rec][0] == 0:
                                    dic_name[rec][4] += 100
                                    dic_name[rec][3] += 100
                                    money -= 100
                        elif dic_name[rec][0] == 0:
                            dic_name[rec][4] += num1 * 3000
                            dic_name[rec][3] += num1 * 3000

                # 준 사람
                dic_name[ta][2] += (num1 * count * 3000)
                money = (num1 * count * 3000)
                while money > 0:
                    if dic_name[ta][4] > 0:
                        dic_name[ta][4] -= 100
                        money -= 100
                    elif dic_name[ta][4] == 0:
                        dic_name[ta][0] += 100
                        money -= 100
                check_gift["선물한 커피 갯수"] += (num1 * count)
                
                
            # 내가 직접 확인해봐야 할 부분(에게가 없는 선물)
            elif ("에게" not in result) and ("선물" in result):
                with open("C:/Users/djdjd/OneDrive/바탕 화면/Python/python_cafe/선물의심.txt","a",encoding="UTF-8") as f:
                    f.write(f"[{ta}]")
                    f.write(" [오전 10:00] ")
                    for i in result:
                        if i in dic_name.keys():
                            f.write(f"{i}에게 ")
                        else:
                            f.write(f"{i} ")
                    f.write("\n")          
            
            
            else:
                try :
                    (list(set(result)&set(menu_list)).pop(0)) and (list(set(result)&set(dic_num.keys())).pop(0))
                except IndexError:
                    pass
                # 메뉴를 시킨 경우
                else :
                    try:
                        list(set(result)&set(zumun)).pop(0) in zumun
                    except IndexError:
                        # 주문 맨트가 없는 주문
                        try:
                            list(set(result)&set(dic_name.keys())).pop(0)  # 여러개의 리스트 원소들중, 여러개 원소가 들어 있는 리스트간의 교집합.
                        except IndexError:
                            print(result)
                            for j in result:
                                if j == "노페":
                                    yes_pay = False
                                    
                            
                                    
                            for i in result:
                                if i in menu_list:
                                    i_menu = i
                                elif i in ["한잔", "두잔", "세잔", "네잔", "다섯잔", "여섯잔", "일곱잔", "하나", "두개", "세개","석잔","넉잔", "네개", "다섯개", "여섯개", "일곱개", "한캔", "두캔", "세캔", "네캔", "다섯캔", "여섯캔","1","2", "3", "4", "5", "6", "7", "8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50"]:
                                    cup = dic_num[i]
                                    menu_all(cup)
                            
                        # 사람 이름이 나오는 경우
                        else:
                            print(result)
                            for j in result:
                                if j == "노페":
                                    yes_pay = False
                                    
                            # 아아 1 - 진호이름으로 먹어요 (이름이 뒤에 나오는 경우)
                            if len(list(set(result)&set(dic_name.keys()))) == 1:
                                for j in result:
                                    if j in dic_name.keys():
                                        ta = j
                                
                                for i in result:
                                    if i in menu_list:
                                        i_menu = i
                                    elif i in ["한잔", "두잔", "세잔", "네잔", "다섯잔", "여섯잔", "일곱잔", "하나", "두개", "세개","석잔","넉잔", "네개", "다섯개", "여섯개", "일곱개", "한캔", "두캔", "세캔", "네캔", "다섯캔", "여섯캔","1","2", "3", "4", "5", "6", "7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50"]:
                                        cup = dic_num[i]
                                        menu_all(cup)
                                        
                            else:          
                                for i in result:
                                    if i in dic_name.keys():
                                        ta = i
                                    elif i in menu_list:
                                        i_menu = i
                                    elif i in ["한잔", "두잔", "세잔", "네잔", "다섯잔", "여섯잔", "일곱잔", "하나", "두개", "세개","석잔","넉잔", "네개", "다섯개", "여섯개", "일곱개", "한캔", "두캔", "세캔", "네캔", "다섯캔", "여섯캔","1","2", "3", "4", "5", "6", "7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50"]:
                                        cup = dic_num[i]
                                        menu_all(cup)
                                        
                                                                              
                                
                    # 주문 맨트가 있는 주문              
                    else:
                        try:
                            list(set(result)&set(zumun)).pop(0) in zumun
                        except IndexError:
                            pass
                        else:
                            try:
                                list(set(result)&set(dic_name.keys())).pop(0)
                            except IndexError:
                                print(result)
                                for j in result:
                                    if j == "노페":
                                        yes_pay = False
                                        
                                for i in result:
                                    if i in menu_list:
                                        i_menu = i
                                    elif i in ["한잔", "두잔", "세잔", "네잔", "다섯잔", "여섯잔", "일곱잔", "하나", "두개", "세개","석잔","넉잔", "네개", "다섯개", "여섯개", "일곱개", "한캔", "두캔", "세캔", "네캔", "다섯캔", "여섯캔","1","2", "3", "4", "5", "6", "7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50"]:
                                        cup = dic_num[i]
                                        menu_all(cup)
                            else:
                                print(result)
                                for j in result:
                                    if j == "노페":
                                        yes_pay = False
                                    
                                # 아아 1 - 진호이름으로 먹어요 (이름이 뒤에 나오는 경우)
                                if len(list(set(result)&set(dic_name.keys()))) == 1:
                                    for j in result:
                                        if j in dic_name.keys():
                                            ta = j
                                    
                                    for i in result:
                                        if i in menu_list:
                                            i_menu = i
                                        elif i in ["한잔", "두잔", "세잔", "네잔", "다섯잔", "여섯잔", "일곱잔", "하나", "두개", "세개","석잔","넉잔", "네개", "다섯개", "여섯개", "일곱개", "한캔", "두캔", "세캔", "네캔", "다섯캔", "여섯캔","1","2", "3", "4", "5", "6", "7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50"]:
                                            cup = dic_num[i]
                                            menu_all(cup)
                                            
                                else:          
                                    for i in result:
                                        if i in dic_name.keys():
                                            ta = i
                                        elif i in menu_list:
                                            i_menu = i
                                        elif i in ["한잔", "두잔", "세잔", "네잔", "다섯잔", "여섯잔", "일곱잔", "하나", "두개", "세개","석잔","넉잔", "네개", "다섯개", "여섯개", "일곱개", "한캔", "두캔", "세캔", "네캔", "다섯캔", "여섯캔","1","2", "3", "4", "5", "6", "7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50"]:
                                            cup = dic_num[i]
                                            menu_all(cup)
                                        
                                
        
        
    # 이름 합치기(오세현과 세현 하나로 합치기)
    for first, second in name_tuple:
        if (dic_name[second][4] != 0) and (dic_name[first+second][0] != 0):
            last = dic_name[first+second][0]
            while last > 0:
                if dic_name[second][4] > 0:
                    dic_name[second][4] -= 100
                    last -= 100
                elif dic_name[second][4] == 0:
                    dic_name[second][0] += 100
                    last -= 100
            dic_name[second][1] += dic_name[first+second][1]
            dic_name[second][2] += dic_name[first+second][2]
            dic_name[second][3] += dic_name[first+second][3]
            dic_name[first+second] = [0, 0, 0, 0, 0]
    
        elif (dic_name[first+second][4] != 0) and (dic_name[second][0] != 0):
            last = dic_name[second][0]
            while last > 0:
                if dic_name[first+second][4] > 0:
                    dic_name[first+second][4] -= 100
                    last -= 100
                elif dic_name[first+second][4] == 0:
                    dic_name[first+second][0] += 100
                    last -= 100
            dic_name[second][0] = dic_name[first+second][0]
            dic_name[second][4] = dic_name[first+second][4]
            dic_name[second][1] += dic_name[first+second][1]
            dic_name[second][2] += dic_name[first+second][2]
            dic_name[second][3] += dic_name[first+second][3]
            dic_name[first+second] = [0 ,0 ,0 ,0 ,0] # 성이 붙은 것은 초기화.
    
        else:
            dic_name[second][0] += dic_name[first+second][0]
            dic_name[second][1] += dic_name[first+second][1]
            dic_name[second][2] += dic_name[first+second][2]
            dic_name[second][3] += dic_name[first+second][3]
            dic_name[second][4] += dic_name[first+second][4]
            dic_name[first+second] = [0, 0, 0, 0, 0]

# dic_name에서 필요한 이름만 거르기
    dic_name_filt = {}
    count = 0  
    for key, value in dic_name.items():
        if count < 174: # 맴버 추가시 +1, 맴버 탈퇴시 -1
            dic_name_filt[key] = value
            count += 1
        else:
            break
    
    """
# 공감 excel에 추가.
    file_path = "C:/Users/djdjd/OneDrive/바탕 화면/카페/카페_4월 - 복사본.xlsx"
    workbook = openpyxl.load_workbook(file_path, data_only=True)
    sheet = workbook["정산"]
    
    
    num = 5
    for name, money in dic_name_filt.items():
        num += 1
        num = str(num)
        if money[0] > 0:
            if sheet["N"+num].value > 0:
                money1 = money[0]
                while money1 > 0:
                    if sheet["N"+num].value > 0:
                        sheet["N"+num].value -= 100
                        money1 -= 100
                    elif sheet["N"+num].value == 0:
                        sheet["F"+num].value += 100
                        money1 -= 100
            else:
                sheet["F"+num].value += money[0]
                
        if money[1] > 0:
            sheet["H"+num].value += money[1]
        
        if money[2] > 0:
            sheet["I"+num].value += money[2]
            
        if (money[1] > 0) or (money[2] > 0):
            sheet["J"+num].value += (money[1] + money[2])
        
        if money[3] > 0:
            sheet["K"+num].value += money[3]
            
        if money[4] > 0:
            sheet["N"+num].value += money[4]
        
        sheet["L"+num].value = sheet["F"+num].value
            
        num = int(num)
    
    workbook.save(file_path)
    """

    # csv파일 만들기
    c = [["이름", "내야할돈", "먹은", "선물한", "선물받은", "남은선물"]]
    d = []
    for name, money in dic_name_filt.items():
        d.append(name)
        d.extend(money)
        c.append(d)
        d = []
    df = pd.DataFrame(c, columns=["이름", "내야할", "먹은금액", "선물한", "선물받은",  "남은선물"])
    
    with open("C:/Users/djdjd/OneDrive/바탕 화면/Python/python_cafe/cafe_data.csv", "w", encoding="UTF-8") as f:
        writer = csv.writer(f)
        writer.writerows(c)

    
    # 페이제외, 먹은 액수와 선물한 액수의 합 
    print(f"페이로 먹은 금액 {eat_sum['페이로 먹은 금액']}, 페이없이 먹은 금액 {eat_sum['페이없이 먹은 금액']}")
    print(check_gift)
    print(except_gift)
    print(dic_doyou)
    print(pay_log)
    print("잔여 페이는 :", pay)
            
    
            
            
    

        











                

