* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/BlendTree-AdditionalOptions.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Animator Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)
  * [Animation State Machine](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html)
  * [Animation Blend Trees](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BlendTree.html)
  * Common Blend Tree Options


[](https://docs.unity3d.com/6000.0/Documentation/Manual/BlendTree-DirectBlending.html)
Direct blending
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBehaviours.html)
State Machine Behaviours
# Common Blend Tree Options
The options in this topic are common to both 1D and 2D blending.
## Time Scale
You can alter the “natural” speed of **animation clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) with the animation speed number fields (the columns with a clock icon). For example, to double the speed of a walk clip, specify a value of `2.0`.
To rescale the speed of each clip in the motions list relative to the minimum and maximum values, Select **Adjust Time Scale** > **Homogeneous Speed**. This preserves the initial relative speed of each clip.
**Note** : The **Adjust Time Scale** is only available if all the clips are animation clips and not child Blend Trees.
## Mirroring
Enable the Mirror checkbox to mirror any **humanoid Animation** An animation using humanoid skeletons. Humanoid models generally have the same basic structure, representing the major articulate parts of the body, head and limbs. This makes it easy to map animations from one humanoid skeleton to another, allowing retargeting and inverse kinematics. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Humanoidanimation) Clip in the motions list. Mirroring uses the same animation as its unmirrored original without doubling the memory and space.
However, mirroring an animation in a blend tree does not create a fully symmetrical animation. Unity automatically adds offsets to ensure that run cycles, walk cycles, and animations such as footsteps are blended correctly with other animation clips and blend trees. For example, if your blend tree has a humanoid running left, and you enable Mirror to switch the humanoid to run right, the foot cycles need to match so that the left foot touches the ground at the same time. This ensures that the mirrored Blend tree correctly blends with surrounding clips and other blend trees that have not been mirrored.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/BlendTree-DirectBlending.html)
Direct blending
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StateMachineBehaviours.html)
State Machine Behaviours
