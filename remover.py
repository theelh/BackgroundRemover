from rembg import remove
import easygui
from PIL import Image

inputPath = easygui.fileopenbox(title='select image file')
outputPath = easygui.filesavebox(title='save file too..')

input = Image.open(inputPath)
ouput = remove(input)
ouput.save(outputPath)