* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.AreStaticEditorFlagsSet.html

#  [GameObjectUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.html).AreStaticEditorFlagsSet
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
public static bool AreStaticEditorFlagsSet([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go, [StaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.html) flags); 
### Parameters
Parameter | Description  
---|---  
go | The GameObject to check.  
flags | The flags you want to check.  
### Returns
**bool** Whether the GameObject's static flags match the flags specified. 
### Description
Returns true if the passed in StaticEditorFlags are set on the GameObject specified.
* * *
