* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html

# RequireComponent
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
The RequireComponent attribute automatically adds required components as dependencies.
When you add a script which uses RequireComponent to a GameObject, the required component is automatically added to the GameObject. This is useful to avoid setup errors. For example a script might require that a Rigidbody is always added to the same GameObject. When you use RequireComponent, this is done automatically, so you are unlikely to get the setup wrong.  
  
**Note:** RequireComponent only checks for missing dependencies when [GameObject.AddComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.AddComponent.html) is called. This happens both in the Editor, or at runtime. Unity does not automatically add any missing dependences to the components with GameObjects that lack the new dependencies.
```
using UnityEngine;  
  
// PlayerScript requires the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to have a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) component
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)))]
public class PlayerScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb;  
  
    void Start()
    {
        rb = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        rb.AddForce(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html));
    }
}

```

### Constructors
Constructor | Description  
---|---  
[RequireComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent-ctor.html) | Require a single component.  
* * *
