* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/hinge-joint-2d-fundamentals.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [2D joints](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/2d-joints-landing.html)
  * [Hinge Joint 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/hinge-joint-2d-landing.html)
  * Hinge Joint 2D fundamentals


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/hinge-joint-2d-landing.html)
Hinge Joint 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/hinge-joint-2d-reference.html)
Hinge Joint 2D component reference
# Hinge Joint 2D fundamentals
The Hinge **Joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) 2D’s is used to have a joint that allows a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to rotate around a particular point, for example a door hinge, wheels, or pendulums.
You can use this joint to make two points overlap. Those two points can be two ****Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) 2D** components, or a **Rigidbody 2D** component and a fixed position in the world space. Connect the **Hinge Joint** A joint that groups together two Rigidbody components, constraining them to move like they are connected by a hinge. It is perfect for doors, but can also be used to model chains, pendulums and so on. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-HingeJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HingeJoint) 2D to a fixed position in the world by setting **Connected Rigidbody** to **None**. The joint applies a linear force to both connected Rigidbody 2D GameObjects.
The Hinge Joint 2D has a simulated rotational motor which you can turn on or off. Set the **Maximum Motor Speed** and **Maximum Motor Force** to control the angular speed (**Torque**) and make the two Rigidbody 2D GameObjects rotate in an arc relative to each other. Set the limits of the arc using **Lower Angle** and **Upper Angle**.
## Constraints
Hinge Joint 2D has three simultaneous constraints. All are optional:
  * Maintain a relative linear distance between two anchor points on two Rigidbody 2D GameObjects.
  * Maintain an angular speed between two anchor points on two Rigidbody 2D GameObjects (limited with a maximum torque in **Maximum Motor Force**).
  * Maintain an angle within a specified arc.


You can use this joint to construct physical GameObjects that need to behave as if they are connected with a rotational pivot. For example:
  * A see-saw pivot where the horizontal section is connected to the base. Use the joint’s **Angle Limits** to simulate the highest and lowest point of the see-saw’s movement.
  * A pair of scissors connected together with a hinge pivot. Use the joint’s **Angle Limits** to simulate the closing and maximum opening of the scissors.
  * A simple wheel connected to the body of a car with the pivot connecting the wheel at its center to the car. In this example you can use the Hinge Joint 2D’s motor to rotate the wheel.


## Additional resources
  * [Joints 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/2d-joints-landing.html)
  * [Hinge Joint 2D component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/hinge-joint-2d-reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/hinge-joint-2d-landing.html)
Hinge Joint 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/hinge-joint-2d-reference.html)
Hinge Joint 2D component reference
