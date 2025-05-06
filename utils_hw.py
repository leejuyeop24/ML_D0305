# 부모 클래스
class Person:
    def __init__(self, nation, name, height, weight):
        self.nation = nation
        self.name = name
        self.height = height
        self.weight = weight

    # 소개 메서드
    def introduce(self):
        print(f"이름: {self.name}")
        print(f"국적: {self.nation}")

    # 신체 정보 출력 메서드
    def bodyinfo(self):
        print(f"키: {self.height}cm")
        print(f"몸무게: {self.weight}kg")


# 자식 클래스: Student
class Student(Person):
    def __init__(self, nation, name, height, weight, grade):
        super().__init__(nation, name, height, weight)
        self.grade = grade  # 추가 속성 (학년)

    # 학생 소개 메서드 오버라이딩
    def introduce(self):
        super().introduce()
        print(f"학생의 학년: {self.grade}")


# 자식 클래스: Doctor
class Doctor(Person):
    def __init__(self, nation, name, height, weight, specialty):
        super().__init__(nation, name, height, weight)
        self.specialty = specialty  # 추가 속성 

    # 의사 소개 메서드 오버라이딩
    def introduce(self):
        super().introduce()
        print(f"전문 분야: {self.specialty}")


# 실행 코드
if __name__ == '__main__':
    ## 객체 생성
    student = Student("대한민국", "이주엽", 170, 63, "졸업생")
    doctor = Doctor("대한민국", "닥터박", 175, 70, "내과")

    # 객체 메서드 실행
    student.introduce()
    print()
    doctor.introduce()

	