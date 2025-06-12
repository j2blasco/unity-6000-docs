* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Mesh components reference](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-components-reference.html)
  * Mesh asset Inspector window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshFilter.html)
Mesh Filter component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/troubleshooting-skinned-mesh-renderer-visibility.html)
Troubleshooting Skinned Mesh Renderer visibility
# Mesh asset Inspector window reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html "Go to Mesh page in the Scripting Reference")
A **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) asset represents a mesh in your Unity project. 
Unity creates mesh assets by default when it imports [models](https://docs.unity3d.com/6000.0/Documentation/Manual/models.html)A 3D model representation of an object, such as a character, a building, or a piece of furniture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/3D-formats.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Model). You can also create mesh assets directly in Unity, for example, by [creating a mesh with code](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-meshes.html) and saving the results as an asset.
Select a mesh asset in the ****Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow)** to open the **Mesh**Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)**. This Inspector displays information about the mesh, such as the total number of vertices or the names of any blend shapes the mesh has. It also displays a visual preview of the mesh.
## Mesh information
The Mesh Inspector displays information about how the mesh **asset stores** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore) its data, but not the values in the data itself. For example, the Inspector shows that Unity stores the value for Position as a set of three Float32 values for each vertex, but it doesn’t show the Position value of a specific vertex.
![The Mesh Inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/mesh-inspector.png) The Mesh Inspector **Property** | **Description**  
---|---  
**Vertices** | The total number of vertices in the mesh, and how much on-disk storage and runtime memory Unity uses to store the vertex data for the mesh. For each vertex attribute, Unity shows how much on-disk storage and runtime memory Unity uses to store that attribute, and the data type that Unity uses for it.  
  
For more information about this data, see [Mesh data](https://docs.unity3d.com/6000.0/Documentation/Manual/AnatomyofaMesh.html). For information about how Unity can compress data in a mesh, see the [Compressing mesh data](https://docs.unity3d.com/6000.0/Documentation/Manual/compressing-mesh-data-optimization.html).  
**Indices** | The total number of indices in the mesh, how much on-disk storage and runtime memory Unity uses to store this data, and information about the indices for each sub-mesh.  
  
For more information about this data, see [Mesh data](https://docs.unity3d.com/6000.0/Documentation/Manual/AnatomyofaMesh.html).  
**Skin** | This section is only visible on a [skinned mesh](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-introduction.html#deformable-meshes).  
  
The options are: 
  * **BlendWeight** : How many bones can affect a vertex.
  * **BlendIndices** : The indices of the bones that affect skinned vertices.
  * **Blend Shapes** : The total number of blend shapes in your mesh and lists their names. The number of frames next to each blend shape describes how many key frames each one has.

  
**Other** | Shows additional information.  
  
The options are: 
  * **Bounds Center** : A bounding box describes where the outermost edges of a mesh lie. The “Bounds Center” stores the location of the center of the mesh’s bounding box.
  * **Bounds Size** : Each value represents the length of the bounding box edges in X, Y and Z directions.
  * **Read/Write Enabled** : The value of the [Mesh.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-isReadable.html) property, which determines whether Unity can access and modify certain mesh data at runtime. You can set this value with the **Read/Write Enabled** checkbox in the [Model Import Settings window](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html).

  
## Mesh preview
This part of the Inspector allows you to preview the appearance of a mesh and explore the mesh data in a visual way. 
You can use the following properties in the UI to configure the view:
**Property** | **Description**  
---|---  
**View mode** | Provides different ways of visualizing the mesh. For more information, refer to [View mode dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html#viewmode).  
**Wireframe** | Not available in UV Layout mode.  
  
If enabled, the preview displays a visualisation of the vertices and edges. Otherwise, it doesn’t.  
**Channel picker** | Only available in UV Checker mode.  
  
This drop-down menu allows you to change which UV channel the preview displays. If the mesh only uses one UV channel, then only “Channel 0” is enabled.  
**Texture size** | Only available in UV Checker mode.  
  
This slider allows you to change the size of the checkered texture on the mesh’s UV map.  
**Blend shape picker** | Only available in Blendshapes mode.  
  
This drop-down allows you to change the blend shape that Unity visualizes in the mesh preview. When you select a different blend shape, Unity no longer applies the previous blend shape to the mesh preview.  
### View mode dropdown
For more information, refer to [Use the Mesh asset Inspector Preview](https://docs.unity3d.com/6000.0/Documentation/Manual/view-mesh-data-visualizations.html).
**Value** | **Description**  
---|---  
**Shaded** | Provides a visualization of the mesh with a basic light. This is the default view. For more information, see [Shaded view](https://docs.unity3d.com/6000.0/Documentation/Manual/view-mesh-data-visualizations.html#shaded).  
**UV Checker** | Applies a checkerboard texture to the mesh to visualize how the mesh’s UV map applies textures. For more information, see [UV Checker view](https://docs.unity3d.com/6000.0/Documentation/Manual/view-mesh-data-visualizations.html#uv-checker)  
**UV Layout** | Displays how the vertices of the mesh are organized in the unwrapped UV map. This view disables the Wireframe toggle. For more information, see [UV Layout view](https://docs.unity3d.com/6000.0/Documentation/Manual/view-mesh-data-visualizations.html#uv-layout)  
**Vertex Color** | Visualizes any vertex colors that the vertices in this mesh have. If no vertices have a vertex color, this menu item is disabled. For more information, see [Vertex Color view](https://docs.unity3d.com/6000.0/Documentation/Manual/view-mesh-data-visualizations.html#vertex-color)  
**Normals** | Visualizes the relative directions of the normals in the mesh with color. For more information, see [Normals view](https://docs.unity3d.com/6000.0/Documentation/Manual/view-mesh-data-visualizations.html#normals)  
**Tangents** | Visualizes the tangent data in the mesh with color. For more information, see [Tangents view](https://docs.unity3d.com/6000.0/Documentation/Manual/view-mesh-data-visualizations.html#tangents)  
**Blendshapes** | Lets you preview blend shape deformations to the mesh. If the mesh has no blend shapes, this menu item is disabled. For more information, see [Blendshapes view](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-data-deformable-meshes.html#blend-shapes)  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshFilter.html)
Mesh Filter component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/troubleshooting-skinned-mesh-renderer-visibility.html)
Troubleshooting Skinned Mesh Renderer visibility
