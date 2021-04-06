# Media Converter

Compilation of documents converter. Join as contributor and add more function. Custom it freely :wink:

## Requirements

- opencv-python
- Pillow
- pyheif
- whatimage

## Installing

**Pip (python3)**

```bash
pip3 install opencv-python
pip3 install Pillow
pip3 install pyheif
pip3 install whatimage
```

## Image Converter

- Convert JPG to JPG

  ```python
  def JPG2JPG(filename, rescale_size=80):
      image = cv2.imread(filename, cv2.IMREAD_LOAD_GDAL)

      scale_percent = rescale_size  # percent of original size
      width = int(image.shape[1] * scale_percent / 100)
      height = int(image.shape[0] * scale_percent / 100)
      dim = (width, height)

      # resize image
      image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
      cv2.imwrite(
          f"{OUT_DIR}/{filename}.jpg", image)
  ```

- Convert PNG to JPG

  ```python
  def PNG2JPG(filename):
      image = Image.open(filename)
      rgb_image = image.convert('RGB')
      rgb_image.save(
          f"{OUT_DIR}/{filename}.jpg", "JPEG")
  ```

- Convert HEIF to JPG

  ```python
  def HEIF2JPG(filename):
      heif_file = pyheif.read(open(f"{filename}", "rb").read())
      image = Image.frombytes(
          heif_file.mode,
          heif_file.size,
          heif_file.data,
          "raw",
          heif_file.mode,
          heif_file.stride,
      )
      rgb_image = image.convert('RGB')
      # rgb_image.thumbnail((2000, 2000))
      rgb_image.save(
          f"{OUT_DIR}/{filename}.jpg", "JPEG")
  ```

## Audio Converter

Convert Audio using [pydub](https://github.com/jiaaro/pydub)

- Convert MP3/M4A/etc to WAV

  ```python
  def Audio2WAV(input_file, output_type="wav"):
      try:
          song = AudioSegment.from_file(
              input_file, format=f"{input_file.split('.')[-1]}")
      except:
          print("Failed")
      song.export(f"{OUT_DIR}/{input_file.split('.')[0]}.{output_type}",
                  format=f"{output_type}")
  ```
