import matplotlib.pyplot as plt

lst = [[i + j for j in range(1500)] for i in range(1500)]

im = plt.imshow(lst, cmap='rainbow')
plt.colorbar(im)
plt.show()
