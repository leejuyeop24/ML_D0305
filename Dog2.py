## 다른 모듈 로딩 -------------------------------------------------------------------
from Animal import * 

## ---------------------------------------------------------------------------------
## 강아지 데이터를 표현/저장하는 클래스 정의/설계
## ---------------------------------------------------------------------------------
## * 특징/속성/성질/외형 : 품종, 털색상, 눈색상, 무게, 나이, 성별, 이름
## * 행동/기능/동작     : 짖는다, 문다, 꼬리친다, 죽는척하기(X - 특별한 강아지)
## ---------------------------------------------------------------------------------
## 클래스이름 : Dog
## 클래스속성 : kind, coat_color, eye_color, weight, age, gender, name
## 클래스기능 : bark(), bite(), tailing()
## ---------------------------------------------------------------------------------
class Dog2(Animal):
	## 객체 즉, 인스턴스 생성 시 Dog마다 속성 저장해주는 메서드
	def __init__(self, kind, coat_color, eye_color, weight, age, gender, name):
		print("Dog__init__()")
		self.kind = kind
		self.coat_color = coat_color
		self.eye_color = eye_color
		self.weight = weight
		self.age = age
		self.gender = gender
		self.name = name
	
	## 메소드이름 : bark()
	## 매개변수들 : 없음
	## 메서드결과 : 없음
	def bark(self):
		print(f"{self.name}가 멍 멍 짖는다.")

	## 메서드이름 : bite
	## 매개변수들 : 무엇을 what
	## 메서드결과 : 없음
	def bite(self, what):
		print(f'{self.name}가 {what}을 물고 있다.')



## ---------------------------------------------------------------------------------
## 객체 생성하기
## - 생성 메서드이름 : 클래스이름() ---> 클래스 내부의 _ _init_ _()호출
## ---------------------------------------------------------------------------------
myDog = Dog2("차우차우", "검은색", "검은색", 20, 2, "남자", "차우")
print( id(myDog) )


## ---------------------------------------------------------------------------------
## 객체의 속성과 메서드 사용하기
## - [속성 읽기] 객체변수명.속성명
## - [속성 변경] 객체변수명.속성명 = 새로운값
## - [메서드호출] 갹체변수명.메서드명()
## ---------------------------------------------------------------------------------
## - 메서드 호출/실행
myDog.bark()
myDog.bite('도둑')
myDog.bite('인형')

## - 속성값 읽기
print( myDog.age )

## - 속성값 변경
myDog.age = 3
print( myDog.age )

## 문자열 타입 즉, str타입의 객체 생성
#msg=str("Good Luck")
msg = "Good Luck"
print(	msg.upper()	 )

# numbers=list([1, 2, 3])
numbers = [1, 2, 3]
print(numbers.count(1))