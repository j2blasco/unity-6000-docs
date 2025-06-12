* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponents.html

#  [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html).GetComponents
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
public T[] GetComponents(); 
### Returns
**T[]** An array containing all matching components of type `T`. 
### Description
Gets references to all components of type `T` on the same GameObject as the component specified.
The typical usage for this method is to call it from a MonoBehaviour script (which itself is a type of component), to find references to other Components or MonoBehaviours attached to the same GameObject as that script. In this case you can call the method with no preceding object specified. For example:  
  
`myResults = GetComponents<ComponentType>()`  
  
You can also call this method on a reference to different component, which might be attached to a different GameObject. In this case, the GameObject to which that component is attached is searched. For example:  
  
`myResults = otherComponent.GetComponents<ComponentType>()`  
  
To find components attached to a particular GameObject, you need a [reference to that other GameObject](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html#AccessingOtherGameObjects) (or any component attached to that GameObject). You can then call `GetComponents` on that reference.  
  
See the [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) and [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) class reference pages for the other variations of the `GetComponent` family of methods.  
  
The following example gets a reference to all hinge joint components on the specified GameObject, and sets a property on each hinge joint component that was found.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html)[] hinges = GetComponents<HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html)>();
        for (int i = 0; i < hinges.Length; i++)
        {
            hinges[i].useSpring = false;
        }
    }
}

```

Note: If the type you request is a derivative of MonoBehaviour and the associated script can't be loaded then this function will return `null` for that component.
* * *
## Declaration
public void GetComponents(List<T> results); 
### Parameters
Parameter | Description  
---|---  
results | A list to use for the returned results.  
### Description
A variation of the GetComponents method which allows you to supply your own List to be filled with results.
This allows you to avoid allocating new List objects for each call to the method. The list you supply is resized to match the number of results found, and any existing values in the list are overritten.
* * *
## Declaration
public Component[] GetComponents(Type type); 
### Parameters
Parameter | Description  
---|---  
type | The type of component to search for.  
### Returns
**Component[]** An array containing all matching components of type `type`. 
### Description
The non-generic version of this method.
This version of GetComponents is not as efficient as the Generic version (above), so you should only use it if necessary.
* * *
## Declaration
public void GetComponents(Type type, List<Component> results); 
### Parameters
Parameter | Description  
---|---  
type | The type of component to search for.  
results | A list to use for the returned results.  
### Description
The non-generic version of this method which allows you to supply your own List to be filled with results.
This version of GetComponents is not as efficient as the Generic version (above), so you should only use it if necessary.
* * *
