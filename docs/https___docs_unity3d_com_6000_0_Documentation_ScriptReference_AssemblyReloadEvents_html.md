* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssemblyReloadEvents.html

# AssemblyReloadEvents
class in UnityEditor
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
This class has event dispatchers for assembly reload events.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class MyWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Test/Show My Window")]
    static void Init()
    {
        GetWindow<MyWindow>();
    }  
  
    void OnEnable()
    {
        AssemblyReloadEvents.beforeAssemblyReload[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssemblyReloadEvents-beforeAssemblyReload.html) += OnBeforeAssemblyReload;
        AssemblyReloadEvents.afterAssemblyReload[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssemblyReloadEvents-afterAssemblyReload.html) += OnAfterAssemblyReload;
    }  
  
    void OnDisable()
    {
        AssemblyReloadEvents.beforeAssemblyReload[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssemblyReloadEvents-beforeAssemblyReload.html) -= OnBeforeAssemblyReload;
        AssemblyReloadEvents.afterAssemblyReload[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssemblyReloadEvents-afterAssemblyReload.html) -= OnAfterAssemblyReload;
    }  
  
    public void OnBeforeAssemblyReload()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Before Assembly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.Assembly.html) Reload");
    }  
  
    public void OnAfterAssemblyReload()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("After Assembly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.Assembly.html) Reload");
    }
}

```

### Events
Event | Description  
---|---  
[afterAssemblyReload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssemblyReloadEvents-afterAssemblyReload.html) | This event is dispatched just after Unity have reloaded all assemblies.  
[beforeAssemblyReload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssemblyReloadEvents-beforeAssemblyReload.html) | This event is dispatched just before Unity reloads all assemblies.  
### Delegates
Delegate | Description  
---|---  
[AssemblyReloadCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssemblyReloadEvents.AssemblyReloadCallback.html) | Delegate used for assembly reload events.  
* * *
