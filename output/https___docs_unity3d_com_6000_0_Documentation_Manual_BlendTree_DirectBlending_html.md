* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/BlendTree-DirectBlending.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Animator Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)
  * [Animation State Machine](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationStateMachines.html)
  * [Animation Blend Trees](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BlendTree.html)
  * Direct blending


[](https://docs.unity3d.com/6000.0/Documentation/Manual/BlendTree-2DBlending.html)
2D Blending
[](https://docs.unity3d.com/6000.0/Documentation/Manual/BlendTree-AdditionalOptions.html)
Common Blend Tree Options
# Direct blending
Use a **Direct Blend Tree** to map animator parameters to the weight of a BlendTree child. This is useful when you want exact control over blending animations rather than the indirectly control provided by 1D blending or 2D blending.
![A Direct Blend Tree with five animation clips assigned.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimatorDirectBlendTree.png) A Direct Blend Tree with five animation clips assigned.
In direct blending, you use the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window to add motions and to also assign an [Animator Parameter](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationParameters.html) to each blend weight. This Direct mode bypasses 2D blending algorithms, such as Freeform Directional and Freeform Cartesian, and allows you to implement a scripting solution to control the mix of blended animations.
For example, you can use Direct mode to to mix blend shape animations for facial expressions or to blend additive animations.
![Example of using Direct Blending for facial expressions](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimatorDirectBlendTreeFacialExpressions.jpg) Example of using Direct Blending for facial expressions
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/BlendTree-2DBlending.html)
2D Blending
[](https://docs.unity3d.com/6000.0/Documentation/Manual/BlendTree-AdditionalOptions.html)
Common Blend Tree Options
