from setuptools import setup

setup(name='gym_rock_paper_scissors',
      version='0.0.124',
      description='OpenAI gym environment for a repeated game of Rock-Paper-Scissors',
      url='https://github.com/Danielhp95/gym-rock-paper-scissors',
      author='Sarios',
      author_email='rockpapersass@xcape.com',
      packages=['gym_rock_paper_scissors', 'fixed_agents'],
      install_requires=['gym']
      )
