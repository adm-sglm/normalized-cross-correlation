import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
  src = cv2.imread('small_check.jpeg', cv2.IMREAD_COLOR)

  gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
  gray = np.float32(gray)

  sbl_x = cv2.Sobel(gray, cv2.CV_16S, 1, 0, ksize=3, scale=1)
  sbl_y = cv2.Sobel(gray, cv2.CV_16S, 0, 1, ksize=3, scale=1)

  abs_x = cv2.convertScaleAbs(sbl_x)
  abs_y = cv2.convertScaleAbs(sbl_y)

  grad = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)

  dst = cv2.cornerHarris(gray, 2, 3, 0.04)
  print(dst.max())
  print(0.01*dst.max())
  # dst = cv2.dilate(dst, None)

  plt.imshow(dst, cmap="gray")

  plt.show()

  src[dst>0.01*dst.max()] = [0, 0, 255]

  # cv2.imwrite('output.tiff', src)

  # cv2.imshow('Image', src)
  # cv2.imshow('Harris', dst)
  # cv2.imshow('X derivative', abs_x)
  # cv2.imshow('Y derivative', abs_y)
  # cv2.imshow('Gradient', grad)

  cv2.waitKey(0)

if __name__ == "__main__":
  main()