* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.ResolvePickingCallback.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).ResolvePickingCallback
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
public delegate Object ResolvePickingCallback(int localPickingIndex); 
### Parameters
Parameter | Description  
---|---  
localPickingIndex | The 0-based index that specifies what picking index was selected.  
### Description
The delegate type to return from [RenderPickingCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.RenderPickingCallback.html) through the [RenderPickingResult.resolver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult-resolver.html) member.
Additional resources: [RenderPickingResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult.html).
* * *
