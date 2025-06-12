* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPostprocessAnimation.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).OnPostprocessAnimation(GameObject, AnimationClip)
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
### Parameters
Parameter | Description  
---|---  
root | The root GameObject of the imported Asset.  
clip | The current animation clip.  
### Description
This function is called when an AnimationClip has finished importing.
This function is called for every AnimationClip in an imported asset file. This lets you modify the imported AnimationClip before it is written to disk.
* * *
