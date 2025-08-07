from pathlib import Path
from Decorators_Manager_Path import createFolders, orgFiles

class Manager_path:
  def __init__(self, relativePath):
    self.relativePath = relativePath
  
  
  def createFile (self,nameNewFile):
    with open(f'{self.relativePath}/{nameNewFile}', "w") as f:
        namePath =f'{self.relativePath}/{nameNewFile}' 
    return namePath
  @orgFiles
  @createFolders
  def fileOrganizer(self):
    rootPath= Path(f'{self.relativePath}')
    Extensionslists = []
    for path in rootPath.glob('*'):
      if path.is_file():
        extension = path.suffix[1:]
        Extensionslists.append(extension)
    extensionSet = set(Extensionslists)
    return (extensionSet,rootPath)
    

  
explorador = Manager_path('Verificador_de_extensão')
explorador.fileOrganizer()

