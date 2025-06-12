* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/L10n.html

# L10n
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
Class for text localization.
Use this class to localize your text shown in the Unity Editor. You need a **po** file (ja.po for example) and an asmdef (Assembly Definition) file. Add this syntax to define the [LocalizationAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LocalizationAttribute.html) in any script in the assembly: [assembly:UnityEditor.Localization].   
Place all **po** files within the asmdef folder. Additional resources: https://docs.unity3d.com/Manual/assembly-definition-files.html
### Static Methods
Method | Description  
---|---  
[Tr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/L10n.Tr.html) | This function referes a po file like ja.po as an asset. Asmdef and [assembly: UnityEditor.Localization] is needed.  
* * *
