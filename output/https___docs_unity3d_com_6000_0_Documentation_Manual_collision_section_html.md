* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * Collision


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConstantForce.html)
Constant Force component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)
Introduction to collision
# Collision
To configure **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) between GameObjects in Unity, you need to use colliders. colliders define the shape of a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) for the purposes of physical collisions. You can then use these colliders to manage collision events. You can configure collisions via **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) components, or their corresponding C# class. 
This documentation describes how to configure collisions and collision events, and how colliders interact with each other and their environment.
**Topic** | **Description**  
---|---  
[Introduction to collision](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html) | Overview of the fundamental concepts around physics collision in Unity.  
[Introduction to collider types](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-types-introduction.html) | The different collider types (static, kinematic, and dynamic), and how collider behaviour differs depending on the collider’s physics body configuration.  
[Collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-shapes.html) | The different collider shapes available, and how collider shape complexity affects performance.  
[Collider surfaces](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-surfaces.html) | How PhysX handles friction and bounciness on a collider’s surface, and how to configure surface properties for each collider.  
[Collider interactions and events](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions.html) | How collisions can call events and functions to trigger changes at run time.  
[Collision detection](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-detection.html)An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CollisionDetection) | How PhysX detects collisions in Unity, and how to select the right algorithm depending on your collider configuration for optimal performance.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConstantForce.html)
Constant Force component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)
Introduction to collision
