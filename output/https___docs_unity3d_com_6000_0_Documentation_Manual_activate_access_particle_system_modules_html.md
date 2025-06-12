* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/activate-access-particle-system-modules.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * [Particle System module component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystemModules.html)
  * Activate and access Particle System modules


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystemModules.html)
Particle System module component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysMainModule.html)
Main module reference
# Activate and access Particle System modules
The Particle System component has many properties, and for convenience, the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) organises them into collapsible sections called “modules”. These modules are documented in separate pages. See documentation on [Particle System Modules](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystemModules.html) to learn about each one.
To expand and collapse modules, click the bar that shows their name. Use the checkbox on the left to enable or disable the functionality of the properties in that module. For example, if you don’t want to vary the sizes of particles over their lifetime, uncheck the **Size over Lifetime** module.
The **Open Editor** button displays the options in a separate Editor window, which allows you to edit multiple systems at once. 
The [Particle Effect panel](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysUsage.html) in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) View contains some additional options for previewing Particle Systems.
All Particle System modules are part of the [Particle System](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) component.
To create a new Particle System and enable a module:
  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the Inspector, find the Particle System component.
  3. In the Particle System component, find the fold-out for the module you want to apply.
  4. To the left of the fold-out header, enable the checkbox.


# Access modules via the API
Modules are part of the Particle System component, so you can access it via the [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) class. 
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystemModules.html)
Particle System module component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysMainModule.html)
Main module reference
