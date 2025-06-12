* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.html

# SpriteDataAccessExtensions
class in UnityEngine.U2D
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
A list of methods designed for reading and writing to the rich internal data of a Sprite.
It is now possible to read and write to all the channels of the VertexAttribute, BoneWeight, BindPose and the SpriteBones of a Sprite.
### Static Methods
Method | Description  
---|---  
[GetBindPoses](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.GetBindPoses.html) | Returns an array of BindPoses.  
[GetBones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.GetBones.html) | Returns a list of SpriteBone in this Sprite.  
[GetIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.GetIndices.html) | Returns a list of indices. This is the same as Sprite.triangle.  
[GetVertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.GetVertexAttribute.html) | Retrieves a strided accessor to the internal vertex attributes.  
[GetVertexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.GetVertexCount.html) | Returns the number of vertices in this Sprite.  
[HasVertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.HasVertexAttribute.html) | Checks if a specific channel exists for this Sprite.  
[SetBindPoses](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.SetBindPoses.html) | Sets the bind poses for this Sprite.  
[SetBones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.SetBones.html) | Sets the SpriteBones for this Sprite.  
[SetIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.SetIndices.html) | Set the indices for this Sprite. This is the same as Sprite.triangle.  
[SetVertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.SetVertexAttribute.html) | Sets a specific channel of the VertexAttribute.  
[SetVertexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.SetVertexCount.html) | Sets the vertex count. This resizes the internal buffer. It also preserves any configurations of VertexAttributes.  
* * *
