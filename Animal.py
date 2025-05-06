## ---------------------------------------------------------------------------------
## 강아지 데이터를 표현/저장하는 클래스 정의/설계
## ---------------------------------------------------------------------------------
## * 특징/속성/성질/외형 : 품종, 털색상, 눈색상, 무게, 나이, 성별, 이름
## * 행동/기능/동작     : 꼬리친다
## ---------------------------------------------------------------------------------
## 클래스이름 : Animal
## 클래스속성 : kind, coat_color, eye_color, weight, age, gender, name
## 클래스기능 : tailing()
## ---------------------------------------------------------------------------------
class Animal:
	## 객체 즉, 인스턴스 생성 시 Dog마다 속성 저장해주는 메서드
	def __init__(self, kind, coat_color, eye_color, weight, age, gender, name):
		print("Animal__init__()")
		self.kind = kind
		self.coat_color = coat_color
		self.eye_color = eye_color
		self.weight = weight
		self.age = age
		self.gender = gender
		self.name = name
	
	## 메소드이름 : tailing
	## 매개변수들 : 없음
	## 메서드결과 : 없음
	def tailing(self):
		print(f"{self.name }가 꼬리친다.")

	