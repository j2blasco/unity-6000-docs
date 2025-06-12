* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.GetHashForStateStorage.html

#  [Stage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.html).GetHashForStateStorage
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
protected [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) GetHashForStateStorage(); 
### Returns
**Hash128** The hash code identifying this stage. 
### Description
Unity calls this method to get a hash code that is used to save the state of the Stage to disk.
The state includes Scene view settings and the Camera position. Some Stage types may store additional state data such as the scroll position in the Hierarchy window. Saving the state ensures that, if you close a stage and later open it, Scene view settings, the Camera position, and other stored objects are in the same state you left them in when you closed the Stage.  
  
For stages that use the [assetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage-assetPath.html) property, the hash code is by default based on the Asset GUID, meaning the state is saved individually per Asset. For stages that don't use the [assetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage-assetPath.html) property, the hash code is by default shared for all stages of that type. Custom stage types can override this method to use different logic to determine in which way stage state should be reused.
* * *
