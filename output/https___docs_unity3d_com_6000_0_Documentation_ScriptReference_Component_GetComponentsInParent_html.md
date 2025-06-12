* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInParent.html

#  [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html).GetComponentsInParent
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
public T[] GetComponentsInParent(); 
## Declaration
public T[] GetComponentsInParent(bool includeInactive); 
### Parameters
Parameter | Description  
---|---  
includeInactive | Whether to include inactive parent GameObjects in the search.  
### Returns
**T[]** An array containing all matching components of type `T`. 
### Description
Gets references to all components of type `T` on the same GameObject as the component specified, and any parent of the GameObject.
The typical usage for this method is to call it from a MonoBehaviour script (which itself is a type of component), to find references to other Components or MonoBehaviours attached to the same GameObject as that script, or its parent GameObjects. In this case you can call the method with no preceding object specified. For example:  
  
`myResults = GetComponentsInParent<ComponentType>()`  
  
You can also call this method on a reference to different component, which might be attached to a different GameObject. In this case, the GameObject to which that component is attached, and its parents, are searched. For example:  
  
`myResults = otherComponent.GetComponentsInParent<ComponentType>()`  
  
This method checks the GameObject on which it is called first, then recurses upwards through each parent GameObject, until it finds a matching Component of the type `T` specified.  
  
Only active GameObjects are included in the search, unless you call the method with the `includeInactive` parameter set to `true`, in which case inactive GameObjects are also included. This applies to the GameObject on which the method is called.  
  
To find components attached to other GameObjects, you need a [reference to that other GameObject](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html#AccessingOtherGameObjects) (or any component attached to that GameObject). You can then call `GetComponentsInParent` on that reference.  
  
See the [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) and [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) class reference pages for the other variations of the `GetComponent` family of methods.  
  
The following example gets a reference to all hinge joint components on the same GameObject as the script, or any of its parents, and if found, sets a property on those components.
```
using UnityEngine;  
  
public class GetComponentsInParentExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)[] hingeJoints;  
  
    void Start()
    {
        // Disable the spring on all HingeJoints
        // in this game object and all its parent game objects
        hingeJoints = GetComponentsInParent<HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html)>();  
  
        foreach (HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) joint in hingeJoints)
        {
            joint.useSpring = false;
        }
    }
}

```

Note: If the type you request is a derivative of MonoBehaviour and the associated script can't be loaded then this function will return `null` for that component.
* * *
## Declaration
public void GetComponentsInParent(bool includeInactive, List<T> results); 
### Parameters
Parameter | Description  
---|---  
includeInactive | Whether to include inactive GameObjects in the search.  
results | A list to use for the returned results.  
### Description
A variation of the GetComponentsInParent method which allows you to supply your own List to be filled with results.
This allows you to avoid allocating new List objects for each call to the method. The list you supply is resized to match the number of results found, and any existing values in the list are overritten.
* * *
## Declaration
public Component[] GetComponentsInParent(Type t, bool includeInactive = false); 
### Parameters
Parameter | Description  
---|---  
t | The type of component to search for.  
includeInactive | Whether to include inactive GameObjects in the search.  
### Returns
**Component[]** An array of all found components matching the specified type. 
### Description
The non-generic version of this method.
This version of GetComponentsInChildren is not as efficient as the Generic version (above), so you should only use it if necessary.
* * *
