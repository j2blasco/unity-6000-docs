* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEulerCurveImport.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Models](https://docs.unity3d.com/6000.0/Documentation/Manual/models.html)
  * [Importing models into Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/models-importing.html)
  * [Model Import Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html)
  * [Animation tab](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)
  * Euler curve resampling


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)
Animation tab
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Splittinganimations.html)
Extracting animation clips
# Euler curve resampling
Rotations in 3D applications are usually represented as **Quaternions** Unity’s standard way of representing rotations as data. When writing code that deals with rotations, you should usually use the Quaternion class and its methods. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/QuaternionAndEulerRotationsInUnity.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Quaternion) or Euler angles. For the most part, Unity represents rotations as Quaternions internally; however, it’s important to have a basic understanding of [rotation and orientation in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/QuaternionAndEulerRotationsInUnity.html).
When you import files containing animation that come from external sources, the imported files usually contain **keyframe** A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#keyframe) animation in Euler format. Unity’s default behavior is to resample these animations as Quaternion values and generate a new Quaternion keyframe for every frame in the animation. This minimizes the differences between the source animation and how it appears in Unity. 
There are still some situations where the quaternion representation of the imported animation may not match the original closely enough, even with resampling. For this reason, Unity provides the option to turn off animation resampling. This means that you can use the original Euler animation keyframes at run-time instead.
**Note:** You should only keep the Euler curves as a last resort, if the default Quaternion interpolation between frames gives bad results and causes issues.
## Keeping the original Euler curves on imported animations
To use the original Euler curve values in an animation file, uncheck the **Resample Curves** option in the [Animation tab](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html):
![The Resample Curves option in the Animations tab](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationImportResampleRotations.png) The Resample Curves option in the Animations tab
When you disable this option, Unity keeps the rotation curve with its original keyframes, in Euler or Quaternion mode as appropriate for the curve type. 
**Note:** The FBX SDK automatically resamples any rotation curve on a **joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) that has pre- or post-rotations. This means that Unity automatically imports them as Quaternion curves.
Unity supports such a wide variety of imported files and attempts to keep the imported curves as close to the original as possible. In order to achieve this, Unity supports all normal (non-repeating) Euler rotation orders, and imports curves in their original rotation orders. 
### Euler values and the Unity engine
When using original Euler (non-resampled) rotations, you can see very little visual difference in the playback of animations. Under the hood, Unity stores these curves in Euler representation even at run-time. However, Unity has to convert rotation values to Quaternions eventually, since the engine only works with Quaternions. 
When you disable the **Resample Curves** option, Unity keeps the rotation values as Euler values up until they are applied to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). This means that the end result should look as good as the original, but with an improvement in memory, since rotation curves that have not been baked in the authoring software take up less memory.
### Non-default Euler orders in the Transform Inspector
By default, Unity applies the Euler angles that appear in the Transform **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) in the Z,X,Y order. 
When playing back or editing imported animations that feature Euler curves with a rotation order different from Unity’s default, Unity displays an indicator of the difference next to the rotation fields:
![The inspector showing that a non-default rotation order is being used for the rotation animation on this object](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEulerAlternateRotationOrderInInspector.png) The inspector showing that a non-default rotation order is being used for the rotation animation on this object
When editing multiple transforms with differing rotation orders, Unity displays a warning message that the same Euler rotation applied will give different results on curves with different rotation orders:
![The inspector showing that a mixture of rotation orders are being used for the rotation animation on the selected group of objects](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AnimationEulerMixedRotationOrderInInspector.png) The inspector showing that a mixture of rotation orders are being used for the rotation animation on the selected group of objects
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)
Animation tab
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Splittinganimations.html)
Extracting animation clips
