* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.MoveKey.html

#  [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html).MoveKey
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
## Declaration
public int MoveKey(int index, [Keyframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html) key); 
### Parameters
Parameter | Description  
---|---  
index | The index of the key to move.  
key | The keyframe containing the new time and value.  
### Returns
**int** The index of the keyframe after moving it. 
### Description
Moves the key at `index` to `key.time` and `key.value`.
This method removes the keyframe at `index` and inserts the updated `key` at the correct sorted position in [AnimationCurve.keys](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve-keys.html).  
Use it to move a keyframe in two dimensions (time and value).  
  
**Notes** :  
- In order for this method to behave as intended, you are expected to acquire the key using [AnimationCurve.keys](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve-keys.html), modify the value and/or time, then invoke `MoveKey` with the updated keyframe. If used with a completely different keyframe, this method essentially replaces the key with a new one.  
- Since AnimationCurve does not support having two keys with the same time, in the event where `key.time` conflicts with the time of another keyframe, `key` will be reinserted at the time of the keyframe at `index`, cancelling the move operation in the time dimension but keeping the modification in the value dimension.  
- This method is used by the Unity curve editor to implement [Keyframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html) dragging.  
  
See Also: [AnimationCurve.keys](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve-keys.html)
* * *
