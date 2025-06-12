* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ContinuousCollisionDetection.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * [Collision detection](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-detection.html)
  * Continuous collision detection (CCD)


[](https://docs.unity3d.com/6000.0/Documentation/Manual/discrete-collision-detection.html)
Discrete collision detection
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sweep-based-ccd.html)
Sweep-based CCD
# Continuous collision detection (CCD)
Continuous **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) detection (CCD) modes use predictive algorithms to calculate collisions that happen between physics timesteps. They are more accurate, but usually require more computational resources than discrete **collision detection** An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CollisionDetection). 
CCD is supported for Box, Sphere and Capsule **colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider). It is intended as a safety net to catch collisions in cases where colliders would otherwise pass through each other. However, it does not always deliver physically accurate collision results, so you might still consider decreasing the physics timestep frequency to make the simulation more precise.
In Unity, there are two CCD algorithms, represented by three **Collision Detection** mode options.
**Topic** | **Description**  
---|---  
[Speculative CCD](https://docs.unity3d.com/6000.0/Documentation/Manual/speculative-ccd.html) | Learn about speculative collision detection. **Continuous Speculative** uses speculative collision detection.  
[Sweep-based CCD](https://docs.unity3d.com/6000.0/Documentation/Manual/sweep-based-ccd.html) | Learn about sweep-based collision detection. Both **Continuous** and **Continuous Dynamic** modes use sweep-based collision detection.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/discrete-collision-detection.html)
Discrete collision detection
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sweep-based-ccd.html)
Sweep-based CCD
