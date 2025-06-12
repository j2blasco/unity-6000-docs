* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderPropertyFlags.NoScaleOffset.html

#  [ShaderPropertyFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderPropertyFlags.html).NoScaleOffset
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
Do not show UV scale/offset fields next to Textures in the default Material Inspector.
This flag is only relevant to Texture shader properties, and only hides the UI for UV scale/offset fields. Unity still serializes the underlying "_YourTexturePropertyName_ _ST" vector property in the Material Assets.  
  
This flag corresponds to the "[NoScaleOffset]" attribute.
* * *
