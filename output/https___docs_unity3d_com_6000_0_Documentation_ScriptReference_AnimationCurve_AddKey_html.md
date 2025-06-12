* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.AddKey.html

#  [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html).AddKey
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
public int AddKey(float time, float value); 
### Parameters
Parameter | Description  
---|---  
time | The time at which to add the key (horizontal axis in the curve graph).  
value | The value for the key (vertical axis in the curve graph).  
### Returns
**int** The index of the added key, or -1 if the key could not be added. 
### Description
Add a new key to the curve.
Smooth tangents are automatically computed for the key. Returns the index of the added key. If no key could be added because there is already another keyframe at the same time -1 will be returned.  
  
Additional resources: [keys](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve-keys.html) variable.
* * *
## Declaration
public int AddKey([Keyframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html) key); 
### Parameters
Parameter | Description  
---|---  
key | The key to add to the curve.  
### Returns
**int** The index of the added key, or -1 if the key could not be added. 
### Description
Add a new key to the curve.
Returns the index of the added key. If no key could be added because there is already another keyframe at the same time -1 will be returned.  
  
Additional resources: [keys](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve-keys.html) variable, [Keyframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html) struct.
* * *
