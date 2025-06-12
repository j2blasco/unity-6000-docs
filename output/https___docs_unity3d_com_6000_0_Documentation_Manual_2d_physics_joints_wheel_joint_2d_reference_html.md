* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/wheel-joint-2d-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [2D joints](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/2d-joints-landing.html)
  * [Wheel Joint 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/wheel-joint-2d-landing.html)
  * Wheel Joint 2D


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/wheel-joint-2d-fundamentals.html)
Wheel Joint 2D fundamentals
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/physics-profiler/physics-2d-profiler-landing.html)
Physics 2D Profiler
# Wheel Joint 2D
Use the **Wheel**Joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) 2D** to simulate a rolling wheel, on which an object can move. You can apply motor power to the joint. The wheel uses a suspension spring to maintain its distance from the main body of the vehicle.
## Properties
**Property** | **Function**  
---|---  
**Enable**Collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision)** | Enable this property to enable collisions between the two connected **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject).  
**Connected Rigid Body** | Specify the other GameObject this joint connects to. If you leave this as **None** , the other end of the joint is fixed to a point in space defined by the **Connected Anchor** setting. Select the circle icon to the right to view a list of GameObjects to connect to.  
**Auto Configure Connected Anchor** | Enable this property to automatically set the anchor location for the other GameObject this **Hinge Joint** A joint that groups together two Rigidbody components, constraining them to move like they are connected by a hinge. It is perfect for doors, but can also be used to model chains, pendulums and so on. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-HingeJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HingeJoint) 2D connects to. You do not need to enter coordinates for the **Connected Anchor** property if you enable this property.  
**Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to this GameObject.  
**Connected Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to the other GameObject.  
**Suspension** | Select this to expand this property’s settings.  
****Damping Ratio** A joint setting to control spring oscillation. A higher damping ratio means the spring will come to rest faster. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/fixed-joint-2d-reference.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DampingRatio)** | Set the degree to suppress spring oscillation. In the range 0 to 1, the higher the value, the less movement.  
**Frequency** | Set the frequency at which the spring oscillates while the GameObjects are approaching the separation distance you want (measured in cycles per second). In the range 0 to 1,000,000 - the higher the value, the stiffer the spring. **Note:** Setting **Frequency** to zero will create the stiffest spring type joint possible.  
**Angle** | Set the world movement angle for the suspension.  
**Use Motor** | Enable this to apply motor force to the joint.  
**Motor** | Select this to expand this property’s settings.  
**Motor Speed** | Target speed (degrees per second) for the motor to reach.  
**Maximum Motor Force** | Set the maximum torque (or rotation) the motor can apply when attempting to reach the target speed.  
**Break Action** | Set the action taken when either the force or torque threshold is exceeded.  
**Break Force** | Set the force threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
**Break Torque** | Set the torque threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/wheel-joint-2d-fundamentals.html)
Wheel Joint 2D fundamentals
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/physics-profiler/physics-2d-profiler-landing.html)
Physics 2D Profiler
