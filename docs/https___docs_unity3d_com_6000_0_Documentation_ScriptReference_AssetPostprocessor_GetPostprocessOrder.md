* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.GetPostprocessOrder.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).GetPostprocessOrder
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
public int GetPostprocessOrder(); 
### Description
Override the order in which importers are processed.
By overriding GetImportOrder you can sort in which order postprocessors are executed. Smaller priorities will be imported first. The GetPostprocessOrder function does not affect the order of OnPostprocessAllAssets calls.
* * *
