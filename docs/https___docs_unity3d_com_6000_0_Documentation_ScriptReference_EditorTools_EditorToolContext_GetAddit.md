* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.GetAdditionalToolTypes.html

#  [EditorToolContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html).GetAdditionalToolTypes
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
public IEnumerable<Type> GetAdditionalToolTypes(); 
### Returns
**IEnumerable <Type>** A collection of [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) types. 
### Description
Get an additional collection of tools to display in the same category as the built-in transform tools.
Implementation of this method is optional, the default value is to return an empty collection.
* * *
