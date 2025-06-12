* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-SphereCollider.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * [Collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-shapes.html)
  * [Primitive collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/primitive-colliders.html)
  * Sphere collider component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BoxCollider.html)
Box collider component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CapsuleCollider.html)
Capsule collider component reference
# Sphere collider component reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html "Go to SphereCollider page in the Scripting Reference")
The Sphere **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) is a built-in sphere-shaped collider. It is useful for in-application items such as balls and marbles, or as a simple collider shape that you can stretch and scale to make marbles, projectiles, planets, and other spherical objects. **Sphere colliders** are also useful for items that need to roll and tumble, such as falling boulders.
The Sphere collider has relatively low resource requirements. 
**Property** | **Description**  
---|---  
**Edit Collider** | Enable the **Edit Collider** button to display the collider’s contact points in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view. You can click and drag these contact points to modify the size and shape of the collider. Alternatively, use the **Center** and **Size** properties.  
**Is Trigger** | If enabled, this collider is used for triggering events, and is ignored by the **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsEngine).  
**Provides Contacts** | Enable **Provides Contacts** to generate contact information for this collider at all times. Usually, a collider only generates contact data if there is something to send it to; in this case, the messages [`OnCollisionEnter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionEnter.html), [`OnCollisionStay`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionStay.html), or [`OnCollisionExit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionExit.html). When **Provides Contacts** is enabled, the collider generates contact data for the physics system at all times. Contact generation is resource-intensive, so **Provides Contacts** is disabled by default.  
**Material** | Reference to the [Physics Material](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsMaterial.html)A physics asset for adjusting the friction and bouncing effects of colliding objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsMaterial.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsMaterial) that determines how this collider interacts with others.  
**Center** | The position of the collider in the object’s local space.  
**Radius** | The size of the collider. This is the only available property for resizing the collider; it is not possible to resize along a specific axis (for example, to flatten the sphere into a non-spherical shape).  
## Layer overrides
The Layer Overrides section provides properties that allow you to override the project-wide [Layer-based collision detection](https://docs.unity3d.com/6000.0/Documentation/Manual/LayerBasedCollision.html) settings for this collider. 
**Property** | **Description**  
---|---  
**Layer Override Priority** | Define the priority of this collider override. When two colliders have conflicting overrides, the settings of the collider with the higher value priority are taken.   
For example, if a collider with a **Layer Override Priority** of 1 collides with a Collider with a **Layer Override Priority** of 2, the physics system uses the settings for the Collider with the **Layer Override Priority** of 2.  
**Include Layers** | Choose which Layers to include in **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) with this collider.  
**Exclude Layers** | Choose which Layers to exclude in collisions with this collider.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BoxCollider.html)
Box collider component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CapsuleCollider.html)
Capsule collider component reference
