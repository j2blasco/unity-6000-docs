* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.html

# ManagedStrippingLevel
enumeration
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
Defines how aggressively Unity strips unused managed (C#) code.
When Unity builds your game or application it can strip unused code from the managed dynamically linked libraries used in the project. Stripping code can make the resulting executable significantly smaller, but can sometimes mistakenly remove code that is actually used. The ManagedStrippingLevel Enum defines the options you can use when specifying how aggressively Unity should remove unused code.  
  
Additional resources: [PlayerSettings.GetManagedStrippingLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetManagedStrippingLevel.html), [PlayerSettings.SetManagedStrippingLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetManagedStrippingLevel.html)
### Properties
Property | Description  
---|---  
[Disabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.Disabled.html) | Do not strip any code.  
[Low](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.Low.html) | Remove unreachable managed code to reduce build size and Mono/IL2CPP build times.  
[Medium](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.Medium.html) | Run UnityLinker in a less conservative mode than Low. This will further reduce code size beyond what Low can achieve. However, this additional reduction may come with tradeoffs. Possible side effects may include, having to maintain a custom link.xml file, and some reflection code paths may not behave the same.  
[High](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.High.html) | UnityLinker will strip as much as possible. This will further reduce code size beyond what Medium can achieve. However, this additional reduction may come with tradeoffs. Possible side effects may include, managed code debugging of some methods may no longer work. You may need to maintain a custom link.xml file, and some reflection code paths may not behave the same.  
[Minimal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.Minimal.html) | The class libraries, UnityEngine, and Windows Runtime assemblies will be stripped. All other assemblies are copied.  
* * *
