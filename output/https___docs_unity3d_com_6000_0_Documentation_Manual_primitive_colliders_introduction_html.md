* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/primitive-colliders-introduction.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * [Collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-shapes.html)
  * [Primitive collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/primitive-colliders.html)
  * Introduction to primitive collider shapes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/primitive-colliders.html)
Primitive collider shapes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BoxCollider.html)
Box collider component reference
# Introduction to primitive collider shapes
Primitive colliders are the most computationally efficient type of **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) in Unity. They are called “primitive” because they are defined by simple geometric shapes such as boxes, spheres, and capsules. They match the [Primitive Objects](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html), which are built-in **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) shapes.
There are three primitive collider shapes in Unity:
  * [Box collider](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BoxCollider.html)A cube-shaped collider component that handles collisions for GameObjects like dice and ice cubes. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BoxCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#boxcollider): A rectangular box-shaped collider that is suitable for most rectangular objects.
  * [Sphere collider](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SphereCollider.html)A sphere-shaped collider component that handles collisions for GameObjects like balls or other things that can be roughly approximated as a sphere for the purposes of physics. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SphereCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SphereCollider): A spherical collider that is suitable for most circular objects.
  * [Capsule collider](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CapsuleCollider.html)A capsule-shaped collider component that handles collisions for GameObjects like barrels and character limbs. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CapsuleCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#capsulecollider): A cylindrical collider that is suitable for objects that have a cylindrical shape, or for rounding out the **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) edges on sharp corners. Capsule colliders are also useful for player and non-player characters.


Primitive colliders are efficient, but they have limitations. For example, you cannot change or deform their shape, only their scale. Unlike **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) colliders, they are not made up of triangles; their shape is fixed (note that the [Physics Debug visualization](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsDebugVisualization.html) does indicate a triangle-based mesh on primitive colliders, but these are for visualization purposes only and do not reflect the collider’s construction). 
Primitive colliders are usually not the best option for complex shapes, wheels, or **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) collision. Unity has specific colliders available for more complex collider shapes (see [Mesh colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-colliders.html)A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshCollider), [Terrain colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-colliders.html)A terrain-shaped collider component that handles collisions for collision surface with the same shape as the Terrain object it is attached to. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TerrainCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TerrainCollider), and [Wheel colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders.html)A special collider for grounded vehicles. It has built-in collision detection, wheel physics, and a slip-based tire friction model. It can be used for objects other than wheels, but it is specifically designed for vehicles with wheels. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WheelCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WheelCollider)). However, if you need a collider shape that fits a complex shape, but does not need to be too accurate, you can use primitive colliders to create a [Compound collider](https://docs.unity3d.com/6000.0/Documentation/Manual/compound-colliders.html). A Compound collider is a collection of primitive colliders in an arrangement that fits the collider shape you need. 
In summary, primitive colliders are an efficient but sometimes inaccurate way to add **collision detection** An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CollisionDetection) to objects in Unity. They are suitable for primitive-shaped GameObjects with regular shapes. However, for more complex objects with irregular shapes, or for more accurate collision detection, you should use a more complex collider shape.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/primitive-colliders.html)
Primitive collider shapes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BoxCollider.html)
Box collider component reference
