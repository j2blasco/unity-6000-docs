* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-configure-colliders.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Rigidbody physics](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-physics-section.html)
  * Configure Rigidbody Colliders 


[](https://docs.unity3d.com/6000.0/Documentation/Manual/RigidbodiesOverview.html)
Introduction to rigid body physics 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-constant-force.html)
Apply constant force to a Rigidbody
# Configure Rigidbody Colliders
[Colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) define the physical boundaries of a **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody). To allow collisions to occur, you must add Colliders to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) alongside a Rigidbody. 
If one Rigidbody collides with another, the **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsEngine) only calculates a collision if both GameObjects have a Collider attached. If one GameObject has a Rigidbody but no Collider, it passes through other GameObjects, and Unity does not include it in collision calculations.
![Colliders define the physical boundaries of a Rigidbody](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/RigidbodyandCollider.png) Colliders define the physical boundaries of a Rigidbody
The relative **Mass** of each Rigidbody in a collision determines how they react when they collide with each other.
See [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) for more information.
## Convex and concave collider geometry
The PhysX physics system requires that any collider you place on a non-kinematic Rigidbody is convex, not concave. All primitive shapes in Unity are convex. However, Unity considers a [Mesh Collider](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshCollider.html)A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshCollider) concave by default.
If you apply a default **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Collider to a non-kinematic Rigidbody, Unity throws an error at runtime. To ensure that your non-kinematic Rigidbody receives physics-based forces, you need to instruct Unity to make the Mesh Collider convex. To do this, enable the Mesh Collider’s **Convex** property. When **Convex** is enabled, Unity automatically calculates a convex collider shape (called a hull) based on the associated mesh. However, because the convex hull of the mesh is only an approximation of the original shape, it can lead to inaccurate simulation. 
For a more accurate collision simulation, you can use one of the following approaches:
  * Use a DCC tool to split the mesh into several parts, so that when Unity calculates their convex hulls, they represent the total shape better.
  * Use several primitive Colliders to manually build a [Compound Collider](https://docs.unity3d.com/6000.0/Documentation/Manual/compound-colliders.html) that is the same shape as the mesh.
  * Use automatic tools that calculate convex approximations of any mesh, such as Unity’s [V-HACD](https://github.com/Unity-Technologies/VHACD).


If a Rigidbody is kinematic (that is, it receives no physics-based forces), you can apply any collider to it. 
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RigidbodiesOverview.html)
Introduction to rigid body physics 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-constant-force.html)
Apply constant force to a Rigidbody
