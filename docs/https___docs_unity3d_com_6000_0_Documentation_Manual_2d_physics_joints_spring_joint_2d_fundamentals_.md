* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/spring-joint-2d-fundamentals.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [2D joints](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/2d-joints-landing.html)
  * [Spring Joint 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/spring-joint-2d-landing.html)
  * Spring Joint 2D fundamentals


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/spring-joint-2d-landing.html)
Spring Joint 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/spring-joint-2d-reference.html)
Spring Joint 2D
# Spring Joint 2D fundamentals
This **joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) behaves like a spring, while keeping a linear distance between two points. You set this via the **Distance** setting. Those two points can be two **Rigidbody2D** components or a **Rigidbody2D** component and a fixed position in the world. (Connect to a fixed position in the world by setting **Connected Rigidbody** to None). The joint applies a linear force to both rigid bodies. It doesn’t apply torque (an angle force). 
The joint uses a simulated spring. You can set the spring’s stiffness and movement:
A stiff, barely moving spring…
  * A high (1,000,000 is the highest) **Frequency** == a stiff spring.
  * A high (1 is the highest) ****Damping Ratio** A joint setting to control spring oscillation. A higher damping ratio means the spring will come to rest faster. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/fixed-joint-2d-reference.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DampingRatio)** == a barely moving spring.


A loose, moving spring…
  * A low **Frequency** == a loose spring.
  * A low **Damping Ratio** == a moving spring.


When the spring applies its force between the objects, it tends to overshoot the distance you have set between them, and then rebound repeatedly, giving in a continuous oscillation. The **Damping Ratio** sets how quickly the objects stop moving. The **Frequency** sets how quickly the objects oscillate either side of the target distance.
This joint has one constraint:
  * Maintain a zero linear distance between two anchor points on two **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) objects.


You can use this joint to construct physical objects that need to react as if they are connected together using a spring or a connection which allows rotation. For example:
  * A character who’s body is composed of multiple objects that act as if they are semi-rigid. Use the **Spring Joint** A joint type that connects two Rigidbody components together but allows the distance between them to change as though they were connected by a spring. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SpringJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpringJoint) to connect the character’s body parts together, allowing them to flex to and from each other. You can specify whether the body parts are held together loosely or tightly.


**Note:** Spring Joint 2D uses a Box 2D spring-joint, which the Distance Joint 2D also uses with its frequency set to zero.
## Additional resources
  * [Joints 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/2d-joints-landing.html)
  * [Spring Joint 2D component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/spring-joint-2d-reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/spring-joint-2d-landing.html)
Spring Joint 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/spring-joint-2d-reference.html)
Spring Joint 2D
