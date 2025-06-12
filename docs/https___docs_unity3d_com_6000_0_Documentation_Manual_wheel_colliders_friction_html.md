* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders-friction.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * [Collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-shapes.html)
  * [Wheel colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders.html)
  * Wheel collider friction


[](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders-introduction.html)
Introduction to Wheel colliders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders-suspension.html)
Wheel collider suspension
# Wheel collider friction
The Wheel **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) calculates wheel friction separately from the rest of the **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsEngine), and ignores standard [Physic Material](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsMaterial.html) settings. Instead, it uses a slip-based friction model, which provides more realistic behavior.
In most cases, the **Wheel collider** A special collider for grounded vehicles. It has built-in collision detection, wheel physics, and a slip-based tire friction model. It can be used for objects other than wheels, but it is specifically designed for vehicles with wheels. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WheelCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WheelCollider)’s default friction settings are sufficient to create a working vehicle. To work with the wheel friction settings, you should have an understanding of forward slip (also called longitudinal slip) and sideways slip (also called lateral slip) in the context of real-world vehicle dynamics. This understanding is necessary if you want to build an extremely realistic vehicle or you want to have finer control of the friction and slip behavior of your wheels. 
On real-world vehicles, wheels can exert high forces and high friction at low slip because the rubber stretches to compensate for the slip. When the slip gets too high, the wheel starts to slide or spin, which reduces the amount of force they exert. Unity uses a wheel friction curve to define and describe this behavior.
## Wheel friction curve properties
The Wheel collider has two groups of properties for wheel friction: **Forward Friction** and **Sideways Friction**. Each group has the same four settings (refer to the [Wheel collider component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WheelCollider.html) for detailed information on each property): 
  * **Extremum Slip** ([`WheelFrictionCurve.extremumSlip`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve-extremumSlip.html))
  * **Extremum Value** ([`WheelFrictionCurve.extremumValue`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve-extremumValue.html))
  * **Asymptote Slip** ([`WheelFrictionCurve.asymptoteSlip`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve-asymptoteSlip.html))
  * **Asymptote Value** ([`WheelFrictionCurve.asymptoteValue`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve-asymptoteValue.html))


These [`WheelFrictionCurve`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve.html) properties describe the curve that demonstrates the relationship between the slip and the wheel’s force in a typical wheel friction setup. There is one curve for forward friction, and one for sideways friction.
![Typical shape of a wheel friction curve.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/WheelFrictionCurve.png) Typical shape of a wheel friction curve.
The curve starts at 0 slip and 0 force. When the slip increases, the force also increases until it reaches a maximum force that the wheel can maintain (the **Extremum** point). The coordinates for this point are (`ExtremumSlip` , `ExtremumValue`). 
When the slip increases further, the wheel starts to slide or spin, and can no longer maintain the maximum force. As a result, the force decreases until it reaches a point where it can remain steady and consistent as the slip continues to increase (the **Asymptote** point). The coordinates for this point are (`AsymptoteSlip` , `AsymptoteValue`).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders-introduction.html)
Introduction to Wheel colliders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders-suspension.html)
Wheel collider suspension
