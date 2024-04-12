from passlib.context import CryptContext

# 비밀번호 해싱을 위한 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 비밀번호를 해싱하는 함수
def hash_password(password: str):
    return pwd_context.hash(password)

def main():
    # 인풋값으로 해싱할 비밀번호 받기
    password = input("Enter password to hash: ")
    print(hash_password(password))

main()

# pip install --upgrade bcrypt