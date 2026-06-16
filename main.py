# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20803 김민재
# 프로젝트 주제: 비밀번호 안전성 평가 및 추천 시스템



password_criteria = [
    ["length", 3, "비밀번호 길이가 8자리 이상인가?"],
    ["special_char", 2, "특수문자가 포함되어 있는가?"],
    ["repetition", -3, "동일한 문자가 3번 연속 반복되는가? (감점)"]
]

def evaluate_password(user_password, criteria):
    total_score = 0
    print("\n--- 안전성 검사 시작 ---")
    
  
    for rule in criteria:
        rule_name = rule[0]   "
        score = rule[1]       
        description = rule[2] 
        
        .
        if rule_name == "length":
            
            if len(user_password) >= 8: 
                print(f"[성공] {description} (+{score}점)")
                total_score += score
            else:
                print(f"[실패] {description} (0점)")
                
        elif rule_name == "special_char":
            
            pass 
            
    return total_score