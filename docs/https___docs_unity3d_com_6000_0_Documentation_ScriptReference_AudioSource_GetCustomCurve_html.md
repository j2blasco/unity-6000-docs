* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.GetCustomCurve.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).GetCustomCurve
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html "Go to AudioSource Component in the Manual")
## Declaration
public [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) GetCustomCurve([AudioSourceCurveType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSourceCurveType.html) type); 
### Parameters
Parameter | Description  
---|---  
type | The curve type to get.  
### Returns
**AnimationCurve** The custom AnimationCurve corresponding to the given curve type. 
### Description
Get the current custom curve for the given AudioSourceCurveType.
Note that if there is no curve set, or the corresponding curve type value setter has been set, a single key AnimationCurve will be returned corresponding to the current value.
* * *
