* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/particle-velocity.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * [Configuring particles](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-particles.html)
  * [Particle movement](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-movement.html)
  * Particle velocity


[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-movement-patterns.html)
Particle movement patterns
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-particles-that-change-velocity-over-time.html)
Create particles that change velocity over time
# Particle velocity
Understand how the **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) can change a particle’s velocity.
## Limiting velocity over lifetime
The [Limit Velocity over Lifetime](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysLimitVelOverLifeModule.html) module is very useful for simulating air resistance that slows the particles, especially when a decreasing curve is used to lower the speed limit over time. For example, an explosion or firework initially bursts at great speed but the particles emitted from it rapidly slow down as they pass through the air.
The **Drag** option offers a more physically accurate simulation of air resistance by offering options to apply varying amounts of resistance based on the size and speed of the particles.
## Inheriting velocity
Use the [Inherit Velocity](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysInheritVelocity.html) module on subemitters. Each particle in the parent system can spawn particles in the subemitter. This module reads the velocity from the parent particle and controls how the speed of the subemitter particles reacts to that velocity over time.
## Details
This effect is very useful for emitting particles from a moving object, such as dust clouds from a car, smoke from a rocket, steam from a steam train’s chimney, or any situation where the particles should initially be moving at a percentage of the speed of the object they appear to come from. This module only has an effect on the particles when **Simulation Space** is set to **World** The area in your scene in which all objects reside. Often used to specify that coordinates are world-relative, as opposed to object-relative.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#World) in the [Main module](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysMainModule.html).
It is also possible to use curves to influence the effect over time. For example, you could apply a strong attraction to newly created particles, which reduces over time. This could be useful for steam train smoke, which would drift off slowly over time and stop following the train it was emitted from. 
Unity calculates the emitter’s velocity in one of two ways: * Based on the velocity of an attached **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) component * Based on how far the Particle System’s **Transform component** A Transform component determines the Position, Rotation, and Scale of each object in the scene. Every GameObject has a Transform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TransformComponent) travelled during the current frame
To specify the method Unity uses, see the Main module’s [Emitter Velocity](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysMainModule.html) property:
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-movement-patterns.html)
Particle movement patterns
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-particles-that-change-velocity-over-time.html)
Create particles that change velocity over time
