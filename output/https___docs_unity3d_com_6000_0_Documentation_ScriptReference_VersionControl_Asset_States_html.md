* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.html

# States
enumeration
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
Describes the various version control states an asset can have.
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.None.html) | The version control state is unknown.  
[Local](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.Local.html) | The asset is not under version control.  
[Synced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.Synced.html) | The asset is up to date.  
[OutOfSync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.OutOfSync.html) | A newer version of the asset is available on the version control server.  
[Missing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.Missing.html) | The asset exists in version control but is missing on the local machine.  
[CheckedOutLocal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.CheckedOutLocal.html) | The asset has been checked out on the local machine.  
[CheckedOutRemote](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.CheckedOutRemote.html) | The asset has been checked out on a remote machine.  
[DeletedLocal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.DeletedLocal.html) | The asset has been deleted locally.  
[DeletedRemote](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.DeletedRemote.html) | The asset has been deleted on a remote machine.  
[AddedLocal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.AddedLocal.html) | The asset was locally added to version control.  
[AddedRemote](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.AddedRemote.html) | Remotely this asset was added to version control.  
[Conflicted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.Conflicted.html) | There is a conflict with the asset that needs to be resolved.  
[LockedLocal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.LockedLocal.html) | The asset is locked by the local machine.  
[LockedRemote](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.LockedRemote.html) | The asset is locked by a remote machine.  
[Updating](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.Updating.html) | The state of the asset is currently being queried from the version control server.  
[ReadOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.ReadOnly.html) | The asset is read only.  
[MetaFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.MetaFile.html) | This instance of the class actaully refers to a .meta file.  
[MovedLocal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.MovedLocal.html) | The asset has been moved locally.  
[MovedRemote](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.MovedRemote.html) | The asset has been moved on a remote machine.  
[Unversioned](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.Unversioned.html) | This asset is either ignored or doesn't exist in version control.  
[Exclusive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.Exclusive.html) | Only a single user can checkout this asset  
* * *
