class product:
  def __init__(self, pid, name, price, stock):
    self.name = name
    self.pid = pid
    self.price=price
    self.stock=stock
  def caltotalprice(self):
    print(int(self.price * 1.12))

p1 = product(11,"Powder",25,10)
p1.caltotalprice()

p2=product(12,"Tablets",100,30)
print(p2.name)
print(getattr(p1,'stock'))
print(hasattr(p2,'st'))

