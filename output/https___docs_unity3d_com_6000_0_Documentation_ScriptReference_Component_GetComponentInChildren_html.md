* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInChildren.html

#  [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html).GetComponentInChildren
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
public T GetComponentInChildren(bool includeInactive = false); 
### Parameters
Parameter | Description  
---|---  
includeInactive | Whether to include inactive child GameObjects in the search.  
### Returns
**T** A Component of the matching type `T`, otherwise `null` if no Component is found. 
### Description
Gets a reference to a component of type `T` on the same GameObject as the component specified, or any child of the GameObject.
The typical usage for this method is to call it from a MonoBehaviour script (which itself is a type of component), to find references to other Components or MonoBehaviours attached to the same GameObject as that script, or its child GameObjects. In this case you can call the method with no preceding object specified. For example:  
  
`myResults = GetComponentInChildren<ComponentType>()`  
  
You can also call this method on a reference to different component, which might be attached to a different GameObject. In this case, the GameObject to which that component is attached, and its children, are searched. For example:  
  
`myResults = otherComponent.GetComponentInChildren<ComponentType>()`  
  
This method checks the GameObject on which it is called first, then recurses downwards through all child GameObjects using a depth-first search, until it finds a matching Component of the type `T` specified.  
  
Only active child GameObjects are included in the search, unless you call the method with the `includeInactive` parameter set to `true`, in which case inactive child GameObjects are also included. The GameObject on which the method is called is always searched regardless of this parameter.  
  
Note: GetComponentInChildren returns only the first matching component found, and the order that the components are checked on any individual GameObject is not defined. Therefore, if there are more than one of the specified type that could match on any individual GameObject, and you need to find a specific one, you should use [Component.GetComponentsInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInChildren.html) and check the list of components returned to identify the one you want.  
  
To find components attached to other GameObjects, you need a [reference to that other GameObject](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html#AccessingOtherGameObjects) (or any component attached to that GameObject). You can then call `GetComponentInChildren` on that reference.  
  
See the [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) and [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) class reference pages for the other variations of the `GetComponent` family of methods.  
  
The following example gets a reference to a hinge joint component on the same GameObject as the script, or any of its children, and if found, sets a property on that hinge joint component.
```
using UnityEngine;  
  
public class GetComponentInChildrenExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) hinge = GetComponentInChildren<HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html)>();  
  
        if (hinge != null)
        {
            hinge.useSpring = false;
        }
        else
        {
            // Try again by including inactive GameObjects.
            hinge = GetComponentInChildren<HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html)>(true);  
  
            if (hinge != null)
                hinge.useSpring = false;
        }
    }
}

```

Note: If the type you request is a derivative of MonoBehaviour and the associated script can't be loaded then this function will return `null` for that component.
* * *
## Declaration
public [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) GetComponentInChildren(Type t, bool includeInactive); 
## Declaration
public [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) GetComponentInChildren(Type t); 
### Parameters
Parameter | Description  
---|---  
t | The type of component to search for.  
includeInactive | Whether to include inactive child GameObjects in the search.  
### Returns
**Component** A Component of the matching `type`, otherwise `null` if no Component is found. 
### Description
This is the non-generic version of this method.
This version of GetComponentInChildren is not as efficient as the Generic version (above), so you should only use it if necessary.
```
using UnityEngine;  
  
public class GetComponentInChildrenExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) hinge = GetComponentInChildren(typeof(HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html))) as HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html);  
  
        if (hinge != null)
        {
            hinge.useSpring = false;
        }
        else
        {
            // Try again by including inactive GameObjects.
            hinge = GetComponentInChildren(typeof(HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html)), true) as HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html);  
  
            if (hinge != null)
                hinge.useSpring = false;
        }
    }
}
```

* * *
