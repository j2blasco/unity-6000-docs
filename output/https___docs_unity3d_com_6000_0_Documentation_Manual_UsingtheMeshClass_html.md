* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UsingtheMeshClass.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Creating and accessing meshes via script](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-meshes.html)
  * Access meshes via the Mesh API


[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-mesh.html)
Create a mesh
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Example-CreatingaBillboardPlane.html)
Create a quad mesh via script
# Access meshes via the Mesh API
The [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) class is the basic script interface to an object’s mesh geometry. It uses arrays to represent the triangles, vertex positions, normals and texture coordinates and also supplies a number of other useful properties and functions to assist mesh generation.
## Access an object’s Mesh
The mesh data is attached to an object using the [Mesh Filter](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshFilter.html)A mesh component that takes a mesh from your assets and passes it to the Mesh Renderer for rendering on the screen. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshFilter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshFilter) component (and the object will also need a [MeshRenderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html) to make the geometry visible). This component is accessed using the familiar GetComponent function:
```
using UnityEngine;
public class ExampleScript : MonoBehaviour
{
    MeshFilter mf;
    void Start()
    {
        //if this gameObject has a MeshFilter, mf will reference the component
        mf = GetComponent<MeshFilter>();    
    }
}

```

## Add mesh data
The Mesh object has properties for the vertices and their associated data (normals and UV coordinates) and also for the triangle data. The vertices may be supplied in any order but the arrays of normals and UVs must be ordered so that the indices all correspond with the vertices (ie, element 0 of the normals array supplies the normal for vertex 0, etc). The vertices are [Vector3s](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) representing points in the object’s local space. The normals are normalised Vector3s representing the directions, again in local coordinates. The UVs are specified as [Vector2s](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html), but since the Vector2 type doesn’t have fields called U and V, you must mentally convert them to X and Y respectively.
The triangles are specified as triples of integers that act as indices into the vertex array. Rather than use a special class to represent a triangle the array is just a simple list of integer indices. These are taken in groups of three for each triangle, so the first three elements define the first triangle, the next three define the second triangle, and so on. An important detail of the triangles is the ordering of the corner vertices. They should be arranged so that the corners go around clockwise as you look down on the visible outer surface of the triangle, although it doesn’t matter which corner you start with.
### Work with raw mesh data
The [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) class also has a lower-level advanced API that enables you to work with raw mesh vertex and index buffer data. This is useful in situations that require maximum performance or the lowest amount of memory allocations.
  * [Mesh.SetIndexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferParams.html) and [Mesh.SetIndexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetIndexBufferData.html) for setting up size, format of the index buffer, and updating data inside it.
  * [Mesh.SetVertexBufferParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferParams.html) and [Mesh.SetVertexBufferData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetVertexBufferData.html) for setting up size, format of the vertex buffer(s), and updating data inside them.
  * [Mesh.SetSubMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetSubMesh.html) for setting up index buffer topology and ranges.


## Additional resources
  * [Mesh data](https://docs.unity3d.com/6000.0/Documentation/Manual/AnatomyofaMesh.html) documentation.
  * [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) API reference.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-mesh.html)
Create a mesh
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Example-CreatingaBillboardPlane.html)
Create a quad mesh via script
