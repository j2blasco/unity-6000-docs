* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkeletonBone.html

# SkeletonBone
struct in UnityEngine
/
Implemented in:[UnityEngine.AnimationModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AnimationModule.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Details of the Transform name mapped to the skeleton bone of a model and its default position and rotation in the T-pose.
The skeleton models used in Unity have multiple bones. The [SkeletonBone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkeletonBone.html) struct has properties that are used to describe the position, rotation and scale of each bone. The bones are not shown. A [MonoBehaviour.OnDrawGizmosSelected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDrawGizmosSelected.html) tool can be created to view the skeleton. An array of [SkeletonBone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkeletonBone.html) positions can be used to make a line model using [Gizmos.DrawLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLine.html).  
  
An array of [SkeletonBone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkeletonBone.html)s are used in [HumanDescription.skeleton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription-skeleton.html).
### Properties
Property | Description  
---|---  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkeletonBone-name.html) | The name of the Transform mapped to the bone.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkeletonBone-position.html) | The T-pose position of the bone in local space.  
[rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkeletonBone-rotation.html) | The T-pose rotation of the bone in local space.  
[scale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkeletonBone-scale.html) | The T-pose scaling of the bone in local space.  
* * *
