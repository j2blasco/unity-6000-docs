* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html

# AnimationCurve
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Store a collection of Keyframes that can be evaluated over time.
### Properties
Property | Description  
---|---  
[keys](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve-keys.html) | All keys defined in the animation curve.  
[length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve-length.html) | The number of keys in the curve. (Read Only)  
[postWrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve-postWrapMode.html) | The behaviour of the animation after the last keyframe.  
[preWrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve-preWrapMode.html) | The behaviour of the animation before the first keyframe.  
[this[int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.Index_operator.html) | Retrieves the key at index. (Read Only)  
### Constructors
Constructor | Description  
---|---  
[AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve-ctor.html) | Creates an animation curve from an arbitrary number of keyframes.  
### Public Methods
Method | Description  
---|---  
[AddKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.AddKey.html) | Add a new key to the curve.  
[ClearKeys](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.ClearKeys.html) | Erases all KeyFrame from this instance of the AnimationCurve.  
[CopyFrom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.CopyFrom.html) | Copies the keys and properties of the specified AnimationCurve object into this instance of the AnimationCurve class.  
[Evaluate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.Evaluate.html) | Evaluate the curve at time.  
[GetHashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.GetHashCode.html) | A HashCode for the animation curve, computed using all individual Keyframe.  
[MoveKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.MoveKey.html) | Moves the key at index to key.time and key.value.  
[RemoveKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.RemoveKey.html) | Removes a key.  
[SmoothTangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.SmoothTangents.html) | Smooth the in and out tangents of the keyframe at index.  
### Static Methods
Method | Description  
---|---  
[Constant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.Constant.html) | Creates a constant "curve" starting at timeStart, ending at timeEnd, and set to the value value.  
[EaseInOut](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.EaseInOut.html) | Creates an ease-in and out curve starting at timeStart, valueStart and ending at timeEnd, valueEnd.  
[Linear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.Linear.html) | A straight Line starting at timeStart, valueStart and ending at timeEnd, valueEnd.  
* * *
