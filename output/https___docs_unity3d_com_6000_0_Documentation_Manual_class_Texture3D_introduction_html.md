* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D-introduction.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [3D textures](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D.html)
  * Introduction to 3D textures


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D.html)
3D textures
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D-import.html)
Create a 3D texture
# Introduction to 3D textures
A 3D texture is a bitmap image that contains information in three dimensions rather than the standard two. 3D textures are commonly used to simulate volumetric effects such as fog or smoke, to approximate a volumetric 3D **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh), or to store animated textures and blend between them.
The source texture files for **2D Array** and **3D** Textures are divided into cells; these textures are called flipbook textures. When Unity imports flipbook textures, it places the contents of each cell into its own 2D array layer or 3D texture slice.
For example, an image with 8x8 cells of smoke effect frames looks like this as a default 2D texture:
![Flipbook image as a 2D shape](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TextureImporter-Flipbook-2D.jpg) Flipbook image as a 2D shape
But when you correctly import is as a 3D texture with 8 Columns and 8 Rows, it looks like this:
![Flipbook image as a 3D shape](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TextureImporter-Flipbook-3D.jpg) Flipbook image as a 3D shape
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D.html)
3D textures
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D-import.html)
Create a 3D texture
