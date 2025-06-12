* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-graphics.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web development](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-develop.html)
  * Web graphics


[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-caching.html)
Cache behavior in Web
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-audio.html)
Audio in Web
# Web graphics
[WebGL](https://www.khronos.org/webgl/)A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WebGL) is an API for rendering graphics in web browsers, which is based on the functionality of the OpenGL ES graphics library. WebGL 2.0 roughly matches with the OpenGL ES 3.0 functionality.
## Camera clear
By default, Unity Web clears the drawing buffer after each frame, which means the content of the frame buffer clears regardless of the [Camera.clearFlags](https://docs.unity3d.com/ScriptReference/Camera-clearFlags.html) setting. However, you can change this behavior at instantiation time. To do this, set `webglContextAttributes.preserveDrawingBuffer` to `true` in the `index.html` file of your Web template.
**Note** : If you set any [WebGL context attributes](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/getContextAttributes), you must also add a line to preserve the **Power Preference** [Player setting](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsWebGL.html#Publishing).
```
script.onload = () => {
  config['webglContextAttributes'] = {
    preserveDrawingBuffer: true, //Add this line to preserve the Camera.clearFlags setting
    powerPreference: {{{ WEBGL_POWER_PREFERENCE }}} //Add this line to preserve the Power Preference Player setting
  };
  createUnityInstance(canvas, config, (progress) => {


```

## Global illumination
Unity Web only supports [baked GI](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingInUnity.html#globalIllumination). Realtime **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination) isn’t currently supported in Web. In addition, Unity Web supports Non-Directional **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) only.
## Linear rendering
Some web browsers don’t support [sRGB DXT texture compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride). This can decrease the quality of rendering performance when using linear rendering, due to runtime decompression of all the DXT textures.
## Video clip importer
You can’t use `VideoClipImporter` to import video clips to your Unity project, because it might increase the initial asset data download size and prevent network streaming. For video playback, use the URL option in the VideoPlayer component and place the asset in the StreamingAssets/ directory to use the built-in network streaming of your browser.
## Web shader code restrictions
The [WebGL 2.0 specification](https://www.khronos.org/registry/webgl/specs/2.0/) imposes some limitations on GLSLS **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) code. This is mainly relevant when you write your own shaders. Here are some of the restrictions:
  * **Precision qualifiers** : WebGL 2.0 requires you to specify the precision of all variables in the shader. You can use `highp`, `mediump`, or `lowp` to specify the precision of the variable. If you don’t specify the precision, the shader will use the default precision, which is `mediump`. You can also use `precision` to specify the precision of a block of variables.


**Note:** Due to limited available memory in Web, avoid including unwanted shader variants which can lead to unnecessary memory usage. Therefore, it’s recommended to familiarize yourself with [shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)A verion of a shader program that Unity generates according to a specific combination of shader keywords and their status. A Shader object can contain multiple shader variants. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadervariant) and [shader stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-stripping.html), and take extra care to ensure that you don’t add shaders with too many variants (for example, Unity’s [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html)) to the [Always-included Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#Always) section in [Graphics Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html).
## Font rendering
Unity Web supports dynamic font rendering similar to other Unity platforms. However, as it doesn’t have access to the fonts installed on the user’s machine, if you want to use any fonts, make sure to include them in the project folder (including any fallback fonts for international characters, or bold/italic versions of fonts), and [set as fallback font names](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-fallback-font.html).
## Anti-aliasing
WebGL supports anti-aliasing on most (but not on all) combinations of browsers and GPUs. To use it, anti-aliasing must be enabled in the default [Quality](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html) setting for the Web platform.
## Reflection probes
Unity Web supports all reflection probes.
## WebGL 2.0 support
Unity includes support for the [WebGL 2.0 API](https://www.khronos.org/registry/webgl/specs/latest/2.0/), which brings OpenGL ES 3.0-level rendering capabilities to the web. By default, Unity Web builds support the WebGL 2.0 API.
Browsers with WebGL 2.0 support have the following advantages:
  * The content in the Standard Shader is of high quality.
  * Support for [GPU Instancing](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing.html) and directional lightmap.
  * There’s no restrictions on indexing and loops in shader code.
  * Improved performance.


### Additional resources:
  * [Reflection Probe](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe)
  * [Build your Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building.html)
  * [Web Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsWebGL.html)


* * *
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-caching.html)
Cache behavior in Web
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-audio.html)
Audio in Web
