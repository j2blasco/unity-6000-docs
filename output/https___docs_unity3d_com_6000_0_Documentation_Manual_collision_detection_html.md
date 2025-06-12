* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/collision-detection.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * Collision detection


[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions-example-scripts.html)
Example scripts for collider events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/choose-collision-detection-mode.html)
Choose a collision detection mode
# Collision detection
Collision detection is the **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsEngine)’s process for detecting when a physics body (Rigidbody or ArticulationBody) comes into contact with a **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider). Unity provides different **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) detection algorithms for different situations, so that you can choose the most efficient approach for each individual physics body (Rigidbody or Articulation Body) in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). 
**Topic** | **Description**  
---|---  
[Choose a collision detection mode](https://docs.unity3d.com/6000.0/Documentation/Manual/choose-collision-detection-mode.html) | Choose the right **collision detection** An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CollisionDetection) mode for each collider in your project.  
[Discrete collision detection](https://docs.unity3d.com/6000.0/Documentation/Manual/discrete-collision-detection.html)A collision detection method that calculates and resolves collisions based on the pose of objects at the end of each physics simulation step. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#discretecollisiondetection) | Overview of the high-efficiency discrete collision detection mode available in Unity.  
[Continuous collision detection (CCD)](https://docs.unity3d.com/6000.0/Documentation/Manual/ContinuousCollisionDetection.html) | Overview of the high-accuracy **continuous collision detection** A collision detection method that calculates and resolves collisions over the entire physics simulation step. This can prevent fast-moving objects from tunnelling through walls during a simulation step. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ContinuousCollisionDetection.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#continuouscollisiondetection) (CCD) modes available in Unity.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions-example-scripts.html)
Example scripts for collider events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/choose-collision-detection-mode.html)
Choose a collision detection mode
