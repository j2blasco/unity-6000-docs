* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-targetTextureMemory.html

#  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).targetTextureMemory
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
targetTextureMemory; 
### Description
The total amount of Texture memory that Unity allocates to the Textures in the scene after it applies the [memory budget](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings#Textures.html) and finishes loading Textures. `targetTextureMemory`also takes mipmap streaming settings into account. This value only includes instances of Texture2D and CubeMap Textures. This value does not include any other Texture types, or 2D and CubeMap Textures that Unity creates internally.
The total amount of Texture memory that Unity would use for the non-streaming and mipmap streaming Textures combined after it applies the [memory budget](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings#Textures.html) and finishes loading Textures. This value also takes mipmap streaming settings into account.  
  
The `currentTextureMemory` value becomes closer to this value as Unity loads or unloads Texture mipmaps.
* * *
