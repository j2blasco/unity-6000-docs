* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Models](https://docs.unity3d.com/6000.0/Documentation/Manual/models.html)
  * [Importing models into Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/models-importing.html)
  * [Model Import Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html)
  * Model tab Import Settings reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html)
Model Import Settings reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html)
Rig tab
# Model tab Import Settings reference
To open a model’s Import Settings, select the model from the [Project window](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow). The [Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) then displays the Import Settings for the selected model. You can also control these settings in your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) with the [`ModelImporter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html) class.
![The Import Settings window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/model-import-settings.png) The Import Settings window ![Import settings for the Model](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/FBXImporter-Model.png) Import settings for the Model
This section provides information about each of the sections on the Model tab:
**(A)** [Scene](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html#sceneprops)A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)-level properties, such as whether to import Lights and **Cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera), and what scale factor to use.
**(B)** Properties specific to [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html#meshprops).
**(C)** [Geometry](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html#geoprops)-related properties, for dealing with topology, UVs, and normals.
## Scene
Scene-level properties, such as whether to import lights and cameras, and what scale factor to use.
**Property** | **Description**  
---|---  
**Scale Factor** | Applies a global scale on the imported model whenever the source file scale doesn’t fit the intended scale in your project. Unity’s physics system expects 1 m in the game world to be 1 unit in the imported file.  
**Convert Units** | Converts the [model scaling](https://docs.unity3d.com/6000.0/Documentation/Manual/models-preparing.html) defined in the **model file** A file containing a 3D data, which may include definitions for meshes, bones, animation, materials and textures. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/3D-formats.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Modelfile) to Unity’s scale.  
**Bake Axis Conversion** | Bakes the results of axis conversion directly into your application’s asset data (for example, vertex or animation data) when you import a model that uses a different axis system than Unity. Disable this property to compensate the **Transform component** A Transform component determines the Position, Rotation, and Scale of each object in the scene. Every GameObject has a Transform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TransformComponent) of the root **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) at runtime to simulate axis conversion.  
**Import BlendShapes** | Imports blend shapes with your mesh. For more information, refer to [Importing blend shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html#importing-blend-shapes).  
  
**Note** : Importing blend shape normals requires smoothing groups in the FBX file.  
**Import Deform Percent** | Only available when **Import BlendShapes** is enabled. Import the blend shape’s deform percent. Leave disabled to set all values to 0.  
**Import Visibility** | Imports the FBX settings that define whether MeshRenderer components are enabled (visible). For more information, refer to [Importing visibility properties](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html#importing-visibility-properties).  
**Import Cameras** | Imports cameras from your .FBX file. For more information, refer to [Camera support](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html#camera-support).  
**Import Lights** | Imports lights from your .FBX file. For more information, refer to [Camera support](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html#light-support).  
**Preserve Hierarchy** | Creates an explicit prefab root, even if this model only has a single root. Normally, the FBX importer strips any empty root nodes from the model to improve performance. However, if you have multiple FBX files with portions of the same hierarchy you can use this option to preserve the original hierarchy.   
  
For example, `file1.fbx` contains a rig and a mesh and `file2.fbx` contains the same rig but only the animation for that rig. If you import `file2.fbx` without enabling this option, Unity strips the root node, the hierarchies don’t match, and the animation breaks.  
**Sort Hierarchy By Name** | Sorts GameObjects by alphabetical order within the hierarchy. Disable this property to preserve the hierarchy order defined in the FBX file.  
## Meshes
**Property** | **Description**  
---|---  
**Mesh Compression** | Set the level of compression ratio to reduce the file size of the mesh. Increase the compression ratio to lower the precision of the mesh. Unity uses the mesh bounds and a lower bit depth per component to compress the mesh data. This is useful for [optimizing game size](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html). The following options are available: 
  * **Off** : Don’t use compression.
  * **Low** : Use a low compression ratio.
  * **Medium** : Use a medium compression ratio.
  * **High** : Use a high compression ratio.

  
**Read/Write** | Allows Unity to access mesh data at runtime, and you to access it from your scripts. Unity uploads the mesh data to GPU-addressable memory, but also keeps it in CPU-addressable memory. For example, you might want to enable this if you’re generating a mesh procedurally, or if you want to copy some data from a mesh.   
  
When this option is disabled, Unity uploads the mesh data to GPU-addressable memory, and then removes it from CPU-addressable memory.   
  
By default, this option is disabled. To save runtime memory usage, leave this option disabled. For information on when to enable Read/Write Enabled, refer to [`Mesh.isReadable`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-isReadable.html).  
**Optimize Mesh** | Set the order in which triangles are listed in the Mesh for better GPU performance. The following options are available: 
  * **Nothing** : No optimization.
  * **Everything** : Let Unity reorder the vertices and indices for both polygons and vertices. This is the default.
  * **Polygon Order** : Reorder only the polygons.
  * **Vertex Order** : Reorder only the vertices.

  
**Generate Colliders** | Import the **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) with mesh **colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) automatically attached. This is useful for quickly generating a **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) mesh for environment geometry, but should be avoided for geometry you’re moving.  
## Geometry
**Property** | **Description**  
---|---  
**Keep Quads** | Prevents Unity from converting polygons that have four vertices to triangles. For example, if you’re using [tessellation shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderTessellation.html), you might want to enable this option because tessellating quads can be more efficient than tessellating polygons.   
  
Unity can import any type of polygon (triangle to N-gon). Polygons that have more than four vertices are always converted to triangles regardless of this setting. However, if a mesh has quads and triangles (or N-gons that get converted to triangles), Unity creates two submeshes to separate quads and triangles. Each submesh contains either triangles only or quads only.   
  
**Tip:** If you want to import quads into Unity from 3ds Max, you have to export it as an Editable Poly.  
**Weld Vertices** | Combine vertices that share the same position in space, if they share all the same properties (including, UVs, Normals, Tangents, and VertexColor).   
  
This optimizes the vertex count on meshes by reducing their total number. This option is enabled by default.   
  
Sometimes, you might need to disable this optimization when importing meshes. For example, if you intentionally have duplicate vertices which occupy the same position in your mesh, you might prefer to use scripting to read or manipulate the individual vertex and triangle data.  
**Index Format** | Defines the size of the Mesh index buffer. The following options are available: 
  * **Auto** : Let Unity decide whether to use 16 or 32 bit indices when importing a mesh, depending on the mesh vertex count. The default setting.
  * **16 bit** : Use 16 bit indices when importing a mesh. If the mesh is larger, then Unity splits it into <64k vertex chunks.
  * **32 bit** - Use 32 bit indices when importing a mesh. If you’re using GPU-based rendering pipelines (for example with compute shader triangle culling), using 32 bit indices ensures that all meshes use the same index format. This reduces shader complexity, because they only need to handle one format.

  
**Note:** For bandwidth and memory storage size reasons, it’s best practice to keep the **16 bit** indices as default, and only use **32 bit** when necessary, which is what the **Auto** option uses.  
**Legacy Blend Shape Normals** | Computes normals based on the **Smoothing Angle** value.  
**Normals** The direction perpendicular to the surface of a mesh, represented by a Vector. Unity uses normals to determine object orientation and apply shading. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-vectors.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normal) | Controls how to calculate normals. This is useful for [optimizing game size](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html). The following options are available: 
  * **Import** : Import normals from the file. This is the default option. If the file doesn’t contain normals, Uity calculates them.
  * **Calculate** : Calculate normals based on **Normals Mode** , **Smoothness Source** , and **Smoothing Angle**.
  * **None** : Disable normals. Use this option if the mesh is neither normal mapped nor affected by real-time lighting.

  
**Blend Shape Normals** | Controls how to calculate normals for blend shapes. This value should match the value for the **Normals** property. This property is only visible when **Legacy Blend Shape Normals** is disabled. The following options are available: 
  * **Import** : Import normals from the file. If the blend shape doesn’t contain normals, the FBX SDK uses its own method to calculate normals, resulting in normal values that usually differ from the normal values that Unity creates with the **Calculate** option.
  * **Calculate** : Calculate normals based on **Normals Mode** , **Smoothness Source** , and **Smoothing Angle**.
  * **None** : The blend shape normals don’t contribute to the base shape.

  
**Normals Mode** | Define how the normals are calculated by Unity. This is only available when **Normals** is set to **Calculate** or **Import**. The following options are available: 
  * **Unweighted Legacy** : The legacy method of computing the normals (prior to version 2017.1).
  * **Unweighted** : The normals aren’t weighted.
  * **Area Weighted** : The normals are weighted by face area.
  * **Angle Weighted** : The normals are weighted by the vertex angle on each face.
  * **Area and Angle Weighted** : The normals are weighted by both the face area and the vertex angle on each face. This is the default option.

  
**Smoothness Source** | Set how to determine the smoothing behavior (which edges should be smooth and which should be hard). This property is only visible when **Legacy Blend Shape Normals** is disabled. The following options are available: 
  * **Prefer Smoothing Groups** : Use smoothing groups from the model file, where possible.
  * **From Smoothing Groups** : Use smoothing groups from the model file only.
  * **From Angle** : Use the **Smoothing Angle** value to determine which edges should be smooth.
  * **None** : Don’t split any vertices at hard edges.

  
**Smoothing Angle** | Controls whether vertices are split for hard edges. Typically higher values result in fewer vertices.   
  
**Note:** Use this setting only on smooth organics or high poly models. For other model types, manually smooth in your 3D modeling software and then import with the **Normals** option set to **Import**. Unity bases hard edges on a single angle so you might end up with smoothing on some parts of the model by mistake.  
  
Only available if **Normals** is set to **Calculate**.  
**Tangents** | Controls how vertex tangents are imported or calculated. This is only available when **Normals** is set to **Calculate** or **Import**. The following options are available: 
  * **Import** : Import vertex tangents from FBX files if **Normals** is set to **Import**. If the mesh has no tangents, it doesn’t work with normal-mapped shaders.
  * **Calculate Legacy** : Calculate tangents with the legacy algorithm.
  * **Calculate Legacy - Split Tangent** : Calculate tangents with the legacy algorithm, with splits across UV charts. Use this if normal map lighting is broken by seams on your mesh. This usually only applies to characters.
  * **Calculate Mikktspace** : Calculate tangents using [MikkTSpace](http://www.mikktspace.com/). This is the default option if **Normals** is set to **Calculate**.
  * **None** : Don’t import vertex tangents. The Mesh has no tangents, so this doesn’t work with normal-mapped shaders.

  
**Swap UVs** | Swap UV channels in the mesh. Use this option if the diffuse Texture uses UVs from the **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap). Unity supports up to eight UV channels but not all 3D modeling applications export more than two.  
**Generate Lightmap UVs** | Creates a second UV channel for the lightmap. For more information, refer to [Generate lightmap UVs](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-GeneratingLightmappingUVs.html).  
## Additional resources
  * [Importing model files](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html)
  * [Rig tab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html)
  * [Animation tab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)
  * [Material tab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Materials.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html)
Model Import Settings reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html)
Rig tab
