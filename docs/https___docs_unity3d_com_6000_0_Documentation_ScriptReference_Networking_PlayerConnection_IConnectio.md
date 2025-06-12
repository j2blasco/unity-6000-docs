* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.IConnectionState.html

# IConnectionState
interface in UnityEngine.Networking.PlayerConnection
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
The state of an Editor-to-Player or Editor-to-Editor connection to be used in [PlayerConnectionGUI.ConnectionTargetSelectionDropdown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.PlayerConnectionGUI.ConnectionTargetSelectionDropdown.html) or [PlayerConnectionGUILayout.ConnectionTargetSelectionDropdown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.PlayerConnectionGUILayout.ConnectionTargetSelectionDropdown.html).
The interface inherits from IDisposable and all instances of it need to be disposed of before the reference to them is lost, for example by closing the window or during an assembly reload. You can get an instance from Networking.PlayerConnection.PlayerConnectionGUIUtility.GetAttachToPlayerState. For usage and code examples see: [PlayerConnectionGUI.ConnectionTargetSelectionDropdown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.PlayerConnectionGUI.ConnectionTargetSelectionDropdown.html) or [PlayerConnectionGUILayout.ConnectionTargetSelectionDropdown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.PlayerConnectionGUILayout.ConnectionTargetSelectionDropdown.html)
### Properties
Property | Description  
---|---  
[connectedToTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.IConnectionState-connectedToTarget.html) | Supplies the type of the established connection, as in whether the target is a Player or an Editor.  
[connectionName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.IConnectionState-connectionName.html) | The name of the connected target.  
* * *
