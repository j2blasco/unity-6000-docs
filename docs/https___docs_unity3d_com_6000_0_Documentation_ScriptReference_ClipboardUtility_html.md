* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClipboardUtility.html

# ClipboardUtility
class in UnityEditor
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
A class containing methods to assist with clipboard operations.
### Static Properties
Property | Description  
---|---  
[canCopyGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClipboardUtility-canCopyGameObject.html) | Optional filtering functions invoked to determine if a GameObject can be copied before any action is taken.  
[canCutGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClipboardUtility-canCutGameObject.html) | Optional filtering functions invoked to determine if a GameObject can be cut before any action is taken.  
[canDuplicateGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClipboardUtility-canDuplicateGameObject.html) | Optional filtering functions invoked to determine if a GameObject can be duplicated before any action is taken.  
### Events
Event | Description  
---|---  
[copyingGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClipboardUtility-copyingGameObjects.html) | Event triggered before the selected GameObjects are copied to the clipboard.  
[cuttingGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClipboardUtility-cuttingGameObjects.html) | Event triggered before the selected GameObjects are cut to the clipboard.  
[duplicatedGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClipboardUtility-duplicatedGameObjects.html) | Event triggered after GameObjects have been duplicated.  
[duplicatingGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClipboardUtility-duplicatingGameObjects.html) | Event triggered before GameObjects are about to be duplicated.  
[pastedGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClipboardUtility-pastedGameObjects.html) | Event triggered after GameObjects are pasted from the clipboard.  
[rejectedGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClipboardUtility-rejectedGameObjects.html) | Event triggered after the filtering process of canCopyGameObject, canCutGameObject or canDuplicateGameObject receiving an array of GameObjects which did not pass the filtering functions.  
* * *
