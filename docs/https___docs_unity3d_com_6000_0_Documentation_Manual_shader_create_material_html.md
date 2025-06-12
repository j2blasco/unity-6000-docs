* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-create-material.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Configuring material properties in prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-configure-properties.html)
  * Creating a material from a prebuilt shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-configure-properties.html)
Configuring material properties in prebuilt shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderTextureMaps.html)
Texture maps
# Creating a material from a prebuilt shader
The Standard **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) allows for many configurations in order to represent a great variety of material types. Values can be set with texture maps or colour pickers and sliders. Generally UV mapping is required in conjunction with textures to describe which part of your **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) refers to which part of the texture map. The Standard Shader material allows you therefore to have different material properties across the same mesh when used in conjunction with specular and smoothness map or a metallic map. In other words you can create rubber, metal and wood on one mesh where the resolution of the texture can exceed the polygon topology allowing for smooth borders and transition between material types, of course this has implications for a greater complexity in the workflow, but this will depend on your texture creation method.
Textures for your materials tend to be generated in one of two ways - painting and compositing in a 2D image editor like Photoshop, or rendering / baking from your 3D package, where you can also make use of higher resolution models to generate your **normal maps** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap) and occlusion maps in addition to the albedo, specular and other maps. This workflow varies dependent on the external packages used.
Generally no texture map should contain inherent lighting (shadows, highlights, etc). One of the advantages of PBS is that objects react to light as you would expect, which is not possible if maps already contain lighting information.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-configure-properties.html)
Configuring material properties in prebuilt shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderTextureMaps.html)
Texture maps
