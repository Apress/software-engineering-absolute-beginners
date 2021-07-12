class DB:
   def connect(self):
       print('DB connect class')

class LogFiles:
   def write(self):
       print('LogFiles connect class')

class InheritanceAccess(LogFiles, DB): #needs database access and log access
   def __init__(self):
       print('Inheritance')

class CompositionAccess(): #needs database access and log access
   def __init__(self, DB, LogFiles):
       print('Composition')

inheritance = InheritanceAccess()
composition = CompositionAccess(DB, LogFiles)
