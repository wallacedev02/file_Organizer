from pathlib import Path
import os
from Decorators_Manager_Path import orgDirectori

# def get_path_files(rootPath):
#   rootPath = Path(rootPath)
#   filePaths = rootPath.iterdir()
#   extensionList= []
  
 
  
#   for file in filePaths:
#     extensionList.append(file.suffix[1:])
#   uniquesExtension = set(extensionList)



#   for extensionsFilePath in uniquesExtension:
#     if extensionsFilePath:
#       os.mkdir(f'{rootPath}\{extensionsFilePath}')
      
  
# print(get_path_files('Verificador_de_extensão'))



class Manager_path:
  def __init__(self, relativePath):
    # self.rootPath = rootPath
    self.relativePath = relativePath
  
  @orgDirectori
  def createFile (self,nameNewFile):
    with open(f'{self.relativePath}/{nameNewFile}', "w") as f:
        nameFile = nameNewFile
    return nameFile
  # def moveFile (self):
  
  # def copyFileOrFolder(self)  
  
explorador = Manager_path('Verificador_de_extensão')
print(explorador.createFile('nameCase.py'))

