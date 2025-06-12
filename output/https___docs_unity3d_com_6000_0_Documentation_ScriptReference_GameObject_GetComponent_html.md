* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.GetComponent.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).GetComponent
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
public T GetComponent(); 
### Returns
**T** A reference to a component of the specified type, returned as an object of type `T`. If no component is found, returns `null`. 
### Description
Retrieves a reference to a component of the specified type, by providing the component type as a type parameter to the generic method.
`GetComponent` returns only the first matching component found on the GameObject, and components aren't checked in a defined order. If there are multiple components of the same type and you need to find a specific one, use [GameObject.GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.GetComponents.html) and check the list of components returned to identify the one you want.  
  
**Note** : If the type you request is a derivative of MonoBehaviour and the script it's defined in can't be loaded, then this function returns `null` for that component. This might happen if you've named your class ambiguously. Refer to [Naming scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/Namespaces.html) in the Manual for more information on naming considerations.  
  
The typical usage for this method is to call it on a reference to a different GameObject than the one your script is on. For example:  
  
`ComponentType myComponent = otherGameObject.GetComponent<ComponentType>()`  
  
To find components attached to other GameObjects, you need a [reference to that other GameObject](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html#AccessingOtherGameObjects), or to any component attached to that GameObject. You can then call `GetComponent` on that reference.  
  
You can also use this method to get a reference to a component on the GameObject that this script is attached to, by calling this method inside a `MonoBehaviour`-derived class attached to the GameObject. You can omit the preceding `GameObject` qualifier to reference the GameObject the script is attached to. In this instance, you're actually calling [Component.GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) because the script itself is a type of component, but the result is the same as if you'd referenced the GameObject itself. For example:  
  
`ComponentType myComponent = GetComponent<ComponentType>()`  
  
The following example gets a reference to a hinge joint component on the referenced GameObject, and if found, sets a property on it.
```
using UnityEngine;  
  
public class GetComponentExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) as a component.
{
// Create a reference to another GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in the scene. Set a value for this in the Other Game Object field
// in the Inspector window before entering Play mode. The referenced GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) must contain a
// HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) component.
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) otherGameObject;  
  
    void Start()
    {
        HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) hinge = otherGameObject.GetComponent<HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html)>();
        // Perform null check to confirm a valid HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) component was successfully returned.
        if (hinge != null)
        {
            hinge.useSpring = false;
        }
    }
}

```

Additional resources: [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html), [GameObject.GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.GetComponents.html)
* * *
## Declaration
public [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) GetComponent(Type type); 
### Parameters
Parameter | Description  
---|---  
type | The type of component to search for, specified as a `Type` object.  
### Returns
**Component** A reference to a component of the specified type, returned as a `Component` type. If no component is found, returns `null`. 
### Description
Retrieves a reference to a component of specified type, by providing the component type as a method parameter.
This version of `GetComponent` isn't as efficient as the generic version. Use this version only if necessary.  
  
`GetComponent` returns only the first matching component found on the GameObject, and components aren't checked in a defined order. If there are multiple components of the same type and you need to find a specific one, use [GameObject.GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.GetComponents.html) and check the list of components returned to identify the one you want.  
  
**Note** : If the type you request is a derivative of MonoBehaviour and the script it's defined in can't be loaded, then this function returns `null` for that component. This might happen if you've named your class ambiguously. Refer to [Naming scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/Namespaces.html) in the Manual for more information on naming considerations.  
  
The typical usage for this method is to call it on a reference to a different GameObject than the one your script is on. For example:  
  
`ComponentType myComponent = otherGameObject.GetComponent(typeof(ComponentType)) as ComponentType`  
  
To find components attached to other GameObjects, you need a [reference to that other GameObject](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html#AccessingOtherGameObjects), or to any component attached to that GameObject. You can then call `GetComponent` on that reference.  
  
You can also use this method to get a reference to a component on the GameObject that this script is attached to, by calling this method inside a `MonoBehaviour`-derived class attached to the GameObject. You can omit the preceding `GameObject` qualifier to reference the GameObject the script is attached to. In this instance, you're actually calling [Component.GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) because the script itself is a type of component, but the result is the same as if you'd referenced the GameObject itself. For example:  
  
`ComponentType myComponent = GetComponent(typeof(ComponentType)) as ComponentType`  
  
The following example gets a reference to a hinge joint component on the referenced GameObject, and if found, sets a property on it. 
```
using UnityEngine;  
  
public class GetComponentExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) as a component.
{
// Create a reference to another GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in the scene. Set a value for this in the Other Game Object field
// in the Inspector window before entering Play mode. The referenced GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) must contain a
// HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) component.
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) otherGameObject;  
  
    void Start()
    {
    // This version of this method returns a Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html), so use the as operator to safely
    // convert it to the derived HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) type
        HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) hinge = otherGameObject.GetComponent(typeof(HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html))) as HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html);
    // Perform null check to confirm that the returned type was successfully converted to HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html).
        if (hinge != null)
        {
            hinge.useSpring = false;
        }
    }
}

```

Additional resources: [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html), [GameObject.GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.GetComponents.html)
* * *
## Declaration
public [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) GetComponent(string type); 
### Parameters
Parameter | Description  
---|---  
type | The name of the type of component to search for, specified as a string.  
### Returns
**Component** A reference to a component of the specified type, returned as a `Component` type. If no component is found, returns `null`. 
### Description
Retrieves a reference to a component of the specified type, by providing the name of the component type as a method parameter.
This version of `GetComponent` isn't as efficient as the generic version. Use this version only if necessary.  
  
`GetComponent` returns only the first matching component found on the GameObject, and components aren't checked in a defined order. If there are multiple components of the same type and you need to find a specific one, use [GameObject.GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.GetComponents.html) and check the list of components returned to identify the one you want.  
  
**Note** : If the type you request is a derivative of MonoBehaviour and the script it's defined in can't be loaded then this function returns `null` for that component. This might happen if you've named your class ambiguously. Refer to [Naming scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/Namespaces.html) in the Manual for more information on naming considerations.  
  
The typical usage for this method is to call it on a reference to a different GameObject than the one your script is on. For example:  
  
`ComponentType myComponent = otherGameObject.GetComponent("ComponentType") as ComponentType`  
  
To find components attached to other GameObjects, you need a [reference to that other GameObject](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html#AccessingOtherGameObjects), or to any component attached to that GameObject. You can then call `GetComponent` on that reference.  
  
You can also use this method to get a reference to a component on the GameObject that this script is attached to, by calling this method inside a `MonoBehaviour`-derived class attached to the GameObject. You can omit the preceding `GameObject` qualifier to reference the GameObject the script is attached to. In this instance, you're actually calling [Component.GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) because the script itself is a type of component, but the result is the same as if you'd referenced the GameObject itself. For example:  
  
`ComponentType myComponent = GetComponent("ComponentType") as ComponentType`  
  
The following example gets a reference to a hinge joint component on the referenced GameObject, and if found, sets a property on it. 
```
using UnityEngine;  
  
public class GetComponentNonPerformantExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) as a component.
{
// Create a reference to another GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in the scene. Set a value for this in the Other Game Object field
// in the Inspector window before entering Play mode. The referenced GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) must contain a
// HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) component.
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) otherGameObject;  
  
    void Start()
    {
        // This version of this method returns a Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html), so use the as operator to safely
        // convert it to the derived HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) type
        HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) hinge = otherGameObject.GetComponent("HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html)") as HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html);
        // Perform null check to confirm a valid HingeJoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HingeJoint.html) component was successfully returned.
        if (hinge != null)
        {
            hinge.useSpring = false;
        }
    }
}

```

Additional resources: [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html), [GameObject.GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.GetComponents.html)
* * *
