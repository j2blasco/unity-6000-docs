* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/configure-driving-forces.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Joints](https://docs.unity3d.com/6000.0/Documentation/Manual/joints-section.html)
  * [Create a configurable joint](https://docs.unity3d.com/6000.0/Documentation/Manual/create-configurable-joint.html)
  * Configure driving forces on a Configurable Joint


[](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-joints-driving-forces.html)
Driving forces with Configurable Joints
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConfigurableJoint.html)
Configurable Joint component reference
# Configure driving forces on a Configurable Joint
Use the Configurable **Joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) to create custom targets and driving forces for a simulated motor.
To configure driving forces on a **Configurable Joint** An extremely customizable joint that other joint types are derived from. It can be used to create anything from adapted versions of existing joints to custom designed and highly specialized joints. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConfigurableJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ConfigurableJoint): 1. Choose whether you want to [apply a target position](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-driving-forces.html#apply-target-position) or [apply a target velocity](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-driving-forces.html#apply-target-velocity) for the driving force to reach. Targets can be linear (directional) or angular (rotational). 1. [Configure driving forces](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-driving-forces.html#configure-driving-forces) for the respective axes, using properties that simulate a spring and damper system.
**Note** : You can apply both a linear force and a rotational force to a joint. However, you should not apply more than one linear force or more than one rotational force. If you apply more than one, the physics system attempts to solve both at once and produces unwanted results. For example, if you apply a rotational force **Target Rotation** and a linear force ****Target Velocity** A joint property to set the desired velocity with which the joint should move to the Target Position under the drive force. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConfigurableJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TargetVelocity)**, you would create a joint that stays at a specific rotation and moves at a specific linear velocity. However, if you apply two rotational forces, a **Target Rotation** and a **Target Angular Velocity** , the physics system attempts to keep the object at a specific rotation while also rotating it at a specific velocity.
## Apply a target position
To apply a spring-like behavior that always tries to return the object to a specified position or rotation, set a **target position** A joint property to set the target position that the joint’s drive force should move it to. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConfigurableJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TargetPosition). You can set a linear position, a rotational position, or both.
  * To set a position in the space defined by **Axis** , use the **Target Position** ’s **X** , **Y** and **Z** values.
  * To set a rotation the space defined by **Axis** , use the **Target Rotation** ’s **X** , **Y** and **Z** values.


You must also set the respective linear or angular axis drives, as described on [Driving forces with Configurable Joints](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-joints-driving-forces.html).
**Important** : For a Configurable Joint to apply the driving force necessary to reach the target position, the **Position Spring** value on any affected axis drive must be something other than `0`. 
## Apply a target velocity
To apply a specific continuous velocity, set a target velocity. You can set a linear motion velocity, a rotational motion velocity, or both.
To set a target linear velocity, use the **Target Velocity** ’s **X** , **Y** and **Z** values. These values configure each axis individually, in meters per second.
To set a target angular velocity, there are two options: 
  * To configure the driving force for each axis individually, set **Rotational Drive Mode** to **X and YZ** , and use the **Target Angular Velocity** ’s **X** , **Y** and **Z** values. These values configure each axis individually, in radians per second.
  * To configure the rotation without setting specific driving forces, set **Rotational Drive Mode** to **Slerp Drive**. The **Slerp Drive** uses the **quaternion** Unity’s standard way of representing rotations as data. When writing code that deals with rotations, you should usually use the Quaternion class and its methods. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/QuaternionAndEulerRotationsInUnity.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Quaternion)’s spherical interpolation or “slerp” functionality to reorient the joint. Rather than isolating individual axes, the slerp process finds the minimum total rotation that takes the object from the current orientation to the target, and applies it on all axes as necessary.


You must also set the respective linear or angular axis drives, as described on [Driving forces with Configurable Joints](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-joints-driving-forces.html).
**Important** : For a Configurable Joint to apply the driving force necessary to reach the target velocity, the **Position Damper** value on any affected axis drive must be something other than `0`. 
## Configure driving forces
For each axis drive you want to apply force on, use **Position Spring** to configure the spring force to apply, and **Position Damper** to configure the damping effect on that spring force.
Apply trial and error on the spring and damper values to achieve the results you need, and test at run time to check that the forces you apply are enough to counter any other forces applied to the object.
**Note** : You can apply both a linear force and a rotational force to a joint. However, you should not apply more than one directional force or more than one rotational force. If you apply more than one, the physics system attempts to solve both at once and produces unwanted results. For example, if you apply a rotational force **Target Rotation** and a linear force **Target Velocity** , you would create a joint that stays at a specific rotation and moves at a specific linear velocity. However, if you apply two rotational forces, a **Target Rotation** and a **Target Angular Velocity** , the physics system attempts to keep the object at a specific rotation while also rotating it at a specific velocity.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-joints-driving-forces.html)
Driving forces with Configurable Joints
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConfigurableJoint.html)
Configurable Joint component reference
