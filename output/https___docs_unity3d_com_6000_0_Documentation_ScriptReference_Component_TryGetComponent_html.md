* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.TryGetComponent.html

#  [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html).TryGetComponent
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
public bool TryGetComponent(out T component); 
### Parameters
Parameter | Description  
---|---  
component | The output argument that will contain the component or `null`.  
### Returns
**bool** Returns `true` if the component is found, `false` otherwise. 
### Description
Gets the component of the specified type, if it exists.
TryGetComponent attempts to retrieve the component of the given type. The notable difference compared to [GameObject.GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.GetComponent.html) is that this method does not allocate in the Editor when the requested component does not exist.
```
using UnityEngine;  
  
public class TryGetComponentExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        if (TryGetComponent<HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html)>(out HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) hinge))
        {
            hinge.useSpring = false;
        }
    }
}

```

* * *
## Declaration
public bool TryGetComponent(Type type, out [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) component); 
### Parameters
Parameter | Description  
---|---  
type | The type of component to search for.  
component | The output argument that will contain the component or `null`.  
### Returns
**bool** Returns `true` if the component is found, `false` otherwise. 
### Description
The non-generic version of this method.
This version of TryGetComponent is not as efficient as the Generic version (above), so you should only use it if necessary.
* * *
