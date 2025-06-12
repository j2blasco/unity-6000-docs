* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/capsule-collider/configure-capsule-collider-2d.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [Collider 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/collider-2d-landing.html)
  * [Capsule Collider 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/capsule-collider/capsule-collider-2d-landing.html)
  * Configure Capsule Collider 2D


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/capsule-collider/capsule-collider-2d-reference.html)
Capsule Collider 2D component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/composite-collider/composite-collider-2d-landing.html)
Composite Collider 2D
# Configure Capsule Collider 2D
There are multiple properties for a Capsule **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) 2D that you must configure before it can be used correctly.
## Defining size and direction
The settings that define the shape of the **Capsule Collider** A capsule-shaped collider component that handles collisions for GameObjects like barrels and character limbs. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CapsuleCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#capsulecollider) 2D are **Size** and **Direction**. Both the Size and Direction properties refer to **X** and **Y** (horizontal and vertical, respectively) in the local space of the Capsule Collider 2D, and not in world space.
A typical way to set up the Capsule Collider 2D is to set the **Size** to match the **Direction**. For example, if the Capsule Collider 2D’s **Direction** is **Vertical** , the **Size** of **X** is 0.5 and the **Size** of **Y** is 1, this makes the vertical direction capsule taller, rather than wider.
In the example below, the **X** and **Y** are represented by the yellow lines.
![An example of a Capsule Collider 2D set so the Size matches Direction](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/CapsuleCollider2D-Example1.png) An example of a Capsule Collider 2D set so the **Size** matches **Direction**
## Capsule configuration examples
You can change the Capsule Collider 2D with different configurations. Below are some examples.
Note that when the **X** and **Y** of the **Size** property are the same, the Capsule Collider 2D always approximates to a circle.
![Examples of Capsule Collider 2D configurations](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/CapsuleCollider2D-Example2.png) Examples of Capsule Collider 2D configurations
**Note:** A known issue in the 2D physics system is that when a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) moves across multiple Colliders, one or several of the Colliders may register a **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) between the Colliders. This may occur even when the Colliders are perfectly aligned. This collision can cause the Collider to slow down or stop.
While constructing a surface with the Capsule Collider 2D can help reduce this problem, it is recommeneded to use a single Collider rather than multiple Colliders for a surface, such as the [Edge Collider 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/edge-collider-2d-reference.html).
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/capsule-collider/capsule-collider-2d-reference.html)
Capsule Collider 2D component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/collider/composite-collider/composite-collider-2d-landing.html)
Composite Collider 2D
