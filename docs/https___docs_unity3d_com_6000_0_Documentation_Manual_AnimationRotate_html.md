* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationRotate.html

  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationSection.html)
  * [Mecanim Animation system](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationOverview.html)
  * [Animation clips](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationClips.html)
  * [Animation window](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEditorGuide.html)
  * Rotation in animations


[](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingCurves.html)
Edit Animation curves
[](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-AdvancedKeySelectionAndManipulation.html)
Key manipulation in Dopesheet mode
# Rotation in animations
You can use Unity to animate your **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject)’s rotations. There are different methods of applying these rotations to suit your project best.
Consult [Rotation and orientation in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/QuaternionAndEulerRotationsInUnity.html) for more information on rotational representations.
## Rotation interpolation
You can use the [Animation window](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEditorGuide.html) to choose how Unity applies rotation to your GameObject. Unity uses interpolation to calculate how a GameObject visually moves from one orientation to another in your animation.
Different interpolation methods look different in motion, but have the same result. Unity offers three types of interpolation for your animations:
![The Animation window, with the interpolation menu expanded to show the rotation interpolation options.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/QuaternionInterpolation.png) The Animation window, with the interpolation menu expanded to show the rotation interpolation options.
### Euler angle interpolation
**Euler Angles** interpolation applies the full range of motion to the GameObject specified by the angles you enter; if the rotation is greater than 360 degrees, the GameObject rotates fully before it stops at the correct orientation.
**Euler Angles (Quaternion)** interpolation uses the above interpolation method but bakes the information into a **quaternion** Unity’s standard way of representing rotations as data. When writing code that deals with rotations, you should usually use the Quaternion class and its methods. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/QuaternionAndEulerRotationsInUnity.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Quaternion) curve. This method uses more memory but results in a slightly faster runtime.
### Quaternion interpolation
**Quaternion** interpolation rotates the GameObject across the shortest distance to a particular orientation. For example, regardless of whether the rotation value is 5 degrees or 365 degrees, the GameObject rotates 5 degrees.
## External animation sources
[Animation from external sources](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationsImport.html) often contains rotational **keyframe** A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#keyframe) animation in Euler format. Unity resamples these animations and generates new keyframes for each frame in the animation to avoid rotations that exceed the valid range of rotational quaternions.
For example, if you have two keyframes that are six frames apart with the x value going from 0 to 270 degrees, the GameObject rotates 90 degrees in the opposite direction because it’s the shortest way to get to the same result. Instead, Unity resamples and adds a keyframe on every frame, so the rotation is only 45 degrees between keyframes and the rotation is correct.
### Resolve rotation problems with external animation sources
If the quaternion resampling of the imported animation doesn’t match the original closely enough for your needs, you can turn off animation resampling and use the original Euler animation keyframes at runtime. For more information, consult [Euler curve resampling](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEulerCurveImport.html).
## Additional resources
  * [Rotation and orientation in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/QuaternionAndEulerRotationsInUnity.html)
  * [Using Animation Curves](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-AnimationCurves.html)
  * [Euler curve resampling](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEulerCurveImport.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingCurves.html)
Edit Animation curves
[](https://docs.unity3d.com/6000.0/Documentation/Manual/animeditor-AdvancedKeySelectionAndManipulation.html)
Key manipulation in Dopesheet mode
