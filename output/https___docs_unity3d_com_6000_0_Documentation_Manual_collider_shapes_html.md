* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/collider-shapes.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * Collider shapes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-types-introduction.html)
Introduction to collider types
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-shapes-introduction.html)
Introduction to collider shapes
# Collider shapes
Colliders are available in different shape configurations. A **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider)’s shape defines how accurately the collider matches the **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) shape, and how computationally efficient the collider is. 
**Topic** | **Description**  
---|---  
[Introduction to collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-shapes-introduction.html) | Overview of the different collider shapes in Unity.  
[Primitive collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/primitive-colliders.html) | Primitive collider shapes are built-in, pre-calculated collider shapes in Unity (Box, Sphere and Capsule colliders).  
[Mesh colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-colliders.html)A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshCollider) | Mesh colliders create **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) geometry that matches the shape of their associated Mesh, for extremely accurate collisions.  
[Wheel colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders.html)A special collider for grounded vehicles. It has built-in collision detection, wheel physics, and a slip-based tire friction model. It can be used for objects other than wheels, but it is specifically designed for vehicles with wheels. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WheelCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WheelCollider) | Wheel colliders use raycasting to form wheel-shaped collision geometry with suspension and tyre-based friction.  
[Terrain colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-colliders.html)A terrain-shaped collider component that handles collisions for collision surface with the same shape as the Terrain object it is attached to. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TerrainCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TerrainCollider) |  **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) colliders create collision geometry that matches the shape of their associated Terrain, for extremely accurate collisions.  
[Compound colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/compound-colliders.html) | Compound colliders are a combination of multiple other colliders, which together have a single **center of mass** Represents the average position of all mass in a Rigidbody for the purposes of physics calculations. By default it is computed from all colliders belonging to the Rigidbody, but can be modified via script. [More info](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-centerOfMass.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CenterofMass).  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-types-introduction.html)
Introduction to collider types
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-shapes-introduction.html)
Introduction to collider shapes
