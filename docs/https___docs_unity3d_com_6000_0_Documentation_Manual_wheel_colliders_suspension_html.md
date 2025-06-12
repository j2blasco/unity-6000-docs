* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders-suspension.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Collision](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
  * [Collider shapes](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-shapes.html)
  * [Wheel colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders.html)
  * Wheel collider suspension


[](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders-friction.html)
Wheel collider friction
[](https://docs.unity3d.com/6000.0/Documentation/Manual/WheelColliderTutorial.html)
Create a car with Wheel colliders
# Wheel collider suspension
The [Wheel collider component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WheelCollider.html) has a set of properties that simulate a vehicle’s suspension system. 
To simulate suspension, the Wheel **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) sets a ****Target Position** A joint property to set the target position that the joint’s drive force should move it to. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConfigurableJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TargetPosition)** on the **Suspension Distance** line that it always tries to return the center to, and has **Spring** and **Damper** properties that affect how it moves away from that position and how it returns to that position. 
## Target Position
The **Target Position** of the **Wheel collider** A special collider for grounded vehicles. It has built-in collision detection, wheel physics, and a slip-based tire friction model. It can be used for objects other than wheels, but it is specifically designed for vehicles with wheels. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WheelCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WheelCollider) is the point along the **Suspension Distance** line that the center of the Wheel collider always returns to when there are no forces (or equal forces) acting upon it. 
To set the **Target Position** , specify a coordinate between 0 and 1 along the **Suspension Distance** line. 
  * A value of 0 sets the target position to the location of the wheel at fully extended suspension (the point furthest from the vehicle body, at the bottom of the **Suspension Distance** line).
  * A value of 1 sets the target position to the location of the wheel at fully compressed suspension (the point closest to the vehicle body, at the top of the **Suspension Distance** line).


By default the target position is 0.5, exactly midway between the points of maximum suspension spring extension and **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression). For most vehicle simulations, a typical value is between 0.3 and 0.7.
## Spring
In a real-world suspension system, the spring connects the wheel and axle to the vehicle’s frame and body, and sustains the weight of the vehicle body. The spring extends and compresses in response to changes in the **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain), and absorbs some of the upward force from the ground, so that the vehicle’s body doesn’t respond to every bump in the ground’s surface. How well the spring can absorb energy depends on its stiffness.
In the Unity PhysX simulation, the Wheel collider simulates the spring by moving up and down the **Suspension Distance** line on the vertical Y axis, away from the **Target Position**. The value of the **Spring** property represents the spring’s stiffness (in newtons per meter). 
A low value simulates a soft, flexible suspension spring that extends and compresses easily, without requiring very much force. In soft suspension, the flexible spring absorbs more bumps and jolts, so the vehicle’s body movement is smoother.
A high value simulates a stiff suspension spring that has more resistance to extension or compression, and therefore requires more force to move. In hard suspension, more bumps and jolts transfer to the vehicle’s body, but the vehicle overall has more responsive handling.
## Damper
In a real-world suspension system, the damper opposes the suspension spring’s movement and dissipates its stored energy. The strength of the damper’s impact defines how quickly the spring slows down and stops bouncing after being compressed or extended. The damper is often called the shock absorber.
In the Unity PhysX simulation, the Wheel collider simulates the damper or shock absorber by reducing the energy of the suspension **Spring**. The value of the **Damper** property represents the rate at which the energy dissipates (in newton seconds per meter). 
A high value simulates a hard damper that dissipates the **Spring** ’s energy quickly. Hard damping quickly reduces bounciness and returns the Wheel collider to a steady state at the **Target Position**. 
A lower value simulates a soft damper that dissipates the **Spring** ’s energy slowly. Soft damping allows more bounciness before the Wheel collider settles back into the **Target Position**.
## Mass and suspension values
By default, the Wheel collider’s **Spring** value is 35000, and the **Damper** value is 4500. These default values assume that the car’s total mass is 1500 kilograms. 
To set the vehicle’s mass, add a [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) component to the vehicle’s root **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). For a vehicle to work well with the default suspension settings, set the Rigidbody’s **Mass** to the recommended value of 1500. You can then test and iterate based on your specific vehicle setup.
PhysX calculates masses and forces proportionally, meaning they depend on the relative distances between each value. If you want to use a lower mass value for your vehicle (to match other Rigidbody masses on different GameObjects in the scene), you must also decrease the Wheel collider’s **Spring** and **Damper** values in the same proportion. For example, if you set the vehicle’s **Mass** to 15, you should also adjust the **Spring** and **Damper** to 350 and 45, respectively, instead of 35000 and 4500. This ensures consistent and realistic behavior in your vehicle simulation.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/wheel-colliders-friction.html)
Wheel collider friction
[](https://docs.unity3d.com/6000.0/Documentation/Manual/WheelColliderTutorial.html)
Create a car with Wheel colliders
