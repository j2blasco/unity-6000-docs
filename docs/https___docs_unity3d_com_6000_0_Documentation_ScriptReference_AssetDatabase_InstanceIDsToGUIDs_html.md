* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.InstanceIDsToGUIDs.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).InstanceIDsToGUIDs
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
public static void InstanceIDsToGUIDs(NativeArray<int> instanceIDs, NativeArray<GUID> guidsOut); 
### Description
Sets a NativeArray of UnityEditor.GUIDs for every valid Instance ID that is an asset.
Both arrays must be the same length and initialised before calling. The caller is responsible for the lifetime of these arrays. If an Instance ID is not valid or does not refer to an Object that is an asset, the GUID will be set to default.
* * *
