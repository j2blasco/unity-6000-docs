* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId-targetObjectId.html

#  [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html).targetObjectId
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
targetObjectId; 
### Description
The local file ID of the referenced object.
This is the ID that uniquely identifies each individual object in an asset file. For objects that are not part of a prefab, this is sufficient to identify the object. For more information on asset files and meta data, refer to [ Asset Metadata](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetMetadata.html) in the Manual.  
  
For a GameObject that's part of a prefab, the `targetObjectId` alone is not sufficient to identify the object because additional instances of the object are created for every instance of the prefab in the scene. To identify such objects unambiguously, the ID of the prefab instance they belong to is also required. For more information, refer to [GlobalObjectId.targetPrefabId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId-targetPrefabId.html).  
  
The `targetObjectId` constitutes the `{l}` element in the string representation of a `GlobalObjectId`, the format of which is:  
  
@@GlobalObjectId_V1-{i}-{a}-{l}-{p  
  
**Note** : Actual local file IDs are signed 64-bit values and can be negative. But in a `GlobalObjectId`, these values are cast to `targetObjectId`, which is an unsigned 64-bit value (`ulong`). Therefore, a negative local file ID will lose its sign when saved to a `GlobalObjectId` and you should not rely on the value of `targetObjectId`, or the `{l}` element from the string representation of a GlobalObjectID, to find an object.   
  
Additional resources: [AssetDatabase.TryGetGUIDAndLocalFileIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)
* * *
