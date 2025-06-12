* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-data-deformable-meshes.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Get started with meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/get-started-with-meshes.html)
  * [Mesh data](https://docs.unity3d.com/6000.0/Documentation/Manual/AnatomyofaMesh.html)
  * Mesh data for deformable meshes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-index-data.html)
Mesh index data
[](https://docs.unity3d.com/6000.0/Documentation/Manual/view-mesh-data-visualizations.html)
View mesh data visualizations
# Mesh data for deformable meshes
Deformable meshes hold data specific to the deformation of the **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh). Deformable meshes contain either:
  * [Blend shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-data-deformable-meshes.html#blend-shapes): Data that describes different deformed versions of the mesh, for use with animation.
  * [Bind poses](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-data-deformable-meshes.html#bind-poses): Data that describes the “base” pose of the skeleton in a skinned mesh.


## Blend shapes
Blend shapes describe versions of the mesh that are deformed into different shapes. Unity interpolates between these shapes. You use blend shapes for [morph target animation](https://en.wikipedia.org/wiki/Morph_target_animation), which is a common technique for facial animation.
Blend shape data is stored as blend shape vertices. Blend shape data is “sparse”. This means that there isn’t a blend shape vertex for every mesh vertex; there is only a corresponding blend shape vertex if the mesh vertex deforms.
A blend shape vertex contains deltas for position, normal, and tangent, and an index value. The meaning of the index value depends on how you request the data.
In the `Mesh` class, you can access blend shape vertex data with [Mesh.GetBlendShapeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBlendShapeBuffer.html). This returns a [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) that provides access to the blend shape vertex data on the GPU. This method allows you to choose between two different buffers; one that orders the data by blend shape, and one that orders the data by mesh vertex. The choice of buffer determines the meaning of the index value and the layout of the data in the buffer. For more information on buffer layouts, see [BlendShapeBufferLayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendShapeBufferLayout.html).
For information on using blend shapes with animations, see [Working with blend shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/BlendShapes.html).
This data is optional.
## Bind poses
In a skinned mesh, the **bind pose** of a bone describes its position when the skeleton is in its default position (also called its bind pose or rest pose).
In the `Mesh` class, you can get and set this data with [Mesh.bindposes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-bindposes.html). Each element contains data for the bone with the same index.
This data is required for skinned meshes.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-index-data.html)
Mesh index data
[](https://docs.unity3d.com/6000.0/Documentation/Manual/view-mesh-data-visualizations.html)
View mesh data visualizations
