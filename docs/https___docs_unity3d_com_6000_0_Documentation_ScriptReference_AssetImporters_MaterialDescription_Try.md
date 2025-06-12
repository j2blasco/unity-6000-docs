* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.MaterialDescription.TryGetAnimationCurve.html

#  [MaterialDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.MaterialDescription.html).TryGetAnimationCurve
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
public bool TryGetAnimationCurve(string clipName, string propertyName, out [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) value); 
### Parameters
Parameter | Description  
---|---  
clipName | The name of the AnimationClip.  
propertyName | The name of the material property.  
value | The retrieved AnimationCurve, if one exists for the specified material property.  
### Returns
**bool** Returns true if the material property is animated. Returns false otherwise. 
### Description
Retrieves the AnimationCurve for an animated material property in a specific AnimationClip.
* * *
