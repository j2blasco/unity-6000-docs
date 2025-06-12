* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html

#  [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html).Instantiate
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
public static Object Instantiate([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) original); 
## Declaration
public static Object Instantiate([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) original, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent); 
## Declaration
public static Object Instantiate([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) original, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent, bool instantiateInWorldSpace); 
## Declaration
public static Object Instantiate([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) original, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
## Declaration
public static Object Instantiate([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) original, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent); 
### Parameters
Parameter | Description  
---|---  
original | An existing object that you want to make a copy of.  
position | Position for the new object.  
rotation | Orientation of the new object.  
parent | Parent that will be assigned to the new object.  
instantiateInWorldSpace | When you assign a parent Object, pass true to position the new object directly in world space. Pass false to set the Object’s position relative to its new parent.  
parameters | A struct containing all the parameters.  
### Returns
**Object** The instantiated clone. 
### Description
Clones the object `original` and returns the clone.
This function makes a copy of an object in a similar way to the Duplicate command in the editor. If you are cloning a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you can specify its position and rotation (these default to the original GameObject's position and rotation otherwise). If you are cloning a [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) the GameObject it is attached to is also cloned, again with an optional position and rotation.  
  
When you clone a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) or [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html), all child objects and components are also cloned with their properties set like those of the original object.  
  
**Note:** When this method clones a child object, it also clones the child's own children. To prevent stack overflow, Unity limits this nested cloning. If you exceed more than half your stack size, Unity throws an `InsufficientExecutionStackException`.  
  
By default the _parent_ of the new object is null; it is not a "sibling" of the original. However, you can still set the parent using the overloaded methods. If a parent is specified and no position and rotation are specified, the original object's position and rotation are used for the cloned object's local position and rotation, or its world position and rotation if the `instantiateInWorldSpace` parameter is true. If the position and rotation are specified, they are used as the object's position and rotation in world space.  
  
The active status of a GameObject at the time of cloning is maintained, so if the original is inactive the clone is created in an inactive state too. Additionally for the object and all child objects in the hierarchy, each of their Monobehaviours and Components will have their Awake and OnEnable methods called only if they are active in the hierarchy at the time of this method call.  
  
For more flexibility, there are generic overrides that take an [InstantiateParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InstantiateParameters.html) struct, allowing to pass any combination of parameters like parent, target scene or world space positions.  
  
These methods do not create a prefab connection to the new instantiated object. Creating objects with a prefab connection can be achieved using [PrefabUtility.InstantiatePrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.InstantiatePrefab.html).  
  
Additional resources:  
  
[Instantiating prefabs at run time](https://docs.unity3d.com/6000.0/Documentation/Manual/instantiating-prefabs.html)  
[PrefabUtility.InstantiatePrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.InstantiatePrefab.html)
```
// Instantiates 10 copies of Prefab each 2 units apart from each other  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefab;
    void Start()
    {
        for (var i = 0; i < 10; i++)
        {
            Instantiate(prefab, new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(i * 2.0f, 0, 0), Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));
        }
    }
}

```

Instantiate can be used to create new objects at runtime. Examples include objects used for projectiles, or particle systems for explosion effects.
```
using UnityEngine;  
  
// Instantiate a rigidbody then set the velocity  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Assign a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) component in the inspector to instantiate  
  
    public Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) projectile;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Ctrl was pressed, launch a projectile
        if (Input.GetButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButtonDown.html)("Fire1"))
        {
            // Instantiate the projectile at the position and rotation of this transform
            Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) clone;
            clone = Instantiate(projectile, transform.position, transform.rotation);  
  
            // Give the cloned object an initial velocity along the current
            // object's Z axis
            clone.velocity = transform.TransformDirection(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html) * 10);
        }
    }
}

```

Instantiate can also clone script instances directly. The entire game object hierarchy will be cloned and the cloned script instance will be returned.
```
using UnityEngine;
using System.Collections;  
  
public class Missile : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int timeoutDestructor;  
  
    // ...other code...
}  
  

public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Instantiate a Prefab with an attached Missile script
    public Missile projectile;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Ctrl was pressed, launch a projectile
        if (Input.GetButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButtonDown.html)("Fire1"))
        {
            // Instantiate the projectile at the position and rotation of this transform
            Missile clone = Instantiate(projectile, transform.position, transform.rotation);  
  
            // Set the missiles timeout destructor to 5
            clone.timeoutDestructor = 5;
        }
    }
}

```

After cloning an object you can also use GetComponent to set properties on a specific component attached to the cloned object.
* * *
## Declaration
public static T Instantiate(T original); 
## Declaration
public static T Instantiate(T original, [InstantiateParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InstantiateParameters.html) parameters); 
## Declaration
public static T Instantiate(T original, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent); 
## Declaration
public static T Instantiate(T original, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent, bool worldPositionStays); 
## Declaration
public static T Instantiate(T original, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
## Declaration
public static T Instantiate(T original, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, [InstantiateParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InstantiateParameters.html) parameters); 
## Declaration
public static T Instantiate(T original, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent); 
### Parameters
Parameter | Description  
---|---  
original | Object of type T that you want to clone.  
### Returns
**T** Object of type T. 
### Description
You can also use Generics to instantiate objects. See the [Generic Functions](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/generics/generic-methods) page for more details.
By using Generics we don't need to cast the result to a specific type.
```
using UnityEngine;  
  
public class Missile : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // ...other code...
}  
  
public class InstantiateGenericsExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Missile missile;  
  
    void Start()
    {
        Missile missileCopy = Instantiate<Missile>(missile);
    }
}

```

* * *
