# ultramarine_meme
a simple YOASOBI &lt;Ultramarine> meme pic generator

## How to use
First download this git to your own directory:
```shell
git clone https://github.com/SeanCho1996/ultramarine_meme.git
```
Make sure you have installed all the dependencies:
```shell
pip install -r requirements.txt
```
Then run with
```shell
python ultramarine.py -i PATH_TO_YOUR_IMAGE
```
## Potential Issues
You may need to modifie Line 87:
```python
font_path = f"/System/Library/Fonts/STHeiti Light.ttc"
```
to your own font path if you're not using a MacOS device.
