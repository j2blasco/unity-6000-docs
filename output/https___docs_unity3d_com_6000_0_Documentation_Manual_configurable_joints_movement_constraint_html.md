* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-joints-movement-constraint.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Joints](https://docs.unity3d.com/6000.0/Documentation/Manual/joints-section.html)
  * [Create a configurable joint](https://docs.unity3d.com/6000.0/Documentation/Manual/create-configurable-joint.html)
  * Customize movement constraint with Configurable Joints


[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-configurable-joint.html)
Create a configurable joint
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-joints-driving-forces.html)
Driving forces with Configurable Joints
# Customize movement constraint with Configurable Joints
You can use the Configurable **Joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) to constrain both the linear and rotational movement on each joint axis independently. 
Use **X, Y, Z Motion** for linear movement, and **X, Y, Z Rotation** for rotational movement. By default, these axes correspond to the object’s local axes, defined by the **Axis** property. To constrain movements to the global axes instead of the object’s local axes, enable **Configured In World Space**. 
You can set each axis to **Locked** , **Limited** or **Free** :
  * A **Locked** axis restricts all movement, so the joint cannot move at all. For example, an object locked in the global y-axis cannot move up or down.
  * A **Limited** axis allows free movement between limits that you define. For example, you could restrict a gun turret’s arc of fire by limiting its Y rotation to a specific angular range.
  * A **Free** axis allows any movement.


To limit linear movement, use the **Linear Limit** property, which defines the maximum distance the joint can move from its point of origin (measured along each axis separately).
![Illustration of a limit along the X axis](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/XZLimit.svg) Illustration of a limit along the X axis
To limit rotation, use the **Angular Limit** properties. You can specify different limit values for each axis with this property. You can also define separate upper and lower limits on the angle of rotation for the x-axis; the other two axes use the same angle either side of the original rotation. 
## Add bounce at the joint limits
You can simulate a bouncy surface at the joint’s limits. By default, a joint stops moving when it reaches its limit. However, a non-elastic **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) like this is rare in the real world, and it is often more realistic to add some bounce to a constrained joint. 
To make the constrained object bounce back after it reaches its limit, use the **Bounciness** property of the linear and angular limits. Use a low number for a more realistic, natural collision, or set it higher to simulate unusually bouncy boundaries like the cushions of a pool table.
![Bouncy joint does not cross the limit](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/CJointBounciness.svg) Bouncy joint does not cross the limit
## Add elasticity at the joint limits
You can simulate a spring-like elastic behavior to the joint when it exceeds its limits. To do this, use the spring properties **Linear Limit Spring** for linear movement, and **Angular X/YZ Limit Spring** for rotation. When you set the **Limit Spring** property to a value above zero, the joint does not stop moving when it hits a limit; instead, it crosses the limit, and the spring force draws it back to the limit position. The **Limit Spring** value determines the strength of the force. By default, the spring pulls the joint in the opposite direction to the collision. 
To reduce the elasticity and return the joint to the limit more gently, use the **Damper** property.
![Spring joint crosses the limit but is pulled back to it](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/CJointSpring.svg) Spring joint crosses the limit but is pulled back to it
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-configurable-joint.html)
Create a configurable joint
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-joints-driving-forces.html)
Driving forces with Configurable Joints
