import os
curdir = os.path.join(os.curdir, '..')

while 'source' not in os.listdir(curdir):
    curdir = os.path.join(curdir, '..')
root_dir = curdir

def checkDuplicate(newPlayer):
  with open(f"{root_dir}/source/leaderboard.txt", 'r') as file:
      lines = file.readlines()
      for line in lines:
        parts = line.strip().split(':')
        if newPlayer.lower() == parts[0].lower():
          return True
      return False
