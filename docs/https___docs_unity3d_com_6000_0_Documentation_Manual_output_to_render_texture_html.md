* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/output-to-render-texture.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Rendering to a texture](https://docs.unity3d.com/6000.0/Documentation/Manual/render-texture-landing.html)
  * Render a camera view to a Render Texture


[](https://docs.unity3d.com/6000.0/Documentation/Manual/render-texture-landing.html)
Rendering to a texture
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture-landing.html)
Drawing to textures with shaders via Custom Render Textures
# Render a camera view to a Render Texture
A **Render Texture** is a type of [Texture](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture) that Unity creates and updates at run time. To use a Render Texture, create a new Render Texture using **Assets > Create > Render Texture** and assign it to **Target Texture** in your [Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) component. Then you can use the Render Texture in a **Material** An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material) just like a regular Texture.
To create a live **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) camera in your game, follow these steps:
  1. To create a Render Texture, go to **Assets** > **Create** > **Rendering** > **Render Texture**.
  2. Select **GameObject** > **Camera** to create a second camera.
  3. Assign the **Render Texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) to the **Target Texture** property in the second camera’s ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window.
  4. Select **GameObject** > **3D Object** > **Quad** to create a quad.
  5. Drag the Render Texture onto the **quad** A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Quad). Unity automatically creates and assigns a material that uses the Render Texture.
  6. Enter Play mode. The quad displays the camera view, which updates in real time.

![Render Textures are set up as demonstrated above](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/RenderTextureLiveCam.jpg) Render Textures are set up as demonstrated above
## Additional resources
  * [Render Texture Inspector window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)
  * [Render a camera’s output to a Render Texture in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-to-a-render-texture.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/render-texture-landing.html)
Rendering to a texture
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture-landing.html)
Drawing to textures with shaders via Custom Render Textures
