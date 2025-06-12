* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.ToString.html

#  [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html).ToString
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
public string ToString(); 
### Returns
**string** The string representation of the `GlobalObjectId`. 
### Description
Obtains the string representation of the unique object identifier.
The string representation of a `GlobalObjectId` can be serialized, then used at a later time to re-initialize a `GlobalObjectID` struct.  
  
The format of the string representation of the ID is `GlobalObjectId_V1-{i}-{a}-{l}-{p}`, where: 
  * `{i}` is the identifier type represented by an integer (0 = Null, 1 = Imported Asset, 2 = Scene Object, 3 = Source Asset).
  * `{a}` is the asset GUID. This is a globally unique identifier that Unity assigns to every newly discovered asset. For more information, refer to [Asset Metadata](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetMetadata.html) in the Manual.
  * `{l}` is the local file ID of the object. For objects inside a prefab instance, this ID is the local file ID of the original source object that is part of the prefab. For more information, refer to [GlobalObjectId.targetObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId-targetObjectId.html).
  * `{p}` is the local file ID of the prefab instance of the object. If the object isn't part of a prefab instance, then `{p}` is `0`.


**Note** : Actual local file IDs are signed 64-bit values and can be negative. But in a `GlobalObjectId`, these values are cast to [GlobalObjectId.targetObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId-targetObjectId.html), which is an unsigned 64-bit value (`ulong`). Therefore, a negative local file ID will lose its sign when saved to a `GlobalObjectId` and you should not rely on the value of `targetObjectId`, or the `{l}` element from the string representation of a GlobalObjectID, to find an object.  
  
Additional resources: [GlobalObjectId.TryParse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.TryParse.html)
* * *
