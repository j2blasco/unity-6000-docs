* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.RemoveConfigObject.html

#  [EditorBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.html).RemoveConfigObject
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
public static bool RemoveConfigObject(string name); 
### Parameters
Parameter | Description  
---|---  
name | The name in string format of the config object reference to be removed. This is the name given to the object when the reference is first created. Note: This may be different than the object name as an object can be added multiple times with different names.  
### Returns
**bool** Returns true if the reference was found and removed, otherwise false. 
### Description
Remove a config object reference by name.
* * *
