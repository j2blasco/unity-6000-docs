* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.AlwaysLinkAssemblyAttribute.html

# AlwaysLinkAssemblyAttribute
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
Ensure an assembly is always processed during managed code stripping.
Use the [assembly: UnityEngine.Scripting.AlwaysLinkAssembly] attribute to force UnityLinker to process the assembly regardless of whether or not the assembly is referenced by another assembly that is included in the build.  
  
Use this attribute on package or precompiled assemblies that contain one or more methods with the `[RuntimeInitializeOnLoadMethod]` attribute, but which may not contain types used directly or indirectly in any scenes built for the project.  
  
Note that this attribute only instructs UnityLinker to process the assembly. If no code elements match the root marking rules for the assembly, UnityLinker still removes the assembly from the build.  
  
The `[AlwaysLinkAssembly]` attribute can only be defined on the assembly. Declare the attribute in any C# file compiled into the assembly, outside the namespace declaration.  
  
Additional resources: [Managed Code Stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/ManagedCodeStripping.html)
```
using UnityEngine;
using UnityEngine.Scripting;  
  
[assembly: AlwaysLinkAssembly]  
  
namespace Example
{
    public class Foo
    {
        [RuntimeInitializeOnLoadMethod]
        public void Initialize() {}
    }
}

```

* * *
