* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.AddComponent.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).AddComponent
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
public [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) AddComponent(Type componentType); 
### Description
Adds a component of the specified type to the GameObject.
There is no corresponding method for removing a component from a GameObject. To remove a component, use [Object.Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html).
```
using UnityEngine;
using System.Collections;  
  
public class AddComponentExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        SphereCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html) sc = gameObject.AddComponent(typeof(SphereCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html))) as SphereCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html);
    }
}

```

Additional resources: [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html), [Object.Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html)
* * *
## Declaration
public T AddComponent(); 
### Description
Generic version of this method.
```
using UnityEngine;
using System.Collections;  
  
public class AddComponentExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        SphereCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html) sc = gameObject.AddComponent<SphereCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html)>();
    }
}

```

Additional resources: [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html), [Object.Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html)
* * *
**Obsolete** GameObject.AddComponent with string argument has been deprecated. Use GameObject.AddComponent<T>() instead.
## Declaration
public [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) AddComponent(string className); 
### Description
Adds a component of the specified class name to the GameObject.
Deprecated: Use AddComponent(Type) or the generic version of this method instead.
* * *
