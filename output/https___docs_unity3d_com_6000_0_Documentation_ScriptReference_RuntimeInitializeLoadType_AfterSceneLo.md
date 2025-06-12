* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.AfterSceneLoad.html

#  [RuntimeInitializeLoadType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.html).AfterSceneLoad
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
Callback invoked when the first scene's objects are loaded into memory and **after** Awake has been called.
At this point active objects can be found with UnityEngine.Object.FindObjectsByType. Before this point the first Scene's objects are considered inactive regardless of their serialized active state.  
  
For more info on ordering see [RuntimeInitializeOnLoadMethodAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeOnLoadMethodAttribute.html).
* * *
