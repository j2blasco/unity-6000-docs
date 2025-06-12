* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/target-joint-2d-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [2D joints](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/2d-joints-landing.html)
  * [Target Joint 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/target-joint-2d-landing.html)
  * Target Joint 2D


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/target-joint-2d-fundamentals.html)
Target Joint 2D fundamentals
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/wheel-joint-2d-landing.html)
Wheel Joint 2D
# Target Joint 2D
This **joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) connects to a specified target, rather than another **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) object as other joints do. This behaves in a similar way to a spring type joint.
## Properties
**Property** | **Function**  
---|---  
**Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to this **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject).  
**Target** | Define where (in terms of x, y-coordinates in world space) the other end of the joint attempts to move.  
**Auto Configure Target** | Enable this property to automatically set the other end of the joint to the current position of the GameObject. **Note:** When this option is enabled, the target changes as you move the GameObject but the target will not change if the option is not enabled.  
**Max Force** | Set the force that the joint can apply when attempting to move the object to the **target position** A joint property to set the target position that the joint’s drive force should move it to. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConfigurableJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TargetPosition). The higher the value, the higher the maximum force.  
****Damping Ratio** A joint setting to control spring oscillation. A higher damping ratio means the spring will come to rest faster. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/fixed-joint-2d-reference.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DampingRatio)** | Set the degree to suppress spring oscillation. In the range 0 to 1, the higher the value, the less movement.  
**Frequency** | Set the frequency at which the spring oscillates while the GameObjects are approaching the separation distance you want (measured in cycles per second). In the range 0 to 1,000,000 - the higher the value, the stiffer the spring. **Note:** Setting **Frequency** to zero will create the stiffest spring type joint possible.  
**Break Action** | Set the action taken when either the force or torque threshold is exceeded.  
**Break Force** | Set the force threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/target-joint-2d-fundamentals.html)
Target Joint 2D fundamentals
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/wheel-joint-2d-landing.html)
Wheel Joint 2D
