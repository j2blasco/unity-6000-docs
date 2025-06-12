* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.IssuePluginEvent.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).IssuePluginEvent
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
public void IssuePluginEvent(IntPtr callback, int eventID); 
### Parameters
Parameter | Description  
---|---  
callback | Native code callback to queue for Unity's renderer to invoke.  
eventID | User defined id to send to the callback.  
### Description
Send a user-defined event to a native code plugin.
See [GL.IssuePluginEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.IssuePluginEvent.html) for more details and an example.
* * *
