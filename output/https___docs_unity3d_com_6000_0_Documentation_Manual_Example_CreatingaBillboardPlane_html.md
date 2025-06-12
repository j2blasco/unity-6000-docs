* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Example-CreatingaBillboardPlane.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Creating and accessing meshes via script](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-meshes.html)
  * Create a quad mesh via script


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingtheMeshClass.html)
Access meshes via the Mesh API
[](https://docs.unity3d.com/6000.0/Documentation/Manual/simplifying-distant-meshes-with-level-of-detail-lod.html)
Simplifying distant meshes with level of detail (LOD)
# Create a quad mesh via script
To represent flat surfaces, Unity includes the Plane and **Quad** A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Quad) [primitive GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html) that you can instantiate in your **Scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). However, it is useful to understand how to use a script to construct a quadrilateral **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) yourself. This is essential for procedural mesh generation. 
**Note** : Unity processes and displays geometry in triangles, and not quads. This means that the Quad primitive consists of two triangles.
## Vertex array
The first thing you need to do is set up the array of vertices that your shape uses. 
This example assumes that the quad lies on the x-axis and y-axis, and that your script contains the variables width and height. 
```
Vector3[] vertices = new Vector3[4]
{
    new Vector3(0, 0, 0),
    new Vector3(width, 0, 0),
    new Vector3(0, height, 0),
    new Vector3(width, height, 0)
};
mesh.vertices = vertices;

```

This example supplies the vertices in the following order:
  1. Bottom-left
  2. Bottom-right
  3. Top-left
  4. Top-right


Due to the way that Unity retrieves Mesh data properties, it is much more efficient to set up data in your own array and then assign the array to a property (for example, to `Mesh.vertices` or `Mesh.normals`), rather than access the property array via individual elements.
## Triangles
Next, you need to set up the triangles. A quad consists of two triangles, each made up of three points in the vertex array you created earlier. To specify the points, you define each triangle as three indices of the the vertex array. For example, the lower left triangle for this quad uses index 0, 2, and 1 which corresponds to coordinates (0, 0, 0), (0, height, 0), and (width, 0, 0) from the vertex array. The ordering is important because you must order the corners clockwise. The upper right triangle uses index 2, 3, and 1.
```
int[] tris = new int[6]
{
    // lower left triangle
    0, 2, 1,
    // upper right triangle
    2, 3, 1
};
mesh.triangles = tris;

```

## Normals
A Mesh with vertices and triangles is visible in the Scene, but Unity does not shade it correctly because it has no normals yet. The normals for this example are simple because they are all identical. Every normal points in the negative z-axis direction in the quad’s local space. When you add the normals, Unity correctly shades the quad, but you need a Light in the Scene to see the effect.
```
Vector3[] normals = new Vector3[4]
{
    -Vector3.forward,
    -Vector3.forward,
    -Vector3.forward,
    -Vector3.forward
};
mesh.normals = normals;

```

If you do not want to define the normals yourself, you can use [Mesh.RecalculateNormals()](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.RecalculateNormals.html).
## Texture coordinates
Finally, to display Textures on the Mesh’s Material correctly, add texture coordinates to the Mesh. Texture coordinates are between 0 and 1. Each vertex in the Mesh has a texture coordinate which specifies where on the Material’s Texture to sample from. To show the whole Texture across the quad, the texture coordinate values on each vertex should all be 0 or 1 so that each corner of the quad corresponds to a corner of the Texture.
```
Vector2[] uv = new Vector2[4]
{
      new Vector2(0, 0),
      new Vector2(1, 0),
      new Vector2(0, 1),
      new Vector2(1, 1)
};
mesh.uv = uv;

```

## Final script
The following script combines everything above to create a quad in your Scene. To use it:
  1. Create a new C# script (menu: **Assets** > **Create** > **MonoBehaviour Script**) and name it QuadCreator.
  2. Open the QuadCreator script, copy the example code into it, and save the script.
  3. Back in the Editor, create a new GameObject in your Scene (menu: **GameObject** > **Create Empty**).
  4. In the Inspector, select **Add Component** > **Scripts** > **Quad Creator**.
  5. Position the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) wherever you want in the Scene.
  6. Enter Play Mode. If you can not see the quad in the Scene or Game view, make sure you are viewing it from the correct side; Unity does not render the back face of this Mesh.

```
using UnityEngine;

public class QuadCreator : MonoBehaviour
{
    public float width = 1;
    public float height = 1;

    public void Start()
    {
        MeshRenderer meshRenderer = gameObject.AddComponent<MeshRenderer>();
        meshRenderer.sharedMaterial = new Material(Shader.Find("Standard"));

        MeshFilter meshFilter = gameObject.AddComponent<MeshFilter>();

        Mesh mesh = new Mesh();

        Vector3[] vertices = new Vector3[4]
        {
            new Vector3(0, 0, 0),
            new Vector3(width, 0, 0),
            new Vector3(0, height, 0),
            new Vector3(width, height, 0)
        };
        mesh.vertices = vertices;

        int[] tris = new int[6]
        {
            // lower left triangle
            0, 2, 1,
            // upper right triangle
            2, 3, 1
        };
        mesh.triangles = tris;

        Vector3[] normals = new Vector3[4]
        {
            -Vector3.forward,
            -Vector3.forward,
            -Vector3.forward,
            -Vector3.forward
        };
        mesh.normals = normals;

        Vector2[] uv = new Vector2[4]
        {
            new Vector2(0, 0),
            new Vector2(1, 0),
            new Vector2(0, 1),
            new Vector2(1, 1)
        };
        mesh.uv = uv;

        meshFilter.mesh = mesh;
    }
}


```

**Note** : This example code is in the `Start` function, which means that it executes once when you enter Play Mode, and the Mesh does not change throughout the application. However, you can add code in the Update function to make the Mesh change each frame. Be aware that this greatly increases the resource intensity of the Mesh generation.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingtheMeshClass.html)
Access meshes via the Mesh API
[](https://docs.unity3d.com/6000.0/Documentation/Manual/simplifying-distant-meshes-with-level-of-detail-lod.html)
Simplifying distant meshes with level of detail (LOD)
