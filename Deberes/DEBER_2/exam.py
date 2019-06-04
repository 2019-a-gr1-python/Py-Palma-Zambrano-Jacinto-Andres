from matplotlib.cbook import get_sample_data
import matplotlib.pyplot as plt
image = plt.imread(get_sample_data('grace_hopper.jpg'))
plt.show(block=True)
plt.interactive(False)
titles = ['Grace Hopper', 'Red channel', 'Green channel', 'Blue channel']
cmaps = [None, plt.cm.Reds_r, plt.cm.Greens_r, plt.cm.Blues_r]

fig, axes = plt.subplots(1, 4, figsize=(13,3))
objs = zip(axes, (image, *image.transpose(2,0,1)), titles, cmaps)

for ax, channel, title, cmap in objs:
    ax.imshow(channel, cmap=cmap)
    ax.set_title(title)
    ax.set_xticks(())
    ax.set_yticks(())

plt.savefig('RGB1.png')