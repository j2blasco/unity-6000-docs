* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/introduction-to-rigidbody-2d.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [Rigidbody 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/rigidbody-2d-landing.html)
  * Introduction to Rigidbody 2D


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/rigidbody-2d-landing.html)
Rigidbody 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/rigidbody-2d-body-types-landing.html)
Rigidbody 2D body types
# Introduction to Rigidbody 2D
You can attach a Rigidbody 2D component to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to control it with the physics system. The Rigidbody 2D shares similar properties with its standard [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) counterpart, but it’s adapted to 2D development. For example, GameObjects that have a Rigidbody 2D component attached to them can only move along the XY plane and can only rotate on an axis perpendicular to that plane.
## How a Rigidbody 2D works
The Unity Editor’s [Transform](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html) component defines how to position, rotate, and scale a GameObject (and its child GameObjects) within the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). When you change this component, it updates other components which can affect where they render or the position of other **colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider). Unity’s 2D physics system can move colliders and make them interact with each other, so Unity requires a method for the physics system to communicate this movement of colliders back to the Transform components. This movement and connection with colliders is what a Rigidbody 2D component is for. The Rigidbody 2D component overrides the **Transform component** A Transform component determines the Position, Rotation, and Scale of each object in the scene. Every GameObject has a Transform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TransformComponent) and updates it to the position and/or rotation it defines instead.
**Note:** You can override the Rigidbody 2D by directly modifying the Transform component yourself (because Unity exposes all properties on all components). However, this will cause issues such as unpredictable movement or GameObjects passing through and into each other.
## Collider 2D and Rigidbody 2D interaction
Any Collider 2D component added to the same GameObject or child GameObject is implicitly attached to that Rigidbody 2D GameObject, causing the Collider 2D to move with the Rigidbody 2D. When attached, you should never move the Collider 2D directly using the Transform or any collider offset; move the Rigidbody 2D instead. Moving the Rigidbody 2D provides the best performance and ensures correct **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) detection. Collider 2Ds attached to the same Rigidbody 2D won’t collide with each other. This means you can create a set of colliders that act effectively as a single compound collider, all moving and rotating in sync with the Rigidbody 2D.
Adding a Rigidbody 2D moves a **sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) in a physically convincing way by applying forces from the scripting API. When you attach the appropriate collider component to the sprite GameObject, it’s affected by collisions with other moving GameObjects. Using the Unity physics system can simplify many common gameplay mechanics and portray realistic behavior with minimal coding.
**Note:** Although Rigidbody 2Ds are often described as colliding with each other, it’s the Collider 2Ds attached to each of those bodies which collide. Rigidbody 2Ds can’t collide with each other without Colliders.
## Additional resources
  * [API documentation on Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)
  * [API documentation on Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html)


Rigidbody2D
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/rigidbody-2d-landing.html)
Rigidbody 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/rigidbody-2d-body-types-landing.html)
Rigidbody 2D body types
