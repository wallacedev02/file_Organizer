import os
from pathlib import Path
def orgDirectori(function):
  def wrapper(*args, **kwargs):
      returnFunc = function(*args, **kwargs)
      separateExtension = returnFunc.split('.')
      upperExtension = separateExtension[1].upper()
      return print(upperExtension)
  return wrapper