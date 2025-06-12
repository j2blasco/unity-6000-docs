* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/introduction-to-rigidbody-2d-body-types.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [Rigidbody 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/rigidbody-2d-landing.html)
  * [Rigidbody 2D body types](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/rigidbody-2d-body-types-landing.html)
  * Introduction to Rigidbody 2D body types


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/rigidbody-2d-body-types-landing.html)
Rigidbody 2D body types
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/dynamic/dynamic-body-type-landing.html)
Dynamic Body Type
# Introduction to Rigidbody 2D body types
There are three options for **Body Type** Defines a fixed behavior for a 2D Rigidbody. Can be Dynamic (the body moves under simulation and is affected by forces like gravity), Kinematic (the body moves under simulation, but and isn’t affected by forces like gravity) or Static (the body doesn’t move under simulation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/introduction-to-rigidbody-2d.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#BodyType) which define the behavior of the **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) 2D. Any **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) 2D attached to that Rigidbody 2D inherits the Rigidbody 2D’s Body Type as well.
The selected Body Type defines the Rigidbody 2D’s movement behavior (position and rotation) and Collider interactions. When a Body Type changes, Unity recalculates various mass-related internal properties, and all existing contacts for the Collider 2Ds attached to the Rigidbody 2D need to be re-evaluated during the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject)’s next FixedUpdate. Depending on how many contacts and Collider 2Ds are attached to the body, changing the Body Type can cause variations in performance.
The properties of the Rigidbody 2D component in its **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window differs depending on which Body Type you have selected.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/rigidbody-2d-body-types-landing.html)
Rigidbody 2D body types
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/body-types/dynamic/dynamic-body-type-landing.html)
Dynamic Body Type
