* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/materials-introduction.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html)
  * Introduction to materials


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html)
Materials
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-material.html)
Create and assign a material
# Introduction to materials
To draw something in Unity, you must provide information that describes its shape, and information that describes the appearance of its surface. You use [meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html) to describe shapes, and materials to describe the appearance of surfaces.
Materials and **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) are closely linked; you always use materials with shaders.
## Render pipeline compatibility
Feature | Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) | High Definition Render Pipeline (HDRP) | Custom Scriptable Render Pipeline (SRP) | Built-in Render Pipeline  
---|---|---|---|---  
Materials | Yes | Yes | Yes | Yes  
## Material fundamentals
A material contains a reference to a [Shader object](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject). If that Shader object defines [material properties](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html), then the material can also contain data such as colors or references to textures.
The [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material) class represents a material in C# code. For information, see [Using Materials with C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/MaterialsAccessingViaScript.html).
A material asset is a file with the `.mat` extension. It represents a material in your Unity project. For information on viewing and editing a material asset using the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, see [Material Inspector reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html).
## Material Variants
Unity supports functionality for creating variants of Materials. To learn more about this functionality, see [Material Variants](https://docs.unity3d.com/6000.0/Documentation/Manual/materialvariant-landingpage.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html)
Materials
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-material.html)
Create and assign a material
