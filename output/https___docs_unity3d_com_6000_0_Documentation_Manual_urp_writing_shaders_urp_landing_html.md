* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-landing.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
  * Examples of writing a custom shader in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
Writing custom shaders in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-basic-prerequisites.html)
Create a sample scene in URP
# Examples of writing a custom shader in URP
Techniques for writing **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP).
Each example covers some extra information compared to the basic shader example. If you’re new to writing shaders using Unity’s **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab) language, consider going through the sections in the order of appearance on this page.
**Page** | **Description**  
---|---  
[Create a sample scene in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-basic-prerequisites.html) | Create a sample **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) for writing shaders in URP.  
[Write an unlit basic shader in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-basic-unlit-structure.html) | An example of a basic URP shader that fills a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) shape with a color.  
[Write an unlit shader with color input in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-color.html) | An example of a URP shader that adds the **Base Color** property to a material.  
[Draw a texture in a shader in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-texture.html) | An example of a URP shader that draws a texture on a mesh.  
[Visualize normal vectors in a shader in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-normals.html) | An example of a URP shader that visualizes the normal vector values on a mesh.  
[Write depth only in a shader in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-depth-only.html) | Add a depth prepass that writes the depth of objects before the opaque and transparent passes.  
[Reconstruct world space positions in a shader in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-reconstruct-world-position.html) | An example of a URP shader that reconstructs the world space positions for **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) using a depth texture and screen space UV coordinates.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
Writing custom shaders in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-basic-prerequisites.html)
Create a sample scene in URP
