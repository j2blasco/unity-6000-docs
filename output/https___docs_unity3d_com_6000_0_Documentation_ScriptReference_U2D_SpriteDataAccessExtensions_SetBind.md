* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.SetBindPoses.html

#  [SpriteDataAccessExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.html).SetBindPoses
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
public static void SetBindPoses([Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) sprite, NativeArray<Matrix4x4> src); 
### Parameters
Parameter | Description  
---|---  
src | The list of bind poses for this Sprite. The array must be disposed of by the caller.  
### Description
Sets the bind poses for this Sprite.
This is usually called as part of the Sprite's post process to imbue it with bind pose data.
* * *
