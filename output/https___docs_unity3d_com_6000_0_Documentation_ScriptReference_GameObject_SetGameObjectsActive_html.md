* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.SetGameObjectsActive.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).SetGameObjectsActive
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
public static void SetGameObjectsActive(NativeArray<int> instanceIDs, bool active); 
## Declaration
public static void SetGameObjectsActive(ReadOnlySpan<int> instanceIDs, bool active); 
### Parameters
Parameter | Description  
---|---  
instanceIDs | Instance IDs of GameObjects to activate or deactive.  
active | The active state to set, where `true` sets the GameObjects to active and `false` sets them to inactive.  
### Description
Activates or deactivates multiple GameObjects identified by instance ID.
Use `SetGameObjectsActive` to activate or deactivate multiple GameObjects as a batch.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using Unity.Collections;
using UnityEngine;
using UnityEngine.InputSystem;  
  
//Add this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). This example requires the Input[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html) package.  
  
public class DeactivateGOComponent : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefab;
public int count = 100;  
  
    NativeArray<int> m_SpawnedInstanceIDsNative;
    int[] m_SpawnedInstanceIDs;
    
    bool m_SetActive = false;
    bool m_UseSlowMethod = false;
    
    void Start()
    {
        m_SpawnedInstanceIDs = new int[count];
        
        //Spawn some prefabs 
        for (int i = 0; i < count; i++)
        {
            //Save their instanceID
            m_SpawnedInstanceIDs[i] = Instantiate(prefab).GetInstanceID();
        }
        
        //Create native array with instanceIDs
        m_SpawnedInstanceIDsNative = new NativeArray<int>(m_SpawnedInstanceIDs, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
        
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Keyboard.current[Key.A].wasPressedThisFrame)
        {
            if (m_UseSlowMethod)
            {
                SetActiveSlow(m_SetActive);
            }
            else
            {
                SetActiveFast(m_SpawnedInstanceIDsNative, m_SetActive);
                
            }
            m_SetActive = !m_SetActive; 
        }
    }
    
    void SetActiveSlow(bool setActive)
    {
        foreach(int id in m_SpawnedInstanceIDs)
        {
            ((GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))Resources.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.InstanceIDToObject.html)(id)).SetActive(setActive);
        }
    }
    
    static void SetActiveFast(NativeArray<int> ids, bool setActive)
    {
        GameObject.SetGameObjectsActive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.SetGameObjectsActive.html)(ids, setActive);
    }  
  
    void OnDestroy()
    {
        m_SpawnedInstanceIDsNative.Dispose();
    }
}

```

Additional resources: [GameObject.SetActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.SetActive.html), [GameObject.InstantiateGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.InstantiateGameObjects.html).
* * *
