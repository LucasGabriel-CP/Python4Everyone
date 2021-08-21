class Category:
  def __init__(self, Tipo):
    self.name = Tipo
    self.ledger = list()
    self.Tot = 0
  
  def getName(self):
    return self.name

  def deposit(self, amount: float, description = None):
    if description is None:
      description = ''
    self.ledger.append({"amount" : amount, "description" : description})
    self.Tot += amount
  
  def check_funds(self, amount: float):
    return amount <= self.Tot

  def withdraw(self, amount: float, description = None):
    if not self.check_funds(amount):
      return False
    if description is None:
      description = ''
    amount = amount * -1
    self.ledger.append({"amount" : amount, "description" : description})
    self.Tot += amount
    Temp = str(amount)
    return True

  def get_balance(self):
    return self.Tot

  def transfer(self, amount: float, Target):
    if self.withdraw(amount, 'Transfer to ' + Target.name):
      Target.deposit(amount, 'Transfer from ' + self.name)
      return True
    else:
      return False

  def __str__(self):
    Conte = '{:*^30}\n'.format(self.name) 
    i = 0
    while i < len(self.ledger):
      Temp = self.ledger[i]['description']
      line = (Temp[:23], f'{self.ledger[i]["amount"]:.2f}')
      Conte += '{:<23}{:>7}'.format(*line) + '\n'
      i += 1
    Conte += "Total: " + str(self.Tot) 
    return Conte

def create_spend_chart(categories: list()):
  Gastos = list()
  Maior = ''
  Tot = 0
  i = 0
  while i < len(categories):
    Aux = 0
    for j in categories[i].ledger:
      if j['amount'] <= 0:
        Aux += j['amount'] * -1
    Tot += Aux
    Gastos.append(Aux)
    if len(Maior) < len(categories[i].getName()):
      Maior = categories[i].getName()
    i += 1
  
  Cont = 100
  ans = 'Percentage spent by category\n'
  while Cont >= 0:
    ans += '{:3}'.format(Cont) + '| '
    for j in Gastos:
      if (j * 100) / Tot >= Cont:
        ans += 'o  '
      else:
        ans += '   '
    ans += '\n'
    Cont -= 10
  tam = len(categories) * 3 + 1
  ans += '    '
  i = 0
  while i < tam:
    ans += '-'
    i += 1
  ans += '\n     '
  tam = len(Maior)
  i = 0
  while i < tam:
    for j in categories:
      Nome = j.getName()
      if i < len(Nome):
        ans += Nome[i] + '  '
      else:
        ans += '   '
    if i < tam - 1:
     ans += '\n     '
    i += 1  
  
  return ans