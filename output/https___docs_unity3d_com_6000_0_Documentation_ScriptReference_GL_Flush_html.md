* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Flush.html

#  [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html).Flush
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
public static void Flush(); 
### Description
Sends queued-up commands in the driver's command buffer to the GPU.
When Direct3D 11 is the active graphics API, this call maps to ID3D11DeviceContext::Flush. When Direct3D 12 is the active graphics API, pending command lists are executed. When OpenGL is the active graphics API, this call maps to glFlush. 
* * *
