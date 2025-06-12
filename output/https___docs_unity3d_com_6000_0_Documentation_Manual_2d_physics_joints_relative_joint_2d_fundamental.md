* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/relative-joint-2d-fundamentals.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * [2D joints](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/2d-joints-landing.html)
  * [Relative Joint 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/relative-joint-2d-landing.html)
  * Relative Joint 2D fundamentals


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/relative-joint-2d-landing.html)
Relative Joint 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/relative-joint-2d-reference.html)
Relative Joint 2D component reference
# Relative Joint 2D fundamentals
The aim of this **joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) is to maintain a relative linear and angular distance (offset) between two points. Those two points can be two **Rigidbody2D** components or a **Rigidbody2D** component and a fixed position in the world. **Note:** Connect to a fixed position in the world by setting **Connected**Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody)** to None.
The joint applies a linear and angular (torque) force to both connected Rigidbody objects. It uses a simulated motor that is preconfigured to be quite powerful: It has a high **Max Force** and **Max Torque** limit. You can lower these values to make the motor less powerful motor or turn-off it off completely.
This joint has two simultaneous constraints:
  * Maintain the specified linear offset between the two Rigidbody objects.
  * Maintain the starting angular offset between the two Rigidbody objects.


You can use this joint to construct physical objects that need to:
  * Keep a distance apart from each other, as if they are unable to move further away from each other or closer together. (You decide the distance they are apart from each other. The distance can change in real-time.)
  * Rotate with respect to each other only at particular angle. (You decide the angle.)


Some uses may need the connection to be flexible, such as: A space-shooter game where the player has extra gun batteries that follow them. You can use the Relative Joint to give the trailing gun batteries a slight lag when they follow, but make them rotate with the player with no lag.
Some uses may need a configurable force, such as: A game where the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) follows a player using a configurable force to keep track.
## Comparing Fixed and Relative joints 2D
**FixedJoint2D** is spring type joint. **RelativeJoint2D** is a motor type joint with a maximum force and/or torque.
  * The **Fixed Joint** A joint type that is completely constrained, allowing two objects to be held together. Implemented as a spring so some motion may still occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FixedJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#FixedJoint) uses a spring to maintain the relative linear and angular offsets and the Relative joint uses a motor. You can configure a joint’s spring or motor.
  * The Fixed joint works with anchor points (it’s derived from script **AnchoredJoint2D**): It maintains the relative linear and angular offset between the anchors. The Relative joint doesn’t have anchor points (it’s derived directly from script **Joint2D**).
  * The Relative joint can modify the relative linear and angular offsets in real time: The Fixed joint cannot.


## Additional resources
  * [Joints 2D](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/2d-joints-landing.html)
  * [Relative Joint 2D component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/relative-joint-2d-reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/relative-joint-2d-landing.html)
Relative Joint 2D
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/joints/relative-joint-2d-reference.html)
Relative Joint 2D component reference
