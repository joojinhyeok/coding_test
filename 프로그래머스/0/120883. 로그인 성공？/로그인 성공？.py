def solution(id_pw, db):
    # db를 딕셔너리로 변환하면 훨씬 편하게 작업할 수 있어요.
    # {"id": "password", ...} 형태로 바뀝니다.
    db_dict = dict(db)
    
    my_id = id_pw[0]
    my_pw = id_pw[1]

    # 1. db에 아이디가 존재하는지 확인
    if my_id in db_dict:
        # 2. 아이디가 존재한다면, 비밀번호가 일치하는지 확인
        if db_dict[my_id] == my_pw:
            return "login"  # 아이디, 비번 모두 일치
        else:
            return "wrong pw" # 아이디는 있지만, 비번이 틀림
    else:
        # 3. db에 아이디가 아예 존재하지 않음
        return "fail"