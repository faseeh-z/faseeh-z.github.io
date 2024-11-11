# My Static Site Generator
This software generates multiple static websites with a cohesive look and feel, using only the provided content and metadata. You simply supply the text and components to include on each page, with most of the HTML formatting capabilities, and the program produces static sites. It allows you to define common elements, like headers and footers, which are applied consistently across all sites.

This program was developed specifically for my personal website, with certain unique requirements in mind. While it's optimized for that use case, it may still be useful for your own project. Feel free to download and give it a try! You may need to make some adjustments to the source code to better align with your setup. While it's tailored to a specific purpose, it could still be useful.

## How to Use
Your sites may be placed as subfolders in the `sites` directory. Name it whatever you like. It doesn’t reflect in your final output.

Each subfolder should contain two files:
1. **content.html** (For the actual html content)
2. **metadata.yaml** (Such as the page title, filename, etc)

Type in your content in `content.html` using simple tags like `h1`, `h2`, `p`, `a`, ect **without boilderplate code and tags like `html`, `head`, `title` etc**. The content will be directly placed in a division on the generated website. Keep that in mind.

You can include images and videos in `content.html` simply with an img tag, as demonstrated below.
```html
<img src="path/to/your/image">
```
If you have a video,
```html
<video autoplay muted loop>
    <source src="path/to/your/video.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>
```
The `img` and `video` tag comes with necessary styling. But you can change it by modifying the CSS source file in `assets/styles.css`. I recommend placing your video and image files in the respective subfolders in the assets directory.

The `metadata.yaml` may look like this.
```yaml
title: Title of the site.
filename: Name of the html file to be generated.

download_links:
  - [Text to show next to the download button, https://path/to/file]
  - [Text to show next to the download button, https://path/to/file]
```
Each generated site has a dedicated section in the bottom to place the items which can be downloaded in a table. The generator creates columns for each text-link pair in `download-links` in `metadata.yaml`, with the text shown at the right and a *Download* button on the left pointing to the corresponding link.

Now you have completed creating one of your site source code. Repeat this until you have created as many as you want.

### Generate Static Site
After creating source codes for all sites, simply run the `generate-static-site.py` file, and the sites will be generated in the root directory.

## How to Customize
As I mentioned before, this was created for a very specific use case. You'll need to edit the source code for futher customization. Fortunately, the source code is simple and is easy to modify.

If you want to edit the styles, go to `assets/styles.css` and modify it as you wish. If you want to add a custom header or footer, you can directly modify the `generate-static-site` file to include them in the final output. You can also add more functionality if you have something specific in mind. You have the complete control, because you have the source code!

# Thanks for Everything
It is your support that keeps me motivated throughout each project’s development journey. Every piece of feedback, suggestion, and encouragement helps me improve and strive to create better results. Thank you for being an invaluable part of this journey. I look forward to achieving even greater things together!

[Visit My Website](https://faseeh-official.github.io/)<br>
[Feedback](https://forms.office.com/r/jN1SMAmma5)<br>
[My YouTube Channel](https://youtube.com/@coderapids?si=Pd3PXfRjw141buM_)<br>

See you again!