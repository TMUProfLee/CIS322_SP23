import os
curdir = os.curdir

while 'source' not in os.listdir(curdir):
    curdir = os.path.join(curdir, '..')
root_dir = os.path.abspath(curdir)

def checkDuplicate(newPlayer):
  print(root_dir)
  with open(f"{root_dir}/source/leaderboard.txt", 'r') as file:
      lines = file.readlines()
      for line in lines:
        parts = line.strip().split(':')
        if newPlayer.lower() == parts[0].lower():
          return True
      return False
