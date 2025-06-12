* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshCollider.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * [Collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-shapes.html)
  * [Mesh colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-colliders.html)
  * Mesh collider component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/prepare-mesh-for-mesh-collider.html)
Prepare a Mesh for Mesh colliders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders.html)
Wheel colliders
# Mesh collider component reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html "Go to MeshCollider page in the Scripting Reference")
The **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) takes a [mesh asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html) and builds a collider that matches the geometry of that mesh. It’s more accurate for **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) detection than using primitives, and is a better option for complicated meshes. 
Mesh colliders that are marked as **Convex** can collide with other **mesh colliders**.
**Property** | **Description**  
---|---  
**Convex** | Make the mesh collider collide with other mesh colliders. **Convex** mesh colliders are limited to 255 triangles.  
**Is Trigger** | Use the collider as a trigger for events. When **Is Trigger** is enabled, other colliders pass through this collider, and trigger the messages [`OnTriggerEnter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerEnter.html), [`OnTriggerStay`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerStay.html), and [`OnTriggerExit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerExit.html).  
**Provides Contacts** | Generate contact information for this collider at all times. Usually, a collider only generates contact data if there is something to send it to; in this case, the messages [`OnCollisionEnter`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionEnter.html), [`OnCollisionStay`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionStay.html), or [`OnCollisionExit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionExit.html). When **Provides Contacts** is enabled, the collider generates contact data for the physics system at all times. Contact generation is resource-intensive, so **Provides Contacts** is disabled by default.  
**Cooking Options** | Enable or disable the mesh cooking options that affect how the physics system processes meshes. When you set the **Cooking Options** to any other value than the default settings (that is, everything enabled except **None**), the mesh collider must use a mesh that has an [`isReadable`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-isReadable.html) value of `true`. For details on mesh cooking, refer to [Prepare a mesh for mesh colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/prepare-mesh-for-mesh-collider.html). Select from the following options:
  * **None** : Disables all **Cooking Options**. This is disabled by default.
  * **Everything** : Enables all **Cooking Options**. This is enabled by default.
  * **Cook for Faster Simulation** : The cooking process preprocesses the mesh data and stores it in memory to speed up runtime calculations. This is useful for complex meshes in the scene. When this setting is disabled, the physics system uses a faster cooking time, but retrieves the mesh data more slowly at runtime. This is enabled by default.
  * **Enable Mesh Cleaning** : The cooking process attempts to clear the mesh of degenerate triangles on the mesh (that is, triangles in which all three points are collinear, and do not form a triangle shape) and other geometrical artifacts. This results in a mesh that is better suited for use in collision detection, and tends to produce more accurate contact points. When this setting is disabled, the physics system uses a faster cooking time but implements less optimization. This is enabled by default.
  * **Weld Colocated Vertices** : The cooking process combines vertices that have the same position. This results in a mesh that is better suited for use in collision detection, and tends to produce more accurate contact points. When this setting is disabled, the physics system uses a faster cooking time but implements less optimization. This is enabled by default.
  * **Use Fast Midphase** : The cooking process uses the fastest mid-phase acceleration structure and algorithm available for your output platform. The fastest algorithm doesn’t require any R-Trees for spatial access. If you encounter midphase issues at runtime, disable this option; Unity then uses the slower legacy midphase algorithm instead. This is enabled by default.

  
**Material** | Reference to the [Physics Material](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsMaterial.html)A physics asset for adjusting the friction and bouncing effects of colliding objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsMaterial.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsMaterial) that determines how this collider interacts with others.  
**Mesh** | Reference to the mesh to use for collisions.  
## Layer overrides
The Layer Overrides section provides properties that allow you to override the project-wide [Layer-based collision detection](https://docs.unity3d.com/6000.0/Documentation/Manual/LayerBasedCollision.html) settings for this collider. 
**Property** | **Description**  
---|---  
**Layer Override Priority** | Define the priority of this collider override. When two colliders have conflicting overrides, the settings of the collider with the higher value priority are taken.   
For example, if a collider with a **Layer Override Priority** of 1 collides with a Collider with a **Layer Override Priority** of 2, the physics system uses the settings for the Collider with the **Layer Override Priority** of 2.  
**Include Layers** | Choose which Layers to include in collisions with this collider.  
**Exclude Layers** | Choose which Layers to exclude in collisions with this collider.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/prepare-mesh-for-mesh-collider.html)
Prepare a Mesh for Mesh colliders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders.html)
Wheel colliders
