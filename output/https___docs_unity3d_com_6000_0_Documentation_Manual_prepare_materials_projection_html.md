* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/prepare-materials-projection.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Decals and projectors](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-decals.html)
  * [Decals in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/decals-birp.html)
  * Prepare materials for projection in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/decals-birp.html)
Decals in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Projector.html)
Projector component reference for the Built-In Render Pipeline
# Prepare materials for projection in the Built-In Render Pipeline
Use a Projector component to create effects such as:
  * Decal effects, like bullet holes or paint splatters
  * Blob shadows
  * Stylized lighting effects
  * The effect of a real-world projector, using another [Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) that renders to a **Render Texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture)


**Note:** This workflow is compatible only with the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline). For similar functionality in other render pipelines, see [Decals and projectors](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-decals.html).
![A Projector creates a Blob Shadow for a robot](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Projector-BlobShadow.jpg) A Projector creates a Blob Shadow for a robot
A Projector works by projecting a material onto all objects that intersect its frustum. The material must use the Projector/Light or Projector/Multiply **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), available in Unity’s [Standard Assets](https://assetstore.unity.com/packages/essentials/asset-packs/standard-assets-for-unity-2017-3-32351).
When configuring a material to use with the Projector/Light and Projector/Multiply shaders, be aware of the following:
**Cookie texture:**
  * Make sure texture wrap mode is set to “Clamp”
  * Turn on “Replicate Border” option in mipmap related import settings
  * Use uncompressed texture format
  * Projector/Shadow also requires alpha channel to be present (typically Alpha from Grayscale option is ok)


**Falloff texture (if present):**
  * Data needs to be in alpha channel, so typically Alpha8 texture format
  * Make sure texture wrap mode is set to “Clamp”
  * Make sure leftmost **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) column is black; and “Border mipmaps” import setting is on.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/decals-birp.html)
Decals in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Projector.html)
Projector component reference for the Built-In Render Pipeline
