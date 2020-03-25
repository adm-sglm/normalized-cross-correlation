from scipy import signal
import imageio
import matplotlib.pyplot as plt
import numpy as np

def main():

  img = imageio.imread('appartment.jpg')

  patch = imageio.imread('patch.jpg')
  patch_shrinked = imageio.imread('patch_shrinked.jpg')

  img = img - img.mean()
  patch = patch - patch.mean()
  patch_shrinked = patch_shrinked - patch_shrinked.mean()

  corr = signal.correlate2d(img, patch, boundary="symm", mode="same")
  corr2 = signal.correlate2d(img, patch_shrinked, boundary="symm", mode="same")

  match_idx = np.unravel_index(np.argmax(corr), corr.shape)
  match2_idx = np.unravel_index(np.argmax(corr2), corr2.shape)

  fig, ((ax1, ax2, ax3), (ay1, ay2, ay3)) = plt.subplots(2,3)
  ax1.imshow(img, cmap="gray")
  ax1.set_title('Original')
  ax2.imshow(patch, cmap="gray")
  ax2.set_title('Patch')
  ax3.imshow(corr, cmap="gray")
  ax3.set_title('Cross Correlation')
  ax3.set_axis_off()
  ax1.plot(match_idx[1], match_idx[0], "ro")

  ay1.imshow(img, cmap="gray")
  ay1.set_title('Original')
  ay2.imshow(patch_shrinked, cmap="gray")
  ay2.set_title('Patch scaled down')

  ay3.imshow(corr2, cmap="gray")
  ay3.set_title('Cross Correlation')
  ay3.set_axis_off()

  ay1.plot(match2_idx[1], match2_idx[0], "ro")

  plt.show()

if __name__ == "__main__":
  main()