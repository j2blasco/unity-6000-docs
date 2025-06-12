* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/configure-mesh-compression.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Compressing mesh data for optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/compressing-mesh-data-optimization.html)
  * Configure mesh compression


[](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-vertex-compression.html)
Configure vertex compression
[](https://docs.unity3d.com/6000.0/Documentation/Manual/loading-texture-mesh-data-asynchronously.html)
Loading texture and mesh data asynchronously
# Configure mesh compression
To use the **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) **Compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) setting: 
  1. Select a Model in your project’s Assets folder to open the Model tab of the Import Settings window.
  2. Navigate to the Meshes heading and find the Mesh Compression setting.
  3. Select the dropdown menu to choose a level for all meshes in that Model. You can also change this setting in code with the ModelImporterMeshCompression enumeration.


Available values are High, Medium, Low, or Off. The following table shows typical compression ratios for each of these settings:
**Value** | **Vertices** | **Normals** | **Tangents** | **UVs** | **Color**  
---|---|---|---|---|---  
**Off** | 1.0 | 1.0 | 1.0 | 1.0 | 1.0  
**Low** | 1.6 | 4.6 | 4.4 | 2.0 | 1.0  
**Medium** | 2.0 | 5.6 | 5.3 | 3.2 | 1.3  
**High** | 3.2 | 7.4 | 6.7 | 4.0 | 2.0  
Compression ratios for the mesh compression technique
Note: The “Color” column in the above table shows ratios for a mesh that uses the UNorm8 format. For a mesh that uses the FP32 format for vertex colors, the ratios are 4.0 on the Low setting, 5.3 on the Medium setting, and 8.0 on the High setting.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-vertex-compression.html)
Configure vertex compression
[](https://docs.unity3d.com/6000.0/Documentation/Manual/loading-texture-mesh-data-asynchronously.html)
Loading texture and mesh data asynchronously
