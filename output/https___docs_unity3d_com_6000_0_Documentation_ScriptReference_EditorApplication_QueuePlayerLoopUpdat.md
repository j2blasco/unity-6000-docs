* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.QueuePlayerLoopUpdate.html

#  [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html).QueuePlayerLoopUpdate
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
public static void QueuePlayerLoopUpdate(); 
### Description
Normally, a player loop update will occur in the editor when the Scene has been modified. This method allows you to queue a player loop update regardless of whether the Scene has been modified.
When the Scene is modified it forces a repaint of any window that has [autoRepaintOnSceneChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-autoRepaintOnSceneChange.html) set to true. Additionally, the player loop will run and consequently update any scripts that are marked with [ExecuteInEditMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html) or MonoBehaviours that have [runInEditMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour-runInEditMode.html) set to true.  
  
Sometimes you may want more consistent updates even when the Scene has not been modified, so you can call this method to queue an update.  
  
Additional resources: [ExecuteInEditMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html), [MonoBehaviour.runInEditMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour-runInEditMode.html), [EditorWindow.autoRepaintOnSceneChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-autoRepaintOnSceneChange.html).
* * *
