* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture-configure.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Rendering to a texture](https://docs.unity3d.com/6000.0/Documentation/Manual/render-texture-landing.html)
  * [Drawing to textures with shaders via Custom Render Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture-landing.html)
  * Control when a Custom Render Texture updates


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture-write-shader.html)
Write a shader for a Custom Render Texture
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MovieTexture-landing.html)
Playing video in Movie Textures
# Control when a Custom Render Texture updates
## Update Zones
When Unity updates a Custom **Render Texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture), it uses the Material to update the whole texture at once by default. The Custom Render Texture allows you to define zones of partial update. You can use this to define as many zones as you want and the order in which the zones are processed.
You can use update zones for various purposes. For example, you could have multiple small zones to splat water drops on the texture and then do a full pass to simulate the ripples. This can also be used as an optimization when you know that you don’t need to update the full texture.
Update zones have their own set of properties. The **Update Zone Space** is visible in the display. Coordinates depend on the **Dimension** of the texture: 2D for 2D and Cube textures, or 3D for 3D textures.
## Controlling Custom Render Texture from Script
You can access most of the Custom Render Texture functionalities in the Scripting API. You can also change Material parameters, update frequency, update zones, request an update, and more using a script.
When Unity updates or initializes a Custom Render Texture, it uses the current properties to render the next frame. This guarantees that any Material that uses this texture has an up-to-date result. For example, in the following script Unity performs two updates using the second Update Zone array:
`customRenderTexture.updateZones = updateZones1;`
`customRenderTexture.Update();`
`customRenderTexture.updateZones = updateZones2;`
`customRenderTexture.Update();`
**Note:** Unity does not update or initialize a Custom Render Texture at the same time you call `Update()` or `Initialize()`. This is because Unity always updates and initializes a Custom Render Texture at the start of the next frame.
## Double Buffered Custom Textures
You can double-buffer Custom Render Textures. To do this, enable **Double Buffered** in the [Custom Render Textures component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture.html), or use [`CustomRenderTexture.doubleBuffered`](https://docs.unity3d.com/ScriptReference/CustomRenderTexture-doubleBuffered.html).
Double-buffering means that inside one Custom Render Texture there are two textures which Unity can swap after each update. This allows you to read the result of the last update while writing a new result in the Custom Render Texture.
Double-buffering is particularly useful if the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) needs to use the content the Unity has already written in the texture but can’t mix the values with classic blend modes. This is also required if the shaders have to sample different **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) from the preceding result.
**Performance warning** : Double-buffering currently involves a copy of the texture at each swap which can lead to a drop in performance depending on the frequency at which it is done and the resolution of the texture.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture-write-shader.html)
Write a shader for a Custom Render Texture
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MovieTexture-landing.html)
Playing video in Movie Textures
