* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/area-effector-2d-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [Effectors 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/effectors-2d-landing.html)
  * Area Effector 2D reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/effectors-2d-landing.html)
Effectors 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/buoyancy-effector-2d-reference.html)
Buoyancy Effector 2D reference
# Area Effector 2D reference
The Area Effector 2D applies forces within an area defined by the attached **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) 2Ds when another (target) Collider 2D comes into contact with the Effector 2D. You can configure the force at any angle with a specific magnitude and random variation on that magnitude. You can also apply both linear and angular drag forces to slow down **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) 2Ds.
Collider 2Ds that you use with the Area Effector 2D would typically be set as triggers, so that other Collider 2Ds can overlap with it to have forces applied. Non-triggers will still work, but forces will only be applied when Collider 2Ds come into contact with them.
## Properties
**Property** | **Function**  
---|---  
**Use Collider Mask** | Check to enable use of the **Collider Mask** property? If this is not enabled, the Global **Collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) Matrix will be used as the default for all Collider 2Ds.  
**Collider Mask** | The mask used to select specific Layers allowed to interact with the Area Effector 2D.  
**Use Global Angle** | Check this to define the **Force Angle** as a global (world-space) angle. If this is not checked, the **Force Angle** is considered a local angle by the **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsEngine).  
**Force Angle** | The angle of the force to be applied.  
**Force Magnitude** | The magnitude of the force to be applied.  
**Force Variation** | The variation of the magnitude of the force to be applied.  
**Drag** | The linear drag to apply to Rigidbody 2Ds.  
**Angular Drag** | The angular drag to apply to Rigidbody 2Ds. The options are: 
  * **Collider** : Defines the target point as the current position of the Collider 2D. Applying force here can generate torque (rotation) if the Collider 2D isn’t positioned at the center of mass.
  * **Rigidbody** : Defines the target point as the current center of mass of the Rigidbody 2D. Applying force here will never generate torque (rotation).

  
AreaEffector2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/effectors-2d-landing.html)
Effectors 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/effectors/buoyancy-effector-2d-reference.html)
Buoyancy Effector 2D reference
