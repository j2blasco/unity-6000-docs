* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/CharacterControllers.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Character control](https://docs.unity3d.com/6000.0/Documentation/Manual/character-control-section.html)
  * Introduction to character control


[](https://docs.unity3d.com/6000.0/Documentation/Manual/character-control-section.html)
Character control
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterController.html)
Character Controller component reference
# Introduction to character control
The character in a first- or third-person game usually needs some collision-based physics so that it doesn’t fall through the floor or walk through walls. In many applications, the character’s acceleration and movement are intentionally not physically realistic, so that the character can accelerate, brake and change direction almost instantly and without being affected by momentum.
In 3D physics, this type of behaviour can be created using a **Character Controller** A simple, capsule-shaped collider component with specialized features for behaving as a character in a game. Unlike true collider components, a Rigidbody is not needed and the momentum effects are not realistic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CharacterController). This component gives the character a simple, capsule-shaped **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) that is always upright. The controller has its own special functions to set the object’s speed and direction but unlike true colliders, a **rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) is not needed and the momentum effects are not realistic.
A character controller cannot walk through static colliders in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), and so will follow floors and be obstructed by walls. It can push rigidbody objects aside while moving but will not be accelerated by incoming **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision). This means that you can use the standard 3D colliders to create a scene around which the controller will walk but you are not limited by realistic physical behaviour on the character itself.
You can find out more about character controllers on the [reference page](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterController.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/character-control-section.html)
Character control
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterController.html)
Character Controller component reference
