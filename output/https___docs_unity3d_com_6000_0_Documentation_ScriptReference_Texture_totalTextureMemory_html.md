* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-totalTextureMemory.html

#  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).totalTextureMemory
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
totalTextureMemory; 
### Description
The total amount of Texture memory that Unity would use if it loads all Textures at mipmap level 0.  
  
This is a theoretical value that does not take into account any input from the streaming system or any other input, for example when you set the`Texture2D.requestedMipmapLevel` manually.  
  
To see a Texture memory value that takes inputs into account, use `desiredTextureMemory`.  
  
`totalTextureMemory` only includes instances of Texture2D and CubeMap Textures. This value does not include any other Texture types, or 2D and CubeMap Textures that Unity creates internally.
* * *
