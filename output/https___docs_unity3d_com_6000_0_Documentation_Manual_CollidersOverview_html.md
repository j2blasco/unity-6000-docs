* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * Introduction to collision


[](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
Collision
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-types-introduction.html)
Introduction to collider types
# Introduction to collision
In Unity, a **collision** happens when two **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that are configured for collision occupy the same physical space. Collision is a foundational part of most games, and many interactive applications and simulators.
To handle collision between GameObjects, Unity uses **colliders**. A **collider** is a Unity component that defines the shape of a GameObject for the purposes of physical collisions. Colliders are invisible, and do not need to be the same shape as the GameObject’s mesh. 
For guidance on how to add components to a GameObject, see [Use Components](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingComponents.html). 
Each 3D collider has a 2D equivalent. In Unity, 2D and 3D physics run on different physics simulation systems. For guidance on 2D physics colliders, see [Collider 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/collider-2d-landing.html).
## Collider types
A collider’s type is based on the configuration of its GameObject’s Collider and **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) components. This configuration determines how a collider behaves, and how it interacts with other colliders. 
  * Static colliders: The GameObject has a collider but no Rigidbody.
  * Rigidbody colliders: The GameObject has a collider and a Rigidbody. 
    * Dynamic colliders: The Rigidbody is dynamic (that is, it has **Is Kinematic** disabled).
    * Kinematic colliders: The Rigidbody is kinematic (that is, it has **Is Kinematic** enabled).


There is also a sub-type of collider called a **Trigger collider**. Trigger colliders do not physically collide with other colliders; instead, Unity calls a function when other colliders pass through them. 
### Trigger colliders
Trigger colliders don’t cause collisions. Instead, they detect other Colliders that pass through them, and call functions that you can use to initiate events (see [Use collisions to trigger other events](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions-other-events.html)). 
To turn a collider into a trigger collider, enable the **Is Trigger** property on the Collider component. A trigger collider does not collide with other colliders; instead, other colliders pass through it. 
For a trigger collider to work, at least one GameObject involved in the collision must have a Rigidbody. Trigger colliders can be any collider type (static or Rigidbody), but in most cases it’s good practice to make the trigger collider a [static collider](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-types-introduction.html). and add a Rigidbody to the GameObject that passes through the trigger. If several GameObjects are passing through one trigger, there must be a Rigidbody on at least one GameObject in each collision pair. 
Triggers can be any collider shape (see [Collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-shapes.html)), and they can be visible or invisible. To make a trigger invisible, add the collider to an empty GameObject. Only add a trigger to a visible GameObject if it is okay for other GameObjects to visibly pass through it.
For gameplay and simulation, triggers might need some adjustment to make them feel intuitive for the player. For example, you could experiment with making a trigger collider slightly larger than its associated visible GameObject, so that it has a wider radius.
For information on how different collider types interact with each other on collision, see [Interaction between collider types](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-types-interaction.html).
## Collider shapes
Collider components are available in different shape configurations. There are three main shape types for colliders:
[Primitive colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/primitive-colliders.html) are built-in simple shapes that you can attach to your GameObject and scale to approximately the same size and shape. You can also combine several primitive collider shapes to create [compound colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/compound-colliders.html). [Mesh colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-colliders.html)A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshCollider) exactly match the shape of the GameObject’s [Mesh](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh). They are more accurate than primitive colliders for complex shapes, but require more computational resources. [Wheel colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders.html)A special collider for grounded vehicles. It has built-in collision detection, wheel physics, and a slip-based tire friction model. It can be used for objects other than wheels, but it is specifically designed for vehicles with wheels. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WheelCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WheelCollider) are raycast-based Colliders specifically for in-game items that have physics-simulated wheels (for example, vehicles). They have built-in wheel physics, and controls for friction.
## Collider surfaces
You can control the friction and bounciness of a collider’s surface. When two colliders meet, the physics system uses the properties of each surface to calculate the friction and bounce between them. 
For more information, see [Collider surfaces](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-surfaces.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
Collision
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-types-introduction.html)
Introduction to collider types
