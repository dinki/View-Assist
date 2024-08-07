# Details for List View
<a href="https://www.youtube.com/watch?v=9hl6zo038Xg"><img src="https://img.youtube.com/vi/9hl6zo038Xg/mqdefault.jpg" width="60%"></a>

Detailed install video:
https://youtu.be/9hl6zo038Xg

This card can be added by copy pasting.  One variable in the configuration will need to be made for the background image to be visible:

```
variables:
  background: /local/viewassist/announcebird.png
```
The background image will need to be uploaded to the web directory located within the config directory of the Home Assistant server.  That path is then added to the configuration file.

You can, of course, use any image you like.  I created this one using a public domain image that you can find [here](https://www.rawpixel.com/image/6293393/vector-background-flower-public-domain)

There are two views, list.yaml and list-nocheckbox.yaml.  Only one is needed, choose the one you would like based on the view you prefer.

## Change log

1.0.0 Initial release

1.0.1 Move list variable out of dictionary
