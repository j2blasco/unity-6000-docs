* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.GetBindPoses.html

#  [SpriteDataAccessExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.html).GetBindPoses
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
public static NativeArray<Matrix4x4> GetBindPoses([Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) sprite); 
### Parameters
Parameter | Description  
---|---  
sprite | The sprite to retrieve the bind pose from.  
### Returns
**NativeArray <Matrix4x4>** A list of bind poses for this sprite. There is no need to dispose the returned NativeArray. 
### Description
Returns an array of BindPoses.
Use this to animate the Sprite at runtime. Or write to it during bind pose editing.
* * *
