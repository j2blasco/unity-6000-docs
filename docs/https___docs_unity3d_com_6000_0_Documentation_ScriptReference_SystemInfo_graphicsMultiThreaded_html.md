* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsMultiThreaded.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).graphicsMultiThreaded
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
graphicsMultiThreaded; 
### Description
Is graphics device using multi-threaded rendering (Read Only)?
On many platforms Unity can use multi-threaded rendering, where actual calls to underlying graphics API are done on a separate thread. Normally you do not have to worry about this, except if you're making native code rendering plugins. In that case, you need to make sure your plugin also does rendering calls on the right thread; use [GL.IssuePluginEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.IssuePluginEvent.html) for that.  
  
Additional resources: [GL.IssuePluginEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.IssuePluginEvent.html), [Native Plugin Interface](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html).
* * *
