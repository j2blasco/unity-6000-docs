* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/particle-rotation.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * [Configuring particles](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-particles.html)
  * [Particle movement](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-movement.html)
  * Particle rotation


[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-particles-that-change-velocity-over-time.html)
Create particles that change velocity over time
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-appearance.html)
Particle appearance
# Particle rotation
Understand how the **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) can change a particle’s rotation based on its speed or lifetime.
## Rotation by speed
The [Rotation by Speed](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysRotBySpeedModule.html) module can change a particle’s rotation based on its speed in distance units per second.
This module can be used when the particles represent solid objects moving over the ground such as rocks from a landslide. The rotation of the particles can be set in proportion to the speed so that they roll over the surface convincingly.
The Speed Range is only applied when the velocity is in one of the curve modes. Fast particles will rotate using the values at the right end of the curve, while slower particles will use values from the left side of the curve.
## Rotation over lifetime
The [Rotation Over Lifetime](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysRotOverLifeModule.html) module can change a particle’s rotation based on how long it has existed.
This module is useful when particles represent small solid objects, such as pieces of debris from an explosion. Assigning random values of rotation will make the effect more realistic than having the particles remain upright as they fly. The random rotations will also help to break up the regularity of similarly shaped particles (the same texture repeated many times can be very noticeable).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-particles-that-change-velocity-over-time.html)
Create particles that change velocity over time
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-appearance.html)
Particle appearance
