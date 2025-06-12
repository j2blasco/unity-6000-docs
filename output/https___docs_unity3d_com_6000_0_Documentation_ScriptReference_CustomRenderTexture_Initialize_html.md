* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.Initialize.html

#  [CustomRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.html).Initialize
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture.html "Go to CustomRenderTexture Component in the Manual")
## Declaration
public void Initialize(); 
### Description
Initializes the Custom Render Texture at the start of the next frame. Unity calls /Initialise()/ before /[CustomRenderTexture.Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.Update.html)/.
You can use /initialize()/ to reset a Custom Render Texture or to execute two passes after each other, where one occurs in /initialize()/ and the other in /[CustomRenderTexture.Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.Update.html)/. When you call /initialize ()/, Unity uses the settings the Custom Render Texture has when Unity renders it. This means if you call /intialize()/ more than once when you have changed settings between calls, Unity runs the initialize render multiple times with the last settings you applied. Additional resources: [Custom Render Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture.html).
* * *
