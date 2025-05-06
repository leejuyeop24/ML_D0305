## --------------------------------------------------------------------------------------
## 클래스 정의 및 설계
## --------------------------------------------------------------------------------------

#* 속성/특징/외형 : x좌표, y좌표, 색상, 반지름	===코드화 ==> 변수명 x, y, color, r
#* 행동/기능/역할 : 점그리기, 정보출력			===코드화 ==> 메서드명 drawing(), printinfo()
#* 데이터타입이름 : Point
#* 부모/슈퍼클래스
class Point:


	# 객체/인스턴스 설계 및 속성 초기화 메서드
	# self : 힙 메모리에 저장되는 주소 저장 매개변수
	def __init__(self, x, y, color, r):
		self.x = x
		self.y = y
		self.color = color
		self.r = r

	# 클래스 전용 함수 즉, 메서드 --------------------------
	# 메서드이름 : drawing
	# 매개변수들 : 없음
	# 메서드결과 : 반환값 없음
	def drawing(self):
		# 예) 파랑색 점 
		print(f"{self.color} ")

	# 메서드이름 : printinfo
	# 매개변수들 : 없음
	# 메서드결과 : 반환값 없음
	def printinfo(self):
		# 예) 위치 : 9, 5
		#     크기 : 3
		#     색상 : 파랑색
		print(f"위치: {self.x}, {self.y} ")
		print(f"크기: {self.r}")
		print(f"색상: {self.color}")


# 속성/특징/외형 : x, y, z, color, r
# 행동/기능/역할 : drawing(), printinfo()
# 데이터타입이름 : Point3D
# 부모클래스이름 : Point
# 자식/슈퍼클래스
class Point3D(Point):
	# 객체/인스턴스 생성 및 속성 초기화 메서드
	def __init__(self, x, y, z, color, r):
		# 부모 생성
		super().__init__(x, y, color, r)
		# 자식 속성 생성 및 저장
		self.z = z
	
	# 메서드 오버라이딩(overriding) : 상속 받은 메서드 재정의
	def printinfo(self):
		# 예) 위치 : 9, 5, z
		#     크기 : 3
		#     색상 : 파랑색
		print(f"종류: 3D Point")
		print(f"위치: {self.x}, {self.y}, {self.z}")
		print(f"크기: {self.r}")
		print(f"색상: {self.color}")

## 매직/스페셜 변수 _ _name_ _
print(f'__name__ -> {__name__}')

if __name__ == '__main__':
	## ---------------------------------------------------------
	## 객체/인스턴스 생성 및 사용
	## ---------------------------------------------------------
	## 객체/인스턴스 생성
	blackPoint = Point(10, 10, 'black', 5)
	redPoint = Point3D(5, 5, 5, 'red', 5)

	## 객체/인스턴스 사용
	blackPoint.drawing()
	redPoint.drawing()

	## 속성 변경
	redPoint.r = 10

	## 정보 출력 메서드 실행
	blackPoint.printinfo()
	redPoint.printinfo()