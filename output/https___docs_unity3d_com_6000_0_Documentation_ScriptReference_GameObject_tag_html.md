* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-tag.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).tag
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
tag; 
### Description
The tag assigned to the GameObject.
A tag can be used to identify a GameObject. Tags must be declared in the [Tags and Layers manager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html) before using them.  
  
**Note:** Do not set a tag from [Awake()](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html) or [OnValidate()](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnValidate.html). The order in which `Awake` is called is not deterministic between components and a tag can be overwritten when its `Awake` is called. If you do this, Unity generates the warning `SendMessage cannot be called during Awake, CheckConsistency, or OnValidate`.  
  
The example below sets the current GameObject's tag to "Player" and then implements [MonoBehaviour.OnTriggerEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnTriggerEnter.html) to check if the [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) on the other object involved in a collision with this object is tagged "Enemy".
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        //Set the tag of this GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to Player
        gameObject.tag = "Player";
    }  
  
    private void OnTriggerEnter(Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) other)
    {
        //Check if the collider of the other GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) involved in the collision is tagged "Enemy"
        if (other.tag == "Enemy")
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Triggered by Enemy");
        }
    }
}

```

Additional resources: [GameObject.CompareTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CompareTag.html), [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
* * *
