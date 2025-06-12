* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/access-particle-system-from-animation.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * Access the Particle System from the Animation system


[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-system-job-system-integration.html)
Optimize the Particle System with the C# Job System
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)
Particle System component reference
# Access the Particle System from the Animation system
All particle properties are accessible by the Animation system, meaning you can **keyframe** A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#keyframe) them in and control them from your animations.
To access the **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem)’s properties, follow these steps:
  1. Attach an **Animator component** A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorComponent) to the Particle System’s **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). An Animation Controller and an Animation are also required.
  2. To animate a Particle System property, open the **Animation Window** with the GameObject containing the Animator and Particle System selected. Click **Add Property** to add properties.
  3. Scroll to the right to reveal the **add controls**.


Note that for curves, you can only keyframe the overall **curve multiplier** , which can be found next to the curve editor in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-system-job-system-integration.html)
Optimize the Particle System with the C# Job System
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)
Particle System component reference
