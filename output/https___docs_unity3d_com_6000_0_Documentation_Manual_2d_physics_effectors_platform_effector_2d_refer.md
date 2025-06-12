* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/platform-effector-2d-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [Effectors 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/effectors-2d-landing.html)
  * Platform Effector 2D reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/point-effector-2d-reference.html)
Point Effector 2D reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/surface-effector-2d-reference.html)
Surface Effector 2D reference
# Platform Effector 2D reference
The Platform Effector 2D applies various platform behavior such as one-way **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision), removal of side-friction/bounce and more.
Colliders used with the Effector are typically not set as triggers so that other **colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) can collide with it.
## Properties
**Property** | **Function**  
---|---  
**Use Collider Mask** | Select this option to indicate the use of the Collider Mask property. If this isn’t selected, the global collision matrix is chosen as the default for all colliders.  
**Collider Mask** | The mask used to select specific layers allowed to interact with the Effector.  
**Use One Way** | Select this option to indicate if one-way collision behavior is used.  
**Use One Way Grouping** | Ensures that all contacts disabled by the one-way behavior act on all colliders. This is useful when using multiple colliders on the object passing through the platform and they all need to act together as a group.  
**Surface Arc** | The angle of an arc centered on the local “up” defines the surface which doesn’t allow colliders to pass. Anything outside of this arc is considered for one-way collision.  
**Use Side Friction** | Select this option to indicate if the friction is used on the platform sides.  
**Use Side Bounce** | Select to indicate if bounce is used on the platform sides.  
**Side Arc** | The angle of an arc that defines the sides of the platform centered on the local “left” and “right” of the Effector. Any collision normals within this arc are considered for the “side” behaviors.  
PlatformEffector2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/point-effector-2d-reference.html)
Point Effector 2D reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/surface-effector-2d-reference.html)
Surface Effector 2D reference
