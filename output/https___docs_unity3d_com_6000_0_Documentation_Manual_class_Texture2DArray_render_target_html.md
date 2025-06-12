* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray-render-target.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [2D texture arrays](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray.html)
  * Render to a 2D texture array


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray-create.html)
Create a 2D texture array in a script
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray-use-in-shader.html)
Sample a 2D texture array in a shader
# Render to a 2D texture array
To render to a 2D texture array, create a [render texture](https://docs.unity3d.com/6000.0/Documentation/Manual/render-texture-landing.html)A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) and set the **Dimension** property to **2D Array**.
If you use the [`Graphics.SetRenderTarget`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.SetRenderTarget.html) API, set the `depthSlice` parameter to the slice you want to render to.
If the platform supports geometry shaders, use a geometry **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) to render to individual slices, or set `depthSlice` to `-1` to render to all the slices.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray-create.html)
Create a 2D texture array in a script
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray-use-in-shader.html)
Sample a 2D texture array in a shader
