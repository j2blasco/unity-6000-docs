* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshFilter.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Mesh components reference](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-components-reference.html)
  * Mesh Filter component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html)
Skinned Mesh Renderer component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html)
Mesh asset Inspector window reference
# Mesh Filter component reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html "Go to MeshFilter page in the Scripting Reference")
A **Mesh Filter** component holds a reference to a mesh. It works with a [Mesh Renderer](https://docs.unity3d.com/Manual/class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) component on the same **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject); the Mesh Renderer renders the mesh that the Mesh Filter references.
To render a deformable mesh, use a [Skinned Mesh Renderer](https://docs.unity3d.com/Manual/class-SkinnedMeshRenderer.html) instead. A Skinned Mesh Renderer component does not need a Mesh Filter component.
## Mesh Filter Inspector reference
**Property** | **Function**  
---|---  
**Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) | A reference to a [mesh asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html).  
  
To change the mesh asset that the Mesh Filter component references, use the picker (circle icon) next to the mesh’s name.  
  
**Note:** The settings for other components on this GameObject don’t change when you change the mesh that the Mesh Filter references. For example, a Mesh Renderer doesn’t update its settings, which might cause Unity to render the mesh with unexpected properties. If this happens, adjust the settings of the other components as needed.  
  
Corresponds to the [MeshFilter.mesh](https://docs.unity3d.com/ScriptReference/MeshFilter-mesh.html) property.  
MeshFilter
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html)
Skinned Mesh Renderer component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html)
Mesh asset Inspector window reference
