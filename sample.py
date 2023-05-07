# Python program to demonstrate
# single inheritance

import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='entellio', password='Gk@991225')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class



class Child(Parent):
	def func2(self):
		print("This function is in child class.")


# Driver's code
object = Child()
object.func1()
object.func2()



