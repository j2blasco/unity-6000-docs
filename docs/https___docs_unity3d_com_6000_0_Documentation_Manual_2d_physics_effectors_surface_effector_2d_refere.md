* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/surface-effector-2d-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [Effectors 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/effectors-2d-landing.html)
  * Surface Effector 2D reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/platform-effector-2d-reference.html)
Platform Effector 2D reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/2d-joints-landing.html)
2D joints
# Surface Effector 2D reference
The Surface Effector 2D applies tangent forces along the surfaces of **colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) used by the effector in an attempt to match a specified speed along the surface. This is analogous to a conveyor belt.
Colliders that you use with the effector would typically be set as non-triggers so that other colliders can come into contact with the surface.
## Properties
**Property** | **Function**  
---|---  
**Use Collider Mask** | Enable this to use the **Collider Mask** property. If this not enabled, the global **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) matrix will be used as the default for all Collider 2Ds.  
**Collider Mask** | The mask used to select specific Layers allowed to interact with the effector. Note that this option only displays if you have selected **Use Collider Mask**.  
**Speed** | Enter the speed to keep along the surface.  
**Speed Variation** | Enter a value here to apply a random increase in speed, where Unity selects a random number between 0 and the **Speed Variation** value. Entering a negative number here will result in a random reduction in speed instead, where Unity selects a random negative number between 0 and the **Speed Variation** value.  
**Force Scale** | Enter a value to scale the force that’s applied when the effector attempts to meet the specified **Speed** along the surface. If this is 0, then Unity applies no force. If this is 1, then Unity applies full force. **Note:** Entering 1 to apply full force can counteract any other forces being applied to the target object and cause unwanted movement or behavior. It’s recommended to enter a value less than 1 to prevent this issue from happening.  
**Use Contact Force** | Enable this to have Unity apply force at the point of contact between the surface and the target collider. Enabling contact forces can cause the target object to rotate when in contact with a surface.  
**Use Friction** | Enable this to enable friction between the collider and the surface it contacts.  
**Use Bounce** | Enable this to enable bounce between the collider and the surface it contacts.  
SurfaceEffector2D
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/platform-effector-2d-reference.html)
Platform Effector 2D reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/2d-joints-landing.html)
2D joints
