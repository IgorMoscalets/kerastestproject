import numpy as np
import cv2

for i in range(1, 21):
    img_path = "images/good/" + str(i) + ".jpg" 

    img = cv2.imread(img_path)
    mean = 0
    var = 10
    sigma = var ** 1.2
    gaussian = np.random.normal(mean, sigma, (img.shape[0], img.shape[1], 3)) #  np.zeros((224, 224), np.float32)

    noisy_image = np.zeros(img.shape, np.float32)
    
    noisy_image = img + gaussian

    cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
    noisy_image = noisy_image.astype(np.uint8)

    #cv2.imshow("img", img)
    #cv2.imshow("gaussian", gaussian)
    #cv2.imshow("noisy", noisy_image)

    cv2.imwrite("images/bad/" + str(i) + ".jpg", noisy_image);