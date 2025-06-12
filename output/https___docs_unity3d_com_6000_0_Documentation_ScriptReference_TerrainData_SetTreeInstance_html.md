* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetTreeInstance.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).SetTreeInstance
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
public void SetTreeInstance(int index, [TreeInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TreeInstance.html) instance); 
### Parameters
Parameter | Description  
---|---  
index | The index of the tree instance.  
instance | The new TreeInstance value.  
### Description
Sets the tree instance with new parameters at the specified index. However, you cannot change [TreeInstance.prototypeIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TreeInstance-prototypeIndex.html) and [TreeInstance.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TreeInstance-position.html). If you change them, the method throws an ArgumentException.
* * *
