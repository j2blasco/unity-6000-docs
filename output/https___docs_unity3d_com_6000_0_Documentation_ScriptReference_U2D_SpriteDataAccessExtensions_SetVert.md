* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.SetVertexAttribute.html

#  [SpriteDataAccessExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.html).SetVertexAttribute
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
public static void SetVertexAttribute([Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) sprite, [Rendering.VertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.html) channel, NativeArray<T> src); 
### Parameters
Parameter | Description  
---|---  
src | The list of values for this specific VertexAttribute channel. The array must be disposed of by the caller.  
### Description
Sets a specific channel of the VertexAttribute.
See [GetVertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.GetVertexAttribute.html).
* * *
