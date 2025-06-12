* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystemForceField.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * [Configuring particles](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-particles.html)
  * [Particle physics](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-physics.html)
  * Particle System Force Field component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-particle-trigger.html)
Configure a particle trigger
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-system-job-system-integration.html)
Optimize the Particle System with the C# Job System
# Particle System Force Field component reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField.html "Go to ParticleSystemForceField page in the Scripting Reference")
The **Particle System Force Field** component applies forces to particles in [Particle Systems](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem). 
## Shape
**Property** | **Function**  
---|---  
Shape | Select the shape of the area of influence.  
Start Range | Set the value for the inner point within the shape where the area of influence begins.  
End Range | Set the value for the outer point of the shape where the area of influence ends.  
Direction X, Y and Z | Set a linear force to apply to particles along the x-axis, y-axis and z-axis. The higher the value, the greater the force. You can specify a **constant force** A simple component for adding a constant force or torque to game objects with a Rigidbody. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConstantForce.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ConstantForce) or vary the force over time. See [Varying properties over time](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html) documentation for more information.  
## Gravity
**Property** | **Function**  
---|---  
Strength | Set the amount of attraction that particles have towards the focal point within the shape. The higher the value, the greater the strength. You can specify a constant strength or vary the strength over time. For more information, see [Varying properties over time](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html) documentation.  
Gravity Focus | Set the focal point for gravity to pull particles towards. A value of 0 attracts particles to the center of the shape, and a value of 1 attracts particles to the outer edge of the shape.  
## Rotation
**Property** | **Function**  
---|---  
Speed | Set the speed for the Particle System to propel particles around the vortex, which is the center of the force field. The higher the value, the faster the speed. You can specify a constant speed or vary the speed over time. For more information, see the [Varying properties over time](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html) documentation.  
Attraction | Set the strength that particles are dragged into the vortex motion. A value of 1 applies the maximum attraction, and a value of 0 applies no attraction. You can specify a constant attraction or vary the attraction over time. For more information, see the [Varying properties over time](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html) documentation.  
Rotation Randomness | Set a random axes of the shape to propel particles around. A value of 1 applies maximum randomness, and a value of 0 applies no randomness.  
## Drag
**Property** | **Function**  
---|---  
Strength | Set the strength of the drag effect which slows particles down. The higher the value, the greater the strength. You can specify a constant strength or vary the strength over time. For more information, see the [Varying properties over time](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html) documentation.  
Multiply Drag by Size | Enable this checkbox to adjust the drag based on the size of the particles.  
Multiply Drag by Velocity | Enable this checkbox to adjust the drag based on the velocity of the particles.  
## Vector Field
**Property** | **Function**  
---|---  
Volume Texture | Select the texture of the vector field.  
Speed | Set the speed of the multiplier to apply to particles traveling through the vector field. The higher the value, the faster the speed. You can specify a constant strength or vary the strength over time. See [Varying properties over time](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html).  
Attraction | Set the strength at which Unity drags particles into the vector field motion. The higher the value, the greater the attraction. You can specify a constant attraction or vary the attraction over time. See [Varying properties over time](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html).  
ParticleSystemForceField
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-particle-trigger.html)
Configure a particle trigger
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-system-job-system-integration.html)
Optimize the Particle System with the C# Job System
