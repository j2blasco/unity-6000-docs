* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-desiredTextureMemory.html

#  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).desiredTextureMemory
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
desiredTextureMemory; 
### Description
The total size of the Textures, in bytes, that Unity loads if there were no other constraints. Before Unity loads any Textures, it applies the [memory budget](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming#memory-budget.html) which reduces the loaded Texture resolution if the Texture sizes exceed its value. The `desiredTextureMemory` value takes into account the mipmap levels that Unity has requested or that you have set manually.  
  
For example, if Unity does not load a Texture at full resolution because it is far away or its requested mipmap level is greater than 0, Unity reduces the `desiredTextureMemory` value to match the total memory needed.  
  
The `desiredTextureMemory` value can be greater than the [Texture.targetTextureMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-targetTextureMemory.html) value. 
* * *
