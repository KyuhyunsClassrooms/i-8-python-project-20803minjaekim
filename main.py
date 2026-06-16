# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20803 김민재
# 프로젝트 주제: 비밀번호 안전성 평가 및 추천 시스템




password_criteria = [
    ["length", 3, "비밀번호 길이가 8자리 이상인가?"],
    ["number", 2, "숫자가 포함되어 있는가?"], 
    ["repetition", -3, "동일한 문자가 3번 연속 반복되는가? (감점)"]
]


def evaluate_password(user_password, criteria, failed_reasons):
    total_score = 0
    print("\n--- 안전성 검사 시작 ---")
    
   
    for rule in criteria:
        rule_name = rule[0]    
        score = rule[1]        
        description = rule[2]  
        
      
        if rule_name == "length":
            
            if len(user_password) >= 8: 
                print(f"[성공] {description} (+{score}점)")
                total_score += score
            else:
                print(f"[실패] {description} (0점)")
                failed_reasons.append("비밀번호 길이가 8자리 미만입니다.")
                
        elif rule_name == "number":
           
            number_count = 0
            number_characters = "0123456789"
            
            for char in user_password:
                if char in number_characters:
                    number_count = number_count + 1
            
            if number_count > 0:
                print(f"[성공] {description} (+{score}점)")
                total_score += score
            else:
                print(f"[실패] {description} (0점)")
                failed_reasons.append("숫자가 포함되어 있지 않습니다.")
                
        elif rule_name == "repetition":
            
            has_repetition = 0 
            
            
            for i in range(len(user_password) - 2):
                if user_password[i] == user_password[i+1] and user_password[i+1] == user_password[i+2]:
                    has_repetition = 1  
                    break  
            
            
            if has_repetition == 1:
                print(f"[위험] {description} ({score}점 감점)")
                total_score += score  # 음수를 더하므로 자동 감점
                failed_reasons.append("동일한 문자가 3번 연속 반복됩니다.")
            else:
                print(f"[안전] 연속된 반복 문자가 없습니다. (0점)")
                
    return total_score



def print_danger_analysis(failed_reasons):
    print("\n--- 위험 원인 분석 ---")
    if len(failed_reasons) == 0:
        print("점검 결과, 특별한 위험 요인이 발견되지 않았습니다. 안전합니다!")
    else:
        for reason in failed_reasons:
            print(f"▶ 위험 요인: {reason}")



def recommend_password(user_password):
    print("\n--- 맞춤형 추천 비밀번호 ---")
    recommended = user_password + "2026!@"
    print(f"기존 비밀번호를 보완한 추천 비밀번호: {recommended}")
    print("TIP: 연속된 문자는 피하고, 대소문자와 숫자를 골고루 섞어주세요.")



if __name__ == "__main__":
    print("====== 회원가입 비밀번호 안전성 진단 프로그램 ======")
    print("※ 주의: 실제 사용 중인 개인 비밀번호는 입력하지 마세요.")
    
    
    user_input = input("검사할 가상의 비밀번호를 입력하세요: ")
    
   
    has_space = 0  
    for char in user_input:
        if char == " ":  
            has_space = 1  
            break
            
    
    if has_space == 1:
        print("\n[오류] 비밀번호 중간에 공백(띄어쓰기)을 포함할 수 없습니다.")
        print("유효하지 않은 입력이므로 프로그램을 종료합니다.")
        
    else:
        
        reasons = []
        score = evaluate_password(user_input, password_criteria, reasons)
        
       
        print("\n==============================")
        print(f"최종 안전성 점수: {score}점")
        if score >= 4:
            print("최종 등급: [안전] 사용 가능한 비밀번호입니다.")
        elif score >= 1:
            print("최종 등급: [보통] 보안 강화를 권장합니다.")
        else:
            print("최종 등급: [위험] 비밀번호를 변경해야 합니다.")
        print("==============================")
        
        
        want_recommend = input("\nQ1. 추천 비밀번호를 생성해 드릴까요? (Y/N): ")
        if want_recommend == 'Y' or want_recommend == 'y':
            recommend_password(user_input)
            
        print("\n프로그램을 종료합니다. 감사합니다.")