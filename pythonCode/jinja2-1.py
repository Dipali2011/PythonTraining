from jinja2 import Template

name = input("Enter name")
tn = Template("hello {{ name }}")
msg =tn.render(name=name)

print(msg)

name = "john"
age = 25

tm = Template("my name is {{name}} and I am {{age}}")
msg = tn.render(name=name, age=age)
print(msg)