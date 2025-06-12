* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/MecanimFAQ.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * Mecanim FAQ


[](https://docs.unity3d.com/6000.0/Documentation/Manual/MecanimPeformanceandOptimization.html)
Performance and optimization
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Animations.html)
Legacy Animation system
# Mecanim FAQ
## General questions
**What’s the difference between the Animation window and the**Animator window** The window where the Animator Controller is visualized and edited. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorWindow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorWindow)?**
Use the **Animation Window** to create and edit **animation clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) within Unity. You can use it to animate almost every property that you can edit in the **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), from a Game Object’s position, a material color, a light’s brightness, a sound’s volume, and even arbitrary values in your own **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
Use the **Animator Window** to organize your existing animation clip assets into a flowchart-like system called a **state machine** The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBasics.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StateMachine).
Both of these windows are part of the Mecanim Animation system, and not the Legacy Animation system.
**We use the Legacy Animation system for character animations. Should we use the Mecanim Animation system instead?**
Generally, yes you should since most character animations are more complex.
## Import
**Why does my imported**mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) have an **animator component** A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorComponent) attached to it?**
When Unity detects that an imported file has animation, it will add an animation component on import. You can modify this in the asset’s import settings by setting the Animation Type to `None` in the import settings under the Rig tab. You can do this with several files at once.
## Layers
**Does the ordering of the layers matter?**
Yes. Layers are evaluated from top to bottom in order. Layers set to override will always override the previous layers (based on their mask, if they have a mask).
**Should the weight value of the base layer always be set to one or should the weight be zero when using another layer?**
The base layer weight is always 1 and override layers will completely override the base layer.
**Is there any way to get a variable value from the controller without using the name string?**
You can use integers to identify the states and parameters. Use the [Animator.StringToHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.StringToHash.html) function to get the integer identifier values. For example:
```
runState = Animator.StringToHash("Base Layer.Run");
animator.SetBool(runState, false);


```

**What happens if a state on a Sync layer has a different length compared to the corresponding state in the base layer?**
If layers are of different lengths, they will become unsynchronized. Enable the Timing option to force the timing of the states on the current layer, on the source layer.
## Avatar Masks
**Is there a way to create AvatarIKGoals other than LeftFoot, RightFoot, LeftHand, RightHand?**
Yes, knee and elbow IK is supported.
**Is there a way to define what transforms are part of the**Avatar** An interface for retargeting animation from one rig to another. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Avatar) Mask?**
Yes, for Generic clips you can define which transform animation is imported or not. For Humanoid clips, all human transforms are always imported and extra transforms can be defined.
## Animations curves
**How do animations that have Curves blend with those that don’t?**
When you have an animation with a curve and another animation without a curve, Unity will use the default value of the parameter connected to the curve to do blending. You can set default values for your parameters, so when blending takes place between a State that has a Curve Parameter and one that does not have one, it will blend between the curve value and the default parameter value. To set a default value for a Parameter, simply set its value in the Animator Tool window while not in LiveLink.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MecanimPeformanceandOptimization.html)
Performance and optimization
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Animations.html)
Legacy Animation system
