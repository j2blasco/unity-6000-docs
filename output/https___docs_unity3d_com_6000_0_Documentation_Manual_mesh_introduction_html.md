* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-introduction.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Get started with meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/get-started-with-meshes.html)
  * Introduction to meshes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/get-started-with-meshes.html)
Get started with meshes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnatomyofaMesh.html)
Mesh data
# Introduction to meshes
A mesh is a collection of data that describes a shape. In Unity, you use meshes in the following ways:
  * In graphics, you use meshes together with [materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html)An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material); meshes describe the shape of an object that the GPU renders, and materials describe the appearance of its surface.
  * In physics, you can use a mesh to determine the shape of a **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider).


## Deformable meshes
In addition to regular meshes, Unity also supports deformable meshes.
Deformable meshes fall into the following categories:
  * Skinned meshes: These meshes work with additional data called bones. Bones form a structure called a skeleton (also called a rig, or joint hierarchy), and the skinned mesh contains data that allows it to deform in a realistic way when the skeleton moves. You usually use skinned meshes for [skeletal animation](https://en.wikipedia.org/wiki/Skeletal_animation) with Unity’s [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html) features, but you can also use them with [Rigidbody components](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html) to create “ragdoll” effects.
  * Meshes with blend shapes: These meshes contain data called blend shapes. Blend shapes describe versions of the mesh that are deformed into different shapes, which Unity interpolates between. You use blend shapes for [morph target animation](https://en.wikipedia.org/wiki/Morph_target_animation), which is a common technique for facial animation.
  * Meshes that work with a [Cloth component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cloth.html) component for realistic fabric simulation.


## Working with meshes
Unity stores meshes in your project as [mesh assets](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html), and represents them in C# code with the [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) class.
Depending on how you use meshes, they work with different components:
  * In graphics, Unity renders regular meshes with [Mesh Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) components, and deformable meshes with [Skinned Mesh Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html) components.
  * In physics, Unity uses the [Mesh Collider](https://docs.unity3d.com/Manual/class-MeshCollider.html)A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshCollider) component to determine the shape of a collider.


For detailed information about the data that a mesh contains and how Unity represents that data, see [Mesh data](https://docs.unity3d.com/6000.0/Documentation/Manual/AnatomyofaMesh.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/get-started-with-meshes.html)
Get started with meshes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnatomyofaMesh.html)
Mesh data
