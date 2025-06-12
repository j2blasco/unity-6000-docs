* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.PreserveAttribute.html

# PreserveAttribute
class in UnityEngine.Scripting
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
PreserveAttribute prevents byte code stripping from removing a class, method, field, or property.
When you create a build, Unity will try to strip unused code from your project. This is great to get small builds. However, sometimes you want some code to not be stripped, even if it looks like it is not used. This can happen for instance if you use reflection to call a method, or instantiate an object of a certain class. You can apply the [Preserve] attribute to classes, methods, fields and properties. In addition to using PreserveAttribute, you can also use the traditional method of a link.xml file to tell the linker to not remove things. PreserveAttribute and link.xml work for both the Mono and IL2CPP scripting backends.  
  
For more details on [Preserve] and link.xml see [Managed Code Stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/ManagedCodeStripping.html)
```
using UnityEngine;
using System.Collections;
using System.Reflection;
using UnityEngine.Scripting;  
  
public class NewBehaviourScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        ReflectionExample.InvokeBoinkByReflection();
    }
}  
  
public class ReflectionExample
{
    static public void InvokeBoinkByReflection()
    {
        typeof(ReflectionExample).GetMethod("Boink", BindingFlags.NonPublic | BindingFlags.Static).Invoke(null, null);
    }  
  
    // No other code directly references the Boink method, so when when stripping is enabled,
    // it will be removed unless the [Preserve] attribute is applied.
    [Preserve]
    static void Boink()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Boink");
    }
}

```

For 3rd party libraries that do not want to take on a dependency on UnityEngine.dll, it is also possible to define their own PreserveAttribute. The code stripper will respect that too, and it will consider any attribute with the exact name "PreserveAttribute" as a reason not to strip the thing it is applied on, regardless of the namespace or assembly of the attribute.
* * *
