* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConstantForce.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * [Rigidbody physics](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-physics-section.html)
  * Constant Force component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)
Rigidbody component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
Collision
# Constant Force component reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConstantForce.html "Go to ConstantForce page in the Scripting Reference")
****Constant Force**** adds constant forces to a [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-physics-section.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody). This is useful for **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) movement that accelerates over time.
If you add a Constant Force component to a GameObject that does not have a Rigidbody, Unity automatically creates and adds a Rigidbody to the same GameObject.
For more details, see [Apply constant force to a Rigidbody](https://docs.unity3d.com/6000.0/Documentation/Manual/rigidbody-constant-force.html).
## Properties
For all values, a higher value produces a stronger force, which in turn produces a faster initial velocity.
**Property:** | **Function:**  
---|---  
**Force** | Define the direction of the linear force. The XYZ vectors refer to the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)’s global axes.  
**Relative Force** | Define the direction of the linear force. The XYZ vectors refer to the Rigidbody’s local axes.  
**Torque** | Define the global axes that the Rigidbody rotates around.  
**Relative Torque** | Define the local axes that the Rigidbody rotates around.  
ConstantForce
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)
Rigidbody component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/collision-section.html)
Collision
