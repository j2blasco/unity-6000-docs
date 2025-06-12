* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-constant-force.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Rigidbody physics](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-physics-section.html)
  * Apply constant force to a Rigidbody


[](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-configure-colliders.html)
Configure Rigidbody Colliders 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-interpolation.html)
Apply interpolation to a Rigidbody
# Apply constant force to a Rigidbody
To apply a constant linear or rotational force to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject)’s **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody), add the **Constant Force** A simple component for adding a constant force or torque to game objects with a Rigidbody. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConstantForce.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ConstantForce) component (represented by the API class [`ConstantForce`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConstantForce.html)) to your GameObject. See [Constant Force component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConstantForce.html) for details on how to configure the properties on the component.
## Set maximum velocity limitations
Constant force is not the same as constant speed. When you apply a constant force, the speed of movement accelerates over time based on the value of the force. In real life, this acceleration continues indefinitely. By default in Unity’s physics simulation, linear acceleration continues indefinitely, and angular acceleration continues until the Rigidbody reaches a max velocity of 50 rad/s. You can change these maximum velocities in code, via the properties [`Rigidbody.maxLinearVelocity`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-maxLinearVelocity.html) and [`Rigidbody.maxAngularVelocity`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-maxAngularVelocity.html).
## Configure constant forward acceleration
To make a GameObject constantly accelerate forward (for example, to make it behave like a rocket), do the following:
  1. Add a Constant Force component to the GameObject.
  2. On the Constant Force component, set the **Relative Force** Z axis to a positive value.
  3. On the Rigidbody, disable **Use Gravity**. This ensures that there is no competing gravitational force acting upon the GameObject.
  4. On the Rigidbody component, set the **Drag** property so that the Rigidbody does not exceed your preferred maximum velocity (the higher the drag, the lower the maximum velocity will be). This might require some trial and error to get the effect you want.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-configure-colliders.html)
Configure Rigidbody Colliders 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-interpolation.html)
Apply interpolation to a Rigidbody
