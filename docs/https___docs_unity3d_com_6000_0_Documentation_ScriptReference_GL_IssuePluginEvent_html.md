* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.IssuePluginEvent.html

#  [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html).IssuePluginEvent
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
**Obsolete** IssuePluginEvent(eventID) is deprecated. Use IssuePluginEvent(callback, eventID) instead.
## Declaration
public static void IssuePluginEvent(int eventID); 
## Declaration
public static void IssuePluginEvent(IntPtr callback, int eventID); 
### Parameters
Parameter | Description  
---|---  
eventID | User defined id to send to the callback.  
callback | Native code callback to queue for Unity's renderer to invoke.  
### Description
Send a user-defined event to a native code plugin.
Rendering in Unity can be multithreaded if the platform and number of available CPUs will allow for it. When multithreaded rendering is used, the rendering API commands happen on a thread which is completely separate from the one that runs the scripts. Consequently, it is not possible for your plugin to start rendering immediately, since it might interfere with what the render thread is doing at the time.  
  
In order to do any rendering from the plugin, you should call GL.IssuePluginEvent from your script, which will cause your native plugin to be called from the render thread. For example, if you call GL.IssuePluginEvent from the camera's OnPostRender function, you'll get a plugin callback immediately after the camera has finished rendering.  
  
Callback must be a native function of "void UNITY_INTERFACE_API UnityRenderingEvent(int eventId)" signature.  
  
See [Native Plugin Interface](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html) for more details and an example.  
  
Additional resources: [SystemInfo.graphicsMultiThreaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsMultiThreaded.html).
* * *
