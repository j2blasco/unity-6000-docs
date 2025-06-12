* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.LightDescription.TryGetAnimationCurve.html

#  [LightDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.LightDescription.html).TryGetAnimationCurve
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
propertyName | The name of the light property.  
value | The retrieved AnimationCurve, if one exists for the specified light property.  
### Returns
**bool** Returns true if the light property is animated. Returns false otherwise. 
### Description
Retrieves the AnimationCurve for an animated light property in a specific AnimationClip.
* * *
