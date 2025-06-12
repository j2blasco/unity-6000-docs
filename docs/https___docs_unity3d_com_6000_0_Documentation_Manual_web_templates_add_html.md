* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-add.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Build and distribute a Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building-distribution.html)
  * [Web templates](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-templates.html)
  * Add a custom Web template


[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-intro.html)
Using Web templates
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-structure.html)
Web template structure and instantiation
# Add a custom Web template
Create a custom Web template to control the appearance of the HTML page that displays your content.
Custom templates appear in [Web Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsWebGL.html) under **Web Template** with the folder name and thumbnail image you provide.
## Create a custom template
The easiest way to create a custom Web template is to copy a built-in template folder then modify it to meet your needs. Each template folder contains an `index.html` file along with any other resources the page needs, such as images or stylesheets.
To create a custom template:
  1. Copy the built-in Default or Minimal template folder from `<Unity Installation>/PlaybackEngines/WebGLSupport/BuildTools/WebGLTemplates/`.   
**Note:** On macOS, you can find the Unity Installation folder in the Applications folder.
  2. In your project’s `Assets` folder, create a subfolder called `WebGLTemplates`.
  3. Place the copied template folder in the `Assets/WebGLTemplates` folder.
  4. Rename the copied template folder so you can identify it later.


## Add a thumbnail image
To give the template a thumbnail image for reference:
  1. Add a `128x128-pixel` image to the template folder.
  2. Name the image `thumbnail.png`.


## Additional resources
  * [Using Web templates](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-intro.html)
  * [Web template variables](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-variables.html)
  * [Web template structure and instantiation](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-structure.html)
  * [Web template build configuration and interaction](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-build-configuration.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-intro.html)
Using Web templates
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-structure.html)
Web template structure and instantiation
