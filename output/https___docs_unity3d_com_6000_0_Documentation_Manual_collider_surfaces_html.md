* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/collider-surfaces.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * Collider surfaces


[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-compound-collider.html)
Create a compound collider
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-surface-friction.html)
Collider surface friction
# Collider surfaces
In real-world physics, objects that can collide have different surface textures and properties that affect how they collide with each other, and how they interact with each other.
To control how objects collide with each other in the physics simulation, you can adjust the friction and bounciness of your **colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider). In Unity, you use the [Physics Material](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsMaterial.html)A physics asset for adjusting the friction and bouncing effects of colliding objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsMaterial.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsMaterial) asset to control these parameters. The Physics Material asset is represented in the API by the [`PhysicsMaterial`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial.html) class.
For more detailed information on how PhysX applies friction and bounce, see the Nvidia PhysX documentation [Rigid Body Dynamics: Friction and Restitution](https://docs.nvidia.com/gameworks/content/gameworkslibrary/physx/guide/Manual/RigidBodyDynamics.html#friction-and-restitution).
**Topic** | **Description**  
---|---  
[Collider surface friction](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-surface-friction.html) | How Unity handles friction on collider surfaces, and how to configure friction properties.  
[Collider surface bounciness](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-surface-bounce.html) | How Unity handles bounciness on collider surfaces, and how to configure bounce properties.  
[How collider surface values combine](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-surfaces-combine.html) | How Unity combines the values of surface properties in a collider pair; for example, how it calculates the friction between two colliders that have different friction values.  
[Create and apply a Physics Material](https://docs.unity3d.com/6000.0/Documentation/Manual/create-apply-physics-material.html) | Create and configure a Physics Material to define a collider’s surface properties, and apply it to a collider.  
[Physics Material component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsMaterial.html) | Reference page for the Physics Material asset.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-compound-collider.html)
Create a compound collider
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-surface-friction.html)
Collider surface friction
