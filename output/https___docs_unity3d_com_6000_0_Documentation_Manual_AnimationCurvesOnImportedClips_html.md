* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationCurvesOnImportedClips.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Models](https://docs.unity3d.com/6000.0/Documentation/Manual/models.html)
  * [Importing models into Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/models-importing.html)
  * [Model Import Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html)
  * [Animation tab](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)
  * Curves


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LoopingAnimationClips.html)
Loop optimization on Animation clips
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEventsOnImportedClips.html)
Events
# Curves
You can attach **animation curves** to imported **animation clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) in the [Animation tab](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html).
You can use these curves to add additional animated data to an imported clip. You can use that data to animate the timings of other items based on the state of an animator. For example, in a game set in icy conditions, an extra animation curve could be used to control the emission rate of a **particle system** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) to show the player’s condensing breath in the cold air.
To add a curve to an imported animation, expand the **Curves** section at the bottom of the [Animation tab](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html), and click the plus icon to add a new curve to the current animation clip:
![The expanded Curves section on the Animation tab](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/classAnimationClip-Curves.png) The expanded Curves section on the Animation tab
If your imported animation file is split into multiple animation clips, each clip can have its own custom curves. 
![The curves on an imported animation clip](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/MecanimCurves.png) The curves on an imported animation clip
The curve’s X-axis represents _normalized time_ and always ranges between 0.0 and 1.0 (corresponding to the beginning and the end of the animation clip respectively, regardless of its duration). 
![Unity Curve Editor](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/CurveEditorPopupDescr.png) Unity Curve Editor
**(A)** Wrapping mode
**(B)** Curve Presets
Double-clicking an animation curve brings up the [standard Unity curve editor](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingCurves.html) which you can use to add **keys** to the curve. Keys are points along the curve’s timeline where it has a value explicitly set by the animator rather than just using an interpolated value. Keys are very useful for marking important points along the timeline of the animation. For example, with a walking animation, you might use keys to mark the points where the left foot is on the ground, then both feet on the ground, right foot on the ground, and so on. Once the keys are set up, you can move conveniently between key frames by pressing the **Previous Key Frame** and **Next Key Frame** buttons. This moves the vertical red line and shows the _normalized time_ at the **keyframe** A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#keyframe). The value you enter in the text box drives the value of the curve at that time. 
## Animation curves and animator controller parameters
If you have a curve with the same name as one of the [parameters](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationParameters.html) in the [Animator Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/Animator.html)Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorController), then that parameter takes its value from the value of the curve at each point in the timeline. For example, if you make a call to [GetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetFloat.html) from a script, the returned value is equal to the value of the curve at the time the call is made. Note that at any given point in time, there might be multiple animation clips attempting to set the same parameter from the same controller. In that case, Unity blends the curve values from the multiple animation clips. If an animation has no curve for a particular parameter, then Unity blends with the default value for that parameter.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LoopingAnimationClips.html)
Loop optimization on Animation clips
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEventsOnImportedClips.html)
Events
