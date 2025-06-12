* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/constant-force-2d-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/2d-physics.html)
  * Constant Force 2D reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/physics-profiler/use-physics-profiler-legacy-mode.html)
Use the Physics Profiler Legacy mode
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/physics-material-2d-reference.html)
Physics Material 2D reference
# Constant Force 2D reference
****Constant Force** A simple component for adding a constant force or torque to game objects with a Rigidbody. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConstantForce.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ConstantForce) 2D** is a quick utility for adding constant forces to a ****Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) 2D**. This works well for one-shot objects like rockets, if you want them to accelerate over time rather than starting with a large velocity.
Constant Force 2D applies both linear and torque (angular) forces continuously to the Rigidbody 2D, each time the **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsEngine) updates at runtime.
## Properties
**Property** | **Function**  
---|---  
**Force** | The linear force applied to the Rigidbody 2D at each physics update.  
**Relative Force** | The linear force, relative to the Rigidbody 2D coordinate system, applied each physics update.  
**Torque** | The torque applied to the Rigidbody 2D at each physics update.  
ConstantForce2D
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/physics-profiler/use-physics-profiler-legacy-mode.html)
Use the Physics Profiler Legacy mode
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/physics-material-2d-reference.html)
Physics Material 2D reference
