* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Simplifying distant meshes with level of detail (LOD)](https://docs.unity3d.com/6000.0/Documentation/Manual/simplifying-distant-meshes-with-level-of-detail-lod.html)
  * Mesh LOD


[](https://docs.unity3d.com/6000.0/Documentation/Manual/simplifying-distant-meshes-with-level-of-detail-lod.html)
Simplifying distant meshes with level of detail (LOD)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-mesh-lod.html)
Configure mesh LOD
# Mesh LOD
This page contains information on **level of detail** (LOD) for meshes. For information on LOD for **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), see [SubShader LOD value](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderLOD.html).
Level of detail (LOD) is a technique that reduces the number of GPU operations that Unity requires to render distant meshes.
When a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) is far away from the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera), you see less detail compared to when the GameObject is close to the Camera. However, by default, Unity uses the same number of triangles to render it at both distances. This can result in wasted GPU operations, which can impact performance in your Scene.
The LOD technique allows Unity to reduce the number of triangles it renders for a GameObject based on its distance from the Camera. To use it, a GameObject must have a number of meshes with decreasing levels of detail in its geometry. These meshes are called LOD levels. The farther a GameObject is from the Camera, the lower-detail LOD level Unity renders. This technique reduces the load on the hardware for these distant GameObjects, and can therefore improve rendering performance. 
To understand how to use LOD in Unity, you must first understand what LOD levels are, and how they work.
## LOD levels
A LOD level is a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) that defines the level of detail Unity renders for a GameObject’s geometry. When a GameObject uses LOD, Unity displays the appropriate LOD level for that GameObject based on the GameObject’s distance from the Camera. 
Each LOD level exists in a separate GameObject, each of which has a **Mesh Renderer** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) component that displays that LOD level. For the very lowest level of detail, you can use a **Billboard** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard) Asset, which Unity displays instead of a 3D mesh. Unity shows and hides these GameObjects as required. LOD levels must be child GameObjects to the GameObject they relate to.
The images below demonstrate how the LOD levels change according to distance from the Camera.
![At LOD 0, the Camera shows a mesh with a large number of small triangles. At LOD 1, the Camera shows the mesh with far fewer triangles, which are much larger in size.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LOD0Image.png) At LOD 0, the Camera shows a mesh with a large number of small triangles. At LOD 1, the Camera shows the mesh with far fewer triangles, which are much larger in size.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/simplifying-distant-meshes-with-level-of-detail-lod.html)
Simplifying distant meshes with level of detail (LOD)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-mesh-lod.html)
Configure mesh LOD
