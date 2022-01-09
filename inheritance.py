class Body():
	def __init__(self,name=''):
		self.name = name
		self.ty = '身體誕生了！'
		self.hp = 100
		self.atk = 20

	def eat(self):
		print('eat something!')

	def sleep(self):
		print('sleeping...')

	def show_status(self):
		print('NAME:', self.name)
		print('TYPE:', self.ty)
		print('HP:', self.hp)
		print('ATK:', self.atk)

class Warrior(Body):
	def __init__(self, name=''):
		super().__init__(name)
		self.ty = '戰士'
		self.atk = 30
	
	def atk_function(self):
		print('now is attacking!!')


class Human(Body):
	def __init__(self,name=''):
		super().__init__(name)
		self.ty = '一般人'



def main():
	steven = Warrior('Steven')
	steven.show_status()
	steven.atk_function()
	steven.sleep()
	alax = Human('Alax')
	alax.show_status()
	alax.eat()

main()