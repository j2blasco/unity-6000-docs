* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/slider-joint-2d-fundamentals.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [2D joints](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/2d-joints-landing.html)
  * [Slider Joint 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/slider-joint-2d-landing.html)
  * Slider Joint 2D fundamentals


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/slider-joint-2d-landing.html)
Slider Joint 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/slider-joint-2d-reference.html)
Slider Joint 2D
# Slider Joint 2D fundamentals
Use this **joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) slide **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) by maintaining the position of two points on a configurable line that extends to infinity. Those two points can be two **Rigidbody2D** components, or a **Rigidbody2D** component and a fixed position in the world (by setting **Connected Rigidbody** to **None**).
The joint applies a linear force to both connected **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) objects to keep them on the line. It also has a simulated linear motor that applies linear force to move the Rigidbody GameObjects along the line. You can turn the motor off or on. Although the line is infinite, you can specify just a segment of the line that you want to use, using the **Translation Limits** option.
This joint has three simultaneous constraints. All are optional:
  * Maintain a relative linear distance away from a specified line between two anchor points on two Rigidbody objects.
  * Maintain a linear speed between two anchor points on two Rigidbody objects along a specified line. (The speed is limited with a maximum force.)
  * Maintain a linear distance between two points along the specified line.


You can use this joint to construct physical objects that need to react as if they are connected together on a line. For example:
  * A platform which can move up or down. The platform reacts by moving down when something lands on it but must never move sideways. You can use this joint to ensure platform to never moves up or down beyond certain limits. Use the motor to make the platform move up.


## Additional resources
  * [Joints 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/2d-joints-landing.html)
  * [Slider Joint 2D component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/slider-joint-2d-reference.html)


SliderJoint2D
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/slider-joint-2d-landing.html)
Slider Joint 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/slider-joint-2d-reference.html)
Slider Joint 2D
