* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/choose-collision-detection-mode.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * [Collision detection](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-detection.html)
  * Choose a collision detection mode


[](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-detection.html)
Collision detection
[](https://docs.unity3d.com/6000.0/Documentation/Manual/discrete-collision-detection.html)
Discrete collision detection
# Choose a collision detection mode
****Collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) Detection** defines which algorithm the physics body (Rigidbody or ArticulationBody) uses to detect collisions. Different algorithms offer different levels of accuracy, but more accurate algorithms require more computational resources.
There are three algorithms available, represented by four **collision detection** An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CollisionDetection) modes:
**Collision detection mode** | **Algorithm** | **Useful for** | **Not useful for**  
---|---|---|---  
**Discrete** | Discrete | - Slow-moving collisions. | - Fast-moving collisions.  
**Continuous Speculative** | Speculative CCD | - Fast-moving collisions. | - Some fast-moving collisions that require an especially high degree of accuracy.  
**Continuous** | Sweep CCD | - Fast-moving linear collisions that require a high degree of accuracy.   
- Physics bodies that only collide with static colliders. | - Collisions that happen as a result of the physics body rotating.   
- Physics bodies that collide with moving colliders.  
**Continuous Dynamic** | Sweep CCD | - Fast-moving linear collisions that require a high degree of accuracy.   
- Physics bodies that collide with moving colliders. | - Collisions that happen as a result of the physics body rotating.  
The following decision flow might provide a starting point for selecting a collision detection type. It starts with the least computationally intensive mode, and progresses to the most computationally intensive mode.
  1. Try **Discrete** first.
  2. If you notice missed collisions in **Discrete** mode, try **Continuous Speculative**.
  3. If you notice missed collisions or false collisions in **Continuous Speculative** mode, try **Continuous** for collisions with static **colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider), or **Continuous Dynamic** for collisions with dynamic **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) colliders.


In some cases, you might find that the physics performance relies on a combination of the collision detection mode and the physics timestep frequency. Experiment with both and profile the results to find the right solution for your project. 
## Select a collision detection mode
To select an algorithm, set the physics body’s **Collision Detection** property in one of the following ways:
  * In the Editor: On the Rigidbody or Articulation Body component **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), change the **Collision Detection** property.
  * In code: Use the API properties [Rigidbody.collisionDetectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-collisionDetectionMode.html) and [ArticulationBody.collisionDetectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-collisionDetectionMode.html).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-detection.html)
Collision detection
[](https://docs.unity3d.com/6000.0/Documentation/Manual/discrete-collision-detection.html)
Discrete collision detection
