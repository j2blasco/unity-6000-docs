* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.InstantiateGameObjects.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).InstantiateGameObjects
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html "Go to GameObject Component in the Manual")
## Declaration
public static void InstantiateGameObjects(int sourceInstanceID, int count, NativeArray<int> newInstanceIDs, NativeArray<int> newTransformInstanceIDs, [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) destinationScene); 
### Parameters
Parameter | Description  
---|---  
sourceInstanceID | The instance ID of the GameObject to create additional instances of.  
count | The number of instances of the GameObject to create.  
newInstanceIDs | Pre-allocated NativeArray to populate with the instance IDs of the new GameObjects. Must be the same size as `count`.  
newTransformInstanceIDs | Pre-allocated NativeArray to populate with the instance IDs of the Transforms of the new GameObjects. Must be the same size as `count`.  
destinationScene | The Scene to place the instantiated GameObjects into. If default, then the GameObjects will be added to the currently active Scene.  
### Description
Creates a specified number of instances of a GameObject identified by its instance ID and populates NativeArrays with the instance IDs of the new GameObjects and their Transform components.
Use `InstantiateGameObjects` to instantiate multiple GameObjects as a batch. An instance ID can be resolved to an object using [Resources.InstanceIDToObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.InstanceIDToObject.html). 
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using Unity.Collections;
using UnityEngine;  
  
public class InstantiateInstanceID : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefab;
public int count = 100;  
  
    int m_InstanceID;
    NativeArray<int> m_InstanceIds;
    NativeArray<int> m_TransformIds;
    
    void Start()
    {
        m_InstanceID = prefab.GetInstanceID();
        m_InstanceIds = new NativeArray<int>(count, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
        m_TransformIds = new NativeArray<int>(count, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
        
        GameObject.InstantiateGameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.InstantiateGameObjects.html)(m_InstanceID, count, m_InstanceIds,m_TransformIds );
    }  
  
    void OnDestroy()
    {
        m_InstanceIds.Dispose();
        m_TransformIds.Dispose();
    }
}

```

Additional resources: [GameObject.SetGameObjectsActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.SetGameObjectsActive.html), [Resources.InstanceIDToObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.InstanceIDToObject.html)
* * *
