* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingTextureandMeshData-make-compatible.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Texture optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureLoading.html)
  * [Loading textures in the background](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingTextureandMeshData-introduction.html)
  * Make a texture compatible with asynchronous texture loading


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingTextureandMeshData.html)
Texture and mesh loading
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html)
Optimizing GPU texture memory with mipmap streaming
# Make a texture compatible with asynchronous texture loading
A texture is eligible for the asynchronous upload pipeline if the following conditions are met:
  * The texture is not read/write enabled.
  * The texture is not in the Resources folder.
  * If the build target is Android, LZ4 **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) is enabled in the [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile) window.


Note that if you load a texture using `LoadImage(byte[] data)`, this forces Unity to use the synchronous upload pipeline, even if the above conditions are met.
A **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) is eligible for the asynchronous upload pipeline if the following conditions are met:
  * The mesh is not read/write enabled.
  * The mesh is not in the Resources folder.
  * The mesh has no [BlendShapes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-blendShapeCount.html).
  * Unity has not applied **Dynamic Batching** An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DynamicBatching) to the mesh, either because the mesh is ineligible for Dynamic Batching or because Dynamic Batching is disabled. For more information on Dynamic Batching, see [Draw call batching](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html).
  * The mesh vertex/index data is not needed by a **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem), a **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain), or a Mesh **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider).
  * The mesh has no [bone weights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-boneWeights.html).
  * The mesh [topology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) is not [quads](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.Quads.html)A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Quad).
  * The [meshCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-meshCompression.html) for the mesh asset is set to [Off](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMeshCompression.Off.html). If the build target is Android, LZ4 compression is enabled in the [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html) window.


In all other circumstances, Unity loads textures and meshes synchronously.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingTextureandMeshData.html)
Texture and mesh loading
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html)
Optimizing GPU texture memory with mipmap streaming
