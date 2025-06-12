* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId-targetPrefabId.html

#  [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html).targetPrefabId
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
targetPrefabId; 
### Description
The ID of the prefab instance that contains the referenced object.
Adding a new prefab instance to a scene creates a new instance of every object the prefab contains, including every GameObject. The GameObject inside a prefab instance doesn't have its own stable local file ID and a single prefab can be instantiated multiple times in a scene. Therefore, to reliably identify a GameObject that's part of a prefab requires both the local file ID of the original version of the GameObject (GameObject.targetObjectId) and the ID of the particular prefab instance it belongs to (`targetPrefabId`).  
  
For more information on creating prefab instances, refer to [Creating Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingPrefabs.html) in the Manual.  
  
The `targetPrefabId` constitutes the `{p}` element in the string representation of a `GlobalObjectId`, the format of which is:  
  
`GlobalObjectId_V1-{i}-{a}-{l}-{p}`  
  
Additional resources: [PrefabUtility.IsPartOfAnyPrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfAnyPrefab.html)
* * *
