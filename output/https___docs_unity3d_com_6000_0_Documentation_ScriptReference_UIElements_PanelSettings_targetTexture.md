* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelSettings-targetTexture.html

#  [PanelSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelSettings.html).targetTexture
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
[RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) targetTexture; 
### Description
Specifies a Render Texture to render the panel's UI on. 
This can be used to display UI on a 3D geometry in the Scene, to perform manual UI post-processing, or render the UI on a MSAA-enabled Render Texture.  
  
When the project color space is linear, you should use a Render Texture whose format is GraphicsFormat.R8G8B8A8_SRGB.  
  
When the project color space is gamma, you should use a Render Texture whose format is GraphicsFormat.R8G8B8A8_UNorm. 
* * *
