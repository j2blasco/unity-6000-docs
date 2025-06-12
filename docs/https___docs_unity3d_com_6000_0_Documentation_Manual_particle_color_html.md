* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/particle-color.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * [Configuring particles](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-particles.html)
  * [Particle appearance](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-appearance.html)
  * Change particle color


[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-size.html)
Particle size
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-lights-trails.html)
Particle lights and trails
# Change particle color
Understand how the **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) can change a particle’s rotation based on its speed or lifetime.
## Color by speed
The [Color by Speed](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysColorBySpeedModule.html) module can change a particle’s color based on its speed in distance units per second.
Burning or glowing particles (such as sparks) tend to burn more brightly when they move quickly through the air (for example, when sparks are exposed to more oxygen), but then dim slightly as they slow down. To simulate this, you might use _Color By Speed_ with a gradient that has white at the upper end of the speed range, and red at the lower end (in the spark example, faster particles will appear white while slower particles are red).
## Color over lifetime
The [Color Over Lifetime](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysColorOverLifeModule.html) module can change a particle’s color based on how long it has existed.
Many types of natural and fantastical particles vary in color over time, and so this property has many uses. For example, white hot sparks will cool as they pass through the air and a magic spell might burst into a rainbow of colors. Equally important, though, is the variation of alpha (transparency). It is very common for particles to burn out, fade or dissipate as they reach the end of their lifetime (for example, hot sparks, fireworks and smoke particles) and a simple diminishing gradient produces this effect.
When also using the [Start Color](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysMainModule.html) property, this module multiples the 2 colors together, to get the final particle color.
## Fade particles near opaque GameObjects
To fade particles near opaque **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), follow these steps:
  1. Enable a [deferred rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-paths-introduction.html#deferred), or [output a depth texture from the camera](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-CameraDepthTexture.html).
  2. Go to **Edit** > **Project Settings** > **Quality** , then enable **Soft Particles**.


Soft particles are supported only on platforms that support [depth textures](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-CameraDepthTexture.html).
![Soft particles disabled, with visible intersections with the scene.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SoftParticlesOff.jpg) Soft particles disabled, with visible intersections with the scene. ![Soft particles enabled, with intersections that fade out smoothly.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SoftParticlesOn.jpg) Soft particles enabled, with intersections that fade out smoothly.
## Additional resources
  * [Quality settings tab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-qualitysettings.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-size.html)
Particle size
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-lights-trails.html)
Particle lights and trails
