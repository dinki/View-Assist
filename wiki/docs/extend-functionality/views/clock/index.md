# Clock View

### Default
![](./clockview.png)
### Alternative
![](./clockaltview.png)
* **Description**: Provides a view for presenting the time, data and weather conditions
* **Default name**:  clock
* **Current Version**: v1.0.0
* **Code link**:  [Clock View Raw Code](https://raw.githubusercontent.com/dinki/View-Assist/main/View%20Assist%20dashboard%20and%20views/views/clock/clock.yaml) [Clock View Alternative Raw Code](https://raw.githubusercontent.com/dinki/View-Assist/refs/heads/main/View%20Assist%20dashboard%20and%20views/views/clock/clockalt.yaml)
* **Special Requirements**: A background image will need to be upload to the HA server and the view code modified to use it

## Installation 

[![Image](https://img.youtube.com/vi/W3wbLjF1n_o/mqdefault.jpg)](https://www.youtube.com/watch?v=W3wbLjF1n_o)

Detailed install video:  https://youtu.be/QmWDNtikHaU



---
One variable in the configuration will need to be made for the background image to be visible:

```
variables:
  background: /local/viewassist/beachcliff.jpg
```
The background image will need to be uploaded to the web directory located within the config directory of the Home Assistant server.  That path is then added to the configuration file.

Some example, free backgrounds are provided in the 'Sample_Backgrounds' directory.  These have all been downloaded using the free license from unsplash.com .  I encourage you to browse this site or any others and find an image that fits your needs and style.


Sample background image credits:

beachcliff.jpg
https://unsplash.com/photos/a-black-and-white-photo-of-a-beach-and-cliffs-TSh4_IYjHRc

birdseyeview.jpg
https://unsplash.com/photos/birds-eye-view-of-mountain-mqO0Rf-PUMs

brownwoodenboard.jpg
https://unsplash.com/photos/brown-wooden-board-6vvIBTvL90A

beigepetalflower.jpg
https://unsplash.com/photos/beige-petaled-flower-on-polka-dot-textile-b12Dp5ynzvQ

greenleafedplant.jpg
https://unsplash.com/photos/green-leafed-plant-COCm5JFTfHc

chairsonbeach.jpg
https://unsplash.com/photos/a-couple-of-chairs-sitting-on-top-of-a-sandy-beach-wk-Z8MlkC7U

pinkbluesky.jpg
https://unsplash.com/photos/a-pink-and-blue-sky-with-a-few-clouds-GLf7bAwCdYg

## Changelog

| Version | Description |
| ------- | ----------- |
| v 1.0.0 | Initial release |


