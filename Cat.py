# ---------------------------------------------------------------------------------
## 고양이이 데이터를 표현/저장하는 클래스 정의/설계
## ---------------------------------------------------------------------------------
## * 특징/속성/성질/외형 : 품종, 털색상, 눈색상, 무게, 나이, 성별, 이름
## * 행동/기능/동작     : 야옹거린다, 식빵굽는다, 사람을 째려본다
## ---------------------------------------------------------------------------------
## 클래스이름 : Cat
## 클래스속성 : kind, coat_color, eye_color, weight, age, gender, name
## 클래스기능 : headhunting(), golgolsong(), tailing(), gukguk()
## ---------------------------------------------------------------------------------
class Cat:
	def __init__(self, kind, coat_color, eye_color, weight, age, gender, name):
		print("Cat__init__()")
		self.kind = kind
		self.coat_color = coat_color
		self.eye_color = eye_color
		self.weight = weight
		self.age = age
		self.gender = gender
		self.name = name
	
	## 메소드 이름 : headhunting
	## 매개변수들 : 없음
	## 메서드결과 : 없음
	def headhunting(self):
		print(f"{self.name}가 헤드헌팅한다.")

	## 메소드 이름 : golgolsong
	## 매개변수들 : 없음
	## 메서드결과 : 없음
	def golgolsong(self):
		# OO이/가 what를 물고 있다.
		print(f"{self.name}가 골골송 한다.")