* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Social.html

**Method group is Obsolete**   

# Social
class in UnityEngine
/
Implemented in:[UnityEngine.GameCenterModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.GameCenterModule.html)
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
**Obsolete** Social is deprecated and will be removed in a future release.
### Description
Generic access to the Social API.
Social.Active can be used to target a specific social platform implementation, but by default GameCenter is used on iOS. All other platforms default to the Local implementation which can be used for testing. See [Social API Reference Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/net-SocialAPI.html) for an overview.  
  
The Social class should always be used as an entry point. It contains helper functions for accessing the current active implementation and always uses the interfaces of the other Social API classes. This way it is easier to use versions of the interfaces which have been extended beyond the generic API by the implementation.  
  
There are various classes associated with the Social API and all of these reside in the UnityEngine.SocialPlatforms namespace. You need to import/use this namespace in order to use these classes.  
  
  
Additional resources: SocialPlatforms.GameCenter.GameCenterPlatform.
* * *
