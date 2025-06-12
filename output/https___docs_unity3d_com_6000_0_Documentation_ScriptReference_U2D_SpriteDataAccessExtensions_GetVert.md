* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.GetVertexAttribute.html

#  [SpriteDataAccessExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.html).GetVertexAttribute
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
public static NativeSlice<T> GetVertexAttribute([Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) sprite, [Rendering.VertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.html) channel); 
### Returns
**NativeSlice <T>** A read-only list of. 
### Description
Retrieves a strided accessor to the internal vertex attributes.
This is the only way to access all the various channels of the vertex attributes.  
  
Here are the types corresponding to the VertexAttributes.  
  
Position -> Vector3  
  
Normal -> Vector3  
  
Color -> Color32  
  
UV0-3 -> Vector2  
  
Tangent -> Vector4.
* * *
