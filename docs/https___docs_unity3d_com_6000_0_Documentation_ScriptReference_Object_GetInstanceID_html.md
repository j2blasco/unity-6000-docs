* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html

#  [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html).GetInstanceID
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Object.html "Go to Object Component in the Manual")
## Declaration
public int GetInstanceID(); 
### Returns
**int** Returns the instance ID of the object. 
### Description
Gets the instance ID of the object.
The instance ID of an object acts like a handle to the in-memory instance. It is always unique, and never has the value 0. Objects loaded from file will be assigned a positive Instance ID. Newly created objects will have a negative Instance ID, and retain that negative value even if the object is later saved to file. Therefore the sign of the InstanceID value is not a safe indicator for whether or not the object is persistent.  
  
The ID changes between sessions of the player runtime and Editor. As such, the ID is not reliable for performing actions that could span between sessions, for example, loading an object state from a file.  
  
Additional resources: [EditorUtility.InstanceIDToObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html), [EditorUtility.IsPersistent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsPersistent.html)
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Create 10 game objects, which will have random Instance IDs
    void Awake()
    {
        for (int i = 0; i < 10; i++)
        {
            GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("abc" + i.ToString("D3"));
        }
    }  
  
    // Find all the game objects and display their Instance IDs
    void Start()
    {
        Object[] allObjects = Object.FindObjectsOfType<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>();  
  
        foreach (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go in allObjects)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(go + " is an active object " + go.GetInstanceID());
        }
    }
}

```

* * *
