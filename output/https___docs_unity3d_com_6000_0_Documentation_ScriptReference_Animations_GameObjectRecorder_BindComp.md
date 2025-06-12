* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.BindComponent.html

#  [GameObjectRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.html).BindComponent
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
public void BindComponent([Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) component); 
### Parameters
Parameter | Description  
---|---  
component | The component to bind.  
### Description
Adds bindings for all the properties of **component**.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Animations;  
  
public class BindComponentScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var recorder = new GameObjectRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.html)(gameObject);  
  
        // Add bindings for all the properties of the Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) and BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html) components.
        recorder.BindComponent(transform);
        recorder.BindComponent(GetComponent<BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html)>());
    }
}

```

* * *
