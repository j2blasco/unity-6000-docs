* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/simplifying-distant-meshes-with-level-of-detail-lod.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * Simplifying distant meshes with level of detail (LOD)


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Example-CreatingaBillboardPlane.html)
Create a quad mesh via script
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)
Mesh LOD
# Simplifying distant meshes with level of detail (LOD)
Strategies and resources for applying **level of detail** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#levelofdetail) (LOD) techniques to meshes, to reduce the number of GPU operations that Unity requires to render distant meshes.
This section contains information on LOD techniques for meshes. For information on LOD techniques for **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), see [SubShader LOD value](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderLOD.html).
**Topic** | **Description**  
---|---  
[Mesh LOD in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html) | Understand level of detail (LOD) and LOD levels for meshes, and how LOD techniques can improve performance.  
[Configure mesh LOD](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-mesh-lod.html) | Configure mesh-specific and project-wide LOD settings.  
[Import a mesh with LOD settings](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-lod-meshes.html) | Import meshes with LOD levels from third-party applications into Unity and retain their LOD settings.  
[LOD Group component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html) | Explore the properties and settings in the **LOD Group** A component to manage level of detail (LOD) for GameObjects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LODGroup) component to manage level of detail on a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh).  
[2D images for low level of detail (LOD)](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-images-lod.html) | Techniques and resources for using 2D **billboards** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard) to simplify 3D meshes that are far away.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Example-CreatingaBillboardPlane.html)
Create a quad mesh via script
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)
Mesh LOD
