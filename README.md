# Media Converter

## Image Converter

- Convert JPG to JPG

  ```
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

  ```
  def PNG2JPG(filename):
      image = Image.open(filename)
      rgb_image = image.convert('RGB')
      rgb_image.save(
          f"{OUT_DIR}/{filename}.jpg", "JPEG")
  ```

- Convert HEIF to JPG

  ```
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
