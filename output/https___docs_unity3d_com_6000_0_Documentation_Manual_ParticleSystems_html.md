* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * Particle systems


[](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
Visual effects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ChoosingYourParticleSystem.html)
Choosing your particle system solution
# Particle systems
A **particle system** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) simulates and renders many small images or Meshes, called particles, to produce a visual effect. Each particle in a system represents an individual graphical element in the effect. The system simulates every particle collectively to create the impression of the complete effect.
![The holo table in Unitys Spaceship demo. Made with the Visual Effect Graph.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ParticleSystems-HoloTable.png) The holo table in Unity’s Spaceship demo. Made with the Visual Effect Graph.
Particle systems are useful when you want to create dynamic objects like fire, smoke, or liquids because it is difficult to depict this kind of object with a **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) (3D) or **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) (2D). Meshes and Sprites are better at depicting solid objects such as a house or a car.
This section contains information on:
  * [Which particle system solution to use for your Project](https://docs.unity3d.com/6000.0/Documentation/Manual/ChoosingYourParticleSystem.html).
  * [The Built-in Particle System](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysUsage.html).
  * [The Visual Effect Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/VFXGraph.html).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
Visual effects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ChoosingYourParticleSystem.html)
Choosing your particle system solution
