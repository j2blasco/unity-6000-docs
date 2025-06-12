* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/applying-2d-billboards-low-lod-meshes.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Simplifying distant meshes with level of detail (LOD)](https://docs.unity3d.com/6000.0/Documentation/Manual/simplifying-distant-meshes-with-level-of-detail-lod.html)
  * [2D images for low level of detail (LOD)](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-images-lod.html)
  * Applying 2D billboards for low LOD meshes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-images-lod.html)
2D images for low level of detail (LOD)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)
Billboard Renderer component reference
# Applying 2D billboards for low LOD meshes
Billboards are a level-of-detail (LOD) method for drawing complicated 3D Meshes in a simpler way when they are far away from the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera). When a **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) is far away from the Camera, its size on screen means there is no need to draw it in full detail. Instead, you can replace the complex 3D Mesh with a 2D **billboard** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard) representation.
The [Billboard Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html) renders [Billboard assets](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardAsset.html). 
A Billboard asset is a collection of pre-rendered images of a mesh. Use it with the [Billboard Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html) to an object that is distant from the Camera at a low [level of detail (LOD)](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html).
The most common way to generate a Billboard Asset is to create files in [SpeedTree Modeler](https://unity.com/products/speedtree), and then import them into Unity.
It is also possible to create your own Billboard Assets from script. For more information, see the API reference for [BillboardAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset.html).
Certain features, such as SpeedTree, export Billboard Assets, but you can also create them yourself. For information on how to create a Billboard Asset, see the [BillboardAssets](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardAsset.html) Manual page and the [BillboardAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset.html) Script reference page.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-images-lod.html)
2D images for low level of detail (LOD)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)
Billboard Renderer component reference
