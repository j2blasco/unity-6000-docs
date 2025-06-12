* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-CapsuleCollider.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * [Collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-shapes.html)
  * [Primitive collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/primitive-colliders.html)
  * Capsule collider component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SphereCollider.html)
Sphere collider component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-colliders.html)
Mesh colliders
# Capsule collider component reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CapsuleCollider.html "Go to CapsuleCollider page in the Scripting Reference")
The Capsule **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) is a built-in 3D capsule-shaped collider made of two half-spheres joined together by a cylinder. It is useful for in-application items that have a cylindrical shape, or as a collider for player and non-player characters in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
Because **Capsule colliders** have no corners, they are also useful to soften the **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) area of sharp corners and edges in level geometry, so that players move more smoothly.
The Capsule collider has relatively low resource requirements. 
**Property** | **Description**  
---|---  
**Edit Collider** | Enable the **Edit Collider** button to display the collider’s contact points in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView). You can click and drag these contact points to modify the size and shape of the collider. Alternatively, use the **Center** , **Radius** , and **Height** properties.  
**Is Trigger** | Enable **Is Trigger** to use the collider as a trigger for events. When **Is Trigger** is enabled, other colliders pass through this collider, and trigger the messages [`OnTriggerEnter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerEnter.html), [`OnTriggerStay`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerStay.html), and [`OnTriggerExit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerExit.html).  
**Provides Contacts** | Enable **Provides Contacts** to generate contact information for this collider at all times. Usually, a collider only generates contact data if there is something to send it to; in this case, the messages [`OnCollisionEnter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionEnter.html), [`OnCollisionStay`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionStay.html), or [`OnCollisionExit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionExit.html). When **Provides Contacts** is enabled, the collider generates contact data for the physics system at all times. Contact generation is resource-intensive, so **Provides Contacts** is disabled by default.  
**Material** | Add the [Physic Material component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsMaterial.html) that determines the friction and bounciness of this collider.  
**Center** | Define the position of the collider on each axis in the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject)’s local space. By default, this is set to (0, 0, 0).  
**Radius** | Define the radius of the collider from its center. You can adjust the **Radius** independently of the **Height**. By default, this is set to 0.5.  
**Height** | Define the total height of the collider in **Unity units** The unit size used in Unity projects. By default, 1 Unity unit is 1 meter. To use a different scale, set the Scale Factor in the Import Settings when importing assets.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Unityunit). You can adjust the **Height** independently of the **Radius**. By default, this is set to 2.  
**Direction** | Define the axis of the capsule’s lengthwise orientation in the object’s local space.  
## Layer overrides
The Layer Overrides section provides properties that allow you to override the project-wide [Layer-based collision detection](https://docs.unity3d.com/6000.0/Documentation/Manual/LayerBasedCollision.html) settings for this collider. 
**Property** | **Description**  
---|---  
**Layer Override Priority** | Define the priority of this collider override. When two colliders have conflicting overrides, the settings of the collider with the higher value priority are taken.   
For example, if a collider with a **Layer Override Priority** of 1 collides with a Collider with a **Layer Override Priority** of 2, the physics system uses the settings for the Collider with the **Layer Override Priority** of 2.  
**Include Layers** | Choose which Layers to include in collisions with this collider.  
**Exclude Layers** | Choose which Layers to exclude in collisions with this collider.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SphereCollider.html)
Sphere collider component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-colliders.html)
Mesh colliders
