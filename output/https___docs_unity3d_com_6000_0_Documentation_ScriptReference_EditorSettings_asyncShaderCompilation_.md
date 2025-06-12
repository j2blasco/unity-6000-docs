* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-asyncShaderCompilation.html

#  [EditorSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings.html).asyncShaderCompilation
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
asyncShaderCompilation; 
### Description
Enable asynchronous Shader compilation in Game and Scene view.
Decouples Shader compilation from rendering to avoid Editor stalls when encountering new Shader variants. A plain cyan color dummy shader is used for rendering until the particular Shader variant compilation has finished. This option affects only Game and Scene view in the Editor.
* * *
