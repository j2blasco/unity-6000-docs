* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animation.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Legacy Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/Animations.html)
  * Legacy Animation component


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Animations.html)
Legacy Animation system
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
Physics
# Legacy Animation component
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html "Go to Animation page in the Scripting Reference")
This is the Legacy Animation component, which was used on **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) for animation purposes prior to the introduction of the Mecanim Animation system. This component is retained in Unity for backwards compatibility. For new projects, use the [Animator component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html)A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorComponent).
![The Animation Inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationInspector35.png) The Animation Inspector
## Properties
**Property** | **Function**  
---|---  
**Animation** | The default animation to play when **Play Automatically** is enabled.  
**Animations** | A list of animations that you can access from **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).  
**Play Automatically** | Enable this option to play animation automatically when the game starts.  
**Animate Physics** | Enable this option to have the animation interact with Physics.  
**Culling Type** | Determine when not to play the animation.
  * **Always Animate** : Always animate.
  * **Based on Renderers** : Cull based on the default animation pose.

  
Consult the [Animation Window Guide](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEditorGuide.html) for more information on how to create animations inside Unity. Consult [Model import workflows](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html) page on how to import animated characters.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Animations.html)
Legacy Animation system
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
Physics
