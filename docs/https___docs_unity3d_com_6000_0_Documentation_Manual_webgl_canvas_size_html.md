* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-canvas-size.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web development](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-develop.html)
  * Configure a Web Canvas size


[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-input.html)
Input in Web
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-browser-access-device.html)
Web browser access to device features
# Configure a Web Canvas size
In a Web application, the canvas element is where the browser draws the graphics when rendering a game. This section describes how to configure the visible size of the Web canvas element, and the resolution that the game renders to.
To configure your Web Canvas size, you must consider the following types of canvas size: 
**Canvas Size elements** | **Description**  
---|---  
**Canvas element CSS size** | This Document Object Model (DOM) specifies the visible area on the web page that the canvas takes up. You can configure the canvas size using HTML or JavaScript.  
**WebGL render target size** | This size specifies the **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) resolution that the GPU renders your game to. You can manage this size in sync with the CSS size to provide pixel-perfect rendering, or decouple it from the CSS size.  
If the above two canvas size elements don’t match, the browser will stretch the rendered **WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WebGL) output to fill the visible canvas area on the web page.
## Decouple the render resolution
Decoupling the render resolution is useful when implementing downscaled low DPI (Dots per inch) rendering on high DPI display. This helps to not only conserve the GPU fill rate power but also helps if your application is sensitive to the rendering resolution. For example, if your application logic uses screen space pixel units, but for the application itself to work properly, it requires a specific resolution.
By default, Unity keeps the canvas element CSS size and the WebGL render target size in sync and provides 1:1 pixel perfect rendering. If the web page in JavaScript modifies the canvas CSS size, Unity will automatically adjust the WebGL render target size to match it. By default, this match is done to implement high DPI rendering. 
### Override DPI scale
If you want to override the DPI scale, open the `index.html` file and add the Unity Instance configuration variable `devicePixelRatio=<double>`. For example, setting `devicePixelRatio=1` on the Web site template page will force Unity to always apply low DPI rendering. Refer to [Web template build configuration and interaction](https://docs.unity3d.com/6000.0/Documentation/Manual/web-templates-build-configuration.html) for an example.
### Manually change the Web canvas render size
To manually configure the canvas size, you must first disable the automatic size synchronization. To do so, in the `index.html` file of the Web template, set the Unity Instance configuration variable to false: `matchWebGLToCanvasSize=false`. When this is set, Unity leaves the render target size of the canvas as-is but you can always configure the size, if required.
For example, to change the CSS size of the canvas, edit the following text in the `index.html` file:
```
<div id="unity-container" style="position: absolute; width: 100%; height: 100%">
  <canvas id="unity-canvas" width={{{ WIDTH }}} height={{{ HEIGHT }}} style="width: 100%; height: 100%"></canvas>
</div>

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-input.html)
Input in Web
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-browser-access-device.html)
Web browser access to device features
