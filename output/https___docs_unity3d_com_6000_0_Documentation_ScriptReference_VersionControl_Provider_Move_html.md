* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Move.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).Move
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
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) Move(string from, string to); 
### Parameters
Parameter | Description  
---|---  
from | Path to the source asset.  
to | Path to the destination.  
### Description
Uses the version control plugin to move an asset from one path to another.
Do note that the source asset will be deleted and a new copy will be created in the destination. This will be reflected in the same manner in the outgoing changelist.  
  
Also, after this operation is completed, Asset Database is not refreshed automatically. It can be updated by calling [AssetDatabase.Refresh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Refresh.html).
* * *
