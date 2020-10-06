class Agent:
  def say_hello(self, first_name):
      return "Bien le bonjour " + first_name + "!"
  def __init__(self, agreeableness):
      self.agreeableness = agreeableness




first_agent = Agent(0)
print(first_agent.agreeableness)

