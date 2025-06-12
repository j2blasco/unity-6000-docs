* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions-create-trigger.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * [Collider interactions](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions.html)
  * Create and configure a trigger collider


[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions-ontrigger.html)
OnTrigger events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions-example-scripts.html)
Example scripts for collider events
# Create and configure a trigger collider
A trigger **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) does not collide with other colliders; instead, other colliders pass through it.
To create a trigger collider:
  1. Create a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject): 
    1. To make an invisible trigger collider, create an empty GameObject. In most cases, trigger colliders are invisible.
    2. To make a visible trigger collider, create a GameObject that has a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh). You should only create a visible trigger collider if it is okay for other GameObjects to visibly pass through it at run time.
  2. Add a Collider to the GameObject.
  3. Make the collider a trigger: 
    1. To do this in the Editor, navigate to the collider’s **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) and enable the **Is Trigger** property.
    2. To do this via script, set the collider’s `IsTrigger` to `true`.


## Configure trigger collisions
Make sure there is at least one [dynamic collider](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-types-introduction.html) in the **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision). At least one GameObject involved in a trigger collision must have a physics body (a Rigidbody or an ArticulationBody). In most cases, trigger colliders are stationary and static (that is, they have no physics body), and the colliders that pass through them are moving and dynamic (that is, they have a physics body). 
Experiment with the size and shape of your trigger collider. For gameplay and simulation, triggers might need some adjustment to make them feel intuitive for the player. For example, you could experiment with making a trigger collider slightly larger than its associated visible GameObject, so that it has a wider radius. 
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions-ontrigger.html)
OnTrigger events
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions-example-scripts.html)
Example scripts for collider events
