import os
from pathlib import Path


def createFolders(function):
  def wrapper(*args, **kwargs):
    extensions, rootPath = function(*args, **kwargs)
    for extension in extensions: 
      extensionUpper = extension.upper()
      folder = f'{rootPath}/{extensionUpper}_FILES'
      if not os.path.exists(folder):
        os.mkdir(folder)
    return extensions,rootPath
  return wrapper

def orgFiles(func):
  def wrapper(*args,**kwargs):
    extensions,rootPath = func(*args, **kwargs)
    pathBase = Path(rootPath)
    filePath = pathBase.glob('*')
    
    for extension in extensions:
      extensionUpper = extension.upper()
      folderPath = f'{pathBase}/{extensionUpper}_FILES'
      
      # if not os.path.exists(folderPath):
      #     os.mkdir(folderPath)
      
      for file in filePath:
        if file.is_file() and file.suffix [1:] == extension:
          newFileName = f'{folderPath}/{file.name}'
          try:
            # newFilePath = file.with_name(newFileName)
            file.rename(newFileName)
          except Exception as e:
            print(f'erro ao mover {file.name}:{e}')
    return extensions,rootPath
  return wrapper