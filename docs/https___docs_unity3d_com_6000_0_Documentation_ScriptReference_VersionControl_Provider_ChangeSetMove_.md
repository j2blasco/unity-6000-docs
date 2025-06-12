* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.ChangeSetMove.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).ChangeSetMove
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
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) ChangeSetMove([VersionControl.AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets, [VersionControl.ChangeSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ChangeSet.html) changeset); 
## Declaration
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) ChangeSetMove([VersionControl.Asset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) asset, [VersionControl.ChangeSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ChangeSet.html) changeset); 
## Declaration
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) ChangeSetMove([VersionControl.AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets, string changesetID); 
## Declaration
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) ChangeSetMove([VersionControl.Asset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) asset, string changesetID); 
### Parameters
Parameter | Description  
---|---  
assets | List of Assets to move to changeset.  
changeset | Changeset to move an Asset to.  
asset | Asset to move to changeset.  
changesetID | ChangesetID to move an Asset to.  
### Description
Move an Asset or a list of Assets from their current changeset to a new changeset.
E.g. in Perforce checked out Assets can be moved to a changeset other than the default changeset.
* * *
