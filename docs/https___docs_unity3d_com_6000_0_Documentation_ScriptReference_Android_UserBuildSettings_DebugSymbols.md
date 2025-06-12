* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.UserBuildSettings.DebugSymbols-level.html

#  [UserBuildSettings.DebugSymbols](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.UserBuildSettings.DebugSymbols.html).level
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
[Unity.Android.Types.DebugSymbolLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Types.DebugSymbolLevel.html) level; 
### Description
Specifies what sections are included into the debug symbol.
```
using UnityEditor.Android;
using Unity.Android.Types;  
  
public class Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html)
{
    public void Setup()
    {
        UserBuildSettings.DebugSymbols.level[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.UserBuildSettings.DebugSymbols-level.html) = DebugSymbolLevel.SymbolTable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Types.DebugSymbolLevel.SymbolTable.html);
    }
}
```

* * *
